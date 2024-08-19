

# Filter

An expression to filter dimension or metric values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**betweenFilter** | [**BetweenFilter**](BetweenFilter.md) |  |  [optional] |
|**fieldName** | **String** | The dimension name or metric name. In most methods, dimensions &amp; metrics can be used for the first time in this field. However in a RunPivotReportRequest, this field must be additionally specified by name in the RunPivotReportRequest&#39;s dimensions or metrics. |  [optional] |
|**inListFilter** | [**InListFilter**](InListFilter.md) |  |  [optional] |
|**numericFilter** | [**NumericFilter**](NumericFilter.md) |  |  [optional] |
|**stringFilter** | [**StringFilter**](StringFilter.md) |  |  [optional] |



