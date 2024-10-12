

# VolumeContainerFailoverMetadata

The metadata of the volume container, that is being considered as part of a failover set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**volumeContainerId** | **String** | The path ID of the volume container. |  [optional] |
|**volumes** | [**List&lt;VolumeFailoverMetadata&gt;**](VolumeFailoverMetadata.md) | The list of metadata of volumes inside the volume container, which contains valid cloud snapshots. |  [optional] |



