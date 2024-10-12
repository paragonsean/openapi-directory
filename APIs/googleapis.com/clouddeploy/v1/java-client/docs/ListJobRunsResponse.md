

# ListJobRunsResponse

ListJobRunsResponse is the response object returned by `ListJobRuns`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobRuns** | [**List&lt;JobRun&gt;**](JobRun.md) | The &#x60;JobRun&#x60; objects. |  [optional] |
|**nextPageToken** | **String** | A token, which can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Locations that could not be reached |  [optional] |



