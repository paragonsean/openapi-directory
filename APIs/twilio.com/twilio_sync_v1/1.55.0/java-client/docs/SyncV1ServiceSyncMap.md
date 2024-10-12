

# SyncV1ServiceSyncMap


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Sync Map resource. |  [optional] |
|**createdBy** | **String** | The identity of the Sync Map&#39;s creator. If the Sync Map is created from the client SDK, the value matches the Access Token&#39;s &#x60;identity&#x60; field. If the Sync Map was created from the REST API, the value is &#x60;system&#x60;. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateExpires** | **OffsetDateTime** | The date and time in GMT when the Sync Map expires and will be deleted, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. If the Sync Map does not expire, this value is &#x60;null&#x60;. The Sync Map might not be deleted immediately after it expires. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**links** | **Object** | The URLs of the Sync Map&#39;s nested resources. |  [optional] |
|**revision** | **String** | The current revision of the Sync Map, represented as a string. |  [optional] |
|**serviceSid** | **String** | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) the resource is associated with. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the Sync Map resource. |  [optional] |
|**uniqueName** | **String** | An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. |  [optional] |
|**url** | **URI** | The absolute URL of the Sync Map resource. |  [optional] |



