# GoogleWalletApi.FlightHeader

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**carrier** | [**FlightCarrier**](FlightCarrier.md) |  | [optional] 
**flightNumber** | **String** | The flight number without IATA carrier code. This field should contain only digits. This is a required property of &#x60;flightHeader&#x60;. eg: \&quot;123\&quot; | [optional] 
**flightNumberDisplayOverride** | **String** | Override value to use for flight number. The default value used for display purposes is carrier + flight_number. If a different value needs to be shown to passengers, use this field to override the default behavior. eg: \&quot;XX1234 / YY576\&quot; | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;walletobjects#flightHeader\&quot;&#x60;. | [optional] 
**operatingCarrier** | [**FlightCarrier**](FlightCarrier.md) |  | [optional] 
**operatingFlightNumber** | **String** | The flight number used by the operating carrier without IATA carrier code. This field should contain only digits. eg: \&quot;234\&quot; | [optional] 


