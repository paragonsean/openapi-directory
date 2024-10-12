

# ExportMssqlDbJobConfig


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowOverwrite** | **Boolean** | A Boolean value that determines whether an existing database can be overwritten by a database this is exported from a backup. Set to false to prevent overwrites. This is the default. Set to true to allow overwrites. |  [optional] |
|**finishRecovery** | **Boolean** | A Boolean value that determines the recovery option to use during database restore. When this value is &#39;true&#39;, the database is restored using the RECOVERY option and is fully functional at the end of the restore operation. When this value is &#39;false&#39;, the database is restored using the NORECOVERY option and remains in recovering mode at the end of the restore operation. |  [optional] |
|**maxDataStreams** | **Integer** | Maximum number of parallel data streams that can be used to copy data to the target system. |  [optional] |
|**recoveryPoint** | [**MssqlRecoveryPoint**](MssqlRecoveryPoint.md) |  |  |
|**targetDataFilePath** | **String** | The target path to store all data files. |  [optional] |
|**targetDatabaseName** | **String** | Name of the new database. |  |
|**targetFilePaths** | [**List&lt;MssqlDbFileExportPath&gt;**](MssqlDbFileExportPath.md) | One target path for each individual database file. Overrides targetDataFilePath and targetLogFilePath. |  [optional] |
|**targetInstanceId** | **String** | ID of the Microsoft SQL instance for the new database. |  |
|**targetLogFilePath** | **String** | The target path to store all log files. |  [optional] |



