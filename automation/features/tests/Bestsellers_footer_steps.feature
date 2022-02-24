# Created by lauren at 2/17/22
#noinspection CucumberUndefinedStep
Feature: # Enter feature name here

 Scenario Outline: # Verify Gettop footer links
  Given Open Gettop page
  When User is at the footer of the homepage
  And Verify if link one is Macbook pro 16
  And Verify if link two is AirPods Pro
  And Verify if link three is AirPods
  Then Verify if link four is Watch Series 3
  Examples:
