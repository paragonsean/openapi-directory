# ApplicationMigrationService.UpdateReplicationConfigurationTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arn** | **String** | Update replication configuration template ARN request. | [optional] 
**associateDefaultSecurityGroup** | **Boolean** | Update replication configuration template associate default Application Migration Service Security group request. | [optional] 
**bandwidthThrottling** | **Number** | Update replication configuration template bandwidth throttling request. | [optional] 
**createPublicIP** | **Boolean** | Update replication configuration template create Public IP request. | [optional] 
**dataPlaneRouting** | **String** | Update replication configuration template data plane routing request. | [optional] 
**defaultLargeStagingDiskType** | **String** | Update replication configuration template use default large Staging Disk type request. | [optional] 
**ebsEncryption** | **String** | Update replication configuration template EBS encryption request. | [optional] 
**ebsEncryptionKeyArn** | **String** | Update replication configuration template EBS encryption key ARN request. | [optional] 
**replicationConfigurationTemplateID** | **String** | Update replication configuration template template ID request. | 
**replicationServerInstanceType** | **String** | Update replication configuration template Replication Server instance type request. | [optional] 
**replicationServersSecurityGroupsIDs** | **[String]** | Update replication configuration template Replication Server Security groups IDs request. | [optional] 
**stagingAreaSubnetId** | **String** | Update replication configuration template Staging Area subnet ID request. | [optional] 
**stagingAreaTags** | **{String: String}** | Update replication configuration template Staging Area Tags request. | [optional] 
**useDedicatedReplicationServer** | **Boolean** | Update replication configuration template use dedicated Replication Server request. | [optional] 
**useFipsEndpoint** | **Boolean** | Update replication configuration template use Fips Endpoint request. | [optional] 



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




