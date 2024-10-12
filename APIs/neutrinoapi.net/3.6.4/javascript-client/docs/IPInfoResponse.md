# NeutrinoApi.IPInfoResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **String** | Name of the city (if detectable) | 
**continentCode** | **String** | ISO 2-letter continent code | 
**country** | **String** | Full country name | 
**countryCode** | **String** | ISO 2-letter country code | 
**countryCode3** | **String** | ISO 3-letter country code | 
**currencyCode** | **String** | ISO 4217 currency code associated with the country | 
**hostDomain** | **String** | The IPs host domain (only set if reverse-lookup has been used) | 
**hostname** | **String** | The IPs full hostname (only set if reverse-lookup has been used) | 
**ip** | **String** | The IP address | 
**isBogon** | **Boolean** | True if this is a bogon IP address such as a private network, local network or reserved address | 
**isV4Mapped** | **Boolean** | True if this is a &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/IPv6#IPv4-mapped_IPv6_addresses\&quot;&gt;IPv4 mapped IPv6 address&lt;/a&gt; | 
**isV6** | **Boolean** | True if this is a IPv6 address. False if IPv4 | 
**latitude** | **Number** | Location latitude | 
**longitude** | **Number** | Location longitude | 
**region** | **String** | Name of the region (if detectable) | 
**regionCode** | **String** | ISO 3166-2 region code (if detectable) | 
**timezone** | [**Timezone**](Timezone.md) |  | 
**valid** | **Boolean** | True if this is a valid IPv4 or IPv6 address | 


