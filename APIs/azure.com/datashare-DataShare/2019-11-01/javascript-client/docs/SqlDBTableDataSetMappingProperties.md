# DataShareManagementClient.SqlDBTableDataSetMappingProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataSetId** | **String** | The id of the source data set. | 
**dataSetMappingStatus** | **String** | Gets the status of the data set mapping. | [optional] [readonly] 
**databaseName** | **String** | DatabaseName name of the sink data set | 
**provisioningState** | **String** | Provisioning state of the data set mapping. | [optional] [readonly] 
**schemaName** | **String** | Schema of the table. Default value is dbo. | 
**sqlServerResourceId** | **String** | Resource id of SQL server | 
**tableName** | **String** | SQL DB table name. | 



## Enum: DataSetMappingStatusEnum


* `Ok` (value: `"Ok"`)

* `Broken` (value: `"Broken"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Moving` (value: `"Moving"`)

* `Failed` (value: `"Failed"`)




