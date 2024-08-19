

# ListLosingBidsResponse

Response message for listing all reasons that bids lost in the auction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creativeStatusRows** | [**List&lt;CreativeStatusRow&gt;**](CreativeStatusRow.md) | List of rows, with counts of losing bids aggregated by loss reason (for example, creative status). |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results. Pass this value in the ListLosingBidsRequest.pageToken field in the subsequent call to the losingBids.list method to retrieve the next page of results. |  [optional] |



