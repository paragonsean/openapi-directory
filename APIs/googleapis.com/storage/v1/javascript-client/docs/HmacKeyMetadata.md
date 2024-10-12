# CloudStorageJsonApi.HmacKeyMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessId** | **String** | The ID of the HMAC Key. | [optional] 
**etag** | **String** | HTTP 1.1 Entity tag for the HMAC key. | [optional] 
**id** | **String** | The ID of the HMAC key, including the Project ID and the Access ID. | [optional] 
**kind** | **String** | The kind of item this is. For HMAC Key metadata, this is always storage#hmacKeyMetadata. | [optional] [default to &#39;storage#hmacKeyMetadata&#39;]
**projectId** | **String** | Project ID owning the service account to which the key authenticates. | [optional] 
**selfLink** | **String** | The link to this resource. | [optional] 
**serviceAccountEmail** | **String** | The email address of the key&#39;s associated service account. | [optional] 
**state** | **String** | The state of the key. Can be one of ACTIVE, INACTIVE, or DELETED. | [optional] 
**timeCreated** | **Date** | The creation time of the HMAC key in RFC 3339 format. | [optional] 
**updated** | **Date** | The last modification time of the HMAC key metadata in RFC 3339 format. | [optional] 


