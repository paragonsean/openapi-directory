

# GoogleAnalyticsAdminV1alphaAudienceSimpleFilter

Defines a simple filter that a user must satisfy to be a member of the Audience.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filterExpression** | [**GoogleAnalyticsAdminV1alphaAudienceFilterExpression**](GoogleAnalyticsAdminV1alphaAudienceFilterExpression.md) |  |  [optional] |
|**scope** | [**ScopeEnum**](#ScopeEnum) | Required. Immutable. Specifies the scope for this filter. |  [optional] |



## Enum: ScopeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AUDIENCE_FILTER_SCOPE_UNSPECIFIED&quot; |
| WITHIN_SAME_EVENT | &quot;AUDIENCE_FILTER_SCOPE_WITHIN_SAME_EVENT&quot; |
| WITHIN_SAME_SESSION | &quot;AUDIENCE_FILTER_SCOPE_WITHIN_SAME_SESSION&quot; |
| ACROSS_ALL_SESSIONS | &quot;AUDIENCE_FILTER_SCOPE_ACROSS_ALL_SESSIONS&quot; |



