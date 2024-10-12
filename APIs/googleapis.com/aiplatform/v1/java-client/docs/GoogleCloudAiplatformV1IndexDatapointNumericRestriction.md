

# GoogleCloudAiplatformV1IndexDatapointNumericRestriction

This field allows restricts to be based on numeric comparisons rather than categorical tokens.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**namespace** | **String** | The namespace of this restriction. e.g.: cost. |  [optional] |
|**op** | [**OpEnum**](#OpEnum) | This MUST be specified for queries and must NOT be specified for datapoints. |  [optional] |
|**valueDouble** | **Double** | Represents 64 bit float. |  [optional] |
|**valueFloat** | **Float** | Represents 32 bit float. |  [optional] |
|**valueInt** | **String** | Represents 64 bit integer. |  [optional] |



## Enum: OpEnum

| Name | Value |
|---- | -----|
| OPERATOR_UNSPECIFIED | &quot;OPERATOR_UNSPECIFIED&quot; |
| LESS | &quot;LESS&quot; |
| LESS_EQUAL | &quot;LESS_EQUAL&quot; |
| EQUAL | &quot;EQUAL&quot; |
| GREATER_EQUAL | &quot;GREATER_EQUAL&quot; |
| GREATER | &quot;GREATER&quot; |
| NOT_EQUAL | &quot;NOT_EQUAL&quot; |



