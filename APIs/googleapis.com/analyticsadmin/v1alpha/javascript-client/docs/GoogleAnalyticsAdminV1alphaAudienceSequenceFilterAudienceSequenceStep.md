# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraintDuration** | **String** | Optional. When set, this step must be satisfied within the constraint_duration of the previous step (For example, t[i] - t[i-1] &lt;&#x3D; constraint_duration). If not set, there is no duration requirement (the duration is effectively unlimited). It is ignored for the first step. | [optional] 
**filterExpression** | [**GoogleAnalyticsAdminV1alphaAudienceFilterExpression**](GoogleAnalyticsAdminV1alphaAudienceFilterExpression.md) |  | [optional] 
**immediatelyFollows** | **Boolean** | Optional. If true, the event satisfying this step must be the very next event after the event satisfying the last step. If unset or false, this step indirectly follows the prior step; for example, there may be events between the prior step and this step. It is ignored for the first step. | [optional] 
**scope** | **String** | Required. Immutable. Specifies the scope for this step. | [optional] 



## Enum: ScopeEnum


* `UNSPECIFIED` (value: `"AUDIENCE_FILTER_SCOPE_UNSPECIFIED"`)

* `WITHIN_SAME_EVENT` (value: `"AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT"`)

* `WITHIN_SAME_SESSION` (value: `"AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION"`)

* `ACROSS_ALL_SESSIONS` (value: `"AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS"`)




