

# ConversationsV1ConfigurationAddress


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The unique ID of the [Account](https://www.twilio.com/docs/iam/api/account) the address belongs to |  [optional] |
|**address** | **String** | The unique address to be configured. The address can be a whatsapp address or phone number |  [optional] |
|**addressCountry** | **String** | An ISO 3166-1 alpha-2n country code which the address belongs to. This is currently only applicable to short code addresses. |  [optional] |
|**autoCreation** | **Object** | Auto Creation configuration for the address. |  [optional] |
|**dateCreated** | **OffsetDateTime** | The date that this resource was created. |  [optional] |
|**dateUpdated** | **OffsetDateTime** | The date that this resource was last updated. |  [optional] |
|**friendlyName** | **String** | The human-readable name of this configuration, limited to 256 characters. Optional. |  [optional] |
|**sid** | **String** | A 34 character string that uniquely identifies this resource. |  [optional] |
|**type** | **String** | Type of Address, value can be &#x60;whatsapp&#x60; or &#x60;sms&#x60;. |  [optional] |
|**url** | **URI** | An absolute API resource URL for this address configuration. |  [optional] |



