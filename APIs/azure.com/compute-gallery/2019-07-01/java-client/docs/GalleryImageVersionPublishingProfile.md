

# GalleryImageVersionPublishingProfile

The publishing profile of a gallery Image Version.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endOfLifeDate** | **OffsetDateTime** | The end of life date of the gallery Image Version. This property can be used for decommissioning purposes. This property is updatable. |  [optional] |
|**excludeFromLatest** | **Boolean** | If set to true, Virtual Machines deployed from the latest version of the Image Definition won&#39;t use this Image Version. |  [optional] |
|**publishedDate** | **OffsetDateTime** | The timestamp for when the gallery Image Version is published. |  [optional] [readonly] |
|**replicaCount** | **Integer** | The number of replicas of the Image Version to be created per region. This property would take effect for a region when regionalReplicaCount is not specified. This property is updatable. |  [optional] |
|**storageAccountType** | [**StorageAccountTypeEnum**](#StorageAccountTypeEnum) | Specifies the storage account type to be used to store the image. This property is not updatable. |  [optional] |
|**targetRegions** | [**List&lt;TargetRegion&gt;**](TargetRegion.md) | The target regions where the Image Version is going to be replicated to. This property is updatable. |  [optional] |



## Enum: StorageAccountTypeEnum

| Name | Value |
|---- | -----|
| LRS | &quot;Standard_LRS&quot; |
| ZRS | &quot;Standard_ZRS&quot; |



