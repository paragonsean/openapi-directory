# CloudDnsApi.PolicyAlternativeNameServerConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **String** |  | [optional] [default to &#39;dns#policyAlternativeNameServerConfig&#39;]
**targetNameServers** | [**[PolicyAlternativeNameServerConfigTargetNameServer]**](PolicyAlternativeNameServerConfigTargetNameServer.md) | Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name server that you choose. Names such as .internal are not available when an alternative name server is specified. | [optional] 


