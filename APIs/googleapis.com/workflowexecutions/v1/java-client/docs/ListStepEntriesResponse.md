

# ListStepEntriesResponse

Response message for ExecutionHistory.ListStepEntries.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token to retrieve next page of results. Pass this value in the ListStepEntriesRequest.page_token field in the subsequent call to &#x60;ListStepEntries&#x60; method to retrieve the next page of results. |  [optional] |
|**stepEntries** | [**List&lt;StepEntry&gt;**](StepEntry.md) | The list of entries. |  [optional] |
|**totalSize** | **Integer** | Indicates the total number of StepEntries that matched the request filter. For running executions, this number shows the number of StepEntries that are executed thus far. |  [optional] |



