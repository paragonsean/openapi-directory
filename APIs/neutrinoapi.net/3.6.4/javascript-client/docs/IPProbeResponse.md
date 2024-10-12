# NeutrinoApi.IPProbeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asAge** | **Number** | The age of the autonomous system (AS) in number of years since registration | 
**asCidr** | **String** | The autonomous system (AS) CIDR range | 
**asCountryCode** | **String** | The autonomous system (AS) ISO 2-letter country code | 
**asCountryCode3** | **String** | The autonomous system (AS) ISO 3-letter country code | 
**asDescription** | **String** | The autonomous system (AS) description / company name | 
**asDomains** | **[String]** | Array of all the domains associated with the autonomous system (AS) | 
**asn** | **String** | The autonomous system (AS) number | 
**city** | **String** | Full city name (if detectable) | 
**continentCode** | **String** | ISO 2-letter continent code | 
**country** | **String** | Full country name | 
**countryCode** | **String** | ISO 2-letter country code | 
**countryCode3** | **String** | ISO 3-letter country code | 
**currencyCode** | **String** | ISO 4217 currency code associated with the country | 
**hostDomain** | **String** | The IPs host domain | 
**hostname** | **String** | The IPs full hostname (PTR) | 
**ip** | **String** | The IP address | 
**isBogon** | **Boolean** | True if this is a bogon IP address such as a private network, local network or reserved address | 
**isHosting** | **Boolean** | True if this IP belongs to a hosting company. Note that this can still be true even if the provider type is VPN/proxy, this occurs in the case that the IP is detected as both types | 
**isIsp** | **Boolean** | True if this IP belongs to an internet service provider. Note that this can still be true even if the provider type is VPN/proxy, this occurs in the case that the IP is detected as both types | 
**isProxy** | **Boolean** | True if this IP ia a proxy | 
**isV4Mapped** | **Boolean** | True if this is a &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/IPv6#IPv4-mapped_IPv6_addresses\&quot;&gt;IPv4 mapped IPv6 address&lt;/a&gt; | 
**isV6** | **Boolean** | True if this is a IPv6 address. False if IPv4 | 
**isVpn** | **Boolean** | True if this IP ia a VPN | 
**providerDescription** | **String** | A description of the provider (usually extracted from the providers website) | 
**providerDomain** | **String** | The domain name of the provider | 
**providerType** | **String** | The detected provider type, possible values are: &lt;br&gt; &lt;ul&gt; &lt;li&gt;isp - IP belongs to an internet service provider. This includes both mobile, home and business internet providers&lt;/li&gt; &lt;li&gt;hosting - IP belongs to a hosting company. This includes website hosting, cloud computing platforms and colocation facilities&lt;/li&gt; &lt;li&gt;vpn - IP belongs to a VPN provider&lt;/li&gt; &lt;li&gt;proxy - IP belongs to a proxy service. This includes HTTP/SOCKS proxies and browser based proxies&lt;/li&gt; &lt;li&gt;university - IP belongs to a university/college/campus&lt;/li&gt; &lt;li&gt;government - IP belongs to a government department. This includes military facilities&lt;/li&gt; &lt;li&gt;commercial - IP belongs to a commercial entity such as a corporate headquarters or company office&lt;/li&gt; &lt;li&gt;unknown - could not identify the provider type&lt;/li&gt; &lt;/ul&gt; | 
**providerWebsite** | **String** | The website URL for the provider | 
**region** | **String** | Full region name (if detectable) | 
**regionCode** | **String** | ISO 3166-2 region code (if detectable) | 
**valid** | **Boolean** | True if this is a valid IPv4 or IPv6 address | 
**vpnDomain** | **String** | The domain of the VPN provider (may be empty if the VPN domain is not detectable) | 


