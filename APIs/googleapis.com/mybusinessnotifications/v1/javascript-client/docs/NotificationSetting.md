# MyBusinessNotificationsApi.NotificationSetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Required. The resource name this setting is for. This is of the form &#x60;accounts/{account_id}/notificationSetting&#x60;. | [optional] 
**notificationTypes** | **[String]** | The types of notifications that will be sent to the Pub/Sub topic. To stop receiving notifications entirely, use NotificationSettings.UpdateNotificationSetting with an empty notification_types or set the pubsub_topic to an empty string. | [optional] 
**pubsubTopic** | **String** | Optional. The Google Pub/Sub topic that will receive notifications when locations managed by this account are updated. If unset, no notifications will be posted. The account mybusiness-api-pubsub@system.gserviceaccount.com must have at least Publish permissions on the Pub/Sub topic. | [optional] 



## Enum: [NotificationTypesEnum]


* `NOTIFICATION_TYPE_UNSPECIFIED` (value: `"NOTIFICATION_TYPE_UNSPECIFIED"`)

* `GOOGLE_UPDATE` (value: `"GOOGLE_UPDATE"`)

* `NEW_REVIEW` (value: `"NEW_REVIEW"`)

* `UPDATED_REVIEW` (value: `"UPDATED_REVIEW"`)

* `NEW_CUSTOMER_MEDIA` (value: `"NEW_CUSTOMER_MEDIA"`)

* `NEW_QUESTION` (value: `"NEW_QUESTION"`)

* `UPDATED_QUESTION` (value: `"UPDATED_QUESTION"`)

* `NEW_ANSWER` (value: `"NEW_ANSWER"`)

* `UPDATED_ANSWER` (value: `"UPDATED_ANSWER"`)

* `DUPLICATE_LOCATION` (value: `"DUPLICATE_LOCATION"`)

* `LOSS_OF_VOICE_OF_MERCHANT` (value: `"LOSS_OF_VOICE_OF_MERCHANT"`)

* `VOICE_OF_MERCHANT_UPDATED` (value: `"VOICE_OF_MERCHANT_UPDATED"`)




