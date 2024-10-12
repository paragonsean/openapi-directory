# CloudStorageJsonApi.ModelObject

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | [**[ObjectAccessControl]**](ObjectAccessControl.md) | Access controls on the object. | [optional] 
**bucket** | **String** | The bucket containing this object. | [optional] 
**cacheControl** | **String** | Cache-Control directive for the object data. | [optional] 
**componentCount** | **Number** | Number of underlying components that make up this object. Components are accumulated by compose operations and are limited to a count of 32. | [optional] 
**contentDisposition** | **String** | Content-Disposition of the object data. | [optional] 
**contentEncoding** | **String** | Content-Encoding of the object data. | [optional] 
**contentLanguage** | **String** | Content-Language of the object data. | [optional] 
**contentType** | **String** | Content-Type of the object data. | [optional] 
**crc32c** | **String** | CRC32c checksum, as described in RFC 4960, Appendix B; encoded using base64. | [optional] 
**etag** | **String** | HTTP 1.1 Entity tag for the object. | [optional] 
**generation** | **String** | The content generation of this object. Used for object versioning. | [optional] 
**id** | **String** | The ID of the object. | [optional] 
**kind** | **String** | The kind of item this is. For objects, this is always storage#object. | [optional] [default to &#39;storage#object&#39;]
**md5Hash** | **String** | MD5 hash of the data; encoded using base64. | [optional] 
**mediaLink** | **String** | Media download link. | [optional] 
**metadata** | **{String: String}** | User-provided metadata, in key/value pairs. | [optional] 
**metageneration** | **String** | The generation of the metadata for this object at this generation. Used for metadata versioning. Has no meaning outside of the context of this generation. | [optional] 
**name** | **String** | The name of this object. Required if not specified by URL parameter. | [optional] 
**owner** | [**ObjectOwner**](ObjectOwner.md) |  | [optional] 
**selfLink** | **String** | The link to this object. | [optional] 
**size** | **String** | Content-Length of the data in bytes. | [optional] 
**storageClass** | **String** | Storage class of the object. | [optional] 
**timeDeleted** | **Date** | Deletion time of the object in RFC 3339 format. Will be returned if and only if this version of the object has been deleted. | [optional] 
**updated** | **Date** | Modification time of the object metadata in RFC 3339 format. | [optional] 


