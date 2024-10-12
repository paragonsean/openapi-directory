# AnchoreEngineApiServer.ImageImportManifest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | [**ImportContentDigests**](ImportContentDigests.md) |  | 
**digest** | **String** |  | 
**localImageId** | **String** | An \&quot;imageId\&quot; as used by Docker if available | [optional] 
**operationUuid** | **String** |  | 
**parentDigest** | **String** | The digest of the images&#39;s manifest-list parent if it was accessed from a multi-arch tag where the tag pointed to a manifest-list. This allows preservation of that relationship in the data | [optional] 
**tags** | **[String]** |  | 


