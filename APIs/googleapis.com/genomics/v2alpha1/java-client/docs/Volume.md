

# Volume

Carries information about storage that can be attached to a VM. Specify either `Volume` or `Disk`, but not both.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**existingDisk** | [**ExistingDisk**](ExistingDisk.md) |  |  [optional] |
|**nfsMount** | [**NFSMount**](NFSMount.md) |  |  [optional] |
|**persistentDisk** | [**PersistentDisk**](PersistentDisk.md) |  |  [optional] |
|**volume** | **String** | A user-supplied name for the volume. Used when mounting the volume into &#x60;Actions&#x60;. The name must contain only upper and lowercase alphanumeric characters and hyphens and cannot start with a hyphen. |  [optional] |



