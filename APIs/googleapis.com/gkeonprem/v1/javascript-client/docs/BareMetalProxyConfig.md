# AnthosOnPremApi.BareMetalProxyConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**noProxy** | **[String]** | A list of IPs, hostnames, and domains that should skip the proxy. Examples: [\&quot;127.0.0.1\&quot;, \&quot;example.com\&quot;, \&quot;.corp\&quot;, \&quot;localhost\&quot;]. | [optional] 
**uri** | **String** | Required. Specifies the address of your proxy server. Examples: &#x60;http://domain&#x60; Do not provide credentials in the format &#x60;http://(username:password@)domain&#x60; these will be rejected by the server. | [optional] 


