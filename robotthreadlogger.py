#  Copyright 2014 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

try:
    from collections import OrderedDict
except ImportError:
    # OrderedDict is wew in 2.7. Should we use 2.4 compatible recipe available
    # at http://code.activestate.com/recipes/576693/?
    OrderedDict = dict
import threading
import time

from robot.api import logger


LOGGING_THREADS = logger.librarylogger.LOGGING_THREADS
MESSAGE_QUEUE = OrderedDict()
LOCK = threading.RLock()


def trace(msg, html=False):
    write(msg, 'TRACE', html)


def debug(msg, html=False):
    write(msg, 'DEBUG', html)


def info(msg, html=False):
    write(msg, 'INFO', html)


def warn(msg, html=False):
    write(msg, 'WARN', html)


def write(msg, level, html=False):
    with LOCK:
        thread = threading.currentThread()
        if thread.getName() in LOGGING_THREADS:
            logger.write(msg, level, html)
        else:
            message = Message(msg, level, html)
            MESSAGE_QUEUE.setdefault(thread.getName(), []).append(message)


def reset_background_messages():
    with LOCK:
        MESSAGE_QUEUE.clear()


def log_background_messages():
    with LOCK:
        for thread in MESSAGE_QUEUE:
            print "*HTML* <b>Messages from thread %s</b>" % thread
            for message in MESSAGE_QUEUE[thread]:
                print message.format()


class Message(object):

    def __init__(self, message, level='INFO', html=False, timestamp=None):
        self.message = message
        self.level = level.upper()
        self.html = html
        self.timestamp = timestamp or int(round(time.time() * 1000))

    def format(self):
        # Can only support HTML logging with INFO level.
        html = self.html and self.level == 'INFO'
        level = self.level if not html else 'HTML'
        return "*%s:%d* %s" % (level, self.timestamp, self.message)
