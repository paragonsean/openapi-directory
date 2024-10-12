

# ADLSGen2FolderDataSetMappingProperties

ADLS Gen 2 folder data set mapping property bag.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataSetId** | **String** | The id of the source data set. |  |
|**dataSetMappingStatus** | [**DataSetMappingStatusEnum**](#DataSetMappingStatusEnum) | Gets the status of the data set mapping. |  [optional] [readonly] |
|**fileSystem** | **String** | File system to which the folder belongs. |  |
|**folderPath** | **String** | Folder path within the file system. |  |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the data set mapping. |  [optional] [readonly] |
|**resourceGroup** | **String** | Resource group of storage account. |  |
|**storageAccountName** | **String** | Storage account name of the source data set. |  |
|**subscriptionId** | **String** | Subscription id of storage account. |  |



## Enum: DataSetMappingStatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;Ok&quot; |
| BROKEN | &quot;Broken&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| MOVING | &quot;Moving&quot; |
| FAILED | &quot;Failed&quot; |



