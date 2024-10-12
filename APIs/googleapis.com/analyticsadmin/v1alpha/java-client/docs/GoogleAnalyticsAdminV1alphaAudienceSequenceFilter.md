

# GoogleAnalyticsAdminV1alphaAudienceSequenceFilter

Defines filters that must occur in a specific order for the user to be a member of the Audience.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**scope** | [**ScopeEnum**](#ScopeEnum) | Required. Immutable. Specifies the scope for this filter. |  [optional] |
|**sequenceMaximumDuration** | **String** | Optional. Defines the time period in which the whole sequence must occur. |  [optional] |
|**sequenceSteps** | [**List&lt;GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep&gt;**](GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep.md) | Required. An ordered sequence of steps. A user must complete each step in order to join the sequence filter. |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AUDIENCE_FILTER_SCOPE_UNSPECIFIED&quot; |
| WITHIN_SAME_EVENT | &quot;AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT&quot; |
| WITHIN_SAME_SESSION | &quot;AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION&quot; |
| ACROSS_ALL_SESSIONS | &quot;AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS&quot; |



