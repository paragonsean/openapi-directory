

# UpdateReplicationConfigurationTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | **String** | Update replication configuration template ARN request. |  [optional] |
|**associateDefaultSecurityGroup** | **Boolean** | Update replication configuration template associate default Application Migration Service Security group request. |  [optional] |
|**bandwidthThrottling** | **Integer** | Update replication configuration template bandwidth throttling request. |  [optional] |
|**createPublicIP** | **Boolean** | Update replication configuration template create Public IP request. |  [optional] |
|**dataPlaneRouting** | [**DataPlaneRoutingEnum**](#DataPlaneRoutingEnum) | Update replication configuration template data plane routing request. |  [optional] |
|**defaultLargeStagingDiskType** | [**DefaultLargeStagingDiskTypeEnum**](#DefaultLargeStagingDiskTypeEnum) | Update replication configuration template use default large Staging Disk type request. |  [optional] |
|**ebsEncryption** | [**EbsEncryptionEnum**](#EbsEncryptionEnum) | Update replication configuration template EBS encryption request. |  [optional] |
|**ebsEncryptionKeyArn** | **String** | Update replication configuration template EBS encryption key ARN request. |  [optional] |
|**replicationConfigurationTemplateID** | **String** | Update replication configuration template template ID request. |  |
|**replicationServerInstanceType** | **String** | Update replication configuration template Replication Server instance type request. |  [optional] |
|**replicationServersSecurityGroupsIDs** | **List&lt;String&gt;** | Update replication configuration template Replication Server Security groups IDs request. |  [optional] |
|**stagingAreaSubnetId** | **String** | Update replication configuration template Staging Area subnet ID request. |  [optional] |
|**stagingAreaTags** | **Map&lt;String, String&gt;** | Update replication configuration template Staging Area Tags request. |  [optional] |
|**useDedicatedReplicationServer** | **Boolean** | Update replication configuration template use dedicated Replication Server request. |  [optional] |
|**useFipsEndpoint** | **Boolean** | Update replication configuration template use Fips Endpoint request. |  [optional] |



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



