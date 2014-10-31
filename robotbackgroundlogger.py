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
except ImportError:  # New in 2.7 but 2.4 compatible recipe would be available.
    OrderedDict = dict
import threading
import time

from robot.api import logger


class Logger(object):

    def trace(self, msg, html=False):
        self.write(msg, 'TRACE', html)

    def debug(self, msg, html=False):
        self.write(msg, 'DEBUG', html)

    def info(self, msg, html=False):
        self.write(msg, 'INFO', html)

    def warn(self, msg, html=False):
        self.write(msg, 'WARN', html)

    def write(self, msg, level, html=False):
        logger.write(msg, level, html)


class BackgroundLogger(Logger):
    LOGGING_THREADS = logger.librarylogger.LOGGING_THREADS

    def __init__(self):
        self.lock = threading.RLock()
        self._messages = OrderedDict()

    def write(self, msg, level, html=False):
        with self.lock:
            thread = threading.currentThread().getName()
            if thread in self.LOGGING_THREADS:
                Logger.write(self, msg, level, html)
            else:
                message = BackgroundMessage(msg, level, html)
                self._messages.setdefault(thread, []).append(message)

    def log_background_messages(self):
        with self.lock:
            for thread in self._messages:
                print "*HTML* <b>Messages from thread '%s'</b>" % thread
                for message in self._messages[thread]:
                    print message.format()
            self.reset_background_messages()

    def reset_background_messages(self):
        with self.lock:
            self._messages.clear()


class BackgroundMessage(object):

    def __init__(self, message, level='INFO', html=False):
        self.message = message
        self.level = level.upper()
        self.html = html
        self.timestamp = time.time() * 1000

    def format(self):
        # Can support HTML logging only with INFO level.
        html = self.html and self.level == 'INFO'
        level = self.level if not html else 'HTML'
        return "*%s:%d* %s" % (level, round(self.timestamp), self.message)
