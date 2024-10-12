

# About

An item with user information and settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalRoleInfo** | [**List&lt;AboutAdditionalRoleInfoInner&gt;**](AboutAdditionalRoleInfoInner.md) | Information about supported additional roles per file type. The most specific type takes precedence. |  [optional] |
|**canCreateDrives** | **Boolean** | Whether the user can create shared drives. |  [optional] |
|**canCreateTeamDrives** | **Boolean** | Deprecated: Use &#x60;canCreateDrives&#x60; instead. |  [optional] |
|**domainSharingPolicy** | **String** | The domain sharing policy for the current user. Possible values are: * &#x60;allowed&#x60; * &#x60;allowedWithWarning&#x60; * &#x60;incomingOnly&#x60; * &#x60;disallowed&#x60; |  [optional] |
|**driveThemes** | [**List&lt;AboutDriveThemesInner&gt;**](AboutDriveThemesInner.md) | A list of themes that are supported for shared drives. |  [optional] |
|**etag** | **String** | The ETag of the item. |  [optional] |
|**exportFormats** | [**List&lt;AboutExportFormatsInner&gt;**](AboutExportFormatsInner.md) | The allowable export formats. |  [optional] |
|**features** | [**List&lt;AboutFeaturesInner&gt;**](AboutFeaturesInner.md) | List of additional features enabled on this account. |  [optional] |
|**folderColorPalette** | **List&lt;String&gt;** | The palette of allowable folder colors as RGB hex strings. |  [optional] |
|**importFormats** | [**List&lt;AboutImportFormatsInner&gt;**](AboutImportFormatsInner.md) | The allowable import formats. |  [optional] |
|**isCurrentAppInstalled** | **Boolean** | A boolean indicating whether the authenticated app is installed by the authenticated user. |  [optional] |
|**kind** | **String** | This is always &#x60;drive#about&#x60;. |  [optional] |
|**languageCode** | **String** | The user&#39;s language or locale code, as defined by BCP 47, with some extensions from Unicode&#39;s LDML format (http://www.unicode.org/reports/tr35/). |  [optional] |
|**largestChangeId** | **String** | The largest change id. |  [optional] |
|**maxUploadSizes** | [**List&lt;AboutMaxUploadSizesInner&gt;**](AboutMaxUploadSizesInner.md) | List of max upload sizes for each file type. The most specific type takes precedence. |  [optional] |
|**name** | **String** | The name of the current user. |  [optional] |
|**permissionId** | **String** | The current user&#39;s ID as visible in the permissions collection. |  [optional] |
|**quotaBytesByService** | [**List&lt;AboutQuotaBytesByServiceInner&gt;**](AboutQuotaBytesByServiceInner.md) | The amount of storage quota used by different Google services. |  [optional] |
|**quotaBytesTotal** | **String** | The total number of quota bytes. This is only relevant when quotaType is LIMITED. |  [optional] |
|**quotaBytesUsed** | **String** | The number of quota bytes used by Google Drive. |  [optional] |
|**quotaBytesUsedAggregate** | **String** | The number of quota bytes used by all Google apps (Drive, Picasa, etc.). |  [optional] |
|**quotaBytesUsedInTrash** | **String** | The number of quota bytes used by trashed items. |  [optional] |
|**quotaType** | **String** | The type of the user&#39;s storage quota. Possible values are: * &#x60;LIMITED&#x60; * &#x60;UNLIMITED&#x60; |  [optional] |
|**remainingChangeIds** | **String** | The number of remaining change ids, limited to no more than 2500. |  [optional] |
|**rootFolderId** | **String** | The id of the root folder. |  [optional] |
|**selfLink** | **String** | A link back to this item. |  [optional] |
|**teamDriveThemes** | [**List&lt;AboutTeamDriveThemesInner&gt;**](AboutTeamDriveThemesInner.md) | Deprecated: Use &#x60;driveThemes&#x60; instead. |  [optional] |
|**user** | [**User**](User.md) |  |  [optional] |



