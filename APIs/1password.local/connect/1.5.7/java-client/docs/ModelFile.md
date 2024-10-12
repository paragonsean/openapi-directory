

# ModelFile


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **byte[]** | Base64-encoded contents of the file. Only set if size &lt;&#x3D; OP_MAX_INLINE_FILE_SIZE_KB kb and &#x60;inline_files&#x60; is set to &#x60;true&#x60;. |  [optional] |
|**contentPath** | **String** | Path of the Connect API that can be used to download the contents of this file. |  [optional] [readonly] |
|**id** | **String** | ID of the file |  [optional] |
|**name** | **String** | Name of the file |  [optional] |
|**section** | [**FileSection**](FileSection.md) |  |  [optional] |
|**size** | **Integer** | Size in bytes of the file |  [optional] |



