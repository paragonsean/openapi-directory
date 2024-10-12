

# PivotTable

A pivot table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columns** | [**List&lt;PivotGroup&gt;**](PivotGroup.md) | Each column grouping in the pivot table. |  [optional] |
|**criteria** | [**Map&lt;String, PivotFilterCriteria&gt;**](PivotFilterCriteria.md) | An optional mapping of filters per source column offset. The filters are applied before aggregating data into the pivot table. The map&#39;s key is the column offset of the source range that you want to filter, and the value is the criteria for that column. For example, if the source was &#x60;C10:E15&#x60;, a key of &#x60;0&#x60; will have the filter for column &#x60;C&#x60;, whereas the key &#x60;1&#x60; is for column &#x60;D&#x60;. This field is deprecated in favor of filter_specs. |  [optional] |
|**dataExecutionStatus** | [**DataExecutionStatus**](DataExecutionStatus.md) |  |  [optional] |
|**dataSourceId** | **String** | The ID of the data source the pivot table is reading data from. |  [optional] |
|**filterSpecs** | [**List&lt;PivotFilterSpec&gt;**](PivotFilterSpec.md) | The filters applied to the source columns before aggregating data for the pivot table. Both criteria and filter_specs are populated in responses. If both fields are specified in an update request, this field takes precedence. |  [optional] |
|**rows** | [**List&lt;PivotGroup&gt;**](PivotGroup.md) | Each row grouping in the pivot table. |  [optional] |
|**source** | [**GridRange**](GridRange.md) |  |  [optional] |
|**valueLayout** | [**ValueLayoutEnum**](#ValueLayoutEnum) | Whether values should be listed horizontally (as columns) or vertically (as rows). |  [optional] |
|**values** | [**List&lt;PivotValue&gt;**](PivotValue.md) | A list of values to include in the pivot table. |  [optional] |



## Enum: ValueLayoutEnum

| Name | Value |
|---- | -----|
| HORIZONTAL | &quot;HORIZONTAL&quot; |
| VERTICAL | &quot;VERTICAL&quot; |



