

# TaskContainerSettings


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerRunOptions** | **String** | These additional options are supplied as arguments to the \&quot;docker create\&quot; command, in addition to those controlled by the Batch Service. |  [optional] |
|**imageName** | **String** | This is the full image reference, as would be specified to \&quot;docker pull\&quot;. If no tag is provided as part of the image name, the tag \&quot;:latest\&quot; is used as a default. |  |
|**registry** | [**ContainerRegistry**](ContainerRegistry.md) |  |  [optional] |



