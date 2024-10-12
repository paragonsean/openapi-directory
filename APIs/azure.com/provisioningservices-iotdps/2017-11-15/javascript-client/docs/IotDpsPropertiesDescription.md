# IotDpsClient.IotDpsPropertiesDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocationPolicy** | **String** | Allocation policy to be used by this provisioning service. | [optional] 
**authorizationPolicies** | [**[SharedAccessSignatureAuthorizationRuleAccessRightsDescription]**](SharedAccessSignatureAuthorizationRuleAccessRightsDescription.md) | List of authorization keys for a provisioning service. | [optional] 
**deviceProvisioningHostName** | **String** | Device endpoint for this provisioning service. | [optional] [readonly] 
**idScope** | **String** | Unique identifier of this provisioning service. | [optional] [readonly] 
**iotHubs** | [**[IotHubDefinitionDescription]**](IotHubDefinitionDescription.md) | List of IoT hubs assosciated with this provisioning service. | [optional] 
**provisioningState** | **String** | The ARM provisioning state of the provisioning service. | [optional] 
**serviceOperationsHostName** | **String** | Service endpoint for provisioning service. | [optional] [readonly] 
**state** | **String** | Current state of the provisioning service. | [optional] 



## Enum: AllocationPolicyEnum


* `Hashed` (value: `"Hashed"`)

* `GeoLatency` (value: `"GeoLatency"`)

* `Static` (value: `"Static"`)





## Enum: StateEnum


* `Activating` (value: `"Activating"`)

* `Active` (value: `"Active"`)

* `Deleting` (value: `"Deleting"`)

* `Deleted` (value: `"Deleted"`)

* `ActivationFailed` (value: `"ActivationFailed"`)

* `DeletionFailed` (value: `"DeletionFailed"`)

* `Transitioning` (value: `"Transitioning"`)

* `Suspending` (value: `"Suspending"`)

* `Suspended` (value: `"Suspended"`)

* `Resuming` (value: `"Resuming"`)

* `FailingOver` (value: `"FailingOver"`)

* `FailoverFailed` (value: `"FailoverFailed"`)




