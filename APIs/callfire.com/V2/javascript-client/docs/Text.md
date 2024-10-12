# CallFireApiDocumentation.Text

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **{String: String}** | Map of user-defined string attributes associated with an action | [optional] 
**batchId** | **Number** | An id of contact batch associated with an action | [optional] [readonly] 
**campaignId** | **Number** | An id of broadcast if given text was sent as a part of text broadcast | [optional] [readonly] 
**contact** | [**Contact**](Contact.md) |  | [optional] 
**created** | **Number** | The time when the given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] [readonly] 
**finalTextResult** | **String** | Result of text (SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED). See [call states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] [readonly] 
**fromNumber** | **String** | Sender&#39;s phone number in E.164 format (11-digit) or short code. Example: 12132000384, 67076 | [optional] 
**id** | **Number** | An id of an action | [optional] 
**inbound** | **Boolean** | An action inbound | [optional] 
**labels** | **[String]** | Labels associated with an action | [optional] 
**media** | [**[Media]**](Media.md) | ~ | [optional] 
**message** | **String** | A text message | [optional] 
**modified** | **Number** | The time when the given resource was modified, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] [readonly] 
**records** | [**[TextRecord]**](TextRecord.md) | List of text records, each record contains additional details: time of sending, cost, current state.  A single contact may have multiple numbers. If given text was sent as part of broadcast with configured retry logic then each text record will contain details about attempted number | [optional] 
**state** | **String** | Current state of an action (READY, SELECTED, CALLBACK, DISABLED, FINISHED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT). See [call states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] [readonly] 
**toNumber** | **String** | Recipient&#39;s phone number in E.164 format (11-digit) or short code. Example: 12132000384, 67076 | [optional] 



## Enum: FinalTextResultEnum


* `SENT` (value: `"SENT"`)

* `RECEIVED` (value: `"RECEIVED"`)

* `DNT` (value: `"DNT"`)

* `TOO_BIG` (value: `"TOO_BIG"`)

* `INTERNAL_ERROR` (value: `"INTERNAL_ERROR"`)

* `CARRIER_ERROR` (value: `"CARRIER_ERROR"`)

* `CARRIER_TEMP_ERROR` (value: `"CARRIER_TEMP_ERROR"`)

* `UNDIALED` (value: `"UNDIALED"`)

* `INVALID_NUMBER` (value: `"INVALID_NUMBER"`)





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




