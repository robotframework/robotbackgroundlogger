import threading

from robotbackgroundlogger import BackgroundLogger


logger = BackgroundLogger()
threads = []


def on_thread(message, level='INFO', html=False, name=None):
    thread = threading.Thread(target=logger.write, args=[message, level, html],
                              name=name)
    thread.start()
    threads.append(thread)


def finish():
    for thread in threads:
        thread.join()
    logger.log_background_messages()
