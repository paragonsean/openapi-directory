# LinodeApi.LKENodePoolRequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscaler** | [**LKENodePoolRequestBodyAutoscaler**](LKENodePoolRequestBodyAutoscaler.md) |  | [optional] 
**count** | **Number** | The number of nodes in the Node Pool. | [optional] 
**disks** | [**[Items]**](Items.md) | **Note**: This field should be omitted except for special use cases. The disks specified here are partitions in *addition* to the primary partition and reduce the size of the primary partition, which can lead to stability problems for the Node.  This Node Pool&#39;s custom disk layout. Each item in this array will create a new disk partition for each node in this Node Pool.    * The custom disk layout is applied to each node in this Node Pool.   * The maximum number of custom disk partitions that can be configured is 7.   * Once the requested disk paritions are allocated, the remaining disk space is allocated to the node&#39;s boot disk.   * A Node Pool&#39;s custom disk layout is immutable over the lifetime of the Node Pool.  | [optional] 
**tags** | **[String]** | An array of tags applied to this object. Tags are for organizational purposes only.  | [optional] 
**type** | **String** | The Linode Type for all of the nodes in the Node Pool. | [optional] 


