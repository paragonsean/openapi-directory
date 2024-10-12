

# Breakdown

Preview: A breakdown is an aggregation applied to the measures over a specified column. A breakdown can result in multiple series across a category for the provided measure. This is a preview feature and may be subject to change before final release.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationFunction** | [**AggregationFunction**](AggregationFunction.md) |  |  [optional] |
|**column** | **String** | Required. The name of the column in the dataset containing the breakdown values. |  [optional] |
|**limit** | **Integer** | Required. A limit to the number of breakdowns. If set to zero then all possible breakdowns are applied. The list of breakdowns is dependent on the value of the sort_order field. |  [optional] |
|**sortOrder** | [**SortOrderEnum**](#SortOrderEnum) | Required. The sort order is applied to the values of the breakdown column. |  [optional] |



## Enum: SortOrderEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SORT_ORDER_UNSPECIFIED&quot; |
| NONE | &quot;SORT_ORDER_NONE&quot; |
| ASCENDING | &quot;SORT_ORDER_ASCENDING&quot; |
| DESCENDING | &quot;SORT_ORDER_DESCENDING&quot; |



