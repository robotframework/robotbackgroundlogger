import threading

import robotthreadlogger as logger


threads = []


def on_thread(message, name=None):
    thread = threading.Thread(target=logger.info, args=[message], name=name)
    thread.start()
    threads.append(thread)


def finish():
    for thread in threads:
        thread.join()
    logger.log_background_messages()
