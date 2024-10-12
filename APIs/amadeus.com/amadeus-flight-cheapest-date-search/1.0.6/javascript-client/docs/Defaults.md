# FlightCheapestDateSearch.Defaults

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**departureDate** | **String** | the date, or range of dates, on which the flight will depart from the origin. Dates are specified in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) YYYY-MM-DD format, e.g. 2017-12-25. Ranges are specified with a comma and are inclusive | [optional] 
**duration** | **String** | exact duration or range of durations of the travel, in days. This parameter must not be set if oneWay is true. Ranges are specified with a comma and are inclusive, e.g. 2,8 | [optional] 
**nonStop** | **Boolean** | if this parameter is set to true, only flights going from the origin to the destination with no stop in-between are considered | [optional] 
**oneWay** | **Boolean** | if this parameter is set to true, only one-way flights are considered. If this parameter is not set or set to false, only round-trip flights are considered | [optional] 
**viewBy** | **String** | view the flight dates by DATE, DURATION, or WEEK. View by DATE to get the cheapest flight dates for every departure date in the given range. View by DURATION to get the cheapest flight dates for every departure date and for every duration in the given ranges. View by WEEK to get the cheapest flight date for every week in the given range of departure dates | [optional] 



## Enum: ViewByEnum


* `DATE` (value: `"DATE"`)

* `DURATION` (value: `"DURATION"`)

* `WEEK` (value: `"WEEK"`)




