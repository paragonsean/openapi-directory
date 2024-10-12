

# TagsPatchResource

Wrapper resource for tags patch API request only.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**operation** | [**OperationEnum**](#OperationEnum) | The operation type for the patch API. |  [optional] |
|**properties** | [**Tags**](Tags.md) |  |  [optional] |



## Enum: OperationEnum

| Name | Value |
|---- | -----|
| REPLACE | &quot;Replace&quot; |
| MERGE | &quot;Merge&quot; |
| DELETE | &quot;Delete&quot; |



