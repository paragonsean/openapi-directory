# CloudWorkstationsApi.GceRegionalPersistentDisk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diskType** | **String** | Optional. The [type of the persistent disk](https://cloud.google.com/compute/docs/disks#disk-types) for the home directory. Defaults to &#x60;\&quot;pd-standard\&quot;&#x60;. | [optional] 
**fsType** | **String** | Optional. Type of file system that the disk should be formatted with. The workstation image must support this file system type. Must be empty if source_snapshot is set. Defaults to &#x60;\&quot;ext4\&quot;&#x60;. | [optional] 
**reclaimPolicy** | **String** | Optional. Whether the persistent disk should be deleted when the workstation is deleted. Valid values are &#x60;DELETE&#x60; and &#x60;RETAIN&#x60;. Defaults to &#x60;DELETE&#x60;. | [optional] 
**sizeGb** | **Number** | Optional. The GB capacity of a persistent home directory for each workstation created with this configuration. Must be empty if source_snapshot is set. Valid values are &#x60;10&#x60;, &#x60;50&#x60;, &#x60;100&#x60;, &#x60;200&#x60;, &#x60;500&#x60;, or &#x60;1000&#x60;. Defaults to &#x60;200&#x60;. If less than &#x60;200&#x60; GB, the disk_type must be &#x60;\&quot;pd-balanced\&quot;&#x60; or &#x60;\&quot;pd-ssd\&quot;&#x60;. | [optional] 
**sourceSnapshot** | **String** | Optional. Name of the snapshot to use as the source for the disk. If set, size_gb and fs_type must be empty. | [optional] 



## Enum: ReclaimPolicyEnum


* `RECLAIM_POLICY_UNSPECIFIED` (value: `"RECLAIM_POLICY_UNSPECIFIED"`)

* `DELETE` (value: `"DELETE"`)

* `RETAIN` (value: `"RETAIN"`)




