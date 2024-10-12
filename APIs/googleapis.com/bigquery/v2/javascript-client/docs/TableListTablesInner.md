# BigQueryApi.TableListTablesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clustering** | [**Clustering**](Clustering.md) |  | [optional] 
**creationTime** | **String** | Output only. The time when this table was created, in milliseconds since the epoch. | [optional] [readonly] 
**expirationTime** | **String** | The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed. | [optional] 
**friendlyName** | **String** | The user-friendly name for this table. | [optional] 
**id** | **String** | An opaque ID of the table. | [optional] 
**kind** | **String** | The resource type. | [optional] 
**labels** | **{String: String}** | The labels associated with this table. You can use these to organize and group your tables. | [optional] 
**rangePartitioning** | [**RangePartitioning**](RangePartitioning.md) |  | [optional] 
**requirePartitionFilter** | **Boolean** | Optional. If set to true, queries including this table must specify a partition filter. This filter is used for partition elimination. | [optional] [default to false]
**tableReference** | [**TableReference**](TableReference.md) |  | [optional] 
**timePartitioning** | [**TimePartitioning**](TimePartitioning.md) |  | [optional] 
**type** | **String** | The type of table. | [optional] 
**view** | [**TableListTablesInnerView**](TableListTablesInnerView.md) |  | [optional] 


