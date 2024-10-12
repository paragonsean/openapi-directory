

# TextRecord

Represents a text message sent to a contact's number

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billedAmount** | **Float** | A cost of a sent text |  [optional] [readonly] |
|**callerName** | **String** | ~ |  [optional] [readonly] |
|**finishTime** | **Long** | A time when the given resource was updated, formatted in unix time milliseconds (read only). Example: 1473781817000 |  [optional] [readonly] |
|**id** | **Long** | An id of a text record |  [optional] |
|**labels** | **Set&lt;String&gt;** | Labels associated with a text action |  [optional] [readonly] |
|**message** | **String** | A text message |  [optional] |
|**switchId** | **String** | ~ |  [optional] [readonly] |
|**textResult** | [**TextResultEnum**](#TextResultEnum) | Result of a text (SENT, RECEIVED, DNT, TOO_BIG, INTERNAL_ERROR, CARRIER_ERROR, CARRIER_TEMP_ERROR, UNDIALED). See [call states and results](https://developers.callfire.com/results-responses-errors.html) |  [optional] |
|**toNumber** | **String** | An attempted phone number |  [optional] [readonly] |



## Enum: TextResultEnum

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



