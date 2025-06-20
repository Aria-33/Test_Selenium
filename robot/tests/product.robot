*** Settings ***
Resource    ../config.robot
Test Setup    Open Browser    http://localhost:3000/    chrome    #headlesschrome
Test Teardown    Close Browser

*** Test Cases ***
delete product
    login+create product
    Click Element    xpath=//a[contains(.,'Products')]
    #Défini la variable pour la checkbox
    ${checkbox_xpath}=    Set Variable    xpath=//tr[td//a[contains(text(), "Gâteau Orchidées")]]//label[input[@type='checkbox']]
    # Scroll vers l’élément avant de cliquer
    Scroll Element Into View    ${checkbox_xpath}
    Wait Until Element Is Visible    ${checkbox_xpath}    1s
    #Clique sur la checkbox
    Click Element    ${checkbox_xpath}
    Sleep    1s
    # Vérifie que la case est bien cochée
    ${is_checked}=    Get Element Attribute    ${checkbox_xpath}    checked
    #Cliquer sur le bouton Delete
    Click Element    xpath=//a[span[normalize-space(text())="Delete"]]
    Sleep    1s
    #Cliquer sur le bouton Delete dans la popup
    Wait Until Element Is Visible    css=.button.critical    10s    Le bouton de suppression n'est pas visible après 10s
    Wait Until Element Is Enabled    css=.button.critical    10s    Le bouton de suppression n'est pas cliquable après 10s
    Click Button    css=.button.critical
    Sleep    1s