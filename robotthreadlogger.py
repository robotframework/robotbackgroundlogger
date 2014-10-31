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
except ImportError:  # New in 2.7.
    OrderedDict = dict
import threading
import time

from robot.api import logger


MESSAGE_QUEUE = OrderedDict()
LOCK = threading.RLock()


def trace(msg, html=False):
    write('trace', msg, html)


def debug(msg, html=False):
    write('debug', msg, html)


def info(msg, html=False):
    write('info', msg, html)


def warn(msg, html=False):
    write('warn', msg, html)


def write(level, msg, html=False):
    with LOCK:
        thread = threading.currentThread()
        if thread.getName() in logger.librarylogger.LOGGING_THREADS:
            logger.write(msg, level, html)
        else:
            MESSAGE_QUEUE.setdefault(thread.name, []).append((round(time.time() * 1000),
                                                               level, msg, html))


def reset_background_messages():
    with LOCK:
        MESSAGE_QUEUE.clear()


def log_background_messages():
    with LOCK:
        for thread in MESSAGE_QUEUE:
            print "*HTML* <b>Messages from thread %s</b>" % thread
            for timestamp, level, msg, html in MESSAGE_QUEUE[thread]:
                print "*%s:%d* %s" % (level.upper(), timestamp, msg)
