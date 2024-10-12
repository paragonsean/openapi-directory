# SiteRecoveryManagementClient.VMwareDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentCount** | **String** | The number of source and target servers configured to talk to this CS. | [optional] 
**agentVersion** | **String** | The agent Version. | [optional] 
**availableMemoryInBytes** | **Number** | The available memory. | [optional] 
**availableSpaceInBytes** | **Number** | The available space. | [optional] 
**cpuLoad** | **String** | The percentage of the CPU load. | [optional] 
**cpuLoadStatus** | **String** | The CPU load status. | [optional] 
**csServiceStatus** | **String** | The CS service status. | [optional] 
**databaseServerLoad** | **String** | The database server load. | [optional] 
**databaseServerLoadStatus** | **String** | The database server load status. | [optional] 
**hostName** | **String** | The host name. | [optional] 
**ipAddress** | **String** | The IP address. | [optional] 
**lastHeartbeat** | **Date** | The last heartbeat received from CS server. | [optional] 
**masterTargetServers** | [**[MasterTargetServer]**](MasterTargetServer.md) | The list of Master Target servers associated with the fabric. | [optional] 
**memoryUsageStatus** | **String** | The memory usage status. | [optional] 
**processServerCount** | **String** | The number of process servers. | [optional] 
**processServers** | [**[ProcessServer]**](ProcessServer.md) | The list of Process Servers associated with the fabric. | [optional] 
**protectedServers** | **String** | The number of protected servers. | [optional] 
**psTemplateVersion** | **String** | PS template version. | [optional] 
**replicationPairCount** | **String** | The number of replication pairs configured in this CS. | [optional] 
**runAsAccounts** | [**[RunAsAccount]**](RunAsAccount.md) | The list of run as accounts created on the server. | [optional] 
**spaceUsageStatus** | **String** | The space usage status. | [optional] 
**sslCertExpiryDate** | **Date** | CS SSL cert expiry date. | [optional] 
**sslCertExpiryRemainingDays** | **Number** | CS SSL cert expiry date. | [optional] 
**systemLoad** | **String** | The percentage of the system load. | [optional] 
**systemLoadStatus** | **String** | The system load status. | [optional] 
**totalMemoryInBytes** | **Number** | The total memory. | [optional] 
**totalSpaceInBytes** | **Number** | The total space. | [optional] 
**versionStatus** | **String** | Version status | [optional] 
**webLoad** | **String** | The web load. | [optional] 
**webLoadStatus** | **String** | The web load status. | [optional] 


