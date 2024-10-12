

# GoogleCloudDatapipelinesV1ListPipelinesResponse

Response message for ListPipelines.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**pipelines** | [**List&lt;GoogleCloudDatapipelinesV1Pipeline&gt;**](GoogleCloudDatapipelinesV1Pipeline.md) | Results that matched the filter criteria and were accessible to the caller. Results are always in descending order of pipeline creation date. |  [optional] |



