

# FilterView

A filter view.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**criteria** | [**Map&lt;String, FilterCriteria&gt;**](FilterCriteria.md) | The criteria for showing/hiding values per column. The map&#39;s key is the column index, and the value is the criteria for that column. This field is deprecated in favor of filter_specs. |  [optional] |
|**filterSpecs** | [**List&lt;FilterSpec&gt;**](FilterSpec.md) | The filter criteria for showing/hiding values per column. Both criteria and filter_specs are populated in responses. If both fields are specified in an update request, this field takes precedence. |  [optional] |
|**filterViewId** | **Integer** | The ID of the filter view. |  [optional] |
|**namedRangeId** | **String** | The named range this filter view is backed by, if any. When writing, only one of range or named_range_id may be set. |  [optional] |
|**range** | [**GridRange**](GridRange.md) |  |  [optional] |
|**sortSpecs** | [**List&lt;SortSpec&gt;**](SortSpec.md) | The sort order per column. Later specifications are used when values are equal in the earlier specifications. |  [optional] |
|**title** | **String** | The name of the filter view. |  [optional] |



