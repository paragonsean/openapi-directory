# PeopleApi.Address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **String** | The city of the address. | [optional] 
**country** | **String** | The country of the address. | [optional] 
**countryCode** | **String** | The [ISO 3166-1 alpha-2](http://www.iso.org/iso/country_codes.htm) country code of the address. | [optional] 
**extendedAddress** | **String** | The extended address of the address; for example, the apartment number. | [optional] 
**formattedType** | **String** | Output only. The type of the address translated and formatted in the viewer&#39;s account locale or the &#x60;Accept-Language&#x60; HTTP header locale. | [optional] [readonly] 
**formattedValue** | **String** | The unstructured value of the address. If this is not set by the user it will be automatically constructed from structured values. | [optional] 
**metadata** | [**FieldMetadata**](FieldMetadata.md) |  | [optional] 
**poBox** | **String** | The P.O. box of the address. | [optional] 
**postalCode** | **String** | The postal code of the address. | [optional] 
**region** | **String** | The region of the address; for example, the state or province. | [optional] 
**streetAddress** | **String** | The street address. | [optional] 
**type** | **String** | The type of the address. The type can be custom or one of these predefined values: * &#x60;home&#x60; * &#x60;work&#x60; * &#x60;other&#x60; | [optional] 


