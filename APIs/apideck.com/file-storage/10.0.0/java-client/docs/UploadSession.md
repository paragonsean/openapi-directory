

# UploadSession


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expiresAt** | **OffsetDateTime** |  |  [optional] [readonly] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**parallelUploadSupported** | **Boolean** | Indicates if parts of the file can uploaded in parallel. |  [optional] [readonly] |
|**partSize** | **BigDecimal** | Size in bytes of each part of the file that you will upload. Uploaded parts need to be this size for the upload to be successful. |  [optional] [readonly] |
|**success** | **Boolean** | Indicates if the upload session was completed successfully. |  [optional] [readonly] |
|**uploadedByteRange** | **String** | The range of bytes that was successfully uploaded. |  [optional] [readonly] |



