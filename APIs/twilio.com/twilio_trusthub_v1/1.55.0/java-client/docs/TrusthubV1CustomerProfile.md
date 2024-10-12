

# TrusthubV1CustomerProfile


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Customer-Profile resource. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**email** | **String** | The email address that will receive updates when the Customer-Profile resource changes status. |  [optional] |
|**friendlyName** | **String** | The string that you assigned to describe the resource. |  [optional] |
|**links** | **Object** | The URLs of the Assigned Items of the Customer-Profile resource. |  [optional] |
|**policySid** | **String** | The unique string of a policy that is associated to the Customer-Profile resource. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Customer-Profile resource. |  [optional] |
|**status** | **CustomerProfileEnumStatus** |  |  [optional] |
|**statusCallback** | **URI** | The URL we call to inform your application of status changes. |  [optional] |
|**url** | **URI** | The absolute URL of the Customer-Profile resource. |  [optional] |
|**validUntil** | **OffsetDateTime** | The date and time in GMT in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format when the resource will be valid until. |  [optional] |



