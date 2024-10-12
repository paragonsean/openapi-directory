# CallFireApiDocumentation.Call

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentCall** | **Boolean** | An internal call to an agent | [optional] [readonly] 
**attributes** | **{String: String}** | Map of user-defined string attributes associated with an action | [optional] 
**batchId** | **Number** | An id of contact batch associated with an action | [optional] [readonly] 
**campaignId** | **Number** | An id of broadcast associated with an action if call is sent as part of call broadcast | [optional] [readonly] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**created** | **Number** | The time when the given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT  | [optional] [readonly] 
**finalCallResult** | **String** | Result of a call (LA, AM, BUSY, DNC, XFER, NO_ANS, XFER_LEG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED, SD, POSTPONED, ABANDONED, SKIPPED). See [call states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] [readonly] 
**fromNumber** | **String** | A sender&#39;s phone number in E.164 (11-digit) format | [optional] 
**id** | **Number** | An id of  an action | [optional] 
**inbound** | **Boolean** | Is action inbound | [optional] 
**labels** | **[String]** | Labels associated with action or broadcast for this action | [optional] 
**modified** | **Number** | The time when the given resource was modified, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT  | [optional] [readonly] 
**notes** | [**[Note]**](Note.md) | Notes of call added by an agent | [optional] 
**records** | [**[CallRecord]**](CallRecord.md) | List of call records, each record contains call details like originate time, duration, cost, notes made by agents. A single contact may have a multiple phone numbers. In this case if given call was sent as a part of broadcast with configured retry logic then each call record will contain details about attempted phone number | [optional] [readonly] 
**state** | **String** | State of an action (READY, SELECTED, CALLBACK, DISABLED, FINISHED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT). See [call states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] [readonly] 
**toNumber** | **String** | A recipient&#39;s phone number in E.164 (11-digit) format | [optional] 



## Enum: FinalCallResultEnum


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





## Enum: StateEnum


* `READY` (value: `"READY"`)

* `SELECTED` (value: `"SELECTED"`)

* `CALLBACK` (value: `"CALLBACK"`)

* `FINISHED` (value: `"FINISHED"`)

* `DISABLED` (value: `"DISABLED"`)

* `SKIPPED` (value: `"SKIPPED"`)

* `DNC` (value: `"DNC"`)

* `DUP` (value: `"DUP"`)

* `INVALID` (value: `"INVALID"`)

* `TIMEOUT` (value: `"TIMEOUT"`)

* `PERIOD_LIMIT` (value: `"PERIOD_LIMIT"`)

* `RESTRICTED_NUMBER` (value: `"RESTRICTED_NUMBER"`)




