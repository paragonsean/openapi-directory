

# BlobMappingProperties

Azure storage Blob data set mapping property bag.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerName** | **String** | Container that has the file path. |  |
|**dataSetId** | **String** | The id of the source data set. |  |
|**dataSetMappingStatus** | [**DataSetMappingStatusEnum**](#DataSetMappingStatusEnum) | Gets the status of the data set mapping. |  [optional] [readonly] |
|**filePath** | **String** | File path within the source data set |  |
|**outputType** | [**OutputTypeEnum**](#OutputTypeEnum) | File output type |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state of the data set mapping. |  [optional] [readonly] |
|**resourceGroup** | **String** | Resource group of storage account. |  |
|**storageAccountName** | **String** | Storage account name of the source data set. |  |
|**subscriptionId** | **String** | Subscription id of storage account. |  |



## Enum: DataSetMappingStatusEnum

| Name | Value |
|---- | -----|
| OK | &quot;Ok&quot; |
| BROKEN | &quot;Broken&quot; |



## Enum: OutputTypeEnum

| Name | Value |
|---- | -----|
| CSV | &quot;Csv&quot; |
| PARQUET | &quot;Parquet&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| CREATING | &quot;Creating&quot; |
| DELETING | &quot;Deleting&quot; |
| MOVING | &quot;Moving&quot; |
| FAILED | &quot;Failed&quot; |



