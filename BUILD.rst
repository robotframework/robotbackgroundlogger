Releasing RobotBackgroundLogger
===============================

1. Set ``$VERSION`` shell variable to ease copy-pasting further commands::

    VERSION=x.y

2. Update ``__version__`` in `<robotbackgroundlogger.py>`__::

    git diff  # verify changes
    git commit -m "Updated __version__ to $VERSION" robotbackgroundlogger.py && git push

3. Tag::

    git tag -a $VERSION -m "Release $VERSION" && git push --tags

4. Create distribution::

    python setup.py sdist register upload

5. Verify that `PyPI <https://pypi.python.org/pypi/robotbackgroundlogger>`__
   looks good.

6. Test that installation works::

    pip install robotbackgroundlogger --upgrade

7. ``__version__`` back to dev (e.g. `1.3dev`)::

    git diff  # verify changes
    git commit -m "__version__ back to dev" robotbackgroundlogger.py && git push

8. Advertise on `Twitter <https://twitter.com/robotframework>`__ and on mailing
   lists as needed.
