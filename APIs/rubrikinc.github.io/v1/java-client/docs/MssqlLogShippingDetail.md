

# MssqlLogShippingDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ID assigned to the log shipping configuration object. |  |
|**lagTime** | **Long** | Number of milliseconds elapsed since the latest backup was applied to the secondary database and the time the backup was taken on the primary database. |  [optional] |
|**lastAppliedPoint** | **OffsetDateTime** | Timestamp of the last transaction applied using the specified log shipping configuration object. |  [optional] |
|**location** | **String** | Location of a specified secondary database. Location uses this format: \&quot;host/instance\&quot;. |  |
|**primaryDatabaseId** | **String** | ID of the primary database. |  |
|**primaryDatabaseLogBackupFrequency** | **Long** | Log backup frequency, in seconds, of the primary database. |  |
|**primaryDatabaseName** | **String** | Name of the primary database. |  |
|**secondaryDatabaseId** | **String** | ID of the secondary database. |  [optional] |
|**secondaryDatabaseName** | **String** | Name of the secondary database. |  |
|**state** | **String** | The current state of the secondary database. |  [optional] |
|**status** | [**MssqlLogShippingStatusInfo**](MssqlLogShippingStatusInfo.md) |  |  |
|**links** | [**MssqlLogShippingLinks**](MssqlLogShippingLinks.md) |  |  |
|**shouldDisconnectStandbyUsers** | **Boolean** | Whether to automatically disconnect users from a secondary database in Standby mode when a restore operation is performed. If this value is false and users remain connected, then any scheduled restore operations will fail. This is only returned when the secondary database is in Standby mode. |  [optional] |



