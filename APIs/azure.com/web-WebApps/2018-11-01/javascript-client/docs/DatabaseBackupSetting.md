# WebAppsApiClient.DatabaseBackupSetting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionString** | **String** | Contains a connection string to a database which is being backed up or restored. If the restore should happen to a new database, the database name inside is the new one. | [optional] 
**connectionStringName** | **String** | Contains a connection string name that is linked to the SiteConfig.ConnectionStrings. This is used during restore with overwrite connection strings options. | [optional] 
**databaseType** | **String** | Database type (e.g. SqlAzure / MySql). | 
**name** | **String** |  | [optional] 



## Enum: DatabaseTypeEnum


* `SqlAzure` (value: `"SqlAzure"`)

* `MySql` (value: `"MySql"`)

* `LocalMySql` (value: `"LocalMySql"`)

* `PostgreSql` (value: `"PostgreSql"`)




