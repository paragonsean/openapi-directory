

# PieChartDataSet

Groups a time series query definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dimensions** | [**List&lt;Dimension&gt;**](Dimension.md) | A dimension is a structured label, class, or category for a set of measurements in your data. |  [optional] |
|**measures** | [**List&lt;Measure&gt;**](Measure.md) | A measure is a measured value of a property in your data. For example, rainfall in inches, number of units sold, revenue gained, etc. |  [optional] |
|**minAlignmentPeriod** | **String** | Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query. For example, if the data is published once every 10 minutes, the min_alignment_period should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals. |  [optional] |
|**sliceNameTemplate** | **String** | Optional. A template for the name of the slice. This name will be displayed in the legend and the tooltip of the pie chart. It replaces the auto-generated names for the slices. For example, if the template is set to ${resource.labels.zone}, the zone&#39;s value will be used for the name instead of the default name. |  [optional] |
|**timeSeriesQuery** | [**TimeSeriesQuery**](TimeSeriesQuery.md) |  |  [optional] |



