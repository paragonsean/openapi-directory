

# ClusterGetProperties

The properties of cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterDefinition** | [**ClusterDefinition**](ClusterDefinition.md) |  |  |
|**clusterState** | **String** | The state of the cluster. |  [optional] |
|**clusterVersion** | **String** | The version of the cluster. |  [optional] |
|**computeProfile** | [**ComputeProfile**](ComputeProfile.md) |  |  [optional] |
|**connectivityEndpoints** | [**List&lt;ConnectivityEndpoint&gt;**](ConnectivityEndpoint.md) | The list of connectivity endpoints. |  [optional] |
|**createdDate** | **String** | The date on which the cluster was created. |  [optional] |
|**diskEncryptionProperties** | [**DiskEncryptionProperties**](DiskEncryptionProperties.md) |  |  [optional] |
|**errors** | [**List&lt;Errors&gt;**](Errors.md) | The list of errors. |  [optional] |
|**kafkaRestProperties** | [**KafkaRestProperties**](KafkaRestProperties.md) |  |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | The type of operating system. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state, which only appears in the response. |  [optional] |
|**quotaInfo** | [**QuotaInfo**](QuotaInfo.md) |  |  [optional] |
|**securityProfile** | [**SecurityProfile**](SecurityProfile.md) |  |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | The cluster tier. |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| IN_PROGRESS | &quot;InProgress&quot; |
| FAILED | &quot;Failed&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| CANCELED | &quot;Canceled&quot; |
| DELETING | &quot;Deleting&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |



