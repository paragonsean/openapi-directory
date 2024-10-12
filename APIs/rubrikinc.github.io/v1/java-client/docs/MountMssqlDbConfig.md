

# MountMssqlDbConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mountedDatabaseName** | **String** | Name to assign to the mounted database. |  |
|**recoveryModel** | **MssqlDatabaseRecoveryModel** |  |  [optional] |
|**recoveryPoint** | [**MssqlRecoveryPoint**](MssqlRecoveryPoint.md) |  |  |
|**targetInstanceId** | **String** | ID of the SQL Server instance to mount the database on. For availability source databases, this must be specified. When unspecified for non-availability source databases, the source SQL Server instance is used. |  [optional] |



