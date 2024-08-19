

# ModelInfo

Basic custom model information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdDateTime** | **OffsetDateTime** | Date and time (UTC) when the model was created. |  |
|**lastUpdatedDateTime** | **OffsetDateTime** | Date and time (UTC) when the status was last updated. |  |
|**modelId** | **UUID** | Model identifier. |  |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the model. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;creating&quot; |
| READY | &quot;ready&quot; |
| INVALID | &quot;invalid&quot; |



