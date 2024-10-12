# CdnManagementClient.CustomDomainProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customHttpsProvisioningState** | **String** | Provisioning status of Custom Https of the custom domain. | [optional] [readonly] 
**customHttpsProvisioningSubstate** | **String** | Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step. | [optional] [readonly] 
**hostName** | **String** | The host name of the custom domain. Must be a domain name. | 
**provisioningState** | **String** | Provisioning status of the custom domain. | [optional] [readonly] 
**resourceState** | **String** | Resource status of the custom domain. | [optional] [readonly] 
**validationData** | **String** | Special validation or data may be required when delivering CDN to some regions due to local compliance reasons. E.g. ICP license number of a custom domain is required to deliver content in China. | [optional] 



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





## Enum: ResourceStateEnum


* `Creating` (value: `"Creating"`)

* `Active` (value: `"Active"`)

* `Deleting` (value: `"Deleting"`)




