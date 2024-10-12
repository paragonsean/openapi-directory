

# ListBatchesResponse

A list of batch workloads.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**batches** | [**List&lt;Batch&gt;**](Batch.md) | Output only. The batches from the specified collection. |  [optional] [readonly] |
|**nextPageToken** | **String** | A token, which can be sent as page_token to retrieve the next page. If this field is omitted, there are no subsequent pages. |  [optional] |
|**unreachable** | **List&lt;String&gt;** | Output only. List of Batches that could not be included in the response. Attempting to get one of these resources may indicate why it was not included in the list response. |  [optional] [readonly] |



