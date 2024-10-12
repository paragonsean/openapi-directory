

# GoogleAnalyticsAdminV1alphaAudience

A resource message representing a GA4 Audience.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**adsPersonalizationEnabled** | **Boolean** | Output only. It is automatically set by GA to false if this is an NPA Audience and is excluded from ads personalization. |  [optional] [readonly] |
|**description** | **String** | Required. The description of the Audience. |  [optional] |
|**displayName** | **String** | Required. The display name of the Audience. |  [optional] |
|**eventTrigger** | [**GoogleAnalyticsAdminV1alphaAudienceEventTrigger**](GoogleAnalyticsAdminV1alphaAudienceEventTrigger.md) |  |  [optional] |
|**exclusionDurationMode** | [**ExclusionDurationModeEnum**](#ExclusionDurationModeEnum) | Immutable. Specifies how long an exclusion lasts for users that meet the exclusion filter. It is applied to all EXCLUDE filter clauses and is ignored when there is no EXCLUDE filter clause in the Audience. |  [optional] |
|**filterClauses** | [**List&lt;GoogleAnalyticsAdminV1alphaAudienceFilterClause&gt;**](GoogleAnalyticsAdminV1alphaAudienceFilterClause.md) | Required. Immutable. Unordered list. Filter clauses that define the Audience. All clauses will be AND’ed together. |  [optional] |
|**membershipDurationDays** | **Integer** | Required. Immutable. The duration a user should stay in an Audience. It cannot be set to more than 540 days. |  [optional] |
|**name** | **String** | Output only. The resource name for this Audience resource. Format: properties/{propertyId}/audiences/{audienceId} |  [optional] [readonly] |



## Enum: ExclusionDurationModeEnum

| Name | Value |
|---- | -----|
| AUDIENCE_EXCLUSION_DURATION_MODE_UNSPECIFIED | &quot;AUDIENCE_EXCLUSION_DURATION_MODE_UNSPECIFIED&quot; |
| EXCLUDE_TEMPORARILY | &quot;EXCLUDE_TEMPORARILY&quot; |
| EXCLUDE_PERMANENTLY | &quot;EXCLUDE_PERMANENTLY&quot; |



