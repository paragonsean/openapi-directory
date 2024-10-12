

# TicketSeat


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**coach** | **String** | The identifier of the train car or coach in which the ticketed seat is located. Eg. \&quot;10\&quot; |  [optional] |
|**customFareClass** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |
|**fareClass** | [**FareClassEnum**](#FareClassEnum) | The fare class of the ticketed seat. |  [optional] |
|**seat** | **String** | The identifier of where the ticketed seat is located. Eg. \&quot;42\&quot;. If there is no specific identifier, use &#x60;seatAssigment&#x60; instead. |  [optional] |
|**seatAssignment** | [**LocalizedString**](LocalizedString.md) |  |  [optional] |



## Enum: FareClassEnum

| Name | Value |
|---- | -----|
| FARE_CLASS_UNSPECIFIED | &quot;FARE_CLASS_UNSPECIFIED&quot; |
| ECONOMY | &quot;ECONOMY&quot; |
| ECONOMY2 | &quot;economy&quot; |
| FIRST | &quot;FIRST&quot; |
| FIRST2 | &quot;first&quot; |
| BUSINESS | &quot;BUSINESS&quot; |
| BUSINESS2 | &quot;business&quot; |



