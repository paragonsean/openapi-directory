

# NotificationSetting

A Google Pub/Sub topic where notifications can be published when a location is updated or has a new review. There will be only one notification setting resource per-account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. The resource name this setting is for. This is of the form &#x60;accounts/{account_id}/notificationSetting&#x60;. |  [optional] |
|**notificationTypes** | [**List&lt;NotificationTypesEnum&gt;**](#List&lt;NotificationTypesEnum&gt;) | The types of notifications that will be sent to the Pub/Sub topic. To stop receiving notifications entirely, use NotificationSettings.UpdateNotificationSetting with an empty notification_types or set the pubsub_topic to an empty string. |  [optional] |
|**pubsubTopic** | **String** | Optional. The Google Pub/Sub topic that will receive notifications when locations managed by this account are updated. If unset, no notifications will be posted. The account mybusiness-api-pubsub@system.gserviceaccount.com must have at least Publish permissions on the Pub/Sub topic. |  [optional] |



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
| DUPLICATE_LOCATION | &quot;DUPLICATE_LOCATION&quot; |
| LOSS_OF_VOICE_OF_MERCHANT | &quot;LOSS_OF_VOICE_OF_MERCHANT&quot; |
| VOICE_OF_MERCHANT_UPDATED | &quot;VOICE_OF_MERCHANT_UPDATED&quot; |



