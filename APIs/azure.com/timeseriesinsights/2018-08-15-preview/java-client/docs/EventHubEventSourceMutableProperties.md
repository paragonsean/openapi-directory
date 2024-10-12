

# EventHubEventSourceMutableProperties

An object that represents a set of mutable EventHub event source resource properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sharedAccessKey** | **String** | The value of the shared access key that grants the Time Series Insights service read access to the event hub. This property is not shown in event source responses. |  [optional] |
|**localTimestamp** | [**LocalTimestamp**](LocalTimestamp.md) |  |  [optional] |
|**timestampPropertyName** | **String** | The event property that will be used as the event source&#39;s timestamp. If a value isn&#39;t specified for timestampPropertyName, or if null or empty-string is specified, the event creation time will be used. |  [optional] |



