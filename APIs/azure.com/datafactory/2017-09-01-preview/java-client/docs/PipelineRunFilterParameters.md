

# PipelineRunFilterParameters

Query parameters for listing pipeline runs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**continuationToken** | **String** | The continuation token for getting the next page of results. Null for first page. |  [optional] |
|**filters** | [**List&lt;PipelineRunQueryFilter&gt;**](PipelineRunQueryFilter.md) | List of filters. |  [optional] |
|**lastUpdatedAfter** | **OffsetDateTime** | The time at or after which the pipeline run event was updated in &#39;ISO 8601&#39; format. |  |
|**lastUpdatedBefore** | **OffsetDateTime** | The time at or before which the pipeline run event was updated in &#39;ISO 8601&#39; format. |  |
|**orderBy** | [**List&lt;PipelineRunQueryOrderBy&gt;**](PipelineRunQueryOrderBy.md) | List of OrderBy option. |  [optional] |



