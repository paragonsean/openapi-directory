

# FrontendEndpointProperties

The JSON object that contains the properties required to create a frontend endpoint.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customHttpsConfiguration** | [**CustomHttpsConfiguration**](CustomHttpsConfiguration.md) |  |  [optional] |
|**customHttpsProvisioningState** | [**CustomHttpsProvisioningStateEnum**](#CustomHttpsProvisioningStateEnum) | Provisioning status of Custom Https of the frontendEndpoint. |  [optional] [readonly] |
|**customHttpsProvisioningSubstate** | [**CustomHttpsProvisioningSubstateEnum**](#CustomHttpsProvisioningSubstateEnum) | Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step. |  [optional] [readonly] |
|**resourceState** | **ResourceState** |  |  [optional] |
|**hostName** | **String** | The host name of the frontendEndpoint. Must be a domain name. |  [optional] |
|**sessionAffinityEnabledState** | [**SessionAffinityEnabledStateEnum**](#SessionAffinityEnabledStateEnum) | Whether to allow session affinity on this host. Valid options are &#39;Enabled&#39; or &#39;Disabled&#39; |  [optional] |
|**sessionAffinityTtlSeconds** | **Integer** | UNUSED. This field will be ignored. The TTL to use in seconds for session affinity, if applicable. |  [optional] |
|**webApplicationFirewallPolicyLink** | [**FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLink**](FrontendEndpointUpdateParametersWebApplicationFirewallPolicyLink.md) |  |  [optional] |



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



## Enum: SessionAffinityEnabledStateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



