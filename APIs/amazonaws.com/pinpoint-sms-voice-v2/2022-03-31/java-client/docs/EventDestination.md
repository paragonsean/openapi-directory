

# EventDestination

<p>Contains information about an event destination.</p> <p>Event destinations are associated with configuration sets, which enable you to publish message sending events to Amazon CloudWatch, Amazon Kinesis Data Firehose, or Amazon SNS.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventDestinationName** | [**String**](String.md) |  |  |
|**enabled** | [**Boolean**](Boolean.md) |  |  |
|**matchingEventTypes** | [**List**](List.md) |  |  |
|**cloudWatchLogsDestination** | [**EventDestinationCloudWatchLogsDestination**](EventDestinationCloudWatchLogsDestination.md) |  |  [optional] |
|**kinesisFirehoseDestination** | [**CreateEventDestinationRequestKinesisFirehoseDestination**](CreateEventDestinationRequestKinesisFirehoseDestination.md) |  |  [optional] |
|**snsDestination** | [**EventDestinationSnsDestination**](EventDestinationSnsDestination.md) |  |  [optional] |



