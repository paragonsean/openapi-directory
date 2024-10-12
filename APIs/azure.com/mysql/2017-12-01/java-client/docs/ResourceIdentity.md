

# ResourceIdentity

Azure Active Directory identity configuration for a resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **UUID** | The Azure Active Directory principal id. |  [optional] [readonly] |
|**tenantId** | **UUID** | The Azure Active Directory tenant id. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The identity type. Set this to &#39;SystemAssigned&#39; in order to automatically create and assign an Azure Active Directory principal for the resource. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SYSTEM_ASSIGNED | &quot;SystemAssigned&quot; |



