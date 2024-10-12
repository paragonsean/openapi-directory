

# LKENodePool

The set of Node Pools which are members of the Kubernetes cluster. Node Pools consist of a Linode type, the number of Linodes to deploy of that type, and additional status information. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoscaler** | [**LKENodePoolAutoscaler**](LKENodePoolAutoscaler.md) |  |  [optional] |
|**count** | **Integer** | The number of nodes in the Node Pool. |  [optional] |
|**disks** | [**List&lt;LKENodePoolDisksInner&gt;**](LKENodePoolDisksInner.md) | This Node Pool&#39;s custom disk layout.  |  [optional] |
|**id** | **Integer** | This Node Pool&#39;s unique ID.  |  [optional] |
|**nodes** | [**List&lt;LKENodeStatus&gt;**](LKENodeStatus.md) | Status information for the Nodes which are members of this Node Pool. If a Linode has not been provisioned for a given Node slot, the instance_id will be returned as null.  |  [optional] |
|**tags** | **List&lt;String&gt;** | An array of tags applied to this object. Tags are for organizational purposes only.  |  [optional] |
|**type** | **String** | The Linode Type for all of the nodes in the Node Pool. |  [optional] |



