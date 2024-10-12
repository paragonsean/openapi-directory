

# ResponsePolicy

A Response Policy is a collection of selectors that apply to queries made against one or more Virtual Private Cloud networks.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | User-provided description for this Response Policy. |  [optional] |
|**gkeClusters** | [**List&lt;ResponsePolicyGKECluster&gt;**](ResponsePolicyGKECluster.md) | The list of Google Kubernetes Engine clusters to which this response policy is applied. |  [optional] |
|**id** | **String** | Unique identifier for the resource; defined by the server (output only). |  [optional] |
|**kind** | **String** |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | User labels. |  [optional] |
|**networks** | [**List&lt;ResponsePolicyNetwork&gt;**](ResponsePolicyNetwork.md) | List of network names specifying networks to which this policy is applied. |  [optional] |
|**responsePolicyName** | **String** | User assigned name for this Response Policy. |  [optional] |



