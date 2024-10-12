

# Media

A reference to data stored on the filesystem, on GFS or in blobstore.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | **String** | Deprecated, use one of explicit hash type fields instead. Algorithm used for calculating the hash. As of 2011/01/21, \&quot;MD5\&quot; is the only possible value for this field. New values may be added at any time. |  [optional] |
|**bigstoreObjectRef** | **byte[]** | Use object_id instead. |  [optional] |
|**blobRef** | **byte[]** | Blobstore v1 reference, set if reference_type is BLOBSTORE_REF This should be the byte representation of a blobstore.BlobRef. Since Blobstore is deprecating v1, use blobstore2_info instead. For now, any v2 blob will also be represented in this field as v1 BlobRef. |  [optional] |
|**blobstore2Info** | [**Blobstore2Info**](Blobstore2Info.md) |  |  [optional] |
|**compositeMedia** | [**List&lt;CompositeMedia&gt;**](CompositeMedia.md) | A composite media composed of one or more media objects, set if reference_type is COMPOSITE_MEDIA. The media length field must be set to the sum of the lengths of all composite media objects. Note: All composite media must have length specified. |  [optional] |
|**contentType** | **String** | MIME type of the data |  [optional] |
|**contentTypeInfo** | [**ContentTypeInfo**](ContentTypeInfo.md) |  |  [optional] |
|**cosmoBinaryReference** | **byte[]** | A binary data reference for a media download. Serves as a technology-agnostic binary reference in some Google infrastructure. This value is a serialized storage_cosmo.BinaryReference proto. Storing it as bytes is a hack to get around the fact that the cosmo proto (as well as others it includes) doesn&#39;t support JavaScript. This prevents us from including the actual type of this field. |  [optional] |
|**crc32cHash** | **Integer** | For Scotty Uploads: Scotty-provided hashes for uploads For Scotty Downloads: (WARNING: DO NOT USE WITHOUT PERMISSION FROM THE SCOTTY TEAM.) A Hash provided by the agent to be used to verify the data being downloaded. Currently only supported for inline payloads. Further, only crc32c_hash is currently supported. |  [optional] |
|**diffChecksumsResponse** | [**DiffChecksumsResponse**](DiffChecksumsResponse.md) |  |  [optional] |
|**diffDownloadResponse** | [**DiffDownloadResponse**](DiffDownloadResponse.md) |  |  [optional] |
|**diffUploadRequest** | [**DiffUploadRequest**](DiffUploadRequest.md) |  |  [optional] |
|**diffUploadResponse** | [**DiffUploadResponse**](DiffUploadResponse.md) |  |  [optional] |
|**diffVersionResponse** | [**DiffVersionResponse**](DiffVersionResponse.md) |  |  [optional] |
|**downloadParameters** | [**DownloadParameters**](DownloadParameters.md) |  |  [optional] |
|**filename** | **String** | Original file name |  [optional] |
|**hash** | **String** | Deprecated, use one of explicit hash type fields instead. These two hash related fields will only be populated on Scotty based media uploads and will contain the content of the hash group in the NotificationRequest: http://cs/#google3/uploader/service/proto/upload_listener.proto&amp;q&#x3D;class:Hash Hex encoded hash value of the uploaded media. |  [optional] |
|**hashVerified** | **Boolean** | For Scotty uploads only. If a user sends a hash code and the backend has requested that Scotty verify the upload against the client hash, Scotty will perform the check on behalf of the backend and will reject it if the hashes don&#39;t match. This is set to true if Scotty performed this verification. |  [optional] |
|**inline** | **byte[]** | Media data, set if reference_type is INLINE |  [optional] |
|**isPotentialRetry** | **Boolean** | |is_potential_retry| is set false only when Scotty is certain that it has not sent the request before. When a client resumes an upload, this field must be set true in agent calls, because Scotty cannot be certain that it has never sent the request before due to potential failure in the session state persistence. |  [optional] |
|**length** | **String** | Size of the data, in bytes |  [optional] |
|**md5Hash** | **byte[]** | Scotty-provided MD5 hash for an upload. |  [optional] |
|**mediaId** | **byte[]** | Media id to forward to the operation GetMedia. Can be set if reference_type is GET_MEDIA. |  [optional] |
|**objectId** | [**ObjectId**](ObjectId.md) |  |  [optional] |
|**path** | **String** | Path to the data, set if reference_type is PATH |  [optional] |
|**referenceType** | [**ReferenceTypeEnum**](#ReferenceTypeEnum) | Describes what the field reference contains. |  [optional] |
|**sha1Hash** | **byte[]** | Scotty-provided SHA1 hash for an upload. |  [optional] |
|**sha256Hash** | **byte[]** | Scotty-provided SHA256 hash for an upload. |  [optional] |
|**timestamp** | **String** | Time at which the media data was last updated, in milliseconds since UNIX epoch |  [optional] |
|**token** | **String** | A unique fingerprint/version id for the media data |  [optional] |



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



