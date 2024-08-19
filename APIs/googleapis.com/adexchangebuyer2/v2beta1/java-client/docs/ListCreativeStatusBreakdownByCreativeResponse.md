

# ListCreativeStatusBreakdownByCreativeResponse

Response message for listing all creatives associated with a given filtered bid reason.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filteredBidCreativeRows** | [**List&lt;FilteredBidCreativeRow&gt;**](FilteredBidCreativeRow.md) | List of rows, with counts of bids with a given creative status aggregated by creative. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results. Pass this value in the ListCreativeStatusBreakdownByCreativeRequest.pageToken field in the subsequent call to the filteredBids.creatives.list method to retrieve the next page of results. |  [optional] |



