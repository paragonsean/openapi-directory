

# GoogleChromePolicyVersionsV1PolicyApiLifecycle

Lifecycle information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deprecatedInFavorOf** | **List&lt;String&gt;** | In the event that this policy was deprecated in favor of another policy, the fully qualified namespace(s) of the new policies as they will show in PolicyAPI. Could only be set if policy_api_lifecycle_stage is API_DEPRECATED. |  [optional] |
|**description** | **String** | Description about current life cycle. |  [optional] |
|**endSupport** | [**GoogleTypeDate**](GoogleTypeDate.md) |  |  [optional] |
|**policyApiLifecycleStage** | [**PolicyApiLifecycleStageEnum**](#PolicyApiLifecycleStageEnum) | Indicates current life cycle stage of the policy API. |  [optional] |
|**scheduledToDeprecatePolicies** | **List&lt;String&gt;** | Corresponding to deprecated_in_favor_of, the fully qualified namespace(s) of the old policies that will be deprecated because of introduction of this policy. This field should not be manually set but will be set and exposed through PolicyAPI automatically. |  [optional] |



## Enum: PolicyApiLifecycleStageEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;API_UNSPECIFIED&quot; |
| PREVIEW | &quot;API_PREVIEW&quot; |
| DEVELOPMENT | &quot;API_DEVELOPMENT&quot; |
| CURRENT | &quot;API_CURRENT&quot; |
| DEPRECATED | &quot;API_DEPRECATED&quot; |



