# GoogleDriveApi.Revision

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**downloadUrl** | **String** | Output only. Short term download URL for the file. This will only be populated on files with content stored in Drive. | [optional] 
**etag** | **String** | Output only. The ETag of the revision. | [optional] 
**exportLinks** | **{String: String}** | Output only. Links for exporting Docs Editors files to specific formats. | [optional] 
**fileSize** | **String** | Output only. The size of the revision in bytes. This will only be populated on files with content stored in Drive. | [optional] 
**id** | **String** | Output only. The ID of the revision. | [optional] 
**kind** | **String** | Output only. This is always &#x60;drive#revision&#x60;. | [optional] [default to &#39;drive#revision&#39;]
**lastModifyingUser** | [**User**](User.md) |  | [optional] 
**lastModifyingUserName** | **String** | Output only. Name of the last user to modify this revision. | [optional] 
**md5Checksum** | **String** | Output only. An MD5 checksum for the content of this revision. This will only be populated on files with content stored in Drive. | [optional] 
**mimeType** | **String** | Output only. The MIME type of the revision. | [optional] 
**modifiedDate** | **Date** | Last time this revision was modified (formatted RFC 3339 timestamp). | [optional] 
**originalFilename** | **String** | Output only. The original filename when this revision was created. This will only be populated on files with content stored in Drive. | [optional] 
**pinned** | **Boolean** | Whether this revision is pinned to prevent automatic purging. If not set, the revision is automatically purged 30 days after newer content is uploaded. This field can only be modified on files with content stored in Drive, excluding Docs Editors files. Revisions can also be pinned when they are created through the drive.files.insert/update/copy by using the pinned query parameter. Pinned revisions are stored indefinitely using additional storage quota, up to a maximum of 200 revisions. | [optional] 
**publishAuto** | **Boolean** | Whether subsequent revisions will be automatically republished. This is only populated and can only be modified for Docs Editors files. | [optional] 
**published** | **Boolean** | Whether this revision is published. This is only populated and can only be modified for Docs Editors files. | [optional] 
**publishedLink** | **String** | Output only. A link to the published revision. This is only populated for Google Sites files. | [optional] 
**publishedOutsideDomain** | **Boolean** | Whether this revision is published outside the domain. This is only populated and can only be modified for Docs Editors files. | [optional] 
**selfLink** | **String** | Output only. A link back to this revision. | [optional] 


