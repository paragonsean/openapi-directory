

# ConversationsV1Role


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Role resource. |  [optional] |
|**chatServiceSid** | **String** | The SID of the [Conversation Service](https://www.twilio.com/docs/conversations/api/service-resource) the Role resource is associated with. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource. |  [optional] |
|**permissions** | **List&lt;String&gt;** | An array of the permissions the role has been granted. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Role resource. |  [optional] |
|**type** | **RoleEnumRoleType** |  |  [optional] |
|**url** | **URI** | An absolute API resource URL for this user role. |  [optional] |



