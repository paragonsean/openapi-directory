

# GcePersistentDisk

An EphemeralDirectory is backed by a Compute Engine persistent disk.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**diskType** | **String** | Optional. Type of the disk to use. Defaults to &#x60;\&quot;pd-standard\&quot;&#x60;. |  [optional] |
|**readOnly** | **Boolean** | Optional. Whether the disk is read only. If true, the disk may be shared by multiple VMs and source_snapshot must be set. |  [optional] |
|**sourceImage** | **String** | Optional. Name of the disk image to use as the source for the disk. Must be empty if source_snapshot is set. Updating source_image will update content in the ephemeral directory after the workstation is restarted. This field is mutable. |  [optional] |
|**sourceSnapshot** | **String** | Optional. Name of the snapshot to use as the source for the disk. Must be empty if source_image is set. Must be empty if read_only is false. Updating source_snapshot will update content in the ephemeral directory after the workstation is restarted. This field is mutable. |  [optional] |



