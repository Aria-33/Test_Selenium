*** Settings ***
Resource    ../config.robot
Test Setup    Open Browser    http://localhost:3000/    chrome    #headlesschrome
Test Teardown    Close Browser

*** Test Cases ***
login success
    login_with    oddone.lea@gmail.com    a123456789
    Wait Until Page Contains    Dashboard

login error email wrong
    login_with    admin@admin.com    a123456789
    Wait Until Page Contains Element  css=.text-critical.py-4    5s
    Element Should Contain    css=.text-critical.py-4    Invalid email or password

login error password wrong
    login_with    oddone.lea@gmail.com    admin
    Wait Until Page Contains Element  css=.text-critical.py-4    5s
    Element Should Contain    css=.text-critical.py-4    Invalid email or password

login error both wrong
    login_with    admin@admin.com    admin
    Wait Until Page Contains Element  css=.text-critical.py-4    5s
    Element Should Contain    css=.text-critical.py-4    Invalid email or password

login email empty
    login_with    ${EMPTY}    a123456789
    Wait Until Page Contains Element  css=.pl025.text-critical    5s
    Element Should Contain    css=.pl025.text-critical    This field can not be empty

login password empty
    login_with    oddone.lea@gmail.com    ${EMPTY}
    Wait Until Page Contains Element  css=.pl025.text-critical    5s
    Element Should Contain    css=.pl025.text-critical    This field can not be empty

login both empty
    login_with    ${EMPTY}    ${EMPTY}
    Wait Until Page Contains Element  css=.pl025.text-critical    5s
    Element Should Contain    css=.pl025.text-critical    This field can not be empty

login email wrong format
    login_with    admin    a123456789
    Wait Until Page Contains Element  css=.pl025.text-critical    5s
    Element Should Contain    css=.pl025.text-critical    Invalid email