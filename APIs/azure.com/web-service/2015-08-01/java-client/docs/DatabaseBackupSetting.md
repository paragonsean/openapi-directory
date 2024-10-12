

# DatabaseBackupSetting

Note: properties are serialized in JSON format and stored in DB.               if new properties are added they might not be in the previous data rows               so please handle nulls

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionString** | **String** | Contains a connection string to a database which is being backed up/restored. If the restore should happen to a new database, the database name inside is the new one. |  [optional] |
|**connectionStringName** | **String** | Contains a connection string name that is linked to the SiteConfig.ConnectionStrings.              This is used during restore with overwrite connection strings options. |  [optional] |
|**databaseType** | **String** | SqlAzure / MySql |  [optional] |
|**name** | **String** |  |  [optional] |



