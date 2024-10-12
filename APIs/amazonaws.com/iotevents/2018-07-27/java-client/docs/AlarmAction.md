

# AlarmAction

Specifies one of the following actions to receive notifications when the alarm state changes.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**sns** | [**SNSTopicPublishAction**](SNSTopicPublishAction.md) |  |  [optional] |
|**iotTopicPublish** | [**IotTopicPublishAction**](IotTopicPublishAction.md) |  |  [optional] |
|**lambda** | [**LambdaAction**](LambdaAction.md) |  |  [optional] |
|**iotEvents** | [**IotEventsAction**](IotEventsAction.md) |  |  [optional] |
|**sqs** | [**SqsAction**](SqsAction.md) |  |  [optional] |
|**firehose** | [**FirehoseAction**](FirehoseAction.md) |  |  [optional] |
|**dynamoDB** | [**DynamoDBAction**](DynamoDBAction.md) |  |  [optional] |
|**dynamoDBv2** | [**DynamoDBv2Action**](DynamoDBv2Action.md) |  |  [optional] |
|**iotSiteWise** | [**IotSiteWiseAction**](IotSiteWiseAction.md) |  |  [optional] |



