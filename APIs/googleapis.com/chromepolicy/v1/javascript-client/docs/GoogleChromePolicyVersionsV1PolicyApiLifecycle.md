# ChromePolicyApi.GoogleChromePolicyVersionsV1PolicyApiLifecycle

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecatedInFavorOf** | **[String]** | In the event that this policy was deprecated in favor of another policy, the fully qualified namespace(s) of the new policies as they will show in PolicyAPI. Could only be set if policy_api_lifecycle_stage is API_DEPRECATED. | [optional] 
**description** | **String** | Description about current life cycle. | [optional] 
**endSupport** | [**GoogleTypeDate**](GoogleTypeDate.md) |  | [optional] 
**policyApiLifecycleStage** | **String** | Indicates current life cycle stage of the policy API. | [optional] 
**scheduledToDeprecatePolicies** | **[String]** | Corresponding to deprecated_in_favor_of, the fully qualified namespace(s) of the old policies that will be deprecated because of introduction of this policy. This field should not be manually set but will be set and exposed through PolicyAPI automatically. | [optional] 



## Enum: PolicyApiLifecycleStageEnum


* `UNSPECIFIED` (value: `"API_UNSPECIFIED"`)

* `PREVIEW` (value: `"API_PREVIEW"`)

* `DEVELOPMENT` (value: `"API_DEVELOPMENT"`)

* `CURRENT` (value: `"API_CURRENT"`)

* `DEPRECATED` (value: `"API_DEPRECATED"`)




