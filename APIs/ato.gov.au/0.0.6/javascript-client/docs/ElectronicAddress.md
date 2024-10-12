# BusinessRegistries.ElectronicAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**areaCode** | **String** | The area code, for example, \&quot;02\&quot;. | [optional] 
**countryPrefix** | **String** | The country prefix, for example, \&quot;61\&quot;. | [optional] 
**electronicAddressType** | **String** | The electronic address type. | [optional] [default to &#39;Landline&#39;]
**email** | **String** | The email address, for example, \&quot;robert.ferguson@ato.gov.au\&quot;. | [optional] 
**extension** | **String** | The extension number, for example, \&quot;4453\&quot;. | [optional] 
**fromDate** | **Date** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 
**id** | [**AddressId**](AddressId.md) | The resource&#39;s unique identifier. | [optional] [readonly] 
**number** | **String** | The number, for example, \&quot;62164453\&quot;. | [optional] 
**toDate** | **Date** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 
**url** | **String** | The website address, for example, \&quot;https://ato.gov.au\&quot;. | [optional] 



## Enum: ElectronicAddressTypeEnum


* `Email` (value: `"Email"`)

* `Fax` (value: `"Fax"`)

* `Landline` (value: `"Landline"`)

* `Mobile` (value: `"Mobile"`)

* `Website` (value: `"Website"`)




