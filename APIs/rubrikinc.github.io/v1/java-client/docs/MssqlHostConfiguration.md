

# MssqlHostConfiguration


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableDatabaseBatchSnapshots** | **HostConfigurationPropertyEnabled** |  |  [optional] |
|**enableGroupFetch** | **HostConfigurationPropertyEnabled** |  |  [optional] |
|**enableVdi** | **HostConfigurationPropertyEnabled** |  |  [optional] |
|**enableVdiDb** | **HostConfigurationPropertyEnabled** |  |  [optional] |
|**fileRestoreReadParallelism** | **Integer** | Number of concurrent read requests for restoring a file from the Rubrik cluster to a remote host. |  [optional] |
|**fileRestoreWriteParallelism** | **Integer** | Number of concurrent write requests for restoring a file from the Rubrik cluster to a remote host. |  [optional] |
|**fileTransferParallelism** | **Integer** | Number of concurrent requests for transferring a file from a remote host to the Rubrik cluster. |  [optional] |
|**mssqlDefaultMaxDataStreamsPerDatabase** | **Integer** | The default value for maximum number of data streams per database. |  [optional] |
|**physicalHostDatabaseRestoreThrottleMaxRefCount** | **Integer** | The maximum number of concurrent database restore job running on a host. |  [optional] |
|**physicalHostLogBackupThrottleMaxRefCount** | **Integer** | Maximum number of concurrent SQL Server log backup jobs per physical host. |  [optional] |
|**throttlePhysicalHostMaxRefCount** | **Integer** | Maximum number of concurrent snapshots per physical host. |  [optional] |



