# ApplicationMigrationService.CreateReplicationConfigurationTemplateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**associateDefaultSecurityGroup** | **Boolean** | Request to associate the default Application Migration Service Security group with the Replication Settings template. | 
**bandwidthThrottling** | **Number** | Request to configure bandwidth throttling during Replication Settings template creation. | 
**createPublicIP** | **Boolean** | Request to create Public IP during Replication Settings template creation. | 
**dataPlaneRouting** | **String** | Request to configure data plane routing during Replication Settings template creation. | 
**defaultLargeStagingDiskType** | **String** | Request to configure the default large staging disk EBS volume type during Replication Settings template creation. | 
**ebsEncryption** | **String** | Request to configure EBS encryption during Replication Settings template creation. | 
**ebsEncryptionKeyArn** | **String** | Request to configure an EBS encryption key during Replication Settings template creation. | [optional] 
**replicationServerInstanceType** | **String** | Request to configure the Replication Server instance type during Replication Settings template creation. | 
**replicationServersSecurityGroupsIDs** | **[String]** | Request to configure the Replication Server Security group ID during Replication Settings template creation. | 
**stagingAreaSubnetId** | **String** | Request to configure the Staging Area subnet ID during Replication Settings template creation. | 
**stagingAreaTags** | **{String: String}** | Request to configure Staging Area tags during Replication Settings template creation. | 
**tags** | **{String: String}** | Request to configure tags during Replication Settings template creation. | [optional] 
**useDedicatedReplicationServer** | **Boolean** | Request to use Dedicated Replication Servers during Replication Settings template creation. | 
**useFipsEndpoint** | **Boolean** | Request to use Fips Endpoint during Replication Settings template creation. | [optional] 



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




