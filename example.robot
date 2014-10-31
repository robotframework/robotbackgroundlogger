*** Settings ***
Library    example.py

*** Test Cases ***
X
    On Thread    Hello, world!
    On Thread    Hi, again!!    name=second
    On Thread    3
    On Thread    4
    On Thread    5
    On Thread    6    DEBUG
    On Thread    7    info
    On Thread    <b style='color: red'>8</b>    html=yes
    On Thread    9
    On Thread    10
    On Thread    And once more...    name=second
    Finish
