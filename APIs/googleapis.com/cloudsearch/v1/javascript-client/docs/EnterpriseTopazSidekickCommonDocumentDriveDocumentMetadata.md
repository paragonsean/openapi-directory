# CloudSearchApi.EnterpriseTopazSidekickCommonDocumentDriveDocumentMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentId** | **String** | The drive document cosmo id. Client could use the id to build a URL to open a document. Please use Document.document_id. | [optional] 
**isPrivate** | **Boolean** | Additional field to identify whether a document is private since scope set to LIMITED can mean both that the doc is private or that it&#39;s shared with others. is_private indicates whether the doc is not shared with anyone except for the owner. | [optional] 
**lastCommentTimeMs** | **String** | Timestamp of the most recent comment added to the document in milliseconds since epoch. | [optional] 
**lastEditTimeMs** | **String** | Timestamp of the most recent edit from the current user in milliseconds since epoch. | [optional] 
**lastModificationTimeMillis** | **String** | Last modification time of the document (independent of the user that modified it). | [optional] 
**lastUpdatedTimeMs** | **String** | Timestamp of the last updated time of the document in milliseconds since epoch. | [optional] 
**lastViewTimeMs** | **String** | Timestamp of the most recent view from the current user in milliseconds since epoch. | [optional] 
**owner** | [**EnterpriseTopazSidekickCommonPerson**](EnterpriseTopazSidekickCommonPerson.md) |  | [optional] 
**scope** | **String** | ACL scope of the document which identifies the sharing status of the doc (e.g., limited, shared with link, team drive, ...). | [optional] 



## Enum: ScopeEnum


* `UNKNOWN_DOCUMENT_SCOPE` (value: `"UNKNOWN_DOCUMENT_SCOPE"`)

* `LIMITED` (value: `"LIMITED"`)

* `DASHER_DOMAIN_WITH_LINK` (value: `"DASHER_DOMAIN_WITH_LINK"`)

* `DASHER_DOMAIN` (value: `"DASHER_DOMAIN"`)

* `PUBLIC_WITH_LINK` (value: `"PUBLIC_WITH_LINK"`)

* `PUBLIC` (value: `"PUBLIC"`)

* `TEAM_DRIVE` (value: `"TEAM_DRIVE"`)




