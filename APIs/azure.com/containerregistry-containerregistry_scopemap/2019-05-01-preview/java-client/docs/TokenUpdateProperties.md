

# TokenUpdateProperties

The parameters for updating token properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**credentials** | [**TokenCredentialsProperties**](TokenCredentialsProperties.md) |  |  [optional] |
|**scopeMapId** | **String** | The resource ID of the scope map to which the token will be associated with. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the token example enabled or disabled. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| DISABLED | &quot;disabled&quot; |



