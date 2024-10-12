

# RestoreDatabaseRequest

The request for RestoreDatabase.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backup** | **String** | Name of the backup from which to restore. Values are of the form &#x60;projects//instances//backups/&#x60;. |  [optional] |
|**databaseId** | **String** | Required. The id of the database to create and restore to. This database must not already exist. The &#x60;database_id&#x60; appended to &#x60;parent&#x60; forms the full database name of the form &#x60;projects//instances//databases/&#x60;. |  [optional] |
|**encryptionConfig** | [**RestoreDatabaseEncryptionConfig**](RestoreDatabaseEncryptionConfig.md) |  |  [optional] |



