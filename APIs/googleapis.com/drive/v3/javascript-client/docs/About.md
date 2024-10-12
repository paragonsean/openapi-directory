# GoogleDriveApi.About

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appInstalled** | **Boolean** | Whether the user has installed the requesting app. | [optional] 
**canCreateDrives** | **Boolean** | Whether the user can create shared drives. | [optional] 
**canCreateTeamDrives** | **Boolean** | Deprecated: Use &#x60;canCreateDrives&#x60; instead. | [optional] 
**driveThemes** | [**[AboutDriveThemesInner]**](AboutDriveThemesInner.md) | A list of themes that are supported for shared drives. | [optional] 
**exportFormats** | **{String: [String]}** | A map of source MIME type to possible targets for all supported exports. | [optional] 
**folderColorPalette** | **[String]** | The currently supported folder colors as RGB hex strings. | [optional] 
**importFormats** | **{String: [String]}** | A map of source MIME type to possible targets for all supported imports. | [optional] 
**kind** | **String** | Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;drive#about\&quot;&#x60;. | [optional] [default to &#39;drive#about&#39;]
**maxImportSizes** | **{String: String}** | A map of maximum import sizes by MIME type, in bytes. | [optional] 
**maxUploadSize** | **String** | The maximum upload size in bytes. | [optional] 
**storageQuota** | [**AboutStorageQuota**](AboutStorageQuota.md) |  | [optional] 
**teamDriveThemes** | [**[AboutTeamDriveThemesInner]**](AboutTeamDriveThemesInner.md) | Deprecated: Use &#x60;driveThemes&#x60; instead. | [optional] 
**user** | [**User**](User.md) |  | [optional] 


