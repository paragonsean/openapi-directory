

# ChatV1ServiceUser


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/api/rest/account) that created the User resource. |  [optional] |
|**attributes** | **String** | The JSON string that stores application-specific data. **Note** If this property has been assigned a value, it&#39;s only  displayed in a FETCH action that returns a single resource; otherwise, it&#39;s null. If the attributes have not been set, &#x60;{}&#x60; is returned. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [RFC 2822](http://www.ietf.org/rfc/rfc2822.txt) format. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource. |  [optional] |
|**identity** | **String** | The application-defined string that uniquely identifies the resource&#39;s User within the [Service](https://www.twilio.com/docs/api/chat/rest/services). This value is often a username or an email address. See [access tokens](https://www.twilio.com/docs/api/chat/guides/create-tokens) for more info. |  [optional] |
|**isNotifiable** | **Boolean** | Whether the User has a potentially valid Push Notification registration (APN or GCM) for the Service instance. If at least one registration exists, &#x60;true&#x60;; otherwise &#x60;false&#x60;. This value is only returned by Fetch actions that return a single resource and &#x60;null&#x60; is always returned by a Read action. This value is &#x60;null&#x60; if the Service&#39;s &#x60;reachability_enabled&#x60; is &#x60;false&#x60;, and if the User has never had a notification registration, even if the Service&#39;s &#x60;reachability_enabled&#x60; is &#x60;true&#x60;. |  [optional] |
|**isOnline** | **Boolean** | Whether the User is actively connected to the Service instance and online. This value is only returned by Fetch actions that return a single resource and &#x60;null&#x60; is always returned by a Read action. This value is &#x60;null&#x60; if the Service&#39;s &#x60;reachability_enabled&#x60; is &#x60;false&#x60;, if the User has never been online for the Service instance, even if the Service&#39;s &#x60;reachability_enabled&#x60; is &#x60;true&#x60;. |  [optional] |
|**joinedChannelsCount** | **Integer** | The number of Channels this User is a Member of. |  [optional] |
|**links** | **Object** | The absolute URLs of the [Channel](https://www.twilio.com/docs/chat/api/channels) and [Binding](https://www.twilio.com/docs/chat/rest/bindings-resource) resources related to the user. |  [optional] |
|**roleSid** | **String** | The SID of the [Role](https://www.twilio.com/docs/api/chat/rest/roles) assigned to the user. |  [optional] |
|**serviceSid** | **String** | The SID of the [Service](https://www.twilio.com/docs/api/chat/rest/services) the resource is associated with. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the User resource. |  [optional] |
|**url** | **URI** | The absolute URL of the User resource. |  [optional] |



