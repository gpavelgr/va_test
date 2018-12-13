Feature: Counts number of days to the date
  Description

  Scenario: VA tells how many days is to the date from now
    Given today is 2018-12-13
     When user says count days to the 2018-12-20
     Then VA tells 7 days


