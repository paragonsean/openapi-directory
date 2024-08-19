

# CustomDomainProperties

The JSON object that contains the properties of the custom domain to create.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customHttpsProvisioningState** | [**CustomHttpsProvisioningStateEnum**](#CustomHttpsProvisioningStateEnum) | Provisioning status of Custom Https of the custom domain. |  [optional] [readonly] |
|**customHttpsProvisioningSubstate** | [**CustomHttpsProvisioningSubstateEnum**](#CustomHttpsProvisioningSubstateEnum) | Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step. |  [optional] [readonly] |
|**hostName** | **String** | The host name of the custom domain. Must be a domain name. |  |
|**provisioningState** | **String** | Provisioning status of the custom domain. |  [optional] [readonly] |
|**resourceState** | [**ResourceStateEnum**](#ResourceStateEnum) | Resource status of the custom domain. |  [optional] [readonly] |
|**validationData** | **String** | Special validation or data may be required when delivering CDN to some regions due to local compliance reasons. E.g. ICP license number of a custom domain is required to deliver content in China. |  [optional] |



## Enum: CustomHttpsProvisioningStateEnum

| Name | Value |
|---- | -----|
| ENABLING | &quot;Enabling&quot; |
| ENABLED | &quot;Enabled&quot; |
| DISABLING | &quot;Disabling&quot; |
| DISABLED | &quot;Disabled&quot; |
| FAILED | &quot;Failed&quot; |



## Enum: CustomHttpsProvisioningSubstateEnum

| Name | Value |
|---- | -----|
| SUBMITTING_DOMAIN_CONTROL_VALIDATION_REQUEST | &quot;SubmittingDomainControlValidationRequest&quot; |
| PENDING_DOMAIN_CONTROL_VALIDATION_R_EQUEST_APPROVAL | &quot;PendingDomainControlValidationREquestApproval&quot; |
| DOMAIN_CONTROL_VALIDATION_REQUEST_APPROVED | &quot;DomainControlValidationRequestApproved&quot; |
| DOMAIN_CONTROL_VALIDATION_REQUEST_REJECTED | &quot;DomainControlValidationRequestRejected&quot; |
| DOMAIN_CONTROL_VALIDATION_REQUEST_TIMED_OUT | &quot;DomainControlValidationRequestTimedOut&quot; |
| ISSUING_CERTIFICATE | &quot;IssuingCertificate&quot; |
| DEPLOYING_CERTIFICATE | &quot;DeployingCertificate&quot; |
| CERTIFICATE_DEPLOYED | &quot;CertificateDeployed&quot; |
| DELETING_CERTIFICATE | &quot;DeletingCertificate&quot; |
| CERTIFICATE_DELETED | &quot;CertificateDeleted&quot; |



## Enum: ResourceStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| ACTIVE | &quot;Active&quot; |
| DELETING | &quot;Deleting&quot; |



