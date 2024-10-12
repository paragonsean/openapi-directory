

# Text

Represents a text action sent or received by CallFire platform

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | **Map&lt;String, String&gt;** | Map of user-defined string attributes associated with an action |  [optional] |
|**batchId** | **Long** | An id of contact batch associated with an action |  [optional] [readonly] |
|**campaignId** | **Long** | An id of broadcast if given text was sent as a part of text broadcast |  [optional] [readonly] |
|**contact** | [**Contact**](Contact.md) |  |  [optional] |
|**created** | **Long** | The time when the given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT |  [optional] [readonly] |
|**finalTextResult** | [**FinalTextResultEnum**](#FinalTextResultEnum) | Result of text (SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED). See [call states and results](https://developers.callfire.com/results-responses-errors.html) |  [optional] [readonly] |
|**fromNumber** | **String** | Sender&#39;s phone number in E.164 format (11-digit) or short code. Example: 12132000384, 67076 |  [optional] |
|**id** | **Long** | An id of an action |  [optional] |
|**inbound** | **Boolean** | An action inbound |  [optional] |
|**labels** | **Set&lt;String&gt;** | Labels associated with an action |  [optional] |
|**media** | [**List&lt;Media&gt;**](Media.md) | ~ |  [optional] |
|**message** | **String** | A text message |  [optional] |
|**modified** | **Long** | The time when the given resource was modified, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT |  [optional] [readonly] |
|**records** | [**List&lt;TextRecord&gt;**](TextRecord.md) | List of text records, each record contains additional details: time of sending, cost, current state.  A single contact may have multiple numbers. If given text was sent as part of broadcast with configured retry logic then each text record will contain details about attempted number |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Current state of an action (READY, SELECTED, CALLBACK, DISABLED, FINISHED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT). See [call states and results](https://developers.callfire.com/results-responses-errors.html) |  [optional] [readonly] |
|**toNumber** | **String** | Recipient&#39;s phone number in E.164 format (11-digit) or short code. Example: 12132000384, 67076 |  [optional] |



## Enum: FinalTextResultEnum

| Name | Value |
|---- | -----|
| SENT | &quot;SENT&quot; |
| RECEIVED | &quot;RECEIVED&quot; |
| DNT | &quot;DNT&quot; |
| TOO_BIG | &quot;TOO_BIG&quot; |
| INTERNAL_ERROR | &quot;INTERNAL_ERROR&quot; |
| CARRIER_ERROR | &quot;CARRIER_ERROR&quot; |
| CARRIER_TEMP_ERROR | &quot;CARRIER_TEMP_ERROR&quot; |
| UNDIALED | &quot;UNDIALED&quot; |
| INVALID_NUMBER | &quot;INVALID_NUMBER&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| READY | &quot;READY&quot; |
| SELECTED | &quot;SELECTED&quot; |
| CALLBACK | &quot;CALLBACK&quot; |
| FINISHED | &quot;FINISHED&quot; |
| DISABLED | &quot;DISABLED&quot; |
| SKIPPED | &quot;SKIPPED&quot; |
| DNC | &quot;DNC&quot; |
| DUP | &quot;DUP&quot; |
| INVALID | &quot;INVALID&quot; |
| TIMEOUT | &quot;TIMEOUT&quot; |
| PERIOD_LIMIT | &quot;PERIOD_LIMIT&quot; |
| RESTRICTED_NUMBER | &quot;RESTRICTED_NUMBER&quot; |



