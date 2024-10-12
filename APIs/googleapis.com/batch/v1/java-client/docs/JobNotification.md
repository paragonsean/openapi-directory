

# JobNotification

Notification configurations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | [**Message**](Message.md) |  |  [optional] |
|**pubsubTopic** | **String** | The Pub/Sub topic where notifications like the job state changes will be published. The topic must exist in the same project as the job and billings will be charged to this project. If not specified, no Pub/Sub messages will be sent. Topic format: &#x60;projects/{project}/topics/{topic}&#x60;. |  [optional] |



