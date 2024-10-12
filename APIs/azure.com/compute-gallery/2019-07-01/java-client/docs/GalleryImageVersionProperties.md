

# GalleryImageVersionProperties

Describes the properties of a gallery Image Version.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state, which only appears in the response. |  [optional] [readonly] |
|**publishingProfile** | [**GalleryImageVersionPublishingProfile**](GalleryImageVersionPublishingProfile.md) |  |  [optional] |
|**replicationStatus** | [**ReplicationStatus**](ReplicationStatus.md) |  |  [optional] |
|**storageProfile** | [**GalleryImageVersionStorageProfile**](GalleryImageVersionStorageProfile.md) |  |  |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| FAILED | &quot;Failed&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| DELETING | &quot;Deleting&quot; |
| MIGRATING | &quot;Migrating&quot; |



