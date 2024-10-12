

# DomainLookupResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**age** | **Integer** | The number of days since the domain was registered. A domain age of under 90 days is generally considered to be potentially risky. A value of 0 indicates no registration date was found for this domain |  |
|**blocklists** | **List&lt;String&gt;** | An array of strings indicating which blocklist categories this domain is listed on. Current categories are: phishing, malware, spam, anonymizer, nefarious |  |
|**dnsProvider** | **String** | The primary domain of the DNS provider for this domain |  |
|**domain** | **String** | The primary domain name excluding any subdomains. This is also referred to as the second-level domain (SLD) |  |
|**fqdn** | **String** | The fully qualified domain name (FQDN) |  |
|**isAdult** | **Boolean** | This domain is hosting adult content such as porn, webcams, escorts, etc |  |
|**isGov** | **Boolean** | Is this domain under a government or military TLD |  |
|**isMalicious** | **Boolean** | Consider this domain malicious as it is currently listed on at least 1 blocklist |  |
|**isOpennic** | **Boolean** | Is this domain under an OpenNIC TLD |  |
|**isPending** | **Boolean** | True if this domain is unseen and is currently being processed in the background. This field only matters when the &#39;live&#39; lookup setting has been explicitly disabled and indicates that not all domain data my be present yet |  |
|**isSubdomain** | **Boolean** | Is the FQDN a subdomain of the primary domain |  |
|**mailProvider** | **String** | The primary domain of the email provider for this domain. An empty value indicates the domain has no valid MX records |  |
|**rank** | **Integer** | The domains estimated global traffic rank with the highest rank being 1. A value of 0 indicates the domain is currently ranked outside of the top 1M of domains |  |
|**registeredDate** | **String** | The ISO date this domain was registered or first seen on the internet. An empty value indicates we could not reliably determine the date |  |
|**registrarId** | **Integer** | The IANA registrar ID (0 if no registrar ID was found) |  |
|**registrarName** | **String** | The name of the domain registrar owning this domain |  |
|**sensors** | [**List&lt;BlocklistSensor&gt;**](BlocklistSensor.md) | An array of objects containing details on which specific blocklist sensors have detected this domain |  |
|**tld** | **String** | The top-level domain (TLD) |  |
|**tldCc** | **String** | For a country code top-level domain (ccTLD) this will contain the associated ISO 2-letter country code |  |
|**valid** | **Boolean** | True if a valid domain was found. For a domain to be considered valid it must be registered and have valid DNS NS records |  |



