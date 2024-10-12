

# SignedUrl

Signed Url object with optional ancillary metadata of requested file

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiresAt** | **OffsetDateTime** | Timestamp of when the URL will no longer grant access to the file. |  |
|**extension** | **String** | Extension of the requested file. |  |
|**height** | **Integer** | For image and video files. The height of the file. |  [optional] |
|**name** | **String** | Name of the requested file. |  |
|**size** | **Integer** | Size in bytes of the requested file. |  |
|**type** | **String** | Type of the file. Can be IMG, DOCUMENT, AUDIO, MOVIE, or OTHER. |  |
|**url** | **String** | Signed URL with access to the specified file. Anyone with this URL will be able to access the file until it expires. |  |
|**width** | **Integer** | For image and video files. The width of the file. |  [optional] |



