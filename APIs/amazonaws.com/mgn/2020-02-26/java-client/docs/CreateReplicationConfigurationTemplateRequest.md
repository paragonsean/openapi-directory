

# CreateReplicationConfigurationTemplateRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**associateDefaultSecurityGroup** | **Boolean** | Request to associate the default Application Migration Service Security group with the Replication Settings template. |  |
|**bandwidthThrottling** | **Integer** | Request to configure bandwidth throttling during Replication Settings template creation. |  |
|**createPublicIP** | **Boolean** | Request to create Public IP during Replication Settings template creation. |  |
|**dataPlaneRouting** | [**DataPlaneRoutingEnum**](#DataPlaneRoutingEnum) | Request to configure data plane routing during Replication Settings template creation. |  |
|**defaultLargeStagingDiskType** | [**DefaultLargeStagingDiskTypeEnum**](#DefaultLargeStagingDiskTypeEnum) | Request to configure the default large staging disk EBS volume type during Replication Settings template creation. |  |
|**ebsEncryption** | [**EbsEncryptionEnum**](#EbsEncryptionEnum) | Request to configure EBS encryption during Replication Settings template creation. |  |
|**ebsEncryptionKeyArn** | **String** | Request to configure an EBS encryption key during Replication Settings template creation. |  [optional] |
|**replicationServerInstanceType** | **String** | Request to configure the Replication Server instance type during Replication Settings template creation. |  |
|**replicationServersSecurityGroupsIDs** | **List&lt;String&gt;** | Request to configure the Replication Server Security group ID during Replication Settings template creation. |  |
|**stagingAreaSubnetId** | **String** | Request to configure the Staging Area subnet ID during Replication Settings template creation. |  |
|**stagingAreaTags** | **Map&lt;String, String&gt;** | Request to configure Staging Area tags during Replication Settings template creation. |  |
|**tags** | **Map&lt;String, String&gt;** | Request to configure tags during Replication Settings template creation. |  [optional] |
|**useDedicatedReplicationServer** | **Boolean** | Request to use Dedicated Replication Servers during Replication Settings template creation. |  |
|**useFipsEndpoint** | **Boolean** | Request to use Fips Endpoint during Replication Settings template creation. |  [optional] |



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



