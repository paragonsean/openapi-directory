

# GoogleFirestoreAdminV1RestoreDatabaseRequest

The request message for FirestoreAdmin.RestoreDatabase.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backup** | **String** | Backup to restore from. Must be from the same project as the parent. Format is: &#x60;projects/{project_id}/locations/{location}/backups/{backup}&#x60; |  [optional] |
|**databaseId** | **String** | Required. The ID to use for the database, which will become the final component of the database&#39;s resource name. This database id must not be associated with an existing database. This value should be 4-63 characters. Valid characters are /a-z-/ with first character a letter and the last a letter or a number. Must not be UUID-like /[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}/. \&quot;(default)\&quot; database id is also valid. |  [optional] |
|**databaseSnapshot** | [**GoogleFirestoreAdminV1DatabaseSnapshot**](GoogleFirestoreAdminV1DatabaseSnapshot.md) |  |  [optional] |



