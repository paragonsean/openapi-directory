

# DataSet

Groups a time series query definition with charting options.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**breakdowns** | [**List&lt;Breakdown&gt;**](Breakdown.md) | Optional. The collection of breakdowns to be applied to the dataset. |  [optional] |
|**dimensions** | [**List&lt;Dimension&gt;**](Dimension.md) | Optional. A collection of dimension columns. |  [optional] |
|**legendTemplate** | **String** | A template string for naming TimeSeries in the resulting data set. This should be a string with interpolations of the form ${label_name}, which will resolve to the label&#39;s value. |  [optional] |
|**measures** | [**List&lt;Measure&gt;**](Measure.md) | Optional. A collection of measures. |  [optional] |
|**minAlignmentPeriod** | **String** | Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query For example, if the data is published once every 10 minutes, the min_alignment_period should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals. |  [optional] |
|**plotType** | [**PlotTypeEnum**](#PlotTypeEnum) | How this data should be plotted on the chart. |  [optional] |
|**targetAxis** | [**TargetAxisEnum**](#TargetAxisEnum) | Optional. The target axis to use for plotting the metric. |  [optional] |
|**timeSeriesQuery** | [**TimeSeriesQuery**](TimeSeriesQuery.md) |  |  [optional] |



## Enum: PlotTypeEnum

| Name | Value |
|---- | -----|
| PLOT_TYPE_UNSPECIFIED | &quot;PLOT_TYPE_UNSPECIFIED&quot; |
| LINE | &quot;LINE&quot; |
| STACKED_AREA | &quot;STACKED_AREA&quot; |
| STACKED_BAR | &quot;STACKED_BAR&quot; |
| HEATMAP | &quot;HEATMAP&quot; |



## Enum: TargetAxisEnum

| Name | Value |
|---- | -----|
| TARGET_AXIS_UNSPECIFIED | &quot;TARGET_AXIS_UNSPECIFIED&quot; |
| Y1 | &quot;Y1&quot; |
| Y2 | &quot;Y2&quot; |



