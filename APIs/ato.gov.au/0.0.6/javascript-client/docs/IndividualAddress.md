# BusinessRegistries.IndividualAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **String** | The city. | [optional] 
**country** | **String** | The country. | [optional] 
**fromDate** | **Date** | The date and time the resource became active in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 
**id** | [**AddressId**](AddressId.md) | The resource&#39;s unique identifier. | [optional] [readonly] 
**line1** | **String** | The address line 1. | [optional] 
**line2** | **String** | The address line 2. | [optional] 
**line3** | **String** | The address line 3. | [optional] 
**name** | **String** | The address name. | [optional] 
**postalCode** | **String** | The postal code. | [optional] 
**suburb** | **String** | The suburb. | [optional] 
**toDate** | **Date** | The date and time the resource became inactive in the format defined by [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601). | [optional] [readonly] 
**addressType** | **String** | The address type. | [optional] [default to &#39;Principal Place of Residence&#39;]



## Enum: AddressTypeEnum


* `Mailing` (value: `"Mailing"`)

* `Principal Place of Business` (value: `"Principal Place of Business"`)

* `Principal Place of Residence` (value: `"Principal Place of Residence"`)




