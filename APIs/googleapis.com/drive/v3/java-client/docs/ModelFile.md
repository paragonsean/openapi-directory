

# ModelFile

The metadata for a file. Some resource methods (such as `files.update`) require a `fileId`. Use the `files.list` method to retrieve the ID for a file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appProperties** | **Map&lt;String, String&gt;** | A collection of arbitrary key-value pairs which are private to the requesting app. Entries with null values are cleared in update and copy requests. These properties can only be retrieved using an authenticated request. An authenticated request uses an access token obtained with a OAuth 2 client ID. You cannot use an API key to retrieve private properties. |  [optional] |
|**capabilities** | [**FileCapabilities**](FileCapabilities.md) |  |  [optional] |
|**contentHints** | [**FileContentHints**](FileContentHints.md) |  |  [optional] |
|**contentRestrictions** | [**List&lt;ContentRestriction&gt;**](ContentRestriction.md) | Restrictions for accessing the content of the file. Only populated if such a restriction exists. |  [optional] |
|**copyRequiresWriterPermission** | **Boolean** | Whether the options to copy, print, or download this file, should be disabled for readers and commenters. |  [optional] |
|**createdTime** | **OffsetDateTime** | The time at which the file was created (RFC 3339 date-time). |  [optional] |
|**description** | **String** | A short description of the file. |  [optional] |
|**driveId** | **String** | Output only. ID of the shared drive the file resides in. Only populated for items in shared drives. |  [optional] |
|**explicitlyTrashed** | **Boolean** | Output only. Whether the file has been explicitly trashed, as opposed to recursively trashed from a parent folder. |  [optional] |
|**exportLinks** | **Map&lt;String, String&gt;** | Output only. Links for exporting Docs Editors files to specific formats. |  [optional] [readonly] |
|**fileExtension** | **String** | Output only. The final component of &#x60;fullFileExtension&#x60;. This is only available for files with binary content in Google Drive. |  [optional] |
|**folderColorRgb** | **String** | The color for a folder or a shortcut to a folder as an RGB hex string. The supported colors are published in the &#x60;folderColorPalette&#x60; field of the About resource. If an unsupported color is specified, the closest color in the palette is used instead. |  [optional] |
|**fullFileExtension** | **String** | Output only. The full file extension extracted from the &#x60;name&#x60; field. May contain multiple concatenated extensions, such as \&quot;tar.gz\&quot;. This is only available for files with binary content in Google Drive. This is automatically updated when the &#x60;name&#x60; field changes, however it is not cleared if the new name does not contain a valid extension. |  [optional] |
|**hasAugmentedPermissions** | **Boolean** | Output only. Whether there are permissions directly on this file. This field is only populated for items in shared drives. |  [optional] |
|**hasThumbnail** | **Boolean** | Output only. Whether this file has a thumbnail. This does not indicate whether the requesting app has access to the thumbnail. To check access, look for the presence of the thumbnailLink field. |  [optional] |
|**headRevisionId** | **String** | Output only. The ID of the file&#39;s head revision. This is currently only available for files with binary content in Google Drive. |  [optional] |
|**iconLink** | **String** | Output only. A static, unauthenticated link to the file&#39;s icon. |  [optional] |
|**id** | **String** | The ID of the file. |  [optional] |
|**imageMediaMetadata** | [**FileImageMediaMetadata**](FileImageMediaMetadata.md) |  |  [optional] |
|**isAppAuthorized** | **Boolean** | Output only. Whether the file was created or opened by the requesting app. |  [optional] |
|**kind** | **String** | Output only. Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;drive#file\&quot;&#x60;. |  [optional] |
|**labelInfo** | [**FileLabelInfo**](FileLabelInfo.md) |  |  [optional] |
|**lastModifyingUser** | [**User**](User.md) |  |  [optional] |
|**linkShareMetadata** | [**FileLinkShareMetadata**](FileLinkShareMetadata.md) |  |  [optional] |
|**md5Checksum** | **String** | Output only. The MD5 checksum for the content of the file. This is only applicable to files with binary content in Google Drive. |  [optional] |
|**mimeType** | **String** | The MIME type of the file. Google Drive attempts to automatically detect an appropriate value from uploaded content, if no value is provided. The value cannot be changed unless a new revision is uploaded. If a file is created with a Google Doc MIME type, the uploaded content is imported, if possible. The supported import formats are published in the About resource. |  [optional] |
|**modifiedByMe** | **Boolean** | Output only. Whether the file has been modified by this user. |  [optional] |
|**modifiedByMeTime** | **OffsetDateTime** | The last time the file was modified by the user (RFC 3339 date-time). |  [optional] |
|**modifiedTime** | **OffsetDateTime** | he last time the file was modified by anyone (RFC 3339 date-time). Note that setting modifiedTime will also update modifiedByMeTime for the user. |  [optional] |
|**name** | **String** | The name of the file. This is not necessarily unique within a folder. Note that for immutable items such as the top level folders of shared drives, My Drive root folder, and Application Data folder the name is constant. |  [optional] |
|**originalFilename** | **String** | The original filename of the uploaded content if available, or else the original value of the &#x60;name&#x60; field. This is only available for files with binary content in Google Drive. |  [optional] |
|**ownedByMe** | **Boolean** | Output only. Whether the user owns the file. Not populated for items in shared drives. |  [optional] |
|**owners** | [**List&lt;User&gt;**](User.md) | Output only. The owner of this file. Only certain legacy files may have more than one owner. This field isn&#39;t populated for items in shared drives. |  [optional] |
|**parents** | **List&lt;String&gt;** | The IDs of the parent folders which contain the file. If not specified as part of a create request, the file is placed directly in the user&#39;s My Drive folder. If not specified as part of a copy request, the file inherits any discoverable parents of the source file. Update requests must use the &#x60;addParents&#x60; and &#x60;removeParents&#x60; parameters to modify the parents list. |  [optional] |
|**permissionIds** | **List&lt;String&gt;** | Output only. List of permission IDs for users with access to this file. |  [optional] |
|**permissions** | [**List&lt;Permission&gt;**](Permission.md) | Output only. The full list of permissions for the file. This is only available if the requesting user can share the file. Not populated for items in shared drives. |  [optional] |
|**properties** | **Map&lt;String, String&gt;** | A collection of arbitrary key-value pairs which are visible to all apps. Entries with null values are cleared in update and copy requests. |  [optional] |
|**quotaBytesUsed** | **String** | Output only. The number of storage quota bytes used by the file. This includes the head revision as well as previous revisions with &#x60;keepForever&#x60; enabled. |  [optional] |
|**resourceKey** | **String** | Output only. A key needed to access the item via a shared link. |  [optional] |
|**sha1Checksum** | **String** | Output only. The SHA1 checksum associated with this file, if available. This field is only populated for files with content stored in Google Drive; it is not populated for Docs Editors or shortcut files. |  [optional] |
|**sha256Checksum** | **String** | Output only. The SHA256 checksum associated with this file, if available. This field is only populated for files with content stored in Google Drive; it is not populated for Docs Editors or shortcut files. |  [optional] |
|**shared** | **Boolean** | Output only. Whether the file has been shared. Not populated for items in shared drives. |  [optional] |
|**sharedWithMeTime** | **OffsetDateTime** | The time at which the file was shared with the user, if applicable (RFC 3339 date-time). |  [optional] |
|**sharingUser** | [**User**](User.md) |  |  [optional] |
|**shortcutDetails** | [**FileShortcutDetails**](FileShortcutDetails.md) |  |  [optional] |
|**size** | **String** | Output only. Size in bytes of blobs and first party editor files. Won&#39;t be populated for files that have no size, like shortcuts and folders. |  [optional] |
|**spaces** | **List&lt;String&gt;** | Output only. The list of spaces which contain the file. The currently supported values are &#39;drive&#39;, &#39;appDataFolder&#39; and &#39;photos&#39;. |  [optional] |
|**starred** | **Boolean** | Whether the user has starred the file. |  [optional] |
|**teamDriveId** | **String** | Deprecated: Output only. Use &#x60;driveId&#x60; instead. |  [optional] |
|**thumbnailLink** | **String** | Output only. A short-lived link to the file&#39;s thumbnail, if available. Typically lasts on the order of hours. Only populated when the requesting app can access the file&#39;s content. If the file isn&#39;t shared publicly, the URL returned in &#x60;Files.thumbnailLink&#x60; must be fetched using a credentialed request. |  [optional] |
|**thumbnailVersion** | **String** | Output only. The thumbnail version for use in thumbnail cache invalidation. |  [optional] |
|**trashed** | **Boolean** | Whether the file has been trashed, either explicitly or from a trashed parent folder. Only the owner may trash a file, and other users cannot see files in the owner&#39;s trash. |  [optional] |
|**trashedTime** | **OffsetDateTime** | The time that the item was trashed (RFC 3339 date-time). Only populated for items in shared drives. |  [optional] |
|**trashingUser** | [**User**](User.md) |  |  [optional] |
|**version** | **String** | Output only. A monotonically increasing version number for the file. This reflects every change made to the file on the server, even those not visible to the user. |  [optional] |
|**videoMediaMetadata** | [**FileVideoMediaMetadata**](FileVideoMediaMetadata.md) |  |  [optional] |
|**viewedByMe** | **Boolean** | Output only. Whether the file has been viewed by this user. |  [optional] |
|**viewedByMeTime** | **OffsetDateTime** | The last time the file was viewed by the user (RFC 3339 date-time). |  [optional] |
|**viewersCanCopyContent** | **Boolean** | Deprecated: Use &#x60;copyRequiresWriterPermission&#x60; instead. |  [optional] |
|**webContentLink** | **String** | Output only. A link for downloading the content of the file in a browser. This is only available for files with binary content in Google Drive. |  [optional] |
|**webViewLink** | **String** | Output only. A link for opening the file in a relevant Google editor or viewer in a browser. |  [optional] |
|**writersCanShare** | **Boolean** | Whether users with only &#x60;writer&#x60; permission can modify the file&#39;s permissions. Not populated for items in shared drives. |  [optional] |



