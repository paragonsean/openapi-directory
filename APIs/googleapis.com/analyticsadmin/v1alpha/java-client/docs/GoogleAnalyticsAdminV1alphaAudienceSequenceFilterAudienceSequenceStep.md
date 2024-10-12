

# GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep

A condition that must occur in the specified step order for this user to match the sequence.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**constraintDuration** | **String** | Optional. When set, this step must be satisfied within the constraint_duration of the previous step (For example, t[i] - t[i-1] &lt;&#x3D; constraint_duration). If not set, there is no duration requirement (the duration is effectively unlimited). It is ignored for the first step. |  [optional] |
|**filterExpression** | [**GoogleAnalyticsAdminV1alphaAudienceFilterExpression**](GoogleAnalyticsAdminV1alphaAudienceFilterExpression.md) |  |  [optional] |
|**immediatelyFollows** | **Boolean** | Optional. If true, the event satisfying this step must be the very next event after the event satisfying the last step. If unset or false, this step indirectly follows the prior step; for example, there may be events between the prior step and this step. It is ignored for the first step. |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | Required. Immutable. Specifies the scope for this step. |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AUDIENCE_FILTER_SCOPE_UNSPECIFIED&quot; |
| WITHIN_SAME_EVENT | &quot;AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT&quot; |
| WITHIN_SAME_SESSION | &quot;AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION&quot; |
| ACROSS_ALL_SESSIONS | &quot;AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS&quot; |



