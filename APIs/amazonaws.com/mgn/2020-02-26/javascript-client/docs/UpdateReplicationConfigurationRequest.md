# ApplicationMigrationService.UpdateReplicationConfigurationRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountID** | **String** | Update replication configuration Account ID request. | [optional] 
**associateDefaultSecurityGroup** | **Boolean** | Update replication configuration associate default Application Migration Service Security group request. | [optional] 
**bandwidthThrottling** | **Number** | Update replication configuration bandwidth throttling request. | [optional] 
**createPublicIP** | **Boolean** | Update replication configuration create Public IP request. | [optional] 
**dataPlaneRouting** | **String** | Update replication configuration data plane routing request. | [optional] 
**defaultLargeStagingDiskType** | **String** | Update replication configuration use default large Staging Disk type request. | [optional] 
**ebsEncryption** | **String** | Update replication configuration EBS encryption request. | [optional] 
**ebsEncryptionKeyArn** | **String** | Update replication configuration EBS encryption key ARN request. | [optional] 
**name** | **String** | Update replication configuration name request. | [optional] 
**replicatedDisks** | [**[ReplicationConfigurationReplicatedDisk]**](ReplicationConfigurationReplicatedDisk.md) | Update replication configuration replicated disks request. | [optional] 
**replicationServerInstanceType** | **String** | Update replication configuration Replication Server instance type request. | [optional] 
**replicationServersSecurityGroupsIDs** | **[String]** | Update replication configuration Replication Server Security Groups IDs request. | [optional] 
**sourceServerID** | **String** | Update replication configuration Source Server ID request. | 
**stagingAreaSubnetId** | **String** | Update replication configuration Staging Area subnet request. | [optional] 
**stagingAreaTags** | **{String: String}** | Update replication configuration Staging Area Tags request. | [optional] 
**useDedicatedReplicationServer** | **Boolean** | Update replication configuration use dedicated Replication Server request. | [optional] 
**useFipsEndpoint** | **Boolean** | Update replication configuration use Fips Endpoint. | [optional] 



## Enum: DataPlaneRoutingEnum


* `PRIVATE_IP` (value: `"PRIVATE_IP"`)

* `PUBLIC_IP` (value: `"PUBLIC_IP"`)





## Enum: DefaultLargeStagingDiskTypeEnum


* `GP2` (value: `"GP2"`)

* `ST1` (value: `"ST1"`)

* `GP3` (value: `"GP3"`)





## Enum: EbsEncryptionEnum


* `DEFAULT` (value: `"DEFAULT"`)

* `CUSTOM` (value: `"CUSTOM"`)




