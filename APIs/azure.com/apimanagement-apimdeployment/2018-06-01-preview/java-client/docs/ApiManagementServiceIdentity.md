

# ApiManagementServiceIdentity

Identity properties of the Api Management service resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **UUID** | The principal id of the identity. |  [optional] [readonly] |
|**tenantId** | **UUID** | The client tenant id of the identity. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The identity type. Currently the only supported type is &#39;SystemAssigned&#39;. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SYSTEM_ASSIGNED | &quot;SystemAssigned&quot; |



