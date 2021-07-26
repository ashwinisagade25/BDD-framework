# Created by Amit at 7/25/2021
Feature: Login orangeHRM
  # Enter feature description here
  Background:


  Scenario: Login to site with valid credentials
    Given Launch chrome browser
    When open homepage
    And Enter username "admin" and Paswword "admin123"
    And click on login button
    Then user must successfully login to dashboard page

  Scenario Outline: Login to site with invalid credentials
    Given Launch chrome browser
    When open homepage
    And Enter username "<username>" and Paswword "<password>"
    And click on login button
    Then user must see error msg

    Examples:
      | username | password |
      | Admin    | 123      |
      | AAAA     | AAAA     |
      | AAAAA    | admin123 |
