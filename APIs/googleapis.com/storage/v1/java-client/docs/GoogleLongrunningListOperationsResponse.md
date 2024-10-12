

# GoogleLongrunningListOperationsResponse

The response message for storage.buckets.operations.list.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | The continuation token, used to page through large result sets. Provide this value in a subsequent request to return the next page of results. |  [optional] |
|**operations** | [**List&lt;GoogleLongrunningOperation&gt;**](GoogleLongrunningOperation.md) | A list of operations that matches the specified filter in the request. |  [optional] |



