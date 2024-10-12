

# PscConnection

Details of consumer resources in a PSC connection.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**address** | **String** | Output only. The IP allocated on the consumer network for the PSC forwarding rule. |  [optional] [readonly] |
|**forwardingRule** | **String** | Output only. The URI of the consumer side forwarding rule. Example: projects/{projectNumOrId}/regions/us-east1/forwardingRules/{resourceId}. |  [optional] [readonly] |
|**network** | **String** | The consumer network where the IP address resides, in the form of projects/{project_id}/global/networks/{network_id}. |  [optional] |
|**projectId** | **String** | Output only. The consumer project_id where the forwarding rule is created from. |  [optional] [readonly] |
|**pscConnectionId** | **String** | Output only. The PSC connection id of the forwarding rule connected to the service attachment. |  [optional] [readonly] |



