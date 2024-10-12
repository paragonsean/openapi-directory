

# SearchApplication

SearchApplication

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSourceRestrictions** | [**List&lt;DataSourceRestriction&gt;**](DataSourceRestriction.md) | Retrictions applied to the configurations. The maximum number of elements is 10. |  [optional] |
|**defaultFacetOptions** | [**List&lt;FacetOptions&gt;**](FacetOptions.md) | The default fields for returning facet results. The sources specified here also have been included in data_source_restrictions above. |  [optional] |
|**defaultSortOptions** | [**SortOptions**](SortOptions.md) |  |  [optional] |
|**displayName** | **String** | Display name of the Search Application. The maximum length is 300 characters. |  [optional] |
|**enableAuditLog** | **Boolean** | Indicates whether audit logging is on/off for requests made for the search application in query APIs. |  [optional] |
|**name** | **String** | The name of the Search Application. Format: searchapplications/{application_id}. |  [optional] |
|**operationIds** | **List&lt;String&gt;** | Output only. IDs of the Long Running Operations (LROs) currently running for this schema. Output only field. |  [optional] [readonly] |
|**queryInterpretationConfig** | [**QueryInterpretationConfig**](QueryInterpretationConfig.md) |  |  [optional] |
|**returnResultThumbnailUrls** | **Boolean** | With each result we should return the URI for its thumbnail (when applicable) |  [optional] |
|**scoringConfig** | [**ScoringConfig**](ScoringConfig.md) |  |  [optional] |
|**sourceConfig** | [**List&lt;SourceConfig&gt;**](SourceConfig.md) | Configuration for a sources specified in data_source_restrictions. |  [optional] |



