*** Settings ***
Library    example.py

*** Test Cases ***
Start threads separately, log all at the end
    Log On Thread    Hello, world!
    Log On Thread    Hi, again!!    name=second
    Log On Thread    3
    Log On Thread    4
    Log On Thread    5
    Log On Thread    6    DEBUG
    Log On Thread    7    info
    Log On Thread    <b style='color: red'>8</b>    html=yes
    Log On Thread    9
    Log On Thread    10
    Log On Thread    And once more...    name=second
    Finish All

Start threads together, log them separately
    Log On Threads    Hello, world!    count=5    name_prefix=My Thread
    Log On Thread    And also <i>Hi, again!!</i>.    name=My Thread 3    html=y
    Finish One    My Thread 1
    Finish One    My Thread 2
    Finish One    My Thread 3
    Finish One    My Thread 5
    Finish One    My Thread 4
