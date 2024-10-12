

# EventDestinationDefinition

An object that defines the event destination. Specifically, it defines which services receive events from emails sent using the configuration set that the event destination is associated with. Also defines the types of events that are sent to the event destination.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enabled** | [**Boolean**](Boolean.md) |  |  [optional] |
|**matchingEventTypes** | [**List**](List.md) |  |  [optional] |
|**kinesisFirehoseDestination** | [**CreateConfigurationSetEventDestinationRequestEventDestinationKinesisFirehoseDestination**](CreateConfigurationSetEventDestinationRequestEventDestinationKinesisFirehoseDestination.md) |  |  [optional] |
|**cloudWatchDestination** | [**CreateConfigurationSetEventDestinationRequestEventDestinationCloudWatchDestination**](CreateConfigurationSetEventDestinationRequestEventDestinationCloudWatchDestination.md) |  |  [optional] |
|**snsDestination** | [**CreateConfigurationSetEventDestinationRequestEventDestinationSnsDestination**](CreateConfigurationSetEventDestinationRequestEventDestinationSnsDestination.md) |  |  [optional] |
|**pinpointDestination** | [**CreateConfigurationSetEventDestinationRequestEventDestinationPinpointDestination**](CreateConfigurationSetEventDestinationRequestEventDestinationPinpointDestination.md) |  |  [optional] |



