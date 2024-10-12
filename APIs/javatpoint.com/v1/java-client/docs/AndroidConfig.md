

# AndroidConfig

Android specific options for messages sent through [FCM connection server](https://goo.gl/4GLdUl).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**collapseKey** | **String** | An identifier of a group of messages that can be collapsed, so that only the last message gets sent when delivery can be resumed. A maximum of 4 different collapse keys is allowed at any given time. |  [optional] |
|**data** | **Map&lt;String, String&gt;** | Arbitrary key/value payload. If present, it will override google.firebase.fcm.v1.Message.data. |  [optional] |
|**directBootOk** | **Boolean** | If set to true, messages will be allowed to be delivered to the app while the device is in direct boot mode. See [Support Direct Boot mode](https://developer.android.com/training/articles/direct-boot). |  [optional] |
|**fcmOptions** | [**AndroidFcmOptions**](AndroidFcmOptions.md) |  |  [optional] |
|**notification** | [**AndroidNotification**](AndroidNotification.md) |  |  [optional] |
|**priority** | [**PriorityEnum**](#PriorityEnum) | Message priority. Can take \&quot;normal\&quot; and \&quot;high\&quot; values. For more information, see [Setting the priority of a message](https://goo.gl/GjONJv). |  [optional] |
|**restrictedPackageName** | **String** | Package name of the application where the registration token must match in order to receive the message. |  [optional] |
|**ttl** | **String** | How long (in seconds) the message should be kept in FCM storage if the device is offline. The maximum time to live supported is 4 weeks, and the default value is 4 weeks if not set. Set it to 0 if want to send the message immediately. In JSON format, the Duration type is encoded as a string rather than an object, where the string ends in the suffix \&quot;s\&quot; (indicating seconds) and is preceded by the number of seconds, with nanoseconds expressed as fractional seconds. For example, 3 seconds with 0 nanoseconds should be encoded in JSON format as \&quot;3s\&quot;, while 3 seconds and 1 nanosecond should be expressed in JSON format as \&quot;3.000000001s\&quot;. The ttl will be rounded down to the nearest second. |  [optional] |



## Enum: PriorityEnum

| Name | Value |
|---- | -----|
| NORMAL | &quot;NORMAL&quot; |
| HIGH | &quot;HIGH&quot; |



