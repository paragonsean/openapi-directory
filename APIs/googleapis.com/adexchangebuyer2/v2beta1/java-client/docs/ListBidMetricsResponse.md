

# ListBidMetricsResponse

Response message for listing the metrics that are measured in number of bids.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidMetricsRows** | [**List&lt;BidMetricsRow&gt;**](BidMetricsRow.md) | List of rows, each containing a set of bid metrics. |  [optional] |
|**nextPageToken** | **String** | A token to retrieve the next page of results. Pass this value in the ListBidMetricsRequest.pageToken field in the subsequent call to the bidMetrics.list method to retrieve the next page of results. |  [optional] |



