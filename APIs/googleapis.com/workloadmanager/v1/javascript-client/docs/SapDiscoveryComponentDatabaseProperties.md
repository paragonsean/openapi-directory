# WorkloadManagerApi.SapDiscoveryComponentDatabaseProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databaseType** | **String** | Required. Type of the database. HANA, DB2, etc. | [optional] 
**databaseVersion** | **String** | Optional. The version of the database software running in the system. | [optional] 
**primaryInstanceUri** | **String** | Required. URI of the recognized primary instance of the database. | [optional] 
**sharedNfsUri** | **String** | Optional. URI of the recognized shared NFS of the database. May be empty if the database has only a single node. | [optional] 



## Enum: DatabaseTypeEnum


* `DATABASE_TYPE_UNSPECIFIED` (value: `"DATABASE_TYPE_UNSPECIFIED"`)

* `HANA` (value: `"HANA"`)

* `MAX_DB` (value: `"MAX_DB"`)

* `DB2` (value: `"DB2"`)




