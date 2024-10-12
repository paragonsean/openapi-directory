

# ModelResult

Result of a model status query operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdDateTime** | **OffsetDateTime** | Get or set the created date time of the model. |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** | Get or set the model last updated datetime. |  [optional] |
|**modelId** | **UUID** | Get or set model identifier. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Get or set the status of model. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CREATED | &quot;created&quot; |
| READY | &quot;ready&quot; |
| INVALID | &quot;invalid&quot; |



