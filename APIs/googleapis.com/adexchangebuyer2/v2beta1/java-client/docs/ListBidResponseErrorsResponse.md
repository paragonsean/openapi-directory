

# ListBidResponseErrorsResponse

Response message for listing all reasons that bid responses resulted in an error.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calloutStatusRows** | [**List&lt;CalloutStatusRow&gt;**](CalloutStatusRow.md) | List of rows, with counts of bid responses aggregated by callout status. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results. Pass this value in the ListBidResponseErrorsRequest.pageToken field in the subsequent call to the bidResponseErrors.list method to retrieve the next page of results. |  [optional] |



