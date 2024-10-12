

# ValidateRequest

Resource validation request content.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | **String** | Expected location of the resource. |  |
|**name** | **String** | Resource name to verify. |  |
|**properties** | [**ValidateProperties**](ValidateProperties.md) |  |  |
|**type** | [**TypeEnum**](#TypeEnum) | Resource type used for verification. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SERVER_FARM | &quot;ServerFarm&quot; |
| SITE | &quot;Site&quot; |



