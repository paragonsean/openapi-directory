

# ListFilteredBidsResponse

Response message for listing all reasons that bids were filtered from the auction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creativeStatusRows** | [**List&lt;CreativeStatusRow&gt;**](CreativeStatusRow.md) | List of rows, with counts of filtered bids aggregated by filtering reason (for example, creative status). |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results. Pass this value in the ListFilteredBidsRequest.pageToken field in the subsequent call to the filteredBids.list method to retrieve the next page of results. |  [optional] |



