# ImpalaHotelBookingApi.CancellationFee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **Number** | The value that is used in calculation of the cost. This could be 50 in case of a 50% fee being charged for a type \&quot;PERCENTAGE\&quot; or 2 in case of the initial two nights of the stay being charged in full as a fee if the type is \&quot;NIGHTS\&quot;. | [optional] 
**price** | [**Money**](Money.md) |  | 
**type** | **String** | The way in which the cancellation fee is calculated. This can be \&quot;NONE\&quot; in case a full refund is paid out, \&quot;NON_REFUNDABLE\&quot; if no refund is paid out and the full amount is due, \&quot;PERCENTAGE\&quot; if a percentage of the total price for the stay is charged as cancellation fee, \&quot;NIGHTS\&quot; if a defined number of initial nights of the stay are charged in full as cancellation fee or \&quot;FLAT\&quot; in case a flat cancellation fee is charged. | 



## Enum: TypeEnum


* `NON_REFUNDABLE` (value: `"NON_REFUNDABLE"`)

* `PERCENTAGE` (value: `"PERCENTAGE"`)

* `NONE` (value: `"NONE"`)

* `NIGHTS` (value: `"NIGHTS"`)

* `FLAT` (value: `"FLAT"`)




