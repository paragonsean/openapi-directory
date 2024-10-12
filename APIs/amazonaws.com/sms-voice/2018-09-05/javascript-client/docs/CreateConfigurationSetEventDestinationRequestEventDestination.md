# AmazonPinpointSmsAndVoiceService.CreateConfigurationSetEventDestinationRequestEventDestination

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloudWatchLogsDestination** | [**CloudWatchLogsDestination**](CloudWatchLogsDestination.md) |  | [optional] 
**enabled** | **Boolean** |  | [optional] 
**kinesisFirehoseDestination** | [**KinesisFirehoseDestination**](KinesisFirehoseDestination.md) |  | [optional] 
**matchingEventTypes** | [**[EventType]**](EventType.md) | An array of EventDestination objects. Each EventDestination object includes ARNs and other information that define an event destination. | [optional] 
**snsDestination** | [**SnsDestination**](SnsDestination.md) |  | [optional] 


