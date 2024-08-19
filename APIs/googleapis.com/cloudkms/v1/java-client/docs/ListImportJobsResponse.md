

# ListImportJobsResponse

Response message for KeyManagementService.ListImportJobs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**importJobs** | [**List&lt;ImportJob&gt;**](ImportJob.md) | The list of ImportJobs. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve next page of results. Pass this value in ListImportJobsRequest.page_token to retrieve the next page of results. |  [optional] |
|**totalSize** | **Integer** | The total number of ImportJobs that matched the query. |  [optional] |



