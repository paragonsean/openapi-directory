# HetrasBookingApiVersion0.MailingAddress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **String** | The address details like street, number, and other in free format | [optional] 
**addressType** | **String** | One of the values from the enumeration of allowed address types | [optional] 
**city** | **String** | The city name for this address | [optional] 
**country** | **String** | The country code for this address in ISO 3166-1 alpha-2 format              (see: &lt;a href&#x3D;\&quot;http://www.iso.org/iso/country_codes/iso_3166_code_lists/country_names_and_code_elements.htm\&quot; onfocus&#x3D;\&quot;this.blur()\&quot; target&#x3D;\&quot;_blank\&quot;&gt;http://www.iso.org/iso/country_codes/iso_3166_code_lists/country_names_and_code_elements.htm&lt;/a&gt;) | [optional] 
**postalCode** | **String** | The postal code for this address | [optional] 



## Enum: AddressTypeEnum


* `Home` (value: `"Home"`)

* `Business` (value: `"Business"`)

* `Billing` (value: `"Billing"`)

* `Other` (value: `"Other"`)




