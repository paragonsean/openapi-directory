# RubrikRestApi.RestoreMssqlDbJobConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**finishRecovery** | **Boolean** | A Boolean value that determines the recovery option to use during database restore. When this value is &#39;true&#39;, the database is restored using the RECOVERY option and is fully functional at the end of the restore operation. When this value is &#39;false&#39;, the database is restored using the NORECOVERY option and remains in recovering mode at the end of the restore operation. | [optional] 
**maxDataStreams** | **Number** | Maximum number of parallel data streams that can be used to copy data to the target system. | [optional] 
**recoveryPoint** | [**MssqlRecoveryPoint**](MssqlRecoveryPoint.md) |  | 


