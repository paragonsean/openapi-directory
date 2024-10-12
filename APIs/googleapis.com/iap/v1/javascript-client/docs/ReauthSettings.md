# CloudIdentityAwareProxyApi.ReauthSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxAge** | **String** | Reauth session lifetime, how long before a user has to reauthenticate again. | [optional] 
**method** | **String** | Reauth method requested. | [optional] 
**policyType** | **String** | How IAP determines the effective policy in cases of hierarchical policies. Policies are merged from higher in the hierarchy to lower in the hierarchy. | [optional] 



## Enum: MethodEnum


* `METHOD_UNSPECIFIED` (value: `"METHOD_UNSPECIFIED"`)

* `LOGIN` (value: `"LOGIN"`)

* `PASSWORD` (value: `"PASSWORD"`)

* `SECURE_KEY` (value: `"SECURE_KEY"`)

* `ENROLLED_SECOND_FACTORS` (value: `"ENROLLED_SECOND_FACTORS"`)





## Enum: PolicyTypeEnum


* `POLICY_TYPE_UNSPECIFIED` (value: `"POLICY_TYPE_UNSPECIFIED"`)

* `MINIMUM` (value: `"MINIMUM"`)

* `DEFAULT` (value: `"DEFAULT"`)




