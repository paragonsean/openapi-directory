# GoogleWalletApi.Media

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **String** | Deprecated, use one of explicit hash type fields instead. Algorithm used for calculating the hash. As of 2011/01/21, \&quot;MD5\&quot; is the only possible value for this field. New values may be added at any time. | [optional] 
**bigstoreObjectRef** | **Blob** | Use object_id instead. | [optional] 
**blobRef** | **Blob** | Blobstore v1 reference, set if reference_type is BLOBSTORE_REF This should be the byte representation of a blobstore.BlobRef. Since Blobstore is deprecating v1, use blobstore2_info instead. For now, any v2 blob will also be represented in this field as v1 BlobRef. | [optional] 
**blobstore2Info** | [**Blobstore2Info**](Blobstore2Info.md) |  | [optional] 
**compositeMedia** | [**[CompositeMedia]**](CompositeMedia.md) | A composite media composed of one or more media objects, set if reference_type is COMPOSITE_MEDIA. The media length field must be set to the sum of the lengths of all composite media objects. Note: All composite media must have length specified. | [optional] 
**contentType** | **String** | MIME type of the data | [optional] 
**contentTypeInfo** | [**ContentTypeInfo**](ContentTypeInfo.md) |  | [optional] 
**cosmoBinaryReference** | **Blob** | A binary data reference for a media download. Serves as a technology-agnostic binary reference in some Google infrastructure. This value is a serialized storage_cosmo.BinaryReference proto. Storing it as bytes is a hack to get around the fact that the cosmo proto (as well as others it includes) doesn&#39;t support JavaScript. This prevents us from including the actual type of this field. | [optional] 
**crc32cHash** | **Number** | For Scotty Uploads: Scotty-provided hashes for uploads For Scotty Downloads: (WARNING: DO NOT USE WITHOUT PERMISSION FROM THE SCOTTY TEAM.) A Hash provided by the agent to be used to verify the data being downloaded. Currently only supported for inline payloads. Further, only crc32c_hash is currently supported. | [optional] 
**diffChecksumsResponse** | [**DiffChecksumsResponse**](DiffChecksumsResponse.md) |  | [optional] 
**diffDownloadResponse** | [**DiffDownloadResponse**](DiffDownloadResponse.md) |  | [optional] 
**diffUploadRequest** | [**DiffUploadRequest**](DiffUploadRequest.md) |  | [optional] 
**diffUploadResponse** | [**DiffUploadResponse**](DiffUploadResponse.md) |  | [optional] 
**diffVersionResponse** | [**DiffVersionResponse**](DiffVersionResponse.md) |  | [optional] 
**downloadParameters** | [**DownloadParameters**](DownloadParameters.md) |  | [optional] 
**filename** | **String** | Original file name | [optional] 
**hash** | **String** | Deprecated, use one of explicit hash type fields instead. These two hash related fields will only be populated on Scotty based media uploads and will contain the content of the hash group in the NotificationRequest: http://cs/#google3/uploader/service/proto/upload_listener.proto&amp;q&#x3D;class:Hash Hex encoded hash value of the uploaded media. | [optional] 
**hashVerified** | **Boolean** | For Scotty uploads only. If a user sends a hash code and the backend has requested that Scotty verify the upload against the client hash, Scotty will perform the check on behalf of the backend and will reject it if the hashes don&#39;t match. This is set to true if Scotty performed this verification. | [optional] 
**inline** | **Blob** | Media data, set if reference_type is INLINE | [optional] 
**isPotentialRetry** | **Boolean** | |is_potential_retry| is set false only when Scotty is certain that it has not sent the request before. When a client resumes an upload, this field must be set true in agent calls, because Scotty cannot be certain that it has never sent the request before due to potential failure in the session state persistence. | [optional] 
**length** | **String** | Size of the data, in bytes | [optional] 
**md5Hash** | **Blob** | Scotty-provided MD5 hash for an upload. | [optional] 
**mediaId** | **Blob** | Media id to forward to the operation GetMedia. Can be set if reference_type is GET_MEDIA. | [optional] 
**objectId** | [**ObjectId**](ObjectId.md) |  | [optional] 
**path** | **String** | Path to the data, set if reference_type is PATH | [optional] 
**referenceType** | **String** | Describes what the field reference contains. | [optional] 
**sha1Hash** | **Blob** | Scotty-provided SHA1 hash for an upload. | [optional] 
**sha256Hash** | **Blob** | Scotty-provided SHA256 hash for an upload. | [optional] 
**timestamp** | **String** | Time at which the media data was last updated, in milliseconds since UNIX epoch | [optional] 
**token** | **String** | A unique fingerprint/version id for the media data | [optional] 



## Enum: ReferenceTypeEnum


* `PATH` (value: `"PATH"`)

* `BLOB_REF` (value: `"BLOB_REF"`)

* `INLINE` (value: `"INLINE"`)

* `GET_MEDIA` (value: `"GET_MEDIA"`)

* `COMPOSITE_MEDIA` (value: `"COMPOSITE_MEDIA"`)

* `BIGSTORE_REF` (value: `"BIGSTORE_REF"`)

* `DIFF_VERSION_RESPONSE` (value: `"DIFF_VERSION_RESPONSE"`)

* `DIFF_CHECKSUMS_RESPONSE` (value: `"DIFF_CHECKSUMS_RESPONSE"`)

* `DIFF_DOWNLOAD_RESPONSE` (value: `"DIFF_DOWNLOAD_RESPONSE"`)

* `DIFF_UPLOAD_REQUEST` (value: `"DIFF_UPLOAD_REQUEST"`)

* `DIFF_UPLOAD_RESPONSE` (value: `"DIFF_UPLOAD_RESPONSE"`)

* `COSMO_BINARY_REFERENCE` (value: `"COSMO_BINARY_REFERENCE"`)

* `ARBITRARY_BYTES` (value: `"ARBITRARY_BYTES"`)




