# ManagedServicesClient.RegistrationAssignmentPropertiesRegistrationDefinitionProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizations** | [**[Authorization]**](Authorization.md) | Authorization tuple containing principal id of the user/security group or service principal and id of the build-in role. | [optional] 
**description** | **String** | Description of the registration definition. | [optional] 
**managedByTenantId** | **String** | Id of the managedBy tenant. | [optional] 
**managedByTenantName** | **String** | Name of the managedBy tenant. | [optional] 
**manageeTenantId** | **String** | Id of the home tenant. | [optional] 
**manageeTenantName** | **String** | Name of the home tenant. | [optional] 
**provisioningState** | **String** | Current state of the registration definition. | [optional] 
**registrationDefinitionName** | **String** | Name of the registration definition. | [optional] 



## Enum: ProvisioningStateEnum


* `NotSpecified` (value: `"NotSpecified"`)

* `Accepted` (value: `"Accepted"`)

* `Running` (value: `"Running"`)

* `Ready` (value: `"Ready"`)

* `Creating` (value: `"Creating"`)

* `Created` (value: `"Created"`)

* `Deleting` (value: `"Deleting"`)

* `Deleted` (value: `"Deleted"`)

* `Canceled` (value: `"Canceled"`)

* `Failed` (value: `"Failed"`)

* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)




