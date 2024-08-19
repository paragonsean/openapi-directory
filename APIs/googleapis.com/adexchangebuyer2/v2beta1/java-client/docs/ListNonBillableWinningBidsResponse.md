

# ListNonBillableWinningBidsResponse

Response message for listing all reasons for which a buyer was not billed for a winning bid.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nextPageToken** | **String** | A token to retrieve the next page of results. Pass this value in the ListNonBillableWinningBidsRequest.pageToken field in the subsequent call to the nonBillableWinningBids.list method to retrieve the next page of results. |  [optional] |
|**nonBillableWinningBidStatusRows** | [**List&lt;NonBillableWinningBidStatusRow&gt;**](NonBillableWinningBidStatusRow.md) | List of rows, with counts of bids not billed aggregated by reason. |  [optional] |



