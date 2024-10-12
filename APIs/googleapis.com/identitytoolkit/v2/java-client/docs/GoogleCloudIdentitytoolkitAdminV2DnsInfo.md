

# GoogleCloudIdentitytoolkitAdminV2DnsInfo

Information of custom domain DNS verification. By default, default_domain will be used. A custom domain can be configured using VerifyCustomDomain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**customDomain** | **String** | Output only. The applied verified custom domain. |  [optional] [readonly] |
|**customDomainState** | [**CustomDomainStateEnum**](#CustomDomainStateEnum) | Output only. The current verification state of the custom domain. The custom domain will only be used once the domain verification is successful. |  [optional] [readonly] |
|**domainVerificationRequestTime** | **String** | Output only. The timestamp of initial request for the current domain verification. |  [optional] [readonly] |
|**pendingCustomDomain** | **String** | Output only. The custom domain that&#39;s to be verified. |  [optional] [readonly] |
|**useCustomDomain** | **Boolean** | Whether to use custom domain. |  [optional] |



## Enum: CustomDomainStateEnum

| Name | Value |
|---- | -----|
| VERIFICATION_STATE_UNSPECIFIED | &quot;VERIFICATION_STATE_UNSPECIFIED&quot; |
| NOT_STARTED | &quot;NOT_STARTED&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| FAILED | &quot;FAILED&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |



