# RubrikRestApi.MssqlLogShippingCreateConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shouldDisconnectStandbyUsers** | **Boolean** | Specifies whether to automatically disconnect users from a secondary database in standby mode when a restore operation is performed. If this value is set to false and users remain connected, any scheduled restore operations fail. If the \&quot;state\&quot; field is &#x60;RESTORING&#x60;, this value can be omitted and is ignored. | [optional] 
**state** | [**MssqlLogShippingOkState**](MssqlLogShippingOkState.md) |  | 
**maxDataStreams** | **Number** | Maximum number of parallel data streams that can be used to copy data to the target system. | [optional] 
**targetDataFilePath** | **String** | The path to the default target location for data file storage. | [optional] 
**targetDatabaseName** | **String** | The name of the secondary database. | 
**targetFilePaths** | [**[MssqlDbFileExportPath]**](MssqlDbFileExportPath.md) | Array of database file storage paths. Each path is the target storage location for a database file. Values in this array override the values in targetDataFilePath and targetLogFilePath for the specified database files. | [optional] 
**targetInstanceId** | **String** | The ID of the SQL Server instance that hosts the secondary database. | 
**targetLogFilePath** | **String** | The path to the location of the log files. | [optional] 


