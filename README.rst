.. default-role:: code

Background logging support to test libraries
============================================

This helper module is indented to be used by Robot Framework test libraries
that run keywords in background using threads and that want those threads
to be able to log. By default, as `explained in Robot Framework User Guide`__,
messages logged by threads using the programmatic APIs are ignored, and results
of logging using the standard output are undefined.

This module provides a custom logger that works mostly like the standard
`robot.api.logger`__, but also stores messages logged by background threads.
It also provides a method the main thread can use to forward the logged
messages to Robot Framework's log.

__ http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#communication-when-using-threads
__ https://robot-framework.readthedocs.org/en/latest/autodoc/robot.api.html#module-robot.api.logger

Usage
-----

The logger can be taken into use like this:

.. sourcecode:: python

    from robotbackgroundlogger import BackgroundLogger
    logger = BackgroundLogger()

After that `logger` can be used mostly like `robot.api.logger`:

.. sourcecode:: python

    logger.debug('Hello, world!')
    logger.info('<b>HTML</b> example', html=True)

When used by the main thread, messages will be logged immediately exactly like
with `robot.api.logger`. When used by other threads, messages will be stored
internally. They can be later logged by the main thread by running:

.. sourcecode:: python

    logger.log_background_messages()

If you want to log only messages logged by a certain thread, you can use
pass the name of the thread as an argument:

.. sourcecode:: python

    logger.log_background_messages('Example thread')

Logged messages are also removed from the internal message storage. It is
possible to do that also without logging:

.. sourcecode:: python

    # Remove all messages
    logger.reset_background_messages()
    # Remove messages logged by the named thread
    logger.reset_background_messages('Another thread')

Example
-------

`<example.py>`__ library that is used by `<example.robot>`__ shows how this
module can be used in practice. You can run the example like::

    pybot example.robot

ToDo
----

- Check compatibility with ``robot.api.logger`` (console, HTML logging, ...).
- Document that libraries should only create one ``BackgroundLogger`` instance
  unless they want to use ``log_background_messages`` multiple times too.
- Review and enhance docs and examples in general.
- 0.1 release.