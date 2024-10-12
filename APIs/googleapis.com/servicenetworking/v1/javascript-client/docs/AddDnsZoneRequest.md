# ServiceNetworkingApi.AddDnsZoneRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerNetwork** | **String** | Required. The network that the consumer is using to connect with services. Must be in the form of projects/{project}/global/networks/{network} {project} is the project number, as in &#39;12345&#39; {network} is the network name. | [optional] 
**dnsSuffix** | **String** | Required. The DNS name suffix for the zones e.g. &#x60;example.com.&#x60;. Cloud DNS requires that a DNS suffix ends with a trailing dot. | [optional] 
**name** | **String** | Required. The name for both the private zone in the shared producer host project and the peering zone in the consumer project. Must be unique within both projects. The name must be 1-63 characters long, must begin with a letter, end with a letter or digit, and only contain lowercase letters, digits or dashes. | [optional] 


