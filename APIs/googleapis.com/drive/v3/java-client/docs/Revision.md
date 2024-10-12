

# Revision

The metadata for a revision to a file. Some resource methods (such as `revisions.update`) require a `revisionId`. Use the `revisions.list` method to retrieve the ID for a revision.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**exportLinks** | **Map&lt;String, String&gt;** | Output only. Links for exporting Docs Editors files to specific formats. |  [optional] |
|**id** | **String** | Output only. The ID of the revision. |  [optional] |
|**keepForever** | **Boolean** | Whether to keep this revision forever, even if it is no longer the head revision. If not set, the revision will be automatically purged 30 days after newer content is uploaded. This can be set on a maximum of 200 revisions for a file. This field is only applicable to files with binary content in Drive. |  [optional] |
|**kind** | **String** | Output only. Identifies what kind of resource this is. Value: the fixed string &#x60;\&quot;drive#revision\&quot;&#x60;. |  [optional] |
|**lastModifyingUser** | [**User**](User.md) |  |  [optional] |
|**md5Checksum** | **String** | Output only. The MD5 checksum of the revision&#39;s content. This is only applicable to files with binary content in Drive. |  [optional] |
|**mimeType** | **String** | Output only. The MIME type of the revision. |  [optional] |
|**modifiedTime** | **OffsetDateTime** | The last time the revision was modified (RFC 3339 date-time). |  [optional] |
|**originalFilename** | **String** | Output only. The original filename used to create this revision. This is only applicable to files with binary content in Drive. |  [optional] |
|**publishAuto** | **Boolean** | Whether subsequent revisions will be automatically republished. This is only applicable to Docs Editors files. |  [optional] |
|**published** | **Boolean** | Whether this revision is published. This is only applicable to Docs Editors files. |  [optional] |
|**publishedLink** | **String** | Output only. A link to the published revision. This is only populated for Google Sites files. |  [optional] |
|**publishedOutsideDomain** | **Boolean** | Whether this revision is published outside the domain. This is only applicable to Docs Editors files. |  [optional] |
|**size** | **String** | Output only. The size of the revision&#39;s content in bytes. This is only applicable to files with binary content in Drive. |  [optional] |



