

# TargetRegion

Describes the target region information.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The name of the region. |  |
|**regionalReplicaCount** | **Integer** | The number of replicas of the Image Version to be created per region. This property is updatable. |  [optional] |
|**storageAccountType** | [**StorageAccountTypeEnum**](#StorageAccountTypeEnum) | Specifies the storage account type to be used to store the image. This property is not updatable. |  [optional] |



## Enum: StorageAccountTypeEnum

| Name | Value |
|---- | -----|
| LRS | &quot;Standard_LRS&quot; |
| ZRS | &quot;Standard_ZRS&quot; |



