# CallFireApiDocumentation.CallRecord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answerTime** | **Number** | Timestamp when call was answered, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] [readonly] 
**billedAmount** | **Number** | A cost of the call | [optional] [readonly] 
**callerName** | **String** | ~ | [optional] [readonly] 
**duration** | **Number** | Duration of the call in seconds | [optional] [readonly] 
**finishTime** | **Number** | Timestamp when call was finished, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] [readonly] 
**id** | **Number** | An id of a call record | [optional] 
**labels** | **[String]** | Labels associated with a call action | [optional] [readonly] 
**notes** | [**[Note]**](Note.md) | Notes of call added by agent | [optional] 
**originateTime** | **Number** | A date and time (timestamp) when call was originated by CallFire platform and went to downstream provider, formatted in unix time milliseconds (read only). Example: 1473781817000  | [optional] [readonly] 
**questionResponses** | [**[QuestionResponse]**](QuestionResponse.md) | Notes of call added by an agent | [optional] 
**recordings** | [**[CallRecording]**](CallRecording.md) | A list of voice recordings of the call | [optional] 
**result** | **String** | ~ | [optional] [readonly] 
**switchId** | **String** | ~ | [optional] [readonly] 
**toNumber** | **String** | A phone number to which a call was addressed. Phone number in E.164 format (11-digit). Example: 12132000384 | [optional] [readonly] 



## Enum: ResultEnum


* `LA` (value: `"LA"`)

* `AM` (value: `"AM"`)

* `BUSY` (value: `"BUSY"`)

* `DNC` (value: `"DNC"`)

* `XFER` (value: `"XFER"`)

* `NO_ANS` (value: `"NO_ANS"`)

* `XFER_LEG` (value: `"XFER_LEG"`)

* `INTERNAL_ERROR` (value: `"INTERNAL_ERROR"`)

* `CARRIER_ERROR` (value: `"CARRIER_ERROR"`)

* `CARRIER_TEMP_ERROR` (value: `"CARRIER_TEMP_ERROR"`)

* `UNDIALED` (value: `"UNDIALED"`)

* `SD` (value: `"SD"`)

* `POSTPONED` (value: `"POSTPONED"`)

* `ABANDONED` (value: `"ABANDONED"`)

* `SKIPPED` (value: `"SKIPPED"`)




