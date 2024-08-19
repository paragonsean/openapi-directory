# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaAudienceSequenceFilter

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scope** | **String** | Required. Immutable. Specifies the scope for this filter. | [optional] 
**sequenceMaximumDuration** | **String** | Optional. Defines the time period in which the whole sequence must occur. | [optional] 
**sequenceSteps** | [**[GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep]**](GoogleAnalyticsAdminV1alphaAudienceSequenceFilterAudienceSequenceStep.md) | Required. An ordered sequence of steps. A user must complete each step in order to join the sequence filter. | [optional] 



## Enum: ScopeEnum


* `UNSPECIFIED` (value: `"AUDIENCE_FILTER_SCOPE_UNSPECIFIED"`)

* `WITHIN_SAME_EVENT` (value: `"AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT"`)

* `WITHIN_SAME_SESSION` (value: `"AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION"`)

* `ACROSS_ALL_SESSIONS` (value: `"AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS"`)




