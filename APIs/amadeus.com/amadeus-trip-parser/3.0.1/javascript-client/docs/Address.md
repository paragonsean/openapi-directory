# TripParser.Address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | Category of the contact element | [optional] 
**cityName** | **String** | Full city name. Example: Dublin | [optional] 
**countryCode** | **String** | ISO 3166-1 country code | [optional] 
**lines** | **[String]** | Line 1 &#x3D; Street address, Line 2 &#x3D; Apartment, suite, unit, building, floor, etc | [optional] 
**postalBox** | **String** | E.g. BP 220 | [optional] 
**postalCode** | **String** | Example: 74130 | [optional] 
**state** | **String** | State, province or country name | [optional] 
**stateCode** | **String** | State code (two character standard IATA state code) | [optional] 
**text** | **String** | Field containing a full unformatted address. Only applicable when the fields lines, postalCode, countryCode, cityName are not filled. | [optional] 


