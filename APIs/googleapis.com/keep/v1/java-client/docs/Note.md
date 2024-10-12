

# Note

A single note.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | [**List&lt;Attachment&gt;**](Attachment.md) | Output only. The attachments attached to this note. |  [optional] [readonly] |
|**body** | [**Section**](Section.md) |  |  [optional] |
|**createTime** | **String** | Output only. When this note was created. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name of this note. See general note on identifiers in KeepService. |  [optional] [readonly] |
|**permissions** | [**List&lt;Permission&gt;**](Permission.md) | Output only. The list of permissions set on the note. Contains at least one entry for the note owner. |  [optional] [readonly] |
|**title** | **String** | The title of the note. Length must be less than 1,000 characters. |  [optional] |
|**trashTime** | **String** | Output only. When this note was trashed. If &#x60;trashed&#x60;, the note is eventually deleted. If the note is not trashed, this field is not set (and the trashed field is &#x60;false&#x60;). |  [optional] [readonly] |
|**trashed** | **Boolean** | Output only. &#x60;true&#x60; if this note has been trashed. If trashed, the note is eventually deleted. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. When this note was last modified. |  [optional] [readonly] |



