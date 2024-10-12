# RubrikRestApi.MssqlHostConfiguration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableDatabaseBatchSnapshots** | [**HostConfigurationPropertyEnabled**](HostConfigurationPropertyEnabled.md) |  | [optional] 
**enableGroupFetch** | [**HostConfigurationPropertyEnabled**](HostConfigurationPropertyEnabled.md) |  | [optional] 
**enableVdi** | [**HostConfigurationPropertyEnabled**](HostConfigurationPropertyEnabled.md) |  | [optional] 
**enableVdiDb** | [**HostConfigurationPropertyEnabled**](HostConfigurationPropertyEnabled.md) |  | [optional] 
**fileRestoreReadParallelism** | **Number** | Number of concurrent read requests for restoring a file from the Rubrik cluster to a remote host. | [optional] 
**fileRestoreWriteParallelism** | **Number** | Number of concurrent write requests for restoring a file from the Rubrik cluster to a remote host. | [optional] 
**fileTransferParallelism** | **Number** | Number of concurrent requests for transferring a file from a remote host to the Rubrik cluster. | [optional] 
**mssqlDefaultMaxDataStreamsPerDatabase** | **Number** | The default value for maximum number of data streams per database. | [optional] 
**physicalHostDatabaseRestoreThrottleMaxRefCount** | **Number** | The maximum number of concurrent database restore job running on a host. | [optional] 
**physicalHostLogBackupThrottleMaxRefCount** | **Number** | Maximum number of concurrent SQL Server log backup jobs per physical host. | [optional] 
**throttlePhysicalHostMaxRefCount** | **Number** | Maximum number of concurrent snapshots per physical host. | [optional] 


