Logging from threads support to test libraries
==============================================

This helper module is indented to be used by Robot Framework test libraries
that run keywords in background using threads and that want those threads
to be able to log. By default Robot Frameworks ignores messages logged by
threads. This module solves that problem by storing messages logged by
threads internally and providing a method that will log them when that is
possible.

Usage
-----

The logger can be taken into use like this:

.. sourcecode:: python

    from robotbackgroundlogger import BackgroundLogger
    logger = BackgroundLogger()

After that ``logger`` can be used mostly like ``robot.api.logger``:

.. sourcecode:: python

    logger.debug('Hello, world!')
    logger.info('<b>HTML</b> example, html=True)

When used by the main thread, messages will be logged immediately exactly like
with ``robot.api.logger``. When used by other threads, messages will be stored
internally. They can be later logged by the main thread by running:

.. sourcecode:: python

    logger.log_background_messages()

The above will also reset the message cache. If you want to just do that,
without logging, run:

.. sourcecode:: python

    logger.reset_background_messages()

Example
-------

`<example.py>`__, used by `<example.robot>`__ shows how this module can be
used in practice. You can run the example like::

    pybot example.robot

ToDo
----

- Check compatibility with ``robot.api.logger`` (console, HTML logging, ...).
- Document that libraries should only create one ``BackgroundLogger`` instance
  unless they want to use ``log_background_messages`` multiple times too.
- Review and enhance docs and examples in general.
- 0.1 release and public announcement.
