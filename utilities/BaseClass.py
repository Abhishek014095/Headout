import pytest


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass

# import time
#
# class BaseClass:
#     def wait_for_seconds(self, seconds):
#         time.sleep(seconds)
