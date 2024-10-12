

# MetricDataQuery

<p>The metric data to return. Also defines whether this call is returning data for one metric only, or whether it is performing a math expression on the values of returned metric statistics to create a new time series. A time series is a series of data points, each of which is associated with a timestamp.</p> <p>For more information and examples, see <a href=\"https://docs.aws.amazon.com/autoscaling/ec2/userguide/predictive-scaling-customized-metric-specification.html\">Advanced predictive scaling policy configurations using custom metrics</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | [**String**](String.md) |  |  |
|**expression** | [**String**](String.md) |  |  [optional] |
|**metricStat** | [**MetricDataQueryMetricStat**](MetricDataQueryMetricStat.md) |  |  [optional] |
|**label** | [**String**](String.md) |  |  [optional] |
|**returnData** | [**Boolean**](Boolean.md) |  |  [optional] |



