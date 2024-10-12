

# RegistrationDefinitionProperties

Properties of a registration definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizations** | [**List&lt;Authorization&gt;**](Authorization.md) | Authorization tuple containing principal id of the user/security group or service principal and id of the build-in role. |  |
|**description** | **String** | Description of the registration definition. |  [optional] |
|**managedByTenantId** | **String** | Id of the managedBy tenant. |  |
|**managedByTenantName** | **String** | Name of the managedBy tenant. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Current state of the registration definition. |  [optional] [readonly] |
|**registrationDefinitionName** | **String** | Name of the registration definition. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| NOT_SPECIFIED | &quot;NotSpecified&quot; |
| ACCEPTED | &quot;Accepted&quot; |
| RUNNING | &quot;Running&quot; |
| READY | &quot;Ready&quot; |
| CREATING | &quot;Creating&quot; |
| CREATED | &quot;Created&quot; |
| DELETING | &quot;Deleting&quot; |
| DELETED | &quot;Deleted&quot; |
| CANCELED | &quot;Canceled&quot; |
| FAILED | &quot;Failed&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |



