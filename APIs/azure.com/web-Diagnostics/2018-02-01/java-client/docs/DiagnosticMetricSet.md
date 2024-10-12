

# DiagnosticMetricSet

Class representing Diagnostic Metric information

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **OffsetDateTime** | End time of the period |  [optional] |
|**name** | **String** | Name of the metric |  [optional] |
|**startTime** | **OffsetDateTime** | Start time of the period |  [optional] |
|**timeGrain** | **String** | Presented time grain. Supported grains at the moment are PT1M, PT1H, P1D |  [optional] |
|**unit** | **String** | Metric&#39;s unit |  [optional] |
|**values** | [**List&lt;DiagnosticMetricSample&gt;**](DiagnosticMetricSample.md) | Collection of metric values for the selected period based on the {Microsoft.Web.Hosting.Administration.DiagnosticMetricSet.TimeGrain} |  [optional] |



