# NetworkServicesApi.TlsRouteRouteMatch

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alpn** | **[String]** | Optional. ALPN (Application-Layer Protocol Negotiation) to match against. Examples: \&quot;http/1.1\&quot;, \&quot;h2\&quot;. At least one of sni_host and alpn is required. Up to 5 alpns across all matches can be set. | [optional] 
**sniHost** | **[String]** | Optional. SNI (server name indicator) to match against. SNI will be matched against all wildcard domains, i.e. &#x60;www.example.com&#x60; will be first matched against &#x60;www.example.com&#x60;, then &#x60;*.example.com&#x60;, then &#x60;*.com.&#x60; Partial wildcards are not supported, and values like *w.example.com are invalid. At least one of sni_host and alpn is required. Up to 5 sni hosts across all matches can be set. | [optional] 


