

# GoogleCloudRetailV2ImportCompletionDataRequest

Request message for ImportCompletionData methods.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inputConfig** | [**GoogleCloudRetailV2CompletionDataInputConfig**](GoogleCloudRetailV2CompletionDataInputConfig.md) |  |  [optional] |
|**notificationPubsubTopic** | **String** | Pub/Sub topic for receiving notification. If this field is set, when the import is finished, a notification is sent to specified Pub/Sub topic. The message data is JSON string of a Operation. Format of the Pub/Sub topic is &#x60;projects/{project}/topics/{topic}&#x60;. |  [optional] |



