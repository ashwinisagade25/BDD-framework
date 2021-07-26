Feature: OrangeHRM logo
  Scenario: Logo is displayed on homepage
    Given Launch chrome browser
    When open homepage
    Then logo is present
    And close browser
