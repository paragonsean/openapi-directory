

# BidResponseWithoutBidsStatusRow

The number of impressions with the specified dimension values that were considered to have no applicable bids, as described by the specified status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**impressionCount** | [**MetricValue**](MetricValue.md) |  |  [optional] |
|**rowDimensions** | [**RowDimensions**](RowDimensions.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status specifying why the bid responses were considered to have no applicable bids. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| RESPONSES_WITHOUT_BIDS | &quot;RESPONSES_WITHOUT_BIDS&quot; |
| RESPONSES_WITHOUT_BIDS_FOR_ACCOUNT | &quot;RESPONSES_WITHOUT_BIDS_FOR_ACCOUNT&quot; |
| RESPONSES_WITHOUT_BIDS_FOR_DEAL | &quot;RESPONSES_WITHOUT_BIDS_FOR_DEAL&quot; |



