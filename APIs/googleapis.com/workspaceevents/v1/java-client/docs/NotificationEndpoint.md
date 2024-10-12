

# NotificationEndpoint

The endpoint where the subscription delivers events.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pubsubTopic** | **String** | Immutable. The Cloud Pub/Sub topic that receives events for the subscription. Format: &#x60;projects/{project}/topics/{topic}&#x60; You must create the topic in the same Google Cloud project where you create this subscription. When the topic receives events, the events are encoded as Cloud Pub/Sub messages. For details, see the [Google Cloud Pub/Sub Protocol Binding for CloudEvents](https://github.com/googleapis/google-cloudevents/blob/main/docs/spec/pubsub.md). |  [optional] |



