

# ImageDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**architecture** | **String** | The hardware architecture for which the image was built for. The architecture can either be Intel (amd64) or Power (ppc64le).  |  [optional] |
|**config** | [**ImageDetailConfig**](ImageDetailConfig.md) |  |  [optional] |
|**container** | **String** | ??? |  [optional] |
|**containerConfig** | [**ContainerConfig**](ContainerConfig.md) |  |  [optional] |
|**created** | **String** | The time when the image was created. |  [optional] |
|**dockerVersion** | **String** | ??? |  [optional] |
|**id** | **String** | Unique ID of the image that you inspected.  |  [optional] |
|**os** | **String** | ??? |  [optional] |
|**parent** | **String** | The ID of the parent image that was used to build this image. |  [optional] |
|**size** | **Integer** | The real size of the image.  |  [optional] |
|**tag** | **String** | The version of the image  |  [optional] |
|**throwaway** | **String** | ??? |  [optional] |
|**virtualSize** | **Integer** | The virtual size of the image. |  [optional] |



