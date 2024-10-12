# FirebaseCloudMessagingApi.WebpushConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **{String: String}** | Arbitrary key/value payload. If present, it will override google.firebase.fcm.v1.Message.data. | [optional] 
**fcmOptions** | [**WebpushFcmOptions**](WebpushFcmOptions.md) |  | [optional] 
**headers** | **{String: String}** | HTTP headers defined in webpush protocol. Refer to [Webpush protocol](https://tools.ietf.org/html/rfc8030#section-5) for supported headers, e.g. \&quot;TTL\&quot;: \&quot;15\&quot;. | [optional] 
**notification** | **{String: Object}** | Web Notification options as a JSON object. Supports Notification instance properties as defined in [Web Notification API](https://developer.mozilla.org/en-US/docs/Web/API/Notification). If present, \&quot;title\&quot; and \&quot;body\&quot; fields override [google.firebase.fcm.v1.Notification.title] and [google.firebase.fcm.v1.Notification.body]. | [optional] 


