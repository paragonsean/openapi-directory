# ServiceUsageApi.ImportConsumerOverridesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **Boolean** | Whether to force the creation of the quota overrides. Setting the force parameter to &#39;true&#39; ignores all quota safety checks that would fail the request. QuotaSafetyCheck lists all such validations. | [optional] 
**forceOnly** | **[String]** | The list of quota safety checks to ignore before the override mutation. Unlike &#39;force&#39; field that ignores all the quota safety checks, the &#39;force_only&#39; field ignores only the specified checks; other checks are still enforced. The &#39;force&#39; and &#39;force_only&#39; fields cannot both be set. | [optional] 
**inlineSource** | [**OverrideInlineSource**](OverrideInlineSource.md) |  | [optional] 



## Enum: [ForceOnlyEnum]


* `QUOTA_SAFETY_CHECK_UNSPECIFIED` (value: `"QUOTA_SAFETY_CHECK_UNSPECIFIED"`)

* `LIMIT_DECREASE_BELOW_USAGE` (value: `"LIMIT_DECREASE_BELOW_USAGE"`)

* `LIMIT_DECREASE_PERCENTAGE_TOO_HIGH` (value: `"LIMIT_DECREASE_PERCENTAGE_TOO_HIGH"`)




