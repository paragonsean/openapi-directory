

# CompositeMedia

A sequence of media data references representing composite data. Introduced to support Bigstore composite objects. For details, visit http://go/bigstore-composites.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**blobRef** | **byte[]** | Blobstore v1 reference, set if reference_type is BLOBSTORE_REF This should be the byte representation of a blobstore.BlobRef. Since Blobstore is deprecating v1, use blobstore2_info instead. For now, any v2 blob will also be represented in this field as v1 BlobRef. |  [optional] |
|**blobstore2Info** | [**Blobstore2Info**](Blobstore2Info.md) |  |  [optional] |
|**cosmoBinaryReference** | **byte[]** | A binary data reference for a media download. Serves as a technology-agnostic binary reference in some Google infrastructure. This value is a serialized storage_cosmo.BinaryReference proto. Storing it as bytes is a hack to get around the fact that the cosmo proto (as well as others it includes) doesn&#39;t support JavaScript. This prevents us from including the actual type of this field. |  [optional] |
|**crc32cHash** | **Integer** | crc32.c hash for the payload. |  [optional] |
|**inline** | **byte[]** | Media data, set if reference_type is INLINE |  [optional] |
|**length** | **String** | Size of the data, in bytes |  [optional] |
|**md5Hash** | **byte[]** | MD5 hash for the payload. |  [optional] |
|**objectId** | [**ObjectId**](ObjectId.md) |  |  [optional] |
|**path** | **String** | Path to the data, set if reference_type is PATH |  [optional] |
|**referenceType** | [**ReferenceTypeEnum**](#ReferenceTypeEnum) | Describes what the field reference contains. |  [optional] |
|**sha1Hash** | **byte[]** | SHA-1 hash for the payload. |  [optional] |



## Enum: ReferenceTypeEnum

| Name | Value |
|---- | -----|
| PATH | &quot;PATH&quot; |
| BLOB_REF | &quot;BLOB_REF&quot; |
| INLINE | &quot;INLINE&quot; |
| BIGSTORE_REF | &quot;BIGSTORE_REF&quot; |
| COSMO_BINARY_REFERENCE | &quot;COSMO_BINARY_REFERENCE&quot; |



