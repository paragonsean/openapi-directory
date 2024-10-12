# CloudDnsApi.ResponsePolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | User-provided description for this Response Policy. | [optional] 
**gkeClusters** | [**[ResponsePolicyGKECluster]**](ResponsePolicyGKECluster.md) | The list of Google Kubernetes Engine clusters to which this response policy is applied. | [optional] 
**id** | **String** | Unique identifier for the resource; defined by the server (output only). | [optional] 
**kind** | **String** |  | [optional] [default to &#39;dns#responsePolicy&#39;]
**labels** | **{String: String}** | User labels. | [optional] 
**networks** | [**[ResponsePolicyNetwork]**](ResponsePolicyNetwork.md) | List of network names specifying networks to which this policy is applied. | [optional] 
**responsePolicyName** | **String** | User assigned name for this Response Policy. | [optional] 


