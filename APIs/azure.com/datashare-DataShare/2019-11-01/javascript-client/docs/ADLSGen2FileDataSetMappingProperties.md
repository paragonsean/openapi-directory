# DataShareManagementClient.ADLSGen2FileDataSetMappingProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataSetId** | **String** | The id of the source data set. | 
**dataSetMappingStatus** | **String** | Gets the status of the data set mapping. | [optional] [readonly] 
**filePath** | **String** | File path within the file system. | 
**fileSystem** | **String** | File system to which the file belongs. | 
**outputType** | **String** | Type of output file | [optional] 
**provisioningState** | **String** | Provisioning state of the data set mapping. | [optional] [readonly] 
**resourceGroup** | **String** | Resource group of storage account. | 
**storageAccountName** | **String** | Storage account name of the source data set. | 
**subscriptionId** | **String** | Subscription id of storage account. | 



## Enum: DataSetMappingStatusEnum


* `Ok` (value: `"Ok"`)

* `Broken` (value: `"Broken"`)





## Enum: OutputTypeEnum


* `Csv` (value: `"Csv"`)

* `Parquet` (value: `"Parquet"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Moving` (value: `"Moving"`)

* `Failed` (value: `"Failed"`)




