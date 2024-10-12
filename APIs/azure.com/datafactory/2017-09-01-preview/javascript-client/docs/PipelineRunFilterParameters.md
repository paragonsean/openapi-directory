# DataFactoryManagementClient.PipelineRunFilterParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continuationToken** | **String** | The continuation token for getting the next page of results. Null for first page. | [optional] 
**filters** | [**[PipelineRunQueryFilter]**](PipelineRunQueryFilter.md) | List of filters. | [optional] 
**lastUpdatedAfter** | **Date** | The time at or after which the pipeline run event was updated in &#39;ISO 8601&#39; format. | 
**lastUpdatedBefore** | **Date** | The time at or before which the pipeline run event was updated in &#39;ISO 8601&#39; format. | 
**orderBy** | [**[PipelineRunQueryOrderBy]**](PipelineRunQueryOrderBy.md) | List of OrderBy option. | [optional] 


