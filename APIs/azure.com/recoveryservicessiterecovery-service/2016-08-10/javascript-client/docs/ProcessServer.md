# SiteRecoveryManagementClient.ProcessServer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentVersion** | **String** | The version of the scout component on the server. | [optional] 
**availableMemoryInBytes** | **Number** | The available memory. | [optional] 
**availableSpaceInBytes** | **Number** | The available space. | [optional] 
**cpuLoad** | **String** | The percentage of the CPU load. | [optional] 
**cpuLoadStatus** | **String** | The CPU load status. | [optional] 
**friendlyName** | **String** | The Process Server&#39;s friendly name. | [optional] 
**hostId** | **String** | The agent generated Id. | [optional] 
**id** | **String** | The Process Server Id. | [optional] 
**ipAddress** | **String** | The IP address of the server. | [optional] 
**lastHeartbeat** | **Date** | The last heartbeat received from the server. | [optional] 
**machineCount** | **String** | The servers configured with this PS. | [optional] 
**memoryUsageStatus** | **String** | The memory usage status. | [optional] 
**mobilityServiceUpdates** | [**[MobilityServiceUpdate]**](MobilityServiceUpdate.md) | The list of the mobility service updates available on the Process Server. | [optional] 
**osType** | **String** | The OS type of the server. | [optional] 
**osVersion** | **String** | OS Version of the process server. Note: This will get populated if user has CS version greater than 9.12.0.0. | [optional] 
**psServiceStatus** | **String** | The PS service status. | [optional] 
**replicationPairCount** | **String** | The number of replication pairs configured in this PS. | [optional] 
**spaceUsageStatus** | **String** | The space usage status. | [optional] 
**sslCertExpiryDate** | **Date** | The PS SSL cert expiry date. | [optional] 
**sslCertExpiryRemainingDays** | **Number** | CS SSL cert expiry date. | [optional] 
**systemLoad** | **String** | The percentage of the system load. | [optional] 
**systemLoadStatus** | **String** | The system load status. | [optional] 
**totalMemoryInBytes** | **Number** | The total memory. | [optional] 
**totalSpaceInBytes** | **Number** | The total space. | [optional] 
**versionStatus** | **String** | Version status | [optional] 


