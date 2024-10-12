

# ModelObject

An object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acl** | [**List&lt;ObjectAccessControl&gt;**](ObjectAccessControl.md) | Access controls on the object. |  [optional] |
|**bucket** | **String** | The name of the bucket containing this object. |  [optional] |
|**cacheControl** | **String** | Cache-Control directive for the object data. If omitted, and the object is accessible to all anonymous users, the default will be public, max-age&#x3D;3600. |  [optional] |
|**componentCount** | **Integer** | Number of underlying components that make up this object. Components are accumulated by compose operations. |  [optional] |
|**contentDisposition** | **String** | Content-Disposition of the object data. |  [optional] |
|**contentEncoding** | **String** | Content-Encoding of the object data. |  [optional] |
|**contentLanguage** | **String** | Content-Language of the object data. |  [optional] |
|**contentType** | **String** | Content-Type of the object data. If an object is stored without a Content-Type, it is served as application/octet-stream. |  [optional] |
|**crc32c** | **String** | CRC32c checksum, as described in RFC 4960, Appendix B; encoded using base64 in big-endian byte order. For more information about using the CRC32c checksum, see Hashes and ETags: Best Practices. |  [optional] |
|**customTime** | **OffsetDateTime** | A timestamp in RFC 3339 format specified by the user for an object. |  [optional] |
|**customerEncryption** | [**ObjectCustomerEncryption**](ObjectCustomerEncryption.md) |  |  [optional] |
|**etag** | **String** | HTTP 1.1 Entity tag for the object. |  [optional] |
|**eventBasedHold** | **Boolean** | Whether an object is under event-based hold. Event-based hold is a way to retain objects until an event occurs, which is signified by the hold&#39;s release (i.e. this value is set to false). After being released (set to false), such objects will be subject to bucket-level retention (if any). One sample use case of this flag is for banks to hold loan documents for at least 3 years after loan is paid in full. Here, bucket-level retention is 3 years and the event is the loan being paid in full. In this example, these objects will be held intact for any number of years until the event has occurred (event-based hold on the object is released) and then 3 more years after that. That means retention duration of the objects begins from the moment event-based hold transitioned from true to false. |  [optional] |
|**generation** | **String** | The content generation of this object. Used for object versioning. |  [optional] |
|**hardDeleteTime** | **OffsetDateTime** | This is the time (in the future) when the soft-deleted object will no longer be restorable. It is equal to the soft delete time plus the current soft delete retention duration of the bucket. |  [optional] |
|**id** | **String** | The ID of the object, including the bucket name, object name, and generation number. |  [optional] |
|**kind** | **String** | The kind of item this is. For objects, this is always storage#object. |  [optional] |
|**kmsKeyName** | **String** | Not currently supported. Specifying the parameter causes the request to fail with status code 400 - Bad Request. |  [optional] |
|**md5Hash** | **String** | MD5 hash of the data; encoded using base64. For more information about using the MD5 hash, see Hashes and ETags: Best Practices. |  [optional] |
|**mediaLink** | **String** | Media download link. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | User-provided metadata, in key/value pairs. |  [optional] |
|**metageneration** | **String** | The version of the metadata for this object at this generation. Used for preconditions and for detecting changes in metadata. A metageneration number is only meaningful in the context of a particular generation of a particular object. |  [optional] |
|**name** | **String** | The name of the object. Required if not specified by URL parameter. |  [optional] |
|**owner** | [**ObjectOwner**](ObjectOwner.md) |  |  [optional] |
|**retention** | [**ObjectRetention**](ObjectRetention.md) |  |  [optional] |
|**retentionExpirationTime** | **OffsetDateTime** | A server-determined value that specifies the earliest time that the object&#39;s retention period expires. This value is in RFC 3339 format. Note 1: This field is not provided for objects with an active event-based hold, since retention expiration is unknown until the hold is removed. Note 2: This value can be provided even when temporary hold is set (so that the user can reason about policy without having to first unset the temporary hold). |  [optional] |
|**selfLink** | **String** | The link to this object. |  [optional] |
|**size** | **String** | Content-Length of the data in bytes. |  [optional] |
|**softDeleteTime** | **OffsetDateTime** | The time at which the object became soft-deleted in RFC 3339 format. |  [optional] |
|**storageClass** | **String** | Storage class of the object. |  [optional] |
|**temporaryHold** | **Boolean** | Whether an object is under temporary hold. While this flag is set to true, the object is protected against deletion and overwrites. A common use case of this flag is regulatory investigations where objects need to be retained while the investigation is ongoing. Note that unlike event-based hold, temporary hold does not impact retention expiration time of an object. |  [optional] |
|**timeCreated** | **OffsetDateTime** | The creation time of the object in RFC 3339 format. |  [optional] |
|**timeDeleted** | **OffsetDateTime** | The time at which the object became noncurrent in RFC 3339 format. Will be returned if and only if this version of the object has been deleted. |  [optional] |
|**timeStorageClassUpdated** | **OffsetDateTime** | The time at which the object&#39;s storage class was last changed. When the object is initially created, it will be set to timeCreated. |  [optional] |
|**updated** | **OffsetDateTime** | The modification time of the object metadata in RFC 3339 format. Set initially to object creation time and then updated whenever any metadata of the object changes. This includes changes made by a requester, such as modifying custom metadata, as well as changes made by Cloud Storage on behalf of a requester, such as changing the storage class based on an Object Lifecycle Configuration. |  [optional] |



