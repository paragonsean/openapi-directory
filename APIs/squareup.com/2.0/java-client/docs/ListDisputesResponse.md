

# ListDisputesResponse

Defines fields in a `ListDisputes` response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The pagination cursor to be used in a subsequent request. If unset, this is the final response. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). |  [optional] |
|**disputes** | [**List&lt;Dispute&gt;**](Dispute.md) | The list of disputes. |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Information about errors encountered during the request. |  [optional] |



