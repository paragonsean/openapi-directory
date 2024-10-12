

# MetricSettings

Part of MultiTenantDiagnosticSettings. Specifies the settings for a particular metric.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | **String** | Name of a Diagnostic Metric category for a resource type this setting is applied to. To obtain the list of Diagnostic metric categories for a resource, first perform a GET diagnostic settings operation. |  [optional] |
|**enabled** | **Boolean** | a value indicating whether this category is enabled. |  |
|**retentionPolicy** | [**RetentionPolicy**](RetentionPolicy.md) |  |  [optional] |
|**timeGrain** | **String** | the timegrain of the metric in ISO8601 format. |  [optional] |



