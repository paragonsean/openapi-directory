

# ElectronicAddress

The Electronic Address resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**areaCode** | **String** | The area code, for example, \&quot;02\&quot;. |  [optional] |
|**countryPrefix** | **String** | The country prefix, for example, \&quot;61\&quot;. |  [optional] |
|**electronicAddressType** | [**ElectronicAddressTypeEnum**](#ElectronicAddressTypeEnum) | The electronic address type. |  [optional] |
|**email** | **String** | The email address, for example, \&quot;robert.ferguson@ato.gov.au\&quot;. |  [optional] |
|**extension** | **String** | The extension number, for example, \&quot;4453\&quot;. |  [optional] |
|**fromDate** | **OffsetDateTime** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |
|**id** | [**AddressId**](AddressId.md) | The resource&#39;s unique identifier. |  [optional] [readonly] |
|**number** | **String** | The number, for example, \&quot;62164453\&quot;. |  [optional] |
|**toDate** | **OffsetDateTime** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). |  [optional] [readonly] |
|**url** | **String** | The website address, for example, \&quot;https://ato.gov.au\&quot;. |  [optional] |



## Enum: ElectronicAddressTypeEnum

| Name | Value |
|---- | -----|
| EMAIL | &quot;Email&quot; |
| FAX | &quot;Fax&quot; |
| LANDLINE | &quot;Landline&quot; |
| MOBILE | &quot;Mobile&quot; |
| WEBSITE | &quot;Website&quot; |



