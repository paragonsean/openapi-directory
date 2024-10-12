

# TaskrouterV1WorkspaceActivity


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Activity resource. |  [optional] |
|**available** | **Boolean** | Whether the Worker is eligible to receive a Task when it occupies the Activity. A value of &#x60;true&#x60;, &#x60;1&#x60;, or &#x60;yes&#x60; indicates the Activity is available. All other values indicate that it is not. The value cannot be changed after the Activity is created. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the Activity resource. |  [optional] |
|**links** | **Object** |  |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Activity resource. |  [optional] |
|**url** | **URI** | The absolute URL of the Activity resource. |  [optional] |
|**workspaceSid** | **String** | The SID of the Workspace that contains the Activity. |  [optional] |



