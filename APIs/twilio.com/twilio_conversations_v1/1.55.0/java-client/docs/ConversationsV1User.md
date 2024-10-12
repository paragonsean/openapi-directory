

# ConversationsV1User


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the User resource. |  [optional] |
|**attributes** | **String** | The JSON Object string that stores application-specific data. If attributes have not been set, &#x60;{}&#x60; is returned. |  [optional] |
|**chatServiceSid** | **String** | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the User resource is associated with. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource. |  [optional] |
|**identity** | **String** | The application-defined string that uniquely identifies the resource&#39;s User within the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource). This value is often a username or an email address, and is case-sensitive. |  [optional] |
|**isNotifiable** | **Boolean** | Whether the User has a potentially valid Push Notification registration (APN or GCM) for this Conversations Service. If at least one registration exists, &#x60;true&#x60;; otherwise &#x60;false&#x60;. This value is only returned by Fetch actions that return a single resource and &#x60;null&#x60; is always returned by a Read action. This value is &#x60;null&#x60; if the Service&#39;s &#x60;reachability_enabled&#x60; is &#x60;false&#x60;, and if the User has never had a notification registration, even if the Service&#39;s &#x60;reachability_enabled&#x60; is &#x60;true&#x60;. |  [optional] |
|**isOnline** | **Boolean** | Whether the User is actively connected to this Conversations Service and online. This value is only returned by Fetch actions that return a single resource and &#x60;null&#x60; is always returned by a Read action. This value is &#x60;null&#x60; if the Service&#39;s &#x60;reachability_enabled&#x60; is &#x60;false&#x60;, if the User has never been online for this Conversations Service, even if the Service&#39;s &#x60;reachability_enabled&#x60; is &#x60;true&#x60;. |  [optional] |
|**links** | **Object** |  |  [optional] |
|**roleSid** | **String** | The SID of a service-level [Role](https://www.twilio.com/docs/conversations/api/role-resource) assigned to the user. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the User resource. |  [optional] |
|**url** | **URI** | An absolute API resource URL for this user. |  [optional] |



