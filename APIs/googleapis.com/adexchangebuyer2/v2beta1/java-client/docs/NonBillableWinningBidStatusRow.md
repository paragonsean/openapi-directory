

# NonBillableWinningBidStatusRow

The number of winning bids with the specified dimension values for which the buyer was not billed, as described by the specified status.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidCount** | [**MetricValue**](MetricValue.md) |  |  [optional] |
|**rowDimensions** | [**RowDimensions**](RowDimensions.md) |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status specifying why the winning bids were not billed. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| AD_NOT_RENDERED | &quot;AD_NOT_RENDERED&quot; |
| INVALID_IMPRESSION | &quot;INVALID_IMPRESSION&quot; |
| FATAL_VAST_ERROR | &quot;FATAL_VAST_ERROR&quot; |
| LOST_IN_MEDIATION | &quot;LOST_IN_MEDIATION&quot; |



