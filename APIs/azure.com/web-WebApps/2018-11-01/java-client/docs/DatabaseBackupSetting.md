

# DatabaseBackupSetting

Database backup settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**connectionString** | **String** | Contains a connection string to a database which is being backed up or restored. If the restore should happen to a new database, the database name inside is the new one. |  [optional] |
|**connectionStringName** | **String** | Contains a connection string name that is linked to the SiteConfig.ConnectionStrings. This is used during restore with overwrite connection strings options. |  [optional] |
|**databaseType** | [**DatabaseTypeEnum**](#DatabaseTypeEnum) | Database type (e.g. SqlAzure / MySql). |  |
|**name** | **String** |  |  [optional] |



## Enum: DatabaseTypeEnum

| Name | Value |
|---- | -----|
| SQL_AZURE | &quot;SqlAzure&quot; |
| MY_SQL | &quot;MySql&quot; |
| LOCAL_MY_SQL | &quot;LocalMySql&quot; |
| POSTGRE_SQL | &quot;PostgreSql&quot; |



