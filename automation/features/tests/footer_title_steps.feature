Feature: #

 Scenario Outline: # Verify Gettop footer links
  Given Open Gettop page
  When User is at the footer of the homepage
  And Verify if link one is Best selling
  And Verify if link two is Latest
  Then Verify if link three is Top rated
  Examples:
   |  |

