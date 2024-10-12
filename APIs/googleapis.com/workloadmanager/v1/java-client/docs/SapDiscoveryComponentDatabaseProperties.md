

# SapDiscoveryComponentDatabaseProperties

A set of properties describing an SAP Database layer.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**databaseType** | [**DatabaseTypeEnum**](#DatabaseTypeEnum) | Required. Type of the database. HANA, DB2, etc. |  [optional] |
|**databaseVersion** | **String** | Optional. The version of the database software running in the system. |  [optional] |
|**primaryInstanceUri** | **String** | Required. URI of the recognized primary instance of the database. |  [optional] |
|**sharedNfsUri** | **String** | Optional. URI of the recognized shared NFS of the database. May be empty if the database has only a single node. |  [optional] |



## Enum: DatabaseTypeEnum

| Name | Value |
|---- | -----|
| DATABASE_TYPE_UNSPECIFIED | &quot;DATABASE_TYPE_UNSPECIFIED&quot; |
| HANA | &quot;HANA&quot; |
| MAX_DB | &quot;MAX_DB&quot; |
| DB2 | &quot;DB2&quot; |



