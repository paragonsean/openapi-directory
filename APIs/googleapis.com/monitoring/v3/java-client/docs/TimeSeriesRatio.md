

# TimeSeriesRatio

A TimeSeriesRatio specifies two TimeSeries to use for computing the good_service / total_service ratio. The specified TimeSeries must have ValueType = DOUBLE or ValueType = INT64 and must have MetricKind = DELTA or MetricKind = CUMULATIVE. The TimeSeriesRatio must specify exactly two of good, bad, and total, and the relationship good_service + bad_service = total_service will be assumed.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**badServiceFilter** | **String** | A monitoring filter (https://cloud.google.com/monitoring/api/v3/filters) specifying a TimeSeries quantifying bad service, either demanded service that was not provided or demanded service that was of inadequate quality. Must have ValueType &#x3D; DOUBLE or ValueType &#x3D; INT64 and must have MetricKind &#x3D; DELTA or MetricKind &#x3D; CUMULATIVE. |  [optional] |
|**goodServiceFilter** | **String** | A monitoring filter (https://cloud.google.com/monitoring/api/v3/filters) specifying a TimeSeries quantifying good service provided. Must have ValueType &#x3D; DOUBLE or ValueType &#x3D; INT64 and must have MetricKind &#x3D; DELTA or MetricKind &#x3D; CUMULATIVE. |  [optional] |
|**totalServiceFilter** | **String** | A monitoring filter (https://cloud.google.com/monitoring/api/v3/filters) specifying a TimeSeries quantifying total demanded service. Must have ValueType &#x3D; DOUBLE or ValueType &#x3D; INT64 and must have MetricKind &#x3D; DELTA or MetricKind &#x3D; CUMULATIVE. |  [optional] |



