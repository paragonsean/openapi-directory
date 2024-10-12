

# ListDisputeEvidenceResponse

Defines the fields in a `ListDisputeEvidence` response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cursor** | **String** | The pagination cursor to be used in a subsequent request. If unset, this is the final response. For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). |  [optional] |
|**errors** | [**List&lt;Error&gt;**](Error.md) | Information about errors encountered during the request. |  [optional] |
|**evidence** | [**List&lt;DisputeEvidence&gt;**](DisputeEvidence.md) | The list of evidence previously uploaded to the specified dispute. |  [optional] |



