# GoogleAnalyticsAdminApi.GoogleAnalyticsAdminV1alphaAudience

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adsPersonalizationEnabled** | **Boolean** | Output only. It is automatically set by GA to false if this is an NPA Audience and is excluded from ads personalization. | [optional] [readonly] 
**description** | **String** | Required. The description of the Audience. | [optional] 
**displayName** | **String** | Required. The display name of the Audience. | [optional] 
**eventTrigger** | [**GoogleAnalyticsAdminV1alphaAudienceEventTrigger**](GoogleAnalyticsAdminV1alphaAudienceEventTrigger.md) |  | [optional] 
**exclusionDurationMode** | **String** | Immutable. Specifies how long an exclusion lasts for users that meet the exclusion filter. It is applied to all EXCLUDE filter clauses and is ignored when there is no EXCLUDE filter clause in the Audience. | [optional] 
**filterClauses** | [**[GoogleAnalyticsAdminV1alphaAudienceFilterClause]**](GoogleAnalyticsAdminV1alphaAudienceFilterClause.md) | Required. Immutable. Unordered list. Filter clauses that define the Audience. All clauses will be AND’ed together. | [optional] 
**membershipDurationDays** | **Number** | Required. Immutable. The duration a user should stay in an Audience. It cannot be set to more than 540 days. | [optional] 
**name** | **String** | Output only. The resource name for this Audience resource. Format: properties/{propertyId}/audiences/{audienceId} | [optional] [readonly] 



## Enum: ExclusionDurationModeEnum


* `AUDIENCE_EXCLUSION_DURATION_MODE_UNSPECIFIED` (value: `"AUDIENCE_EXCLUSION_DURATION_MODE_UNSPECIFIED"`)

* `EXCLUDE_TEMPORARILY` (value: `"EXCLUDE_TEMPORARILY"`)

* `EXCLUDE_PERMANENTLY` (value: `"EXCLUDE_PERMANENTLY"`)




