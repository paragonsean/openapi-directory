# BulkSmsJsonRestApi.MessageStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | A concatenated value A.B where A is the &#x60;status.type&#x60; and B is the &#x60;status.subtype&#x60;.   It there is no value for &#x60;subtype&#x60; then B takes string value &#x60;\&quot;null\&quot;&#x60; (e.g. &#x60;\&quot;SENT.null\&quot;&#x60;).     | 
**subtype** | **String** | Has a value only if the &#x60;type&#x60; is FAILED.  EXPIRED  Delivery failed because message expired before delivery was possible.  HANDSET_ERROR  Delivery failed because of a problem related to the phone (e.g. message storage area full).  BLOCKED  Your account has been blocked from sending to this phone (e.g. recipient replied STOP to block communication).  NOT_SENT  Message delivery was not attempted (e.g. because we were not able to find a route for the supplied phone number).  | [optional] 
**type** | **String** |  ACCEPTED  Message accepted for delivery. Only returned for initial message submissions.  SCHEDULED  Message accepted for delivery at a later date. Only returned for initial message  submissions.  SENT  Message has been relayed away from our systems.  DELIVERED  Successfully delivered to phone.  UNKNOWN  Message is in an unknown state.  FAILED  Delivery failed.  | 



## Enum: SubtypeEnum


* `EXPIRED` (value: `"EXPIRED"`)

* `HANDSET_ERROR` (value: `"HANDSET_ERROR"`)

* `BLOCKED` (value: `"BLOCKED"`)

* `NOT_SENT` (value: `"NOT_SENT"`)





## Enum: TypeEnum


* `ACCEPTED` (value: `"ACCEPTED"`)

* `SCHEDULED` (value: `"SCHEDULED"`)

* `SENT` (value: `"SENT"`)

* `DELIVERED` (value: `"DELIVERED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `FAILED` (value: `"FAILED"`)




