

# NotifyV1ServiceBinding


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Binding resource. |  [optional] |
|**address** | **String** | The channel-specific address. For APNS, the device token. For FCM and GCM, the registration token. For SMS, a phone number in E.164 format. For Facebook Messenger, the Messenger ID of the user or a phone number in E.164 format. |  [optional] |
|**bindingType** | **String** | The transport technology to use for the Binding. Can be: &#x60;apn&#x60;, &#x60;fcm&#x60;, &#x60;gcm&#x60;, &#x60;sms&#x60;, or &#x60;facebook-messenger&#x60;. |  [optional] |
|**credentialSid** | **String** | The SID of the [Credential](https://www.twilio.com/docs/notify/api/credential-resource) resource to be used to send notifications to this Binding. If present, this overrides the Credential specified in the Service resource. Applicable only to &#x60;apn&#x60;, &#x60;fcm&#x60;, and &#x60;gcm&#x60; type Bindings. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**endpoint** | **String** | Deprecated. |  [optional] |
|**identity** | **String** | The &#x60;identity&#x60; value that uniquely identifies the resource&#39;s [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/notify/api/service-resource). Up to 20 Bindings can be created for the same Identity in a given Service. |  [optional] |
|**links** | **Object** | The URLs of related resources. |  [optional] |
|**notificationProtocolVersion** | **String** | The protocol version to use to send the notification. This defaults to the value of &#x60;default_xxxx_notification_protocol_version&#x60; in the [Service](https://www.twilio.com/docs/notify/api/service-resource) for the protocol. The current version is &#x60;\&quot;3\&quot;&#x60; for &#x60;apn&#x60;, &#x60;fcm&#x60;, and &#x60;gcm&#x60; type Bindings. The parameter is not applicable to &#x60;sms&#x60; and &#x60;facebook-messenger&#x60; type Bindings as the data format is fixed. |  [optional] |
|**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/notify/api/service-resource) the resource is associated with. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Binding resource. |  [optional] |
|**tags** | **List&lt;String&gt;** | The list of tags associated with this Binding. Tags can be used to select the Bindings to use when sending a notification. Maximum 20 tags are allowed. |  [optional] |
|**url** | **URI** | The absolute URL of the Binding resource. |  [optional] |



