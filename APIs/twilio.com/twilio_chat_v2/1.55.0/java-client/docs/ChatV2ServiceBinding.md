

# ChatV2ServiceBinding


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Binding resource. |  [optional] |
|**bindingType** | **BindingEnumBindingType** |  |  [optional] |
|**credentialSid** | **String** | The SID of the [Credential](https://www.twilio.com/docs/chat/rest/credential-resource) for the binding. See [push notification configuration](https://www.twilio.com/docs/chat/push-notification-configuration) for more info. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**endpoint** | **String** | The unique endpoint identifier for the Binding. The format of this value depends on the &#x60;binding_type&#x60;. |  [optional] |
|**identity** | **String** | The application-defined string that uniquely identifies the resource&#39;s [User](https://www.twilio.com/docs/chat/rest/user-resource) within the [Service](https://www.twilio.com/docs/chat/rest/service-resource). See [access tokens](https://www.twilio.com/docs/chat/create-tokens) for more info. |  [optional] |
|**links** | **Object** | The absolute URLs of the Binding&#39;s [User](https://www.twilio.com/docs/chat/rest/user-resource). |  [optional] |
|**messageTypes** | **List&lt;String&gt;** | The [Programmable Chat message types](https://www.twilio.com/docs/chat/push-notification-configuration#push-types) the binding is subscribed to. |  [optional] |
|**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the Binding resource is associated with. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Binding resource. |  [optional] |
|**url** | **URI** | The absolute URL of the Binding resource. |  [optional] |



