# DataShareManagementClient.KustoClusterDataSetMappingProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataSetId** | **String** | The id of the source data set. | 
**dataSetMappingStatus** | **String** | Gets the status of the data set mapping. | [optional] [readonly] 
**kustoClusterResourceId** | **String** | Resource id of the sink kusto cluster. | 
**location** | **String** | Location of the sink kusto cluster. | [optional] [readonly] 
**provisioningState** | **String** | Provisioning state of the data set mapping. | [optional] [readonly] 



## Enum: DataSetMappingStatusEnum


* `Ok` (value: `"Ok"`)

* `Broken` (value: `"Broken"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Moving` (value: `"Moving"`)

* `Failed` (value: `"Failed"`)




