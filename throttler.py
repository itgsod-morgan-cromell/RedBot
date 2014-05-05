import time


class Throttler(object):
    """
    The throttler keeps track of the amount of requests sent per minute.
    If the amount of requests reaches 30 within a minute, the throttler prevents the RedBot to send more requests.
    """

    def __init__(self, max_amount_of_requests_per_interval, time_interval_in_seconds):
        self.last_reset_in_time = int(time.time())
        self.processed_requests = 0
        self.reset_time_interval = time_interval_in_seconds
        self.max_amount_of_requests_per_interval = max_amount_of_requests_per_interval

    @property
    def is_request_allowed(self):
        """
        Checks if RedBot is allowed to send a request.
        Returns a boolean.
        """
        self._update()
        if self.processed_requests < self.max_amount_of_requests_per_interval:
            return True
        else:
            return False

    def request_sent(self):
        if self.is_request_allowed:
            self.processed_requests += 1

    def _update(self):
        """
        This function updates the timer and resets the timer to 0 when it reaches 60 seconds.
        """
        self.passed_time_since_last_reset = int(time.time() - self.last_reset_in_time)
        if self.passed_time_since_last_reset >= self.reset_time_interval:
            self._reset()

    def _reset(self):
        self.processed_requests = 0
        self.last_reset_in_time = int(time.time())

    def remaining_time_until_reset(self):
        self._update()
        return self.reset_time_interval - self.passed_time_since_last_reset