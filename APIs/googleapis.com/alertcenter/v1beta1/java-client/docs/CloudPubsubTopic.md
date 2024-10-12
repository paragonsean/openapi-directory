

# CloudPubsubTopic

A reference to a Cloud Pubsub topic. To register for notifications, the owner of the topic must grant `alerts-api-push-notifications@system.gserviceaccount.com` the `projects.topics.publish` permission.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**payloadFormat** | [**PayloadFormatEnum**](#PayloadFormatEnum) | Optional. The format of the payload that would be sent. If not specified the format will be JSON. |  [optional] |
|**topicName** | **String** | The &#x60;name&#x60; field of a Cloud Pubsub [Topic] (https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics#Topic). |  [optional] |



## Enum: PayloadFormatEnum

| Name | Value |
|---- | -----|
| PAYLOAD_FORMAT_UNSPECIFIED | &quot;PAYLOAD_FORMAT_UNSPECIFIED&quot; |
| JSON | &quot;JSON&quot; |



