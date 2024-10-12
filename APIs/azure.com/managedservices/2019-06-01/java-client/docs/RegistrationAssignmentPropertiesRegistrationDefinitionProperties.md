

# RegistrationAssignmentPropertiesRegistrationDefinitionProperties

Properties of registration definition inside registration assignment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**authorizations** | [**List&lt;Authorization&gt;**](Authorization.md) | Authorization tuple containing principal id of the user/security group or service principal and id of the build-in role. |  [optional] |
|**description** | **String** | Description of the registration definition. |  [optional] |
|**managedByTenantId** | **String** | Id of the managedBy tenant. |  [optional] |
|**managedByTenantName** | **String** | Name of the managedBy tenant. |  [optional] |
|**manageeTenantId** | **String** | Id of the home tenant. |  [optional] |
|**manageeTenantName** | **String** | Name of the home tenant. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Current state of the registration definition. |  [optional] |
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



