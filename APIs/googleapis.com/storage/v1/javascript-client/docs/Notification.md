# CloudStorageJsonApi.Notification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customAttributes** | **{String: String}** | An optional list of additional attributes to attach to each Cloud PubSub message published for this notification subscription. | [optional] 
**etag** | **String** | HTTP 1.1 Entity tag for this subscription notification. | [optional] 
**eventTypes** | **[String]** | If present, only send notifications about listed event types. If empty, sent notifications for all event types. | [optional] 
**id** | **String** | The ID of the notification. | [optional] 
**kind** | **String** | The kind of item this is. For notifications, this is always storage#notification. | [optional] [default to &#39;storage#notification&#39;]
**objectNamePrefix** | **String** | If present, only apply this notification configuration to object names that begin with this prefix. | [optional] 
**payloadFormat** | **String** | The desired content of the Payload. | [optional] [default to &#39;JSON_API_V1&#39;]
**selfLink** | **String** | The canonical URL of this notification. | [optional] 
**topic** | **String** | The Cloud PubSub topic to which this subscription publishes. Formatted as: &#39;//pubsub.googleapis.com/projects/{project-identifier}/topics/{my-topic}&#39; | [optional] 


