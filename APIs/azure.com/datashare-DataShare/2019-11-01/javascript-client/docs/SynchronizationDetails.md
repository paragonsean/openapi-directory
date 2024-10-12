# DataShareManagementClient.SynchronizationDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataSetId** | **String** | Id of data set | [optional] [readonly] 
**dataSetType** | **String** | Type of the data set | [optional] [readonly] 
**durationMs** | **Number** | Duration of data set level copy | [optional] [readonly] 
**endTime** | **Date** | End time of data set level copy | [optional] [readonly] 
**filesRead** | **Number** | The number of files read from the source data set | [optional] [readonly] 
**filesWritten** | **Number** | The number of files written into the sink data set | [optional] [readonly] 
**message** | **String** | Error message if any | [optional] [readonly] 
**name** | **String** | Name of the data set | [optional] [readonly] 
**rowsCopied** | **Number** | The number of files copied into the sink data set | [optional] [readonly] 
**rowsRead** | **Number** | The number of rows read from the source data set. | [optional] [readonly] 
**sizeRead** | **Number** | The size of the data read from the source data set in bytes | [optional] [readonly] 
**sizeWritten** | **Number** | The size of the data written into the sink data set in bytes | [optional] [readonly] 
**startTime** | **Date** | Start time of data set level copy | [optional] [readonly] 
**status** | **String** | Raw Status | [optional] [readonly] 
**vCore** | **Number** | The vCore units consumed for the data set synchronization | [optional] [readonly] 



## Enum: DataSetTypeEnum


* `Blob` (value: `"Blob"`)

* `Container` (value: `"Container"`)

* `BlobFolder` (value: `"BlobFolder"`)

* `AdlsGen2FileSystem` (value: `"AdlsGen2FileSystem"`)

* `AdlsGen2Folder` (value: `"AdlsGen2Folder"`)

* `AdlsGen2File` (value: `"AdlsGen2File"`)

* `AdlsGen1Folder` (value: `"AdlsGen1Folder"`)

* `AdlsGen1File` (value: `"AdlsGen1File"`)

* `KustoCluster` (value: `"KustoCluster"`)

* `KustoDatabase` (value: `"KustoDatabase"`)

* `SqlDBTable` (value: `"SqlDBTable"`)

* `SqlDWTable` (value: `"SqlDWTable"`)




