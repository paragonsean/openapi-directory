

# Address

Represents a postal address in a country. The address format is based  on an [open-source library from Google](https://github.com/google/libaddressinput). For more information,  see [AddressValidationMetadata](https://github.com/google/libaddressinput/wiki/AddressValidationMetadata).  This format has dedicated fields for four address components: postal code,  locality (city), administrative district (state, prefecture, or province), and  sublocality (town or village). These components have dedicated fields in the  `Address` object because software sometimes behaves differently based on them.  For example, sales tax software may charge different amounts of sales tax  based on the postal code, and some software is only available in  certain states due to compliance reasons.  For the remaining address components, the `Address` type provides the  `address_line_1` and `address_line_2` fields for free-form data entry.  These fields are free-form because the remaining address components have  too many variations around the world and typical software does not parse  these components. These fields enable users to enter anything they want.   Note that, in the current implementation, all other `Address` type fields are blank.  These include `address_line_3`, `sublocality_2`, `sublocality_3`,  `administrative_district_level_2`, `administrative_district_level_3`,  `first_name`, `last_name`, and `organization`.   When it comes to localization, the seller's language preferences  (see [Language preferences](https://developer.squareup.com/docs/locations-api#location-specific-and-seller-level-language-preferences))  are ignored for addresses. Even though Square products (such as Square Point of Sale  and the Seller Dashboard) mostly use a seller's language preference in  communication, when it comes to addresses, they will use English for a US address,  Japanese for an address in Japan, and so on.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressLine1** | **String** | The first line of the address.  Fields that start with &#x60;address_line&#x60; provide the address&#39;s most specific details, like street number, street name, and building name. They do *not* provide less specific details like city, state/province, or country (these details are provided in other fields). |  [optional] |
|**addressLine2** | **String** | The second line of the address, if any. |  [optional] |
|**addressLine3** | **String** | The third line of the address, if any. |  [optional] |
|**administrativeDistrictLevel1** | **String** | A civil entity within the address&#39;s country. In the US, this is the state. |  [optional] |
|**administrativeDistrictLevel2** | **String** | A civil entity within the address&#39;s &#x60;administrative_district_level_1&#x60;. In the US, this is the county. |  [optional] |
|**administrativeDistrictLevel3** | **String** | A civil entity within the address&#39;s &#x60;administrative_district_level_2&#x60;, if any. |  [optional] |
|**country** | **String** | The address&#39;s country, in ISO 3166-1-alpha-2 format. |  [optional] |
|**firstName** | **String** | Optional first name when it&#39;s representing recipient. |  [optional] |
|**lastName** | **String** | Optional last name when it&#39;s representing recipient. |  [optional] |
|**locality** | **String** | The city or town of the address. |  [optional] |
|**organization** | **String** | Optional organization name when it&#39;s representing recipient. |  [optional] |
|**postalCode** | **String** | The address&#39;s postal code. |  [optional] |
|**sublocality** | **String** | A civil region within the address&#39;s &#x60;locality&#x60;, if any. |  [optional] |
|**sublocality2** | **String** | A civil region within the address&#39;s &#x60;sublocality&#x60;, if any. |  [optional] |
|**sublocality3** | **String** | A civil region within the address&#39;s &#x60;sublocality_2&#x60;, if any. |  [optional] |



