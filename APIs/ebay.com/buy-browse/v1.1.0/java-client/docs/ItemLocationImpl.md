

# ItemLocationImpl

The type that defines the fields for the location of an item, such as information typically used for an address, including postal code, county, state/province, street address, city, and country (2-digit ISO code).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressLine1** | **String** | The first line of the street address. |  [optional] |
|**addressLine2** | **String** | The second line of the street address. This field may contain such values as an apartment or suite number. |  [optional] |
|**city** | **String** | The city in which the item is located. Restriction: This field is populated in the search method response only when fieldgroups &#x3D; EXTENDED. |  [optional] |
|**country** | **String** | The two-letter ISO 3166 standard code that indicates the country in which the item is located. For implementation help, refer to &lt;a href&#x3D;&#39;https://developer.ebay.com/api-docs/buy/browse/types/ba:CountryCodeEnum&#39;&gt;eBay API documentation&lt;/a&gt; |  [optional] |
|**county** | **String** | The county in which the item is located. |  [optional] |
|**postalCode** | **String** | The postal code (or zip code in US) where the item is located. Sellers set a postal code (or zip code in US) for items when they are listed. The postal code is used for calculating proximity searches. It is anonymized when returned in itemLocation.postalCode via the API. |  [optional] |
|**stateOrProvince** | **String** | The state or province in which the item is located. |  [optional] |



