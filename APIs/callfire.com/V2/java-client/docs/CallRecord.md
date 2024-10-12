

# CallRecord

Represents a call sent to a contact's number

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**answerTime** | **Long** | Timestamp when call was answered, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT |  [optional] [readonly] |
|**billedAmount** | **Float** | A cost of the call |  [optional] [readonly] |
|**callerName** | **String** | ~ |  [optional] [readonly] |
|**duration** | **Long** | Duration of the call in seconds |  [optional] [readonly] |
|**finishTime** | **Long** | Timestamp when call was finished, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT |  [optional] [readonly] |
|**id** | **Long** | An id of a call record |  [optional] |
|**labels** | **Set&lt;String&gt;** | Labels associated with a call action |  [optional] [readonly] |
|**notes** | [**List&lt;Note&gt;**](Note.md) | Notes of call added by agent |  [optional] |
|**originateTime** | **Long** | A date and time (timestamp) when call was originated by CallFire platform and went to downstream provider, formatted in unix time milliseconds (read only). Example: 1473781817000  |  [optional] [readonly] |
|**questionResponses** | [**List&lt;QuestionResponse&gt;**](QuestionResponse.md) | Notes of call added by an agent |  [optional] |
|**recordings** | [**List&lt;CallRecording&gt;**](CallRecording.md) | A list of voice recordings of the call |  [optional] |
|**result** | [**ResultEnum**](#ResultEnum) | ~ |  [optional] [readonly] |
|**switchId** | **String** | ~ |  [optional] [readonly] |
|**toNumber** | **String** | A phone number to which a call was addressed. Phone number in E.164 format (11-digit). Example: 12132000384 |  [optional] [readonly] |



## Enum: ResultEnum

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



