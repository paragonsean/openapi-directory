# HdInsightManagementClient.ClusterGetProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterDefinition** | [**ClusterDefinition**](ClusterDefinition.md) |  | 
**clusterState** | **String** | The state of the cluster. | [optional] 
**clusterVersion** | **String** | The version of the cluster. | [optional] 
**computeProfile** | [**ComputeProfile**](ComputeProfile.md) |  | [optional] 
**connectivityEndpoints** | [**[ConnectivityEndpoint]**](ConnectivityEndpoint.md) | The list of connectivity endpoints. | [optional] 
**createdDate** | **String** | The date on which the cluster was created. | [optional] 
**diskEncryptionProperties** | [**DiskEncryptionProperties**](DiskEncryptionProperties.md) |  | [optional] 
**errors** | [**[Errors]**](Errors.md) | The list of errors. | [optional] 
**kafkaRestProperties** | [**KafkaRestProperties**](KafkaRestProperties.md) |  | [optional] 
**osType** | **String** | The type of operating system. | [optional] 
**provisioningState** | **String** | The provisioning state, which only appears in the response. | [optional] 
**quotaInfo** | [**QuotaInfo**](QuotaInfo.md) |  | [optional] 
**securityProfile** | [**SecurityProfile**](SecurityProfile.md) |  | [optional] 
**tier** | **String** | The cluster tier. | [optional] 



## Enum: OsTypeEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)





## Enum: ProvisioningStateEnum


* `InProgress` (value: `"InProgress"`)

* `Failed` (value: `"Failed"`)

* `Succeeded` (value: `"Succeeded"`)

* `Canceled` (value: `"Canceled"`)

* `Deleting` (value: `"Deleting"`)





## Enum: TierEnum


* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)




