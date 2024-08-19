

# FilteredBidDetailRow

The number of filtered bids with the specified dimension values, among those filtered due to the requested filtering reason (for example, creative status), that have the specified detail.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidCount** | [**MetricValue**](MetricValue.md) |  |  [optional] |
|**detail** | **String** | The ID of the detail, can be numeric or text. The associated value can be looked up in the dictionary file corresponding to the DetailType in the response message. |  [optional] |
|**detailId** | **Integer** | Note: this field will be deprecated, use \&quot;detail\&quot; field instead. When \&quot;detail\&quot; field represents an integer value, this field is populated as the same integer value \&quot;detail\&quot; field represents, otherwise this field will be 0. The ID of the detail. The associated value can be looked up in the dictionary file corresponding to the DetailType in the response message. |  [optional] |
|**rowDimensions** | [**RowDimensions**](RowDimensions.md) |  |  [optional] |



