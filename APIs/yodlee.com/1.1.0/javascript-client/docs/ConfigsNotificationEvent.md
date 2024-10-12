# YodleeCoreApis.ConfigsNotificationEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callbackUrl** | **String** | URL to which the notification should be posted.&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET configs/notifications/events&lt;/li&gt;&lt;/ul&gt; | [optional] 
**name** | **String** | Name of the event for which the customers must subscribe to receive notifications.&lt;br&gt;&lt;b&gt;Valid Value:&lt;/b&gt; Notification Events Name&lt;br&gt;&lt;br&gt;&lt;b&gt;Endpoints&lt;/b&gt;:&lt;ul&gt;&lt;li&gt;GET configs/notifications/events&lt;/li&gt;&lt;/ul&gt;&lt;b&gt;Applicable Values&lt;/b&gt;&lt;br&gt; | [optional] 



## Enum: NameEnum


* `REFRESH` (value: `"REFRESH"`)

* `DATA_UPDATES` (value: `"DATA_UPDATES"`)

* `AUTO_REFRESH_UPDATES` (value: `"AUTO_REFRESH_UPDATES"`)




