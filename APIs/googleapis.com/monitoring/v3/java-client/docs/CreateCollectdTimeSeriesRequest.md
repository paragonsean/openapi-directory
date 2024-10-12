

# CreateCollectdTimeSeriesRequest

The CreateCollectdTimeSeries request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collectdPayloads** | [**List&lt;CollectdPayload&gt;**](CollectdPayload.md) | The collectd payloads representing the time series data. You must not include more than a single point for each time series, so no two payloads can have the same values for all of the fields plugin, plugin_instance, type, and type_instance. |  [optional] |
|**collectdVersion** | **String** | The version of collectd that collected the data. Example: \&quot;5.3.0-192.el6\&quot;. |  [optional] |
|**resource** | [**MonitoredResource**](MonitoredResource.md) |  |  [optional] |



