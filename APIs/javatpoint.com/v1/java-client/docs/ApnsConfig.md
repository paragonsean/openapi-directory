

# ApnsConfig

[Apple Push Notification Service](https://goo.gl/MXRTPa) specific options.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**fcmOptions** | [**ApnsFcmOptions**](ApnsFcmOptions.md) |  |  [optional] |
|**headers** | **Map&lt;String, String&gt;** | HTTP request headers defined in Apple Push Notification Service. Refer to [APNs request headers](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/sending_notification_requests_to_apns) for supported headers such as &#x60;apns-expiration&#x60; and &#x60;apns-priority&#x60;. The backend sets a default value for &#x60;apns-expiration&#x60; of 30 days and a default value for &#x60;apns-priority&#x60; of 10 if not explicitly set. |  [optional] |
|**payload** | **Map&lt;String, Object&gt;** | APNs payload as a JSON object, including both &#x60;aps&#x60; dictionary and custom payload. See [Payload Key Reference](https://developer.apple.com/documentation/usernotifications/setting_up_a_remote_notification_server/generating_a_remote_notification). If present, it overrides google.firebase.fcm.v1.Notification.title and google.firebase.fcm.v1.Notification.body. |  [optional] |



