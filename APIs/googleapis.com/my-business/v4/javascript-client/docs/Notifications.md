# GoogleMyBusinessApi.Notifications

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Output only. The notifications resource name. | [optional] 
**notificationTypes** | **[String]** | The types of notifications that will be sent to the Cloud Pub/Sub topic. At least one must be specified. To stop receiving notifications entirely, use DeleteNotifications. | [optional] 
**topicName** | **String** | The Google Cloud Pub/Sub topic that will receive notifications when locations managed by this account are updated. If unset, no notifications will be posted. The account mybusiness-api-pubsub@system.gserviceaccount.com must have at least Publish permissions on the Cloud Pub/Sub topic. | [optional] 



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

* `UPDATED_LOCATION_STATE` (value: `"UPDATED_LOCATION_STATE"`)




