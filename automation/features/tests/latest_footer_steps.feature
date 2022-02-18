Feature: #

 Scenario Outline: # Verify Gettop footer links
  Given Open Gettop page
  When User is at the footer of the homepage
  And Verify if link one is Macbookair
  And Verify if link two is Macbook Pro
  And Verify if link three is iPhone SE
  Then Verify if link three is iPhone 11
  Examples:
   |  |