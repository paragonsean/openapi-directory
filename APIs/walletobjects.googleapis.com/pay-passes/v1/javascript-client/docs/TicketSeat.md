# GooglePayPassesApi.TicketSeat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coach** | **String** | The identifier of the train car or coach in which the ticketed seat is located. Eg. \&quot;10\&quot; | [optional] 
**customFareClass** | [**LocalizedString**](LocalizedString.md) |  | [optional] 
**fareClass** | **String** | The fare class of the ticketed seat. | [optional] 
**seat** | **String** | The identifier of where the ticketed seat is located. Eg. \&quot;42\&quot;. If there is no specific identifier, use &#x60;seatAssigment&#x60; instead. | [optional] 
**seatAssignment** | [**LocalizedString**](LocalizedString.md) |  | [optional] 



## Enum: FareClassEnum


* `FARE_CLASS_UNSPECIFIED` (value: `"FARE_CLASS_UNSPECIFIED"`)

* `ECONOMY` (value: `"ECONOMY"`)

* `economy` (value: `"economy"`)

* `FIRST` (value: `"FIRST"`)

* `first` (value: `"first"`)

* `BUSINESS` (value: `"BUSINESS"`)

* `business` (value: `"business"`)




