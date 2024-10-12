# LinodeApi.LKENodePool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscaler** | [**LKENodePoolAutoscaler**](LKENodePoolAutoscaler.md) |  | [optional] 
**count** | **Number** | The number of nodes in the Node Pool. | [optional] 
**disks** | [**[LKENodePoolDisksInner]**](LKENodePoolDisksInner.md) | This Node Pool&#39;s custom disk layout.  | [optional] 
**id** | **Number** | This Node Pool&#39;s unique ID.  | [optional] 
**nodes** | [**[LKENodeStatus]**](LKENodeStatus.md) | Status information for the Nodes which are members of this Node Pool. If a Linode has not been provisioned for a given Node slot, the instance_id will be returned as null.  | [optional] 
**tags** | **[String]** | An array of tags applied to this object. Tags are for organizational purposes only.  | [optional] 
**type** | **String** | The Linode Type for all of the nodes in the Node Pool. | [optional] 


