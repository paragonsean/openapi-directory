

# ClusterCreateProperties

The cluster create parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clusterDefinition** | [**ClusterDefinition**](ClusterDefinition.md) |  |  [optional] |
|**clusterVersion** | **String** | The version of the cluster. |  [optional] |
|**computeProfile** | [**ComputeProfile**](ComputeProfile.md) |  |  [optional] |
|**diskEncryptionProperties** | [**DiskEncryptionProperties**](DiskEncryptionProperties.md) |  |  [optional] |
|**kafkaRestProperties** | [**KafkaRestProperties**](KafkaRestProperties.md) |  |  [optional] |
|**osType** | [**OsTypeEnum**](#OsTypeEnum) | The type of operating system. |  [optional] |
|**securityProfile** | [**SecurityProfile**](SecurityProfile.md) |  |  [optional] |
|**storageProfile** | [**StorageProfile**](StorageProfile.md) |  |  [optional] |
|**tier** | [**TierEnum**](#TierEnum) | The cluster tier. |  [optional] |



## Enum: OsTypeEnum

| Name | Value |
|---- | -----|
| WINDOWS | &quot;Windows&quot; |
| LINUX | &quot;Linux&quot; |



## Enum: TierEnum

| Name | Value |
|---- | -----|
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |



