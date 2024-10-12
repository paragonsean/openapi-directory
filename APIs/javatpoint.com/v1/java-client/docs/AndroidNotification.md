

# AndroidNotification

Notification to send to android devices.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**body** | **String** | The notification&#39;s body text. If present, it will override google.firebase.fcm.v1.Notification.body. |  [optional] |
|**bodyLocArgs** | **List&lt;String&gt;** | Variable string values to be used in place of the format specifiers in body_loc_key to use to localize the body text to the user&#39;s current localization. See [Formatting and Styling](https://goo.gl/MalYE3) for more information. |  [optional] |
|**bodyLocKey** | **String** | The key to the body string in the app&#39;s string resources to use to localize the body text to the user&#39;s current localization. See [String Resources](https://goo.gl/NdFZGI) for more information. |  [optional] |
|**bypassProxyNotification** | **Boolean** | If set, display notifications delivered to the device will be handled by the app instead of the proxy. |  [optional] |
|**channelId** | **String** | The [notification&#39;s channel id](https://developer.android.com/guide/topics/ui/notifiers/notifications#ManageChannels) (new in Android O). The app must create a channel with this channel ID before any notification with this channel ID is received. If you don&#39;t send this channel ID in the request, or if the channel ID provided has not yet been created by the app, FCM uses the channel ID specified in the app manifest. |  [optional] |
|**clickAction** | **String** | The action associated with a user click on the notification. If specified, an activity with a matching intent filter is launched when a user clicks on the notification. |  [optional] |
|**color** | **String** | The notification&#39;s icon color, expressed in #rrggbb format. |  [optional] |
|**defaultLightSettings** | **Boolean** | If set to true, use the Android framework&#39;s default LED light settings for the notification. Default values are specified in [config.xml](https://android.googlesource.com/platform/frameworks/base/+/master/core/res/res/values/config.xml). If &#x60;default_light_settings&#x60; is set to true and &#x60;light_settings&#x60; is also set, the user-specified &#x60;light_settings&#x60; is used instead of the default value. |  [optional] |
|**defaultSound** | **Boolean** | If set to true, use the Android framework&#39;s default sound for the notification. Default values are specified in [config.xml](https://android.googlesource.com/platform/frameworks/base/+/master/core/res/res/values/config.xml). |  [optional] |
|**defaultVibrateTimings** | **Boolean** | If set to true, use the Android framework&#39;s default vibrate pattern for the notification. Default values are specified in [config.xml](https://android.googlesource.com/platform/frameworks/base/+/master/core/res/res/values/config.xml). If &#x60;default_vibrate_timings&#x60; is set to true and &#x60;vibrate_timings&#x60; is also set, the default value is used instead of the user-specified &#x60;vibrate_timings&#x60;. |  [optional] |
|**eventTime** | **String** | Set the time that the event in the notification occurred. Notifications in the panel are sorted by this time. A point in time is represented using [protobuf.Timestamp](https://developers.google.com/protocol-buffers/docs/reference/java/com/google/protobuf/Timestamp). |  [optional] |
|**icon** | **String** | The notification&#39;s icon. Sets the notification icon to myicon for drawable resource myicon. If you don&#39;t send this key in the request, FCM displays the launcher icon specified in your app manifest. |  [optional] |
|**image** | **String** | Contains the URL of an image that is going to be displayed in a notification. If present, it will override google.firebase.fcm.v1.Notification.image. |  [optional] |
|**lightSettings** | [**LightSettings**](LightSettings.md) |  |  [optional] |
|**localOnly** | **Boolean** | Set whether or not this notification is relevant only to the current device. Some notifications can be bridged to other devices for remote display, such as a Wear OS watch. This hint can be set to recommend this notification not be bridged. See [Wear OS guides](https://developer.android.com/training/wearables/notifications/bridger#existing-method-of-preventing-bridging) |  [optional] |
|**notificationCount** | **Integer** | Sets the number of items this notification represents. May be displayed as a badge count for launchers that support badging.See [Notification Badge](https://developer.android.com/training/notify-user/badges). For example, this might be useful if you&#39;re using just one notification to represent multiple new messages but you want the count here to represent the number of total new messages. If zero or unspecified, systems that support badging use the default, which is to increment a number displayed on the long-press menu each time a new notification arrives. |  [optional] |
|**notificationPriority** | [**NotificationPriorityEnum**](#NotificationPriorityEnum) | Set the relative priority for this notification. Priority is an indication of how much of the user&#39;s attention should be consumed by this notification. Low-priority notifications may be hidden from the user in certain situations, while the user might be interrupted for a higher-priority notification. The effect of setting the same priorities may differ slightly on different platforms. Note this priority differs from &#x60;AndroidMessagePriority&#x60;. This priority is processed by the client after the message has been delivered, whereas [AndroidMessagePriority](https://firebase.google.com/docs/reference/fcm/rest/v1/projects.messages#androidmessagepriority) is an FCM concept that controls when the message is delivered. |  [optional] |
|**sound** | **String** | The sound to play when the device receives the notification. Supports \&quot;default\&quot; or the filename of a sound resource bundled in the app. Sound files must reside in /res/raw/. |  [optional] |
|**sticky** | **Boolean** | When set to false or unset, the notification is automatically dismissed when the user clicks it in the panel. When set to true, the notification persists even when the user clicks it. |  [optional] |
|**tag** | **String** | Identifier used to replace existing notifications in the notification drawer. If not specified, each request creates a new notification. If specified and a notification with the same tag is already being shown, the new notification replaces the existing one in the notification drawer. |  [optional] |
|**ticker** | **String** | Sets the \&quot;ticker\&quot; text, which is sent to accessibility services. Prior to API level 21 (&#x60;Lollipop&#x60;), sets the text that is displayed in the status bar when the notification first arrives. |  [optional] |
|**title** | **String** | The notification&#39;s title. If present, it will override google.firebase.fcm.v1.Notification.title. |  [optional] |
|**titleLocArgs** | **List&lt;String&gt;** | Variable string values to be used in place of the format specifiers in title_loc_key to use to localize the title text to the user&#39;s current localization. See [Formatting and Styling](https://goo.gl/MalYE3) for more information. |  [optional] |
|**titleLocKey** | **String** | The key to the title string in the app&#39;s string resources to use to localize the title text to the user&#39;s current localization. See [String Resources](https://goo.gl/NdFZGI) for more information. |  [optional] |
|**vibrateTimings** | **List&lt;String&gt;** | Set the vibration pattern to use. Pass in an array of [protobuf.Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration) to turn on or off the vibrator. The first value indicates the &#x60;Duration&#x60; to wait before turning the vibrator on. The next value indicates the &#x60;Duration&#x60; to keep the vibrator on. Subsequent values alternate between &#x60;Duration&#x60; to turn the vibrator off and to turn the vibrator on. If &#x60;vibrate_timings&#x60; is set and &#x60;default_vibrate_timings&#x60; is set to &#x60;true&#x60;, the default value is used instead of the user-specified &#x60;vibrate_timings&#x60;. |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | Set the [Notification.visibility](https://developer.android.com/reference/android/app/Notification.html#visibility) of the notification. |  [optional] |



## Enum: NotificationPriorityEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PRIORITY_UNSPECIFIED&quot; |
| MIN | &quot;PRIORITY_MIN&quot; |
| LOW | &quot;PRIORITY_LOW&quot; |
| DEFAULT | &quot;PRIORITY_DEFAULT&quot; |
| HIGH | &quot;PRIORITY_HIGH&quot; |
| MAX | &quot;PRIORITY_MAX&quot; |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| VISIBILITY_UNSPECIFIED | &quot;VISIBILITY_UNSPECIFIED&quot; |
| PRIVATE | &quot;PRIVATE&quot; |
| PUBLIC | &quot;PUBLIC&quot; |
| SECRET | &quot;SECRET&quot; |



