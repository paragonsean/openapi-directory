

# Database

A Cloud Spanner database.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. If exists, the time at which the database creation started. |  [optional] [readonly] |
|**databaseDialect** | [**DatabaseDialectEnum**](#DatabaseDialectEnum) | Output only. The dialect of the Cloud Spanner Database. |  [optional] [readonly] |
|**defaultLeader** | **String** | Output only. The read-write region which contains the database&#39;s leader replicas. This is the same as the value of default_leader database option set using DatabaseAdmin.CreateDatabase or DatabaseAdmin.UpdateDatabaseDdl. If not explicitly set, this is empty. |  [optional] [readonly] |
|**earliestVersionTime** | **String** | Output only. Earliest timestamp at which older versions of the data can be read. This value is continuously updated by Cloud Spanner and becomes stale the moment it is queried. If you are using this value to recover data, make sure to account for the time from the moment when the value is queried to the moment when you initiate the recovery. |  [optional] [readonly] |
|**enableDropProtection** | **Boolean** | Whether drop protection is enabled for this database. Defaults to false, if not set. For more details, please see how to [prevent accidental database deletion](https://cloud.google.com/spanner/docs/prevent-database-deletion). |  [optional] |
|**encryptionConfig** | [**EncryptionConfig**](EncryptionConfig.md) |  |  [optional] |
|**encryptionInfo** | [**List&lt;EncryptionInfo&gt;**](EncryptionInfo.md) | Output only. For databases that are using customer managed encryption, this field contains the encryption information for the database, such as all Cloud KMS key versions that are in use. The &#x60;encryption_status&#39; field inside of each &#x60;EncryptionInfo&#x60; is not populated. For databases that are using Google default or other types of encryption, this field is empty. This field is propagated lazily from the backend. There might be a delay from when a key version is being used and when it appears in this field. |  [optional] [readonly] |
|**name** | **String** | Required. The name of the database. Values are of the form &#x60;projects//instances//databases/&#x60;, where &#x60;&#x60; is as specified in the &#x60;CREATE DATABASE&#x60; statement. This name can be passed to other API methods to identify the database. |  [optional] |
|**reconciling** | **Boolean** | Output only. If true, the database is being updated. If false, there are no ongoing update operations for the database. |  [optional] [readonly] |
|**restoreInfo** | [**RestoreInfo**](RestoreInfo.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current database state. |  [optional] [readonly] |
|**versionRetentionPeriod** | **String** | Output only. The period in which Cloud Spanner retains all versions of data for the database. This is the same as the value of version_retention_period database option set using UpdateDatabaseDdl. Defaults to 1 hour, if not set. |  [optional] [readonly] |



## Enum: DatabaseDialectEnum

| Name | Value |
|---- | -----|
| DATABASE_DIALECT_UNSPECIFIED | &quot;DATABASE_DIALECT_UNSPECIFIED&quot; |
| GOOGLE_STANDARD_SQL | &quot;GOOGLE_STANDARD_SQL&quot; |
| POSTGRESQL | &quot;POSTGRESQL&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| READY | &quot;READY&quot; |
| READY_OPTIMIZING | &quot;READY_OPTIMIZING&quot; |



