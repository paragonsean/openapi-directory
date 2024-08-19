

# GoogleAnalyticsAdminV1alphaAudienceFilterClause

A clause for defining either a simple or sequence filter. A filter can be inclusive (For example, users satisfying the filter clause are included in the Audience) or exclusive (For example, users satisfying the filter clause are excluded from the Audience).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clauseType** | [**ClauseTypeEnum**](#ClauseTypeEnum) | Required. Specifies whether this is an include or exclude filter clause. |  [optional] |
|**sequenceFilter** | [**GoogleAnalyticsAdminV1alphaAudienceSequenceFilter**](GoogleAnalyticsAdminV1alphaAudienceSequenceFilter.md) |  |  [optional] |
|**simpleFilter** | [**GoogleAnalyticsAdminV1alphaAudienceSimpleFilter**](GoogleAnalyticsAdminV1alphaAudienceSimpleFilter.md) |  |  [optional] |



## Enum: ClauseTypeEnum

| Name | Value |
|---- | -----|
| AUDIENCE_CLAUSE_TYPE_UNSPECIFIED | &quot;AUDIENCE_CLAUSE_TYPE_UNSPECIFIED&quot; |
| INCLUDE | &quot;INCLUDE&quot; |
| EXCLUDE | &quot;EXCLUDE&quot; |



