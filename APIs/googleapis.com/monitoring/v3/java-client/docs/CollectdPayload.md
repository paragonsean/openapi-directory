

# CollectdPayload

A collection of data points sent from a collectd-based plugin. See the collectd documentation for more information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | The end time of the interval. |  [optional] |
|**metadata** | [**Map&lt;String, TypedValue&gt;**](TypedValue.md) | The measurement metadata. Example: \&quot;process_id\&quot; -&gt; 12345 |  [optional] |
|**plugin** | **String** | The name of the plugin. Example: \&quot;disk\&quot;. |  [optional] |
|**pluginInstance** | **String** | The instance name of the plugin Example: \&quot;hdcl\&quot;. |  [optional] |
|**startTime** | **String** | The start time of the interval. |  [optional] |
|**type** | **String** | The measurement type. Example: \&quot;memory\&quot;. |  [optional] |
|**typeInstance** | **String** | The measurement type instance. Example: \&quot;used\&quot;. |  [optional] |
|**values** | [**List&lt;CollectdValue&gt;**](CollectdValue.md) | The measured values during this time interval. Each value must have a different data_source_name. |  [optional] |



