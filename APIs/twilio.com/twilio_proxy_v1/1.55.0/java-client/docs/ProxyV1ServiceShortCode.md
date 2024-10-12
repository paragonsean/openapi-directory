

# ProxyV1ServiceShortCode


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource. |  [optional] |
|**capabilities** | [**ProxyV1ServiceShortCodeCapabilities**](ProxyV1ServiceShortCodeCapabilities.md) |  |  [optional] |
|**dateCreated** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was created. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) date and time in GMT when the resource was last updated. |  [optional] |
|**isReserved** | **Boolean** | Whether the short code should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information. |  [optional] |
|**isoCountry** | **String** | The ISO Country Code for the short code. |  [optional] |
|**serviceSid** | **String** | The SID of the ShortCode resource&#39;s parent [Service](https://www.twilio.com/docs/proxy/api/service) resource. |  [optional] |
|**shortCode** | **String** | The short code&#39;s number. |  [optional] |
|**sid** | **String** | The unique string that we created to identify the ShortCode resource. |  [optional] |
|**url** | **URI** | The absolute URL of the ShortCode resource. |  [optional] |



