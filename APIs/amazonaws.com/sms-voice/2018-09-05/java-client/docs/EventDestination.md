

# EventDestination

An object that defines an event destination.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cloudWatchLogsDestination** | [**CloudWatchLogsDestination**](CloudWatchLogsDestination.md) |  |  [optional] |
|**enabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**kinesisFirehoseDestination** | [**KinesisFirehoseDestination**](KinesisFirehoseDestination.md) |  |  [optional] |
|**matchingEventTypes** | **List&lt;EventType&gt;** | An array of EventDestination objects. Each EventDestination object includes ARNs and other information that define an event destination. |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**snsDestination** | [**SnsDestination**](SnsDestination.md) |  |  [optional] |



