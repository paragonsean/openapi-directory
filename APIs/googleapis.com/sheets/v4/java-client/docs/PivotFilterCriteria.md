

# PivotFilterCriteria

Criteria for showing/hiding rows in a pivot table.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**condition** | [**BooleanCondition**](BooleanCondition.md) |  |  [optional] |
|**visibleByDefault** | **Boolean** | Whether values are visible by default. If true, the visible_values are ignored, all values that meet condition (if specified) are shown. If false, values that are both in visible_values and meet condition are shown. |  [optional] |
|**visibleValues** | **List&lt;String&gt;** | Values that should be included. Values not listed here are excluded. |  [optional] |



