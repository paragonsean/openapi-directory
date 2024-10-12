

# GalleryProperties

Describes the properties of a Shared Image Gallery.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of this Shared Image Gallery resource. This property is updatable. |  [optional] |
|**identifier** | [**GalleryIdentifier**](GalleryIdentifier.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state, which only appears in the response. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| UPDATING | &quot;Updating&quot; |
| FAILED | &quot;Failed&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| DELETING | &quot;Deleting&quot; |
| MIGRATING | &quot;Migrating&quot; |



