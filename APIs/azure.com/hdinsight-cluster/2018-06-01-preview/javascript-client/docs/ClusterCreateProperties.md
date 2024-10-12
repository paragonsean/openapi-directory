# HdInsightManagementClient.ClusterCreateProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusterDefinition** | [**ClusterDefinition**](ClusterDefinition.md) |  | [optional] 
**clusterVersion** | **String** | The version of the cluster. | [optional] 
**computeProfile** | [**ComputeProfile**](ComputeProfile.md) |  | [optional] 
**diskEncryptionProperties** | [**DiskEncryptionProperties**](DiskEncryptionProperties.md) |  | [optional] 
**kafkaRestProperties** | [**KafkaRestProperties**](KafkaRestProperties.md) |  | [optional] 
**osType** | **String** | The type of operating system. | [optional] 
**securityProfile** | [**SecurityProfile**](SecurityProfile.md) |  | [optional] 
**storageProfile** | [**StorageProfile**](StorageProfile.md) |  | [optional] 
**tier** | **String** | The cluster tier. | [optional] 



## Enum: OsTypeEnum


* `Windows` (value: `"Windows"`)

* `Linux` (value: `"Linux"`)





## Enum: TierEnum


* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)




