

# ListFilteredBidRequestsResponse

Response message for listing all reasons that bid requests were filtered and not sent to the buyer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calloutStatusRows** | [**List&lt;CalloutStatusRow&gt;**](CalloutStatusRow.md) | List of rows, with counts of filtered bid requests aggregated by callout status. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results. Pass this value in the ListFilteredBidRequestsRequest.pageToken field in the subsequent call to the filteredBidRequests.list method to retrieve the next page of results. |  [optional] |



