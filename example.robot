*** Settings ***
Library    example.py

*** Test Cases ***
X
    On Thread    Hello, world!
    On Thread    Hillo, purkki!    second
    On Thread    3
    On Thread    4
    On Thread    5
    On Thread    6
    On Thread    7
    On Thread    8
    On Thread    9
    On Thread    10
    On Thread    Uuudestaan!!    second
    Finish
