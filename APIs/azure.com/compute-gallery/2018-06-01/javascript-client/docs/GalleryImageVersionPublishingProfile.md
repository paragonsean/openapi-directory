# SharedImageGalleryServiceClient.GalleryImageVersionPublishingProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endOfLifeDate** | **Date** | The end of life date of the gallery Image Version. This property can be used for decommissioning purposes. This property is updatable. | [optional] 
**excludeFromLatest** | **Boolean** | If set to true, Virtual Machines deployed from the latest version of the Image Definition won&#39;t use this Image Version. | [optional] 
**publishedDate** | **Date** | The timestamp for when the gallery Image Version is published. | [optional] [readonly] 
**replicaCount** | **Number** | The number of replicas of the Image Version to be created per region. This property would take effect for a region when regionalReplicaCount is not specified. This property is updatable. | [optional] 
**source** | [**GalleryArtifactSource**](GalleryArtifactSource.md) |  | 
**targetRegions** | [**[TargetRegion]**](TargetRegion.md) | The target regions where the Image Version is going to be replicated to. This property is updatable. | [optional] 


