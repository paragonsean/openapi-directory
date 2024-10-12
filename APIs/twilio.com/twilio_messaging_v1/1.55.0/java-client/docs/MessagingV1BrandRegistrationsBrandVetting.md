

# MessagingV1BrandRegistrationsBrandVetting


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the vetting record. |  [optional] |
|**brandSid** | **String** | The unique string to identify Brand Registration. |  [optional] |
|**brandVettingSid** | **String** | The Twilio SID of the third-party vetting record. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format. |  [optional] |
|**url** | **URI** | The absolute URL of the Brand Vetting resource. |  [optional] |
|**vettingClass** | **String** | The type of vetting that has been conducted. One of “STANDARD” (Aegis) or “POLITICAL” (Campaign Verify). |  [optional] |
|**vettingId** | **String** | The unique identifier of the vetting from the third-party provider. |  [optional] |
|**vettingProvider** | **BrandVettingEnumVettingProvider** |  |  [optional] |
|**vettingStatus** | **String** | The status of the import vetting attempt. One of “PENDING,” “SUCCESS,” or “FAILED”. |  [optional] |



