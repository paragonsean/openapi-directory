# CallFireApiDocumentation.TextRecord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billedAmount** | **Number** | A cost of a sent text | [optional] [readonly] 
**callerName** | **String** | ~ | [optional] [readonly] 
**finishTime** | **Number** | A time when the given resource was updated, formatted in unix time milliseconds (read only). Example: 1473781817000 | [optional] [readonly] 
**id** | **Number** | An id of a text record | [optional] 
**labels** | **[String]** | Labels associated with a text action | [optional] [readonly] 
**message** | **String** | A text message | [optional] 
**switchId** | **String** | ~ | [optional] [readonly] 
**textResult** | **String** | Result of a text (SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED). See [call states and results](https://developers.callfire.com/results-responses-errors.html) | [optional] 
**toNumber** | **String** | An attempted phone number | [optional] [readonly] 



## Enum: TextResultEnum


* `SENT` (value: `"SENT"`)

* `RECEIVED` (value: `"RECEIVED"`)

* `DNT` (value: `"DNT"`)

* `TOO_BIG` (value: `"TOO_BIG"`)

* `INTERNAL_ERROR` (value: `"INTERNAL_ERROR"`)

* `CARRIER_ERROR` (value: `"CARRIER_ERROR"`)

* `CARRIER_TEMP_ERROR` (value: `"CARRIER_TEMP_ERROR"`)

* `UNDIALED` (value: `"UNDIALED"`)

* `INVALID_NUMBER` (value: `"INVALID_NUMBER"`)




