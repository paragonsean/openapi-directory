# FrontDoorManagementClient.FrontendEndpointProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customHttpsConfiguration** | [**CustomHttpsConfiguration**](CustomHttpsConfiguration.md) |  | [optional] 
**customHttpsProvisioningState** | **String** | Provisioning status of Custom Https of the frontendEndpoint. | [optional] [readonly] 
**customHttpsProvisioningSubstate** | **String** | Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step. | [optional] [readonly] 
**resourceState** | [**ResourceState**](ResourceState.md) |  | [optional] 
**hostName** | **String** | The host name of the frontendEndpoint. Must be a domain name. | [optional] 
**sessionAffinityEnabledState** | **String** | Whether to allow session affinity on this host. Valid options are &#39;Enabled&#39; or &#39;Disabled&#39; | [optional] 
**sessionAffinityTtlSeconds** | **Number** | UNUSED. This field will be ignored. The TTL to use in seconds for session affinity, if applicable. | [optional] 
**webApplicationFirewallPolicyLink** | [**FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLink**](FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLink.md) |  | [optional] 



## Enum: CustomHttpsProvisioningStateEnum


* `Enabling` (value: `"Enabling"`)

* `Enabled` (value: `"Enabled"`)

* `Disabling` (value: `"Disabling"`)

* `Disabled` (value: `"Disabled"`)

* `Failed` (value: `"Failed"`)





## Enum: CustomHttpsProvisioningSubstateEnum


* `SubmittingDomainControlValidationRequest` (value: `"SubmittingDomainControlValidationRequest"`)

* `PendingDomainControlValidationREquestApproval` (value: `"PendingDomainControlValidationREquestApproval"`)

* `DomainControlValidationRequestApproved` (value: `"DomainControlValidationRequestApproved"`)

* `DomainControlValidationRequestRejected` (value: `"DomainControlValidationRequestRejected"`)

* `DomainControlValidationRequestTimedOut` (value: `"DomainControlValidationRequestTimedOut"`)

* `IssuingCertificate` (value: `"IssuingCertificate"`)

* `DeployingCertificate` (value: `"DeployingCertificate"`)

* `CertificateDeployed` (value: `"CertificateDeployed"`)

* `DeletingCertificate` (value: `"DeletingCertificate"`)

* `CertificateDeleted` (value: `"CertificateDeleted"`)





## Enum: SessionAffinityEnabledStateEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




