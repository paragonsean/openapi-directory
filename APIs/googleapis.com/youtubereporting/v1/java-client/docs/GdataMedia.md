

# GdataMedia

gdata

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | **String** | gdata |  [optional] |
|**bigstoreObjectRef** | **byte[]** | gdata |  [optional] |
|**blobRef** | **byte[]** | gdata |  [optional] |
|**blobstore2Info** | [**GdataBlobstore2Info**](GdataBlobstore2Info.md) |  |  [optional] |
|**compositeMedia** | [**List&lt;GdataCompositeMedia&gt;**](GdataCompositeMedia.md) | gdata |  [optional] |
|**contentType** | **String** | gdata |  [optional] |
|**contentTypeInfo** | [**GdataContentTypeInfo**](GdataContentTypeInfo.md) |  |  [optional] |
|**cosmoBinaryReference** | **byte[]** | gdata |  [optional] |
|**crc32cHash** | **Integer** | gdata |  [optional] |
|**diffChecksumsResponse** | [**GdataDiffChecksumsResponse**](GdataDiffChecksumsResponse.md) |  |  [optional] |
|**diffDownloadResponse** | [**GdataDiffDownloadResponse**](GdataDiffDownloadResponse.md) |  |  [optional] |
|**diffUploadRequest** | [**GdataDiffUploadRequest**](GdataDiffUploadRequest.md) |  |  [optional] |
|**diffUploadResponse** | [**GdataDiffUploadResponse**](GdataDiffUploadResponse.md) |  |  [optional] |
|**diffVersionResponse** | [**GdataDiffVersionResponse**](GdataDiffVersionResponse.md) |  |  [optional] |
|**downloadParameters** | [**GdataDownloadParameters**](GdataDownloadParameters.md) |  |  [optional] |
|**filename** | **String** | gdata |  [optional] |
|**hash** | **String** | gdata |  [optional] |
|**hashVerified** | **Boolean** | gdata |  [optional] |
|**inline** | **byte[]** | gdata |  [optional] |
|**isPotentialRetry** | **Boolean** | gdata |  [optional] |
|**length** | **String** | gdata |  [optional] |
|**md5Hash** | **byte[]** | gdata |  [optional] |
|**mediaId** | **byte[]** | gdata |  [optional] |
|**objectId** | [**GdataObjectId**](GdataObjectId.md) |  |  [optional] |
|**path** | **String** | gdata |  [optional] |
|**referenceType** | [**ReferenceTypeEnum**](#ReferenceTypeEnum) | gdata |  [optional] |
|**sha1Hash** | **byte[]** | gdata |  [optional] |
|**sha256Hash** | **byte[]** | gdata |  [optional] |
|**timestamp** | **String** | gdata |  [optional] |
|**token** | **String** | gdata |  [optional] |



## Enum: ReferenceTypeEnum

| Name | Value |
|---- | -----|
| PATH | &quot;PATH&quot; |
| BLOB_REF | &quot;BLOB_REF&quot; |
| INLINE | &quot;INLINE&quot; |
| GET_MEDIA | &quot;GET_MEDIA&quot; |
| COMPOSITE_MEDIA | &quot;COMPOSITE_MEDIA&quot; |
| BIGSTORE_REF | &quot;BIGSTORE_REF&quot; |
| DIFF_VERSION_RESPONSE | &quot;DIFF_VERSION_RESPONSE&quot; |
| DIFF_CHECKSUMS_RESPONSE | &quot;DIFF_CHECKSUMS_RESPONSE&quot; |
| DIFF_DOWNLOAD_RESPONSE | &quot;DIFF_DOWNLOAD_RESPONSE&quot; |
| DIFF_UPLOAD_REQUEST | &quot;DIFF_UPLOAD_REQUEST&quot; |
| DIFF_UPLOAD_RESPONSE | &quot;DIFF_UPLOAD_RESPONSE&quot; |
| COSMO_BINARY_REFERENCE | &quot;COSMO_BINARY_REFERENCE&quot; |
| ARBITRARY_BYTES | &quot;ARBITRARY_BYTES&quot; |



