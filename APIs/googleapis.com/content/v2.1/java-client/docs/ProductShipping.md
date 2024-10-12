

# ProductShipping


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**country** | **String** | The CLDR territory code of the country to which an item will ship. |  [optional] |
|**locationGroupName** | **String** | The location where the shipping is applicable, represented by a location group name. |  [optional] |
|**locationId** | **String** | The numeric ID of a location that the shipping rate applies to as defined in the Google Ads API. |  [optional] |
|**maxHandlingTime** | **String** | Maximum handling time (inclusive) between when the order is received and shipped in business days. 0 means that the order is shipped on the same day as it&#39;s received if it happens before the cut-off time. Both maxHandlingTime and maxTransitTime are required if providing shipping speeds. |  [optional] |
|**maxTransitTime** | **String** | Maximum transit time (inclusive) between when the order has shipped and when it&#39;s delivered in business days. 0 means that the order is delivered on the same day as it ships. Both maxHandlingTime and maxTransitTime are required if providing shipping speeds. |  [optional] |
|**minHandlingTime** | **String** | Minimum handling time (inclusive) between when the order is received and shipped in business days. 0 means that the order is shipped on the same day as it&#39;s received if it happens before the cut-off time. minHandlingTime can only be present together with maxHandlingTime; but it&#39;s not required if maxHandlingTime is present. |  [optional] |
|**minTransitTime** | **String** | Minimum transit time (inclusive) between when the order has shipped and when it&#39;s delivered in business days. 0 means that the order is delivered on the same day as it ships. minTransitTime can only be present together with maxTransitTime; but it&#39;s not required if maxTransitTime is present. |  [optional] |
|**postalCode** | **String** | The postal code range that the shipping rate applies to, represented by a postal code, a postal code prefix followed by a * wildcard, a range between two postal codes or two postal code prefixes of equal length. |  [optional] |
|**price** | [**Price**](Price.md) |  |  [optional] |
|**region** | **String** | The geographic region to which a shipping rate applies. |  [optional] |
|**service** | **String** | A free-form description of the service class or delivery speed. |  [optional] |



