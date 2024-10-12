# CloudMonitoringApi.SparkChartView

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minAlignmentPeriod** | **String** | The lower bound on data point frequency in the chart implemented by specifying the minimum alignment period to use in a time series query. For example, if the data is published once every 10 minutes it would not make sense to fetch and align data at one minute intervals. This field is optional and exists only as a hint. | [optional] 
**sparkChartType** | **String** | Required. The type of sparkchart to show in this chartView. | [optional] 



## Enum: SparkChartTypeEnum


* `CHART_TYPE_UNSPECIFIED` (value: `"SPARK_CHART_TYPE_UNSPECIFIED"`)

* `LINE` (value: `"SPARK_LINE"`)

* `BAR` (value: `"SPARK_BAR"`)




