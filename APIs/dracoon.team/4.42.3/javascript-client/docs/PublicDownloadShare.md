# DracoonApi.PublicDownloadShare

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | Creation date | 
**creatorName** | **String** | Creator name | 
**creatorUsername** | **String** | Creator username | [optional] 
**expireAt** | **Date** | Expiration date | [optional] 
**fileKey** | [**FileKey**](FileKey.md) |  | [optional] 
**fileName** | **String** | File name | 
**hasDownloadLimit** | **Boolean** | &amp;#128640; Since v4.11.0  Determines whether Download Share has a limit for amount of downloads | 
**isEncrypted** | **Boolean** | Encryption state | [optional] 
**isProtected** | **Boolean** | Is share protected by password | 
**limitReached** | **Boolean** | Downloads limit reached | 
**mediaType** | **String** | &amp;#128640; Since v4.11.0  * &#x60;application/zip&#x60; (for folders and rooms)  * actual file media type (for files only) | 
**name** | **String** | Share display name (alias name) | [optional] 
**notes** | **String** | User notes | [optional] 
**privateKeyContainer** | [**PrivateKeyContainer**](PrivateKeyContainer.md) |  | [optional] 
**size** | **Number** | File size or container size not compressed (in bytes) | 


