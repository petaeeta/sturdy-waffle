*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And password
    Input Credentials    pekka    pekka123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    kalle    pekka123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials    ad    kalle123
    Output Should Contain  Username should only contain characters a-z, with minimum length of 3
Register With Enough Long But Invalid Username And Valid Password
    Input Credentials    ad123123123    kalle123
    Output Should Contain  Username should only contain characters a-z, with minimum length of 3
Register With Valid Username And Too Short Password
    Input Credentials    pekka    kal
    Output Should Contain  Password should be at least 8 characters, and cannot contain ONLY alphabetical characters
Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    pekka    pekkapekkapekkapekka
    Output Should Contain  Password should be at least 8 characters, and cannot contain ONLY alphabetical characters
*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command