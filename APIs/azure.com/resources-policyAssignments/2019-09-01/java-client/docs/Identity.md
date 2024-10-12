

# Identity

Identity for the resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **String** | The principal ID of the resource identity. |  [optional] [readonly] |
|**tenantId** | **String** | The tenant ID of the resource identity. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The identity type. This is the only required field when adding a system assigned identity to a resource. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SYSTEM_ASSIGNED | &quot;SystemAssigned&quot; |
| NONE | &quot;None&quot; |



