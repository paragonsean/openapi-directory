# CloudMonitoringApi.Breakdown

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregationFunction** | [**AggregationFunction**](AggregationFunction.md) |  | [optional] 
**column** | **String** | Required. The name of the column in the dataset containing the breakdown values. | [optional] 
**limit** | **Number** | Required. A limit to the number of breakdowns. If set to zero then all possible breakdowns are applied. The list of breakdowns is dependent on the value of the sort_order field. | [optional] 
**sortOrder** | **String** | Required. The sort order is applied to the values of the breakdown column. | [optional] 



## Enum: SortOrderEnum


* `UNSPECIFIED` (value: `"SORT_ORDER_UNSPECIFIED"`)

* `NONE` (value: `"SORT_ORDER_NONE"`)

* `ASCENDING` (value: `"SORT_ORDER_ASCENDING"`)

* `DESCENDING` (value: `"SORT_ORDER_DESCENDING"`)




