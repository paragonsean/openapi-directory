

# SyncV1ServiceSyncListSyncListItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the List Item resource. |  [optional] |
|**createdBy** | **String** | The identity of the List Item&#39;s creator. If the item is created from the client SDK, the value matches the Access Token&#39;s &#x60;identity&#x60; field. If the item was created from the REST API, the value is &#x60;system&#x60;. |  [optional] |
|**data** | **Object** | An arbitrary, schema-less object that the List Item stores. Can be up to 16 KiB in length. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateExpires** | **OffsetDateTime** | The date and time in GMT when the List Item expires and will be deleted, specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. If the List Item does not expire, this value is &#x60;null&#x60;. The List Item resource might not be deleted immediately after it expires. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**index** | **Integer** | The automatically generated index of the List Item. The &#x60;index&#x60; values of the List Items in a Sync List can have gaps in their sequence. |  [optional] |
|**listSid** | **String** | The SID of the Sync List that contains the List Item. |  [optional] |
|**revision** | **String** | The current revision of the item, represented as a string. |  [optional] |
|**serviceSid** | **String** | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) the resource is associated with. |  [optional] |
|**url** | **URI** | The absolute URL of the List Item resource. |  [optional] |



