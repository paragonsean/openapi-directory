# CloudMonitoringApi.DataSet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**breakdowns** | [**[Breakdown]**](Breakdown.md) | Optional. The collection of breakdowns to be applied to the dataset. | [optional] 
**dimensions** | [**[Dimension]**](Dimension.md) | Optional. A collection of dimension columns. | [optional] 
**legendTemplate** | **String** | A template string for naming TimeSeries in the resulting data set. This should be a string with interpolations of the form ${label_name}, which will resolve to the label&#39;s value. | [optional] 
**measures** | [**[Measure]**](Measure.md) | Optional. A collection of measures. | [optional] 
**minAlignmentPeriod** | **String** | Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query For example, if the data is published once every 10 minutes, the min_alignment_period should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals. | [optional] 
**plotType** | **String** | How this data should be plotted on the chart. | [optional] 
**targetAxis** | **String** | Optional. The target axis to use for plotting the metric. | [optional] 
**timeSeriesQuery** | [**TimeSeriesQuery**](TimeSeriesQuery.md) |  | [optional] 



## Enum: PlotTypeEnum


* `PLOT_TYPE_UNSPECIFIED` (value: `"PLOT_TYPE_UNSPECIFIED"`)

* `LINE` (value: `"LINE"`)

* `STACKED_AREA` (value: `"STACKED_AREA"`)

* `STACKED_BAR` (value: `"STACKED_BAR"`)

* `HEATMAP` (value: `"HEATMAP"`)





## Enum: TargetAxisEnum


* `TARGET_AXIS_UNSPECIFIED` (value: `"TARGET_AXIS_UNSPECIFIED"`)

* `Y1` (value: `"Y1"`)

* `Y2` (value: `"Y2"`)




