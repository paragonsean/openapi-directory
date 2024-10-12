# AnalyticsReportingApi.OrderBy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fieldName** | **String** | The field which to sort by. The default sort order is ascending. Example: &#x60;ga:browser&#x60;. Note, that you can only specify one field for sort here. For example, &#x60;ga:browser, ga:city&#x60; is not valid. | [optional] 
**orderType** | **String** | The order type. The default orderType is &#x60;VALUE&#x60;. | [optional] 
**sortOrder** | **String** | The sorting order for the field. | [optional] 



## Enum: OrderTypeEnum


* `ORDER_TYPE_UNSPECIFIED` (value: `"ORDER_TYPE_UNSPECIFIED"`)

* `VALUE` (value: `"VALUE"`)

* `DELTA` (value: `"DELTA"`)

* `SMART` (value: `"SMART"`)

* `HISTOGRAM_BUCKET` (value: `"HISTOGRAM_BUCKET"`)

* `DIMENSION_AS_INTEGER` (value: `"DIMENSION_AS_INTEGER"`)





## Enum: SortOrderEnum


* `SORT_ORDER_UNSPECIFIED` (value: `"SORT_ORDER_UNSPECIFIED"`)

* `ASCENDING` (value: `"ASCENDING"`)

* `DESCENDING` (value: `"DESCENDING"`)




