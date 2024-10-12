

# MetricFilter

Metric filters express how CloudWatch Logs would extract metric observations from ingested log events and transform them into metric data in a CloudWatch metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filterName** | [**String**](String.md) |  |  [optional] |
|**filterPattern** | **String** | A symbolic description of how CloudWatch Logs should interpret the data in each log event. For example, a log event can contain timestamps, IP addresses, strings, and so on. You use the filter pattern to specify what to look for in the log event message. |  [optional] |
|**metricTransformations** | [**List**](List.md) |  |  [optional] |
|**creationTime** | [**Integer**](Integer.md) |  |  [optional] |
|**logGroupName** | [**String**](String.md) |  |  [optional] |



