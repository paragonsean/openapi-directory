

# AddressObject


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**addressId** | **UUID** | As addresses are added to an entity, they&#39;re assigned an id to assist with tracking.   If you&#39;re adjusting an address, you will need to include the addressId so as to be able to reference it correctly in the list.  |  [optional] |
|**addressType** | **EnumAddressType** |  |  [optional] |
|**buildingName** | **String** | The name of the building, apartment block, condo, etc |  [optional] |
|**careOf** | **String** | Individual or business name at this address if not the same as the name of the entity to which this address belongs.  |  [optional] |
|**country** | **String** | The ISO-3166-1 country. You must use the alpha3 country code (e.g. AUS, USA, IDR, KOR, etc) We&#39;ll convert as needed.   See: https://en.wikipedia.org/wiki/ISO_3166-1  |  |
|**endDate** | **LocalDate** | The date this address was no longer used (if available). Used mostly with business addresses.  |  [optional] |
|**longForm** | **String** | In some cases, the address will need to be supplied in \&quot;long form\&quot;, such as when it is determined from a document scan, or is un-parsable in some way. The service will attempt to convert it to it&#39;s constituent parts where possible.  WARNING: Use of longForm is not guaranteed to produce perfect results, due to the variety of potential formats. You&#39;ve been warned.  Failure to break down or disambiguate the address will result in an error.  |  [optional] |
|**postalCode** | **String** | The post code of the address. |  [optional] |
|**region** | **String** | The county, province, cantonment |  [optional] |
|**startDate** | **LocalDate** | The date this address first because active. Used mostly with business addresses.  |  [optional] |
|**state** | **String** | The state. Use local abbreviations, such as VIC(toria) or TX (Texas) |  [optional] |
|**streetName** | **String** | The name of the street  This field can in fact be a bit flexible, potentially containing the streetNumber and streetType as well. Most services in use can work it out.  If this field has been auto-populated by Google (see writeup here:  https://apidocs.frankiefinancial.com/docs/working-with-addresses then the bulk of the address will be in this field.  If you can avoid it though, please try and keep things separate.  |  [optional] |
|**streetNumber** | **String** | The number on the street. Generally a number, but can also be alphanumeric (e.g. 3A)  |  [optional] |
|**streetType** | **String** | The street \&quot;type\&quot; - e.g. Road, St, Ave, Circuit, etc |  [optional] |
|**suburb** | **String** | The suburb in the town/city. Only use this if you require a suburb AND a town/city, otherwise, just use the \&quot;town\&quot; parameter. |  [optional] |
|**town** | **String** | The town/village/suburb/city |  [optional] |
|**unitNumber** | **String** | Unit/Apartment/Flat/Suite/etc number |  [optional] |



