

# RunFilterParameters

Query parameters for listing runs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**continuationToken** | **String** | The continuation token for getting the next page of results. Null for first page. |  [optional] |
|**filters** | [**List&lt;RunQueryFilter&gt;**](RunQueryFilter.md) | List of filters. |  [optional] |
|**lastUpdatedAfter** | **OffsetDateTime** | The time at or after which the run event was updated in &#39;ISO 8601&#39; format. |  |
|**lastUpdatedBefore** | **OffsetDateTime** | The time at or before which the run event was updated in &#39;ISO 8601&#39; format. |  |
|**orderBy** | [**List&lt;RunQueryOrderBy&gt;**](RunQueryOrderBy.md) | List of OrderBy option. |  [optional] |



