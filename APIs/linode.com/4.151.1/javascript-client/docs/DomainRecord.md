# LinodeApi.DomainRecord

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | When this Domain Record was created. | [optional] [readonly] 
**id** | **Number** | This Record&#39;s unique ID. | [optional] [readonly] 
**name** | **String** | The name of this Record. For requests, this property&#39;s actual usage and whether it is required depends on the type of record this represents:  &#x60;A&#x60; and &#x60;AAAA&#x60;: The hostname or FQDN of the Record.  &#x60;NS&#x60;: The subdomain, if any, to use with the Domain of the Record. Wildcard NS records (&#x60;*&#x60;) are not supported.  &#x60;MX&#x60;: The mail subdomain. For example, &#x60;sub&#x60; for the address &#x60;user@sub.example.com&#x60; under the &#x60;example.com&#x60; Domain. Must be an empty string (&#x60;\&quot;\&quot;&#x60;) for a Null MX Record.  &#x60;CNAME&#x60;: The hostname. Must be unique. Required.  &#x60;TXT&#x60;: The hostname.  &#x60;SRV&#x60;: Unused. Use the &#x60;service&#x60; property to set the service name for this record.  &#x60;CAA&#x60;: The subdomain. Omit or enter an empty string (&#x60;\&quot;\&quot;&#x60;) to apply to the entire Domain.  &#x60;PTR&#x60;: See our guide on how to [Configure Your Linode for Reverse DNS (rDNS)](/docs/guides/configure-rdns/).  | [optional] 
**port** | **Number** | The port this Record points to. Only valid and required for SRV record requests.  | [optional] 
**priority** | **Number** | The priority of the target host for this Record. Lower values are preferred. Only valid for MX and SRV record requests. Required for SRV record requests.  Defaults to &#x60;0&#x60; for MX record requests. Must be &#x60;0&#x60; for Null MX records.  | [optional] 
**protocol** | **String** | The protocol this Record&#39;s service communicates with. An underscore (&#x60;_&#x60;) is prepended automatically to the submitted value for this property. Only valid for SRV record requests.  | [optional] 
**service** | **String** | The name of the service. An underscore (&#x60;_&#x60;) is prepended and a period (&#x60;.&#x60;) is appended automatically to the submitted value for this property. Only valid and required for SRV record requests.  | [optional] 
**tag** | **String** | The tag portion of a CAA record. Only valid and required for CAA record requests.  | [optional] 
**target** | **String** | The target for this Record. For requests, this property&#39;s actual usage and whether it is required depends on the type of record this represents:  &#x60;A&#x60; and &#x60;AAAA&#x60;: The IP address. Use &#x60;[remote_addr]&#x60; to submit the IPv4 address of the request. Required.  &#x60;NS&#x60;: The name server. Must be a valid domain. Required.  &#x60;MX&#x60;: The mail server. Must be a valid domain unless creating a Null MX Record. To create a [Null MX Record](https://datatracker.ietf.org/doc/html/rfc7505), first [remove](/docs/api/domains/#domain-record-delete) any additional MX records, create an MX record with empty strings (&#x60;\&quot;\&quot;&#x60;) for the &#x60;target&#x60; and &#x60;name&#x60;. If a Domain has a Null MX record, new MX records cannot be created. Required.  &#x60;CNAME&#x60;: The alias. Must be a valid domain. Required.  &#x60;TXT&#x60;: The value. Required.  &#x60;SRV&#x60;: The target domain or subdomain. If a subdomain is entered, it is automatically used with the Domain. To configure for a different domain, enter a valid FQDN. For example, the value &#x60;www&#x60; with a Domain for &#x60;example.com&#x60; results in a target set to &#x60;www.example.com&#x60;, whereas the value &#x60;sample.com&#x60; results in a target set to &#x60;sample.com&#x60;. Required.  &#x60;CAA&#x60;: The value. For &#x60;issue&#x60; or &#x60;issuewild&#x60; tags, the domain of your certificate issuer. For the &#x60;iodef&#x60; tag, a contact or submission URL (domain, http, https, or mailto). Requirements depend on the tag for this record:   * &#x60;issue&#x60;: The domain of your certificate issuer. Must be a valid domain.   * &#x60;issuewild&#x60;: The domain of your wildcard certificate issuer. Must be a valid domain and must not start with an asterisk (&#x60;*&#x60;).   * &#x60;iodef&#x60;: Must be either (1) a valid domain, (2) a valid domain prepended with &#x60;http://&#x60; or &#x60;https://&#x60;, or (3) a valid email address prepended with &#x60;mailto:&#x60;.  &#x60;PTR&#x60;: Required. See our guide on how to [Configure Your Linode for Reverse DNS (rDNS)](/docs/guides/configure-rdns/).  With the exception of A, AAAA, and CAA records, this field accepts a trailing period.  | [optional] 
**ttlSec** | **Number** | \&quot;Time to Live\&quot; - the amount of time in seconds that this Domain&#39;s records may be cached by resolvers or other domain servers. Valid values are 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200 - any other value will be rounded to the nearest valid value.  | [optional] 
**type** | **String** | The type of Record this is in the DNS system. For example, A records associate a domain name with an IPv4 address, and AAAA records associate a domain name with an IPv6 address. For more information, see the guides on [DNS Record Types](/docs/products/networking/dns-manager/guides/#dns-record-types).  | [optional] 
**updated** | **Date** | When this Domain Record was last updated. | [optional] [readonly] 
**weight** | **Number** | The relative weight of this Record used in the case of identical priority. Higher values are preferred. Only valid and required for SRV record requests.  | [optional] 



## Enum: TagEnum


* `issue` (value: `"issue"`)

* `issuewild` (value: `"issuewild"`)

* `iodef` (value: `"iodef"`)





## Enum: TypeEnum


* `A` (value: `"A"`)

* `AAAA` (value: `"AAAA"`)

* `NS` (value: `"NS"`)

* `MX` (value: `"MX"`)

* `CNAME` (value: `"CNAME"`)

* `TXT` (value: `"TXT"`)

* `SRV` (value: `"SRV"`)

* `PTR` (value: `"PTR"`)

* `CAA` (value: `"CAA"`)




