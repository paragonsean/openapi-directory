

# ListBidResponsesWithoutBidsResponse

Response message for listing all reasons that bid responses were considered to have no applicable bids.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidResponseWithoutBidsStatusRows** | [**List&lt;BidResponseWithoutBidsStatusRow&gt;**](BidResponseWithoutBidsStatusRow.md) | List of rows, with counts of bid responses without bids aggregated by status. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results. Pass this value in the ListBidResponsesWithoutBidsRequest.pageToken field in the subsequent call to the bidResponsesWithoutBids.list method to retrieve the next page of results. |  [optional] |



