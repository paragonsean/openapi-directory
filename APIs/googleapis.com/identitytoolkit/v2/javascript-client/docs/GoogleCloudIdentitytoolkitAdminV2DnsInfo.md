# IdentityToolkitApi.GoogleCloudIdentitytoolkitAdminV2DnsInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customDomain** | **String** | Output only. The applied verified custom domain. | [optional] [readonly] 
**customDomainState** | **String** | Output only. The current verification state of the custom domain. The custom domain will only be used once the domain verification is successful. | [optional] [readonly] 
**domainVerificationRequestTime** | **String** | Output only. The timestamp of initial request for the current domain verification. | [optional] [readonly] 
**pendingCustomDomain** | **String** | Output only. The custom domain that&#39;s to be verified. | [optional] [readonly] 
**useCustomDomain** | **Boolean** | Whether to use custom domain. | [optional] 



## Enum: CustomDomainStateEnum


* `VERIFICATION_STATE_UNSPECIFIED` (value: `"VERIFICATION_STATE_UNSPECIFIED"`)

* `NOT_STARTED` (value: `"NOT_STARTED"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `FAILED` (value: `"FAILED"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)




