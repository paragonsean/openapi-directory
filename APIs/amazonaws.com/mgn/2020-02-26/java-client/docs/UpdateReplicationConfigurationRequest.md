

# UpdateReplicationConfigurationRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountID** | **String** | Update replication configuration Account ID request. |  [optional] |
|**associateDefaultSecurityGroup** | **Boolean** | Update replication configuration associate default Application Migration Service Security group request. |  [optional] |
|**bandwidthThrottling** | **Integer** | Update replication configuration bandwidth throttling request. |  [optional] |
|**createPublicIP** | **Boolean** | Update replication configuration create Public IP request. |  [optional] |
|**dataPlaneRouting** | [**DataPlaneRoutingEnum**](#DataPlaneRoutingEnum) | Update replication configuration data plane routing request. |  [optional] |
|**defaultLargeStagingDiskType** | [**DefaultLargeStagingDiskTypeEnum**](#DefaultLargeStagingDiskTypeEnum) | Update replication configuration use default large Staging Disk type request. |  [optional] |
|**ebsEncryption** | [**EbsEncryptionEnum**](#EbsEncryptionEnum) | Update replication configuration EBS encryption request. |  [optional] |
|**ebsEncryptionKeyArn** | **String** | Update replication configuration EBS encryption key ARN request. |  [optional] |
|**name** | **String** | Update replication configuration name request. |  [optional] |
|**replicatedDisks** | [**List&lt;ReplicationConfigurationReplicatedDisk&gt;**](ReplicationConfigurationReplicatedDisk.md) | Update replication configuration replicated disks request. |  [optional] |
|**replicationServerInstanceType** | **String** | Update replication configuration Replication Server instance type request. |  [optional] |
|**replicationServersSecurityGroupsIDs** | **List&lt;String&gt;** | Update replication configuration Replication Server Security Groups IDs request. |  [optional] |
|**sourceServerID** | **String** | Update replication configuration Source Server ID request. |  |
|**stagingAreaSubnetId** | **String** | Update replication configuration Staging Area subnet request. |  [optional] |
|**stagingAreaTags** | **Map&lt;String, String&gt;** | Update replication configuration Staging Area Tags request. |  [optional] |
|**useDedicatedReplicationServer** | **Boolean** | Update replication configuration use dedicated Replication Server request. |  [optional] |
|**useFipsEndpoint** | **Boolean** | Update replication configuration use Fips Endpoint. |  [optional] |



## Enum: DataPlaneRoutingEnum

| Name | Value |
|---- | -----|
| PRIVATE_IP | &quot;PRIVATE_IP&quot; |
| PUBLIC_IP | &quot;PUBLIC_IP&quot; |



## Enum: DefaultLargeStagingDiskTypeEnum

| Name | Value |
|---- | -----|
| GP2 | &quot;GP2&quot; |
| ST1 | &quot;ST1&quot; |
| GP3 | &quot;GP3&quot; |



## Enum: EbsEncryptionEnum

| Name | Value |
|---- | -----|
| DEFAULT | &quot;DEFAULT&quot; |
| CUSTOM | &quot;CUSTOM&quot; |



