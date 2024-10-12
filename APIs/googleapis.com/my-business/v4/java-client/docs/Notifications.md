

# Notifications

A Google Cloud Pub/Sub topic where notifications can be published when a location is updated or has a new review. There will be only one notification settings resource per-account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Output only. The notifications resource name. |  [optional] |
|**notificationTypes** | [**List&lt;NotificationTypesEnum&gt;**](#List&lt;NotificationTypesEnum&gt;) | The types of notifications that will be sent to the Cloud Pub/Sub topic. At least one must be specified. To stop receiving notifications entirely, use DeleteNotifications. |  [optional] |
|**topicName** | **String** | The Google Cloud Pub/Sub topic that will receive notifications when locations managed by this account are updated. If unset, no notifications will be posted. The account mybusiness-api-pubsub@system.gserviceaccount.com must have at least Publish permissions on the Cloud Pub/Sub topic. |  [optional] |



## Enum: List&lt;NotificationTypesEnum&gt;

| Name | Value |
|---- | -----|
| NOTIFICATION_TYPE_UNSPECIFIED | &quot;NOTIFICATION_TYPE_UNSPECIFIED&quot; |
| GOOGLE_UPDATE | &quot;GOOGLE_UPDATE&quot; |
| NEW_REVIEW | &quot;NEW_REVIEW&quot; |
| UPDATED_REVIEW | &quot;UPDATED_REVIEW&quot; |
| NEW_CUSTOMER_MEDIA | &quot;NEW_CUSTOMER_MEDIA&quot; |
| NEW_QUESTION | &quot;NEW_QUESTION&quot; |
| UPDATED_QUESTION | &quot;UPDATED_QUESTION&quot; |
| NEW_ANSWER | &quot;NEW_ANSWER&quot; |
| UPDATED_ANSWER | &quot;UPDATED_ANSWER&quot; |
| UPDATED_LOCATION_STATE | &quot;UPDATED_LOCATION_STATE&quot; |



