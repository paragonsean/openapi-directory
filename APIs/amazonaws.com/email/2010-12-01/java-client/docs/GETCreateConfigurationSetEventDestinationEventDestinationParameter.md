

# GETCreateConfigurationSetEventDestinationEventDestinationParameter

<p>Contains information about the event destination that the specified email sending events will be published to.</p> <note> <p>When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose or Amazon Simple Notification Service (Amazon SNS).</p> </note> <p>Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see the <a href=\"https://docs.aws.amazon.com/ses/latest/DeveloperGuide/monitor-sending-activity.html\">Amazon SES Developer Guide</a>.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**String**](String.md) |  |  |
|**enabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**matchingEventTypes** | [**List**](List.md) |  |  |
|**kinesisFirehoseDestination** | [**GETCreateConfigurationSetEventDestinationEventDestinationParameterKinesisFirehoseDestination**](GETCreateConfigurationSetEventDestinationEventDestinationParameterKinesisFirehoseDestination.md) |  |  [optional] |
|**cloudWatchDestination** | [**GETCreateConfigurationSetEventDestinationEventDestinationParameterCloudWatchDestination**](GETCreateConfigurationSetEventDestinationEventDestinationParameterCloudWatchDestination.md) |  |  [optional] |
|**snSDestination** | [**GETCreateConfigurationSetEventDestinationEventDestinationParameterSNSDestination**](GETCreateConfigurationSetEventDestinationEventDestinationParameterSNSDestination.md) |  |  [optional] |



