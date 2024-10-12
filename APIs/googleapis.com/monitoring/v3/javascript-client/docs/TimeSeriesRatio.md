# CloudMonitoringApi.TimeSeriesRatio

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badServiceFilter** | **String** | A monitoring filter (https://cloud.google.com/monitoring/api/v3/filters) specifying a TimeSeries quantifying bad service, either demanded service that was not provided or demanded service that was of inadequate quality. Must have ValueType &#x3D; DOUBLE or ValueType &#x3D; INT64 and must have MetricKind &#x3D; DELTA or MetricKind &#x3D; CUMULATIVE. | [optional] 
**goodServiceFilter** | **String** | A monitoring filter (https://cloud.google.com/monitoring/api/v3/filters) specifying a TimeSeries quantifying good service provided. Must have ValueType &#x3D; DOUBLE or ValueType &#x3D; INT64 and must have MetricKind &#x3D; DELTA or MetricKind &#x3D; CUMULATIVE. | [optional] 
**totalServiceFilter** | **String** | A monitoring filter (https://cloud.google.com/monitoring/api/v3/filters) specifying a TimeSeries quantifying total demanded service. Must have ValueType &#x3D; DOUBLE or ValueType &#x3D; INT64 and must have MetricKind &#x3D; DELTA or MetricKind &#x3D; CUMULATIVE. | [optional] 


