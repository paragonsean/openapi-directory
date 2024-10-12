# GooglePayPassesApi.CompositeMedia

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blobRef** | **Blob** | Blobstore v1 reference, set if reference_type is BLOBSTORE_REF This should be the byte representation of a blobstore.BlobRef. Since Blobstore is deprecating v1, use blobstore2_info instead. For now, any v2 blob will also be represented in this field as v1 BlobRef. | [optional] 
**blobstore2Info** | [**Blobstore2Info**](Blobstore2Info.md) |  | [optional] 
**cosmoBinaryReference** | **Blob** | A binary data reference for a media download. Serves as a technology-agnostic binary reference in some Google infrastructure. This value is a serialized storage_cosmo.BinaryReference proto. Storing it as bytes is a hack to get around the fact that the cosmo proto (as well as others it includes) doesn&#39;t support JavaScript. This prevents us from including the actual type of this field. | [optional] 
**crc32cHash** | **Number** | crc32.c hash for the payload. | [optional] 
**inline** | **Blob** | Media data, set if reference_type is INLINE | [optional] 
**length** | **String** | Size of the data, in bytes | [optional] 
**md5Hash** | **Blob** | MD5 hash for the payload. | [optional] 
**objectId** | [**ObjectId**](ObjectId.md) |  | [optional] 
**path** | **String** | Path to the data, set if reference_type is PATH | [optional] 
**referenceType** | **String** | Describes what the field reference contains. | [optional] 
**sha1Hash** | **Blob** | SHA-1 hash for the payload. | [optional] 



## Enum: ReferenceTypeEnum


* `PATH` (value: `"PATH"`)

* `BLOB_REF` (value: `"BLOB_REF"`)

* `INLINE` (value: `"INLINE"`)

* `BIGSTORE_REF` (value: `"BIGSTORE_REF"`)

* `COSMO_BINARY_REFERENCE` (value: `"COSMO_BINARY_REFERENCE"`)




