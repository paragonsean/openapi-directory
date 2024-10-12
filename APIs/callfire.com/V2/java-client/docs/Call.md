

# Call

Represents a call action sent or received by CallFire platform

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentCall** | **Boolean** | An internal call to an agent |  [optional] [readonly] |
|**attributes** | **Map&lt;String, String&gt;** | Map of user-defined string attributes associated with an action |  [optional] |
|**batchId** | **Long** | An id of contact batch associated with an action |  [optional] [readonly] |
|**campaignId** | **Long** | An id of broadcast associated with an action if call is sent as part of call broadcast |  [optional] [readonly] |
|**contact** | [**Contact**](Contact.md) |  |  [optional] |
|**created** | **Long** | The time when the given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT  |  [optional] [readonly] |
|**finalCallResult** | [**FinalCallResultEnum**](#FinalCallResultEnum) | Result of a call (LA, AM, BUSY, DNC, XFER, NO_ANS, XFER_LEG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED, SD, POSTPONED, ABANDONED, SKIPPED). See [call states and results](https://developers.callfire.com/results-responses-errors.html) |  [optional] [readonly] |
|**fromNumber** | **String** | A sender&#39;s phone number in E.164 (11-digit) format |  [optional] |
|**id** | **Long** | An id of  an action |  [optional] |
|**inbound** | **Boolean** | Is action inbound |  [optional] |
|**labels** | **Set&lt;String&gt;** | Labels associated with action or broadcast for this action |  [optional] |
|**modified** | **Long** | The time when the given resource was modified, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT  |  [optional] [readonly] |
|**notes** | [**List&lt;Note&gt;**](Note.md) | Notes of call added by an agent |  [optional] |
|**records** | [**List&lt;CallRecord&gt;**](CallRecord.md) | List of call records, each record contains call details like originate time, duration, cost, notes made by agents. A single contact may have a multiple phone numbers. In this case if given call was sent as a part of broadcast with configured retry logic then each call record will contain details about attempted phone number |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | State of an action (READY, SELECTED, CALLBACK, DISABLED, FINISHED, DNC, DUP, INVALID, TIMEOUT, PERIOD_LIMIT). See [call states and results](https://developers.callfire.com/results-responses-errors.html) |  [optional] [readonly] |
|**toNumber** | **String** | A recipient&#39;s phone number in E.164 (11-digit) format |  [optional] |



## Enum: FinalCallResultEnum

| Name | Value |
|---- | -----|
| LA | &quot;LA&quot; |
| AM | &quot;AM&quot; |
| BUSY | &quot;BUSY&quot; |
| DNC | &quot;DNC&quot; |
| XFER | &quot;XFER&quot; |
| NO_ANS | &quot;NO_ANS&quot; |
| XFER_LEG | &quot;XFER_LEG&quot; |
| INTERNAL_ERROR | &quot;INTERNAL_ERROR&quot; |
| CARRIER_ERROR | &quot;CARRIER_ERROR&quot; |
| CARRIER_TEMP_ERROR | &quot;CARRIER_TEMP_ERROR&quot; |
| UNDIALED | &quot;UNDIALED&quot; |
| SD | &quot;SD&quot; |
| POSTPONED | &quot;POSTPONED&quot; |
| ABANDONED | &quot;ABANDONED&quot; |
| SKIPPED | &quot;SKIPPED&quot; |



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



