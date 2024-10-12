

# ModelFile

The metadata for a file. Some resource methods (such as `files.update`) require a `fileId`. Use the `files.list` method to retrieve the ID for a file.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alternateLink** | **String** | Output only. A link for opening the file in a relevant Google editor or viewer. |  [optional] |
|**appDataContents** | **Boolean** | Output only. Whether this file is in the Application Data folder. |  [optional] |
|**canComment** | **Boolean** | Output only. Deprecated: Use &#x60;capabilities/canComment&#x60; instead. |  [optional] |
|**canReadRevisions** | **Boolean** | Output only. Deprecated: Use &#x60;capabilities/canReadRevisions&#x60; instead. |  [optional] |
|**capabilities** | [**FileCapabilities**](FileCapabilities.md) |  |  [optional] |
|**contentRestrictions** | [**List&lt;ContentRestriction&gt;**](ContentRestriction.md) | Restrictions for accessing the content of the file. Only populated if such a restriction exists. |  [optional] |
|**copyRequiresWriterPermission** | **Boolean** | Whether the options to copy, print, or download this file, should be disabled for readers and commenters. |  [optional] |
|**copyable** | **Boolean** | Output only. Deprecated: Use &#x60;capabilities/canCopy&#x60; instead. |  [optional] |
|**createdDate** | **OffsetDateTime** | Create time for this file (formatted RFC 3339 timestamp). |  [optional] |
|**defaultOpenWithLink** | **String** | Output only. A link to open this file with the user&#39;s default app for this file. Only populated when the drive.apps.readonly scope is used. |  [optional] |
|**description** | **String** | A short description of the file. |  [optional] |
|**downloadUrl** | **String** | Output only. Short lived download URL for the file. This field is only populated for files with content stored in Google Drive; it is not populated for Google Docs or shortcut files. |  [optional] |
|**driveId** | **String** | Output only. ID of the shared drive the file resides in. Only populated for items in shared drives. |  [optional] |
|**editable** | **Boolean** | Output only. Deprecated: Use &#x60;capabilities/canEdit&#x60; instead. |  [optional] |
|**embedLink** | **String** | Output only. A link for embedding the file. |  [optional] |
|**etag** | **String** | Output only. ETag of the file. |  [optional] |
|**explicitlyTrashed** | **Boolean** | Output only. Whether this file has been explicitly trashed, as opposed to recursively trashed. |  [optional] |
|**exportLinks** | **Map&lt;String, String&gt;** | Output only. Links for exporting Docs Editors files to specific formats. |  [optional] [readonly] |
|**fileExtension** | **String** | Output only. The final component of &#x60;fullFileExtension&#x60; with trailing text that does not appear to be part of the extension removed. This field is only populated for files with content stored in Google Drive; it is not populated for Docs Editors or shortcut files. |  [optional] |
|**fileSize** | **String** | Output only. Size in bytes of blobs and first party editor files. Won&#39;t be populated for files that have no size, like shortcuts and folders. |  [optional] |
|**folderColorRgb** | **String** | Folder color as an RGB hex string if the file is a folder or a shortcut to a folder. The list of supported colors is available in the folderColorPalette field of the About resource. If an unsupported color is specified, it will be changed to the closest color in the palette. |  [optional] |
|**fullFileExtension** | **String** | Output only. The full file extension; extracted from the title. May contain multiple concatenated extensions, such as \&quot;tar.gz\&quot;. Removing an extension from the title does not clear this field; however, changing the extension on the title does update this field. This field is only populated for files with content stored in Google Drive; it is not populated for Docs Editors or shortcut files. |  [optional] |
|**hasAugmentedPermissions** | **Boolean** | Output only. Whether there are permissions directly on this file. This field is only populated for items in shared drives. |  [optional] |
|**hasThumbnail** | **Boolean** | Output only. Whether this file has a thumbnail. This does not indicate whether the requesting app has access to the thumbnail. To check access, look for the presence of the thumbnailLink field. |  [optional] |
|**headRevisionId** | **String** | Output only. The ID of the file&#39;s head revision. This field is only populated for files with content stored in Google Drive; it is not populated for Docs Editors or shortcut files. |  [optional] |
|**iconLink** | **String** | Output only. A link to the file&#39;s icon. |  [optional] |
|**id** | **String** | The ID of the file. |  [optional] |
|**imageMediaMetadata** | [**FileImageMediaMetadata**](FileImageMediaMetadata.md) |  |  [optional] |
|**indexableText** | [**FileIndexableText**](FileIndexableText.md) |  |  [optional] |
|**isAppAuthorized** | **Boolean** | Output only. Whether the file was created or opened by the requesting app. |  [optional] |
|**kind** | **String** | Output only. The type of file. This is always &#x60;drive#file&#x60;. |  [optional] |
|**labelInfo** | [**FileLabelInfo**](FileLabelInfo.md) |  |  [optional] |
|**labels** | [**FileLabels**](FileLabels.md) |  |  [optional] |
|**lastModifyingUser** | [**User**](User.md) |  |  [optional] |
|**lastModifyingUserName** | **String** | Output only. Name of the last user to modify this file. |  [optional] |
|**lastViewedByMeDate** | **OffsetDateTime** | Last time this file was viewed by the user (formatted RFC 3339 timestamp). |  [optional] |
|**linkShareMetadata** | [**FileLinkShareMetadata**](FileLinkShareMetadata.md) |  |  [optional] |
|**markedViewedByMeDate** | **OffsetDateTime** | Deprecated. |  [optional] |
|**md5Checksum** | **String** | Output only. An MD5 checksum for the content of this file. This field is only populated for files with content stored in Google Drive; it is not populated for Docs Editors or shortcut files. |  [optional] |
|**mimeType** | **String** | The MIME type of the file. This is only mutable on update when uploading new content. This field can be left blank, and the mimetype will be determined from the uploaded content&#39;s MIME type. |  [optional] |
|**modifiedByMeDate** | **OffsetDateTime** | Last time this file was modified by the user (formatted RFC 3339 timestamp). Note that setting modifiedDate will also update the modifiedByMe date for the user which set the date. |  [optional] |
|**modifiedDate** | **OffsetDateTime** | Last time this file was modified by anyone (formatted RFC 3339 timestamp). This is only mutable on update when the setModifiedDate parameter is set. |  [optional] |
|**openWithLinks** | **Map&lt;String, String&gt;** | Output only. A map of the id of each of the user&#39;s apps to a link to open this file with that app. Only populated when the drive.apps.readonly scope is used. |  [optional] |
|**originalFilename** | **String** | The original filename of the uploaded content if available, or else the original value of the &#x60;title&#x60; field. This is only available for files with binary content in Google Drive. |  [optional] |
|**ownedByMe** | **Boolean** | Output only. Whether the file is owned by the current user. Not populated for items in shared drives. |  [optional] |
|**ownerNames** | **List&lt;String&gt;** | Output only. Name(s) of the owner(s) of this file. Not populated for items in shared drives. |  [optional] |
|**owners** | [**List&lt;User&gt;**](User.md) | Output only. The owner of this file. Only certain legacy files may have more than one owner. This field isn&#39;t populated for items in shared drives. |  [optional] |
|**parents** | [**List&lt;ParentReference&gt;**](ParentReference.md) | Collection of parent folders which contain this file. If not specified as part of an insert request, the file will be placed directly in the user&#39;s My Drive folder. If not specified as part of a copy request, the file will inherit any discoverable parents of the source file. Update requests can also use the &#x60;addParents&#x60; and &#x60;removeParents&#x60; parameters to modify the parents list. |  [optional] |
|**permissionIds** | **List&lt;String&gt;** | Output only. List of permission IDs for users with access to this file. |  [optional] |
|**permissions** | [**List&lt;Permission&gt;**](Permission.md) | Output only. The list of permissions for users with access to this file. Not populated for items in shared drives. |  [optional] |
|**properties** | [**List&lt;Property&gt;**](Property.md) | The list of properties. |  [optional] |
|**quotaBytesUsed** | **String** | Output only. The number of quota bytes used by this file. |  [optional] |
|**resourceKey** | **String** | Output only. A key needed to access the item via a shared link. |  [optional] |
|**selfLink** | **String** | Output only. A link back to this file. |  [optional] |
|**sha1Checksum** | **String** | Output only. The SHA1 checksum associated with this file, if available. This field is only populated for files with content stored in Google Drive; it is not populated for Docs Editors or shortcut files. |  [optional] |
|**sha256Checksum** | **String** | Output only. The SHA256 checksum associated with this file, if available. This field is only populated for files with content stored in Google Drive; it is not populated for Docs Editors or shortcut files. |  [optional] |
|**shareable** | **Boolean** | Output only. Deprecated: Use &#x60;capabilities/canShare&#x60; instead. |  [optional] |
|**shared** | **Boolean** | Output only. Whether the file has been shared. Not populated for items in shared drives. |  [optional] |
|**sharedWithMeDate** | **OffsetDateTime** | Time at which this file was shared with the user (formatted RFC 3339 timestamp). |  [optional] |
|**sharingUser** | [**User**](User.md) |  |  [optional] |
|**shortcutDetails** | [**FileShortcutDetails**](FileShortcutDetails.md) |  |  [optional] |
|**spaces** | **List&lt;String&gt;** | Output only. The list of spaces which contain the file. Supported values are &#x60;drive&#x60;, &#x60;appDataFolder&#x60; and &#x60;photos&#x60;. |  [optional] |
|**teamDriveId** | **String** | Output only. Deprecated: Use &#x60;driveId&#x60; instead. |  [optional] |
|**thumbnail** | [**FileThumbnail**](FileThumbnail.md) |  |  [optional] |
|**thumbnailLink** | **String** | Output only. A short-lived link to the file&#39;s thumbnail, if available. Typically lasts on the order of hours. Only populated when the requesting app can access the file&#39;s content. If the file isn&#39;t shared publicly, the URL returned in &#x60;Files.thumbnailLink&#x60; must be fetched using a credentialed request. |  [optional] |
|**thumbnailVersion** | **String** | Output only. The thumbnail version for use in thumbnail cache invalidation. |  [optional] |
|**title** | **String** | The title of this file. Note that for immutable items such as the top level folders of shared drives, My Drive root folder, and Application Data folder the title is constant. |  [optional] |
|**trashedDate** | **OffsetDateTime** | The time that the item was trashed (formatted RFC 3339 timestamp). Only populated for items in shared drives. |  [optional] |
|**trashingUser** | [**User**](User.md) |  |  [optional] |
|**userPermission** | [**Permission**](Permission.md) |  |  [optional] |
|**version** | **String** | Output only. A monotonically increasing version number for the file. This reflects every change made to the file on the server, even those not visible to the requesting user. |  [optional] |
|**videoMediaMetadata** | [**FileVideoMediaMetadata**](FileVideoMediaMetadata.md) |  |  [optional] |
|**webContentLink** | **String** | Output only. A link for downloading the content of the file in a browser using cookie based authentication. In cases where the content is shared publicly, the content can be downloaded without any credentials. |  [optional] |
|**webViewLink** | **String** | Output only. A link only available on public folders for viewing their static web assets (HTML, CSS, JS, etc) via Google Drive&#39;s Website Hosting. |  [optional] |
|**writersCanShare** | **Boolean** | Whether writers can share the document with other users. Not populated for items in shared drives. |  [optional] |



