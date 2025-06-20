*** Settings ***
Library    SeleniumLibrary
Resource    login_success.robot

*** Keywords ***
login+create product
    login_with   oddone.lea@gmail.com    a123456789
    Wait Until Element Is Visible    xpath=//a[contains(.,'New Product')]    5s
    Click Element    xpath=//a[contains(.,'New Product')]
    Sleep    1
    # Champs name -> weight et liste Tax
    Input Text    id=name    Gâteau Orchidées
    Input Text    id=sku    123456
    Input Text    id=price    100
    Input Text    id=weight    3
    Select From List By Label    id=tax_class    Taxable Goods
    # Pour le champ 'category', il faut gérer le clic via JavasScript
    Execute Javascript    document.querySelector('#rows').innerText = 'Mariage et pacs';
    # Champs url Key -> meta description
    Input Text    id=urlKey    gateau-orchidees
    Input Text    id=metaTitle    Gâteau Orchidées
    Input Text    id=metaKeywords    gâteau orchidées
    Input Text    id=meta_description    Gâteau Orchidées
    # Champs quantity, size et color
    Input Text    name=qty    1
    Select From List By Label    name=attributes[0][value]    White
    Select From List By Label    name=attributes[1][value]    XXL
    # Soumission du formulaire
    Click Button    css=.button.primary

Highlight Element
    [Arguments]    ${locator}
    Execute Javascript    arguments[0].style.border='3px solid red'    ${locator}