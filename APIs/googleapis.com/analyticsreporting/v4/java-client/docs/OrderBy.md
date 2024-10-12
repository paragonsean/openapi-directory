

# OrderBy

Specifies the sorting options.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fieldName** | **String** | The field which to sort by. The default sort order is ascending. Example: &#x60;ga:browser&#x60;. Note, that you can only specify one field for sort here. For example, &#x60;ga:browser, ga:city&#x60; is not valid. |  [optional] |
|**orderType** | [**OrderTypeEnum**](#OrderTypeEnum) | The order type. The default orderType is &#x60;VALUE&#x60;. |  [optional] |
|**sortOrder** | [**SortOrderEnum**](#SortOrderEnum) | The sorting order for the field. |  [optional] |



## Enum: OrderTypeEnum

| Name | Value |
|---- | -----|
| ORDER_TYPE_UNSPECIFIED | &quot;ORDER_TYPE_UNSPECIFIED&quot; |
| VALUE | &quot;VALUE&quot; |
| DELTA | &quot;DELTA&quot; |
| SMART | &quot;SMART&quot; |
| HISTOGRAM_BUCKET | &quot;HISTOGRAM_BUCKET&quot; |
| DIMENSION_AS_INTEGER | &quot;DIMENSION_AS_INTEGER&quot; |



## Enum: SortOrderEnum

| Name | Value |
|---- | -----|
| SORT_ORDER_UNSPECIFIED | &quot;SORT_ORDER_UNSPECIFIED&quot; |
| ASCENDING | &quot;ASCENDING&quot; |
| DESCENDING | &quot;DESCENDING&quot; |



