# SeatmapDisplay.Address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | Category of the contact element | [optional] 
**cityName** | **String** | Full city name. Example: Dublin | [optional] 
**countryCode** | **String** | country code [ISO 3166-1 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) | [optional] 
**lines** | **[String]** | Line 1 &#x3D; Street address, Line 2 &#x3D; Apartment, suite, unit, building, floor, etc | [optional] 
**postalBox** | **String** | E.g. BP 220 | [optional] 
**postalCode** | **String** | Example: 74130 | [optional] 
**stateCode** | **String** | State code - two character standard [ISO 3166-2 state code](https://en.wikipedia.org/wiki/ISO_3166-2) | [optional] 
**stateName** | **String** | Full state name | [optional] 
**text** | **String** | Field containing a full unformatted address. Only applicable when the fields lines, postalCode, countryCode, cityName are not filled. | [optional] 



## Enum: CategoryEnum


* `BUSINESS` (value: `"BUSINESS"`)

* `PERSONAL` (value: `"PERSONAL"`)

* `OTHER` (value: `"OTHER"`)




