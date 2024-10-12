

# DeliveryArea

A delivery area for the product. Only one of `countryCode` or `postalCodeRange` must be set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countryCode** | **String** | Required. The country that the product can be delivered to. Submit a [unicode CLDR region](http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml) such as &#x60;US&#x60; or &#x60;CH&#x60;. |  [optional] |
|**postalCodeRange** | [**DeliveryAreaPostalCodeRange**](DeliveryAreaPostalCodeRange.md) |  |  [optional] |
|**regionCode** | **String** | A state, territory, or prefecture. This is supported for the United States, Australia, and Japan. Provide a subdivision code from the ISO 3166-2 code tables ([US](https://en.wikipedia.org/wiki/ISO_3166-2:US), [AU](https://en.wikipedia.org/wiki/ISO_3166-2:AU), or [JP](https://en.wikipedia.org/wiki/ISO_3166-2:JP)) without country prefix (for example, &#x60;\&quot;NY\&quot;&#x60;, &#x60;\&quot;NSW\&quot;&#x60;, &#x60;\&quot;03\&quot;&#x60;). |  [optional] |



