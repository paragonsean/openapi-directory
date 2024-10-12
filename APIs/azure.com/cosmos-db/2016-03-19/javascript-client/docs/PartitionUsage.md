# CosmosDb.PartitionUsage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partitionId** | **String** | The partition id (GUID identifier) of the usages. | [optional] [readonly] 
**partitionKeyRangeId** | **String** | The partition key range id (integer identifier) of the usages. | [optional] [readonly] 
**currentValue** | **Number** | Current value for this metric | [optional] [readonly] 
**limit** | **Number** | Maximum value for this metric | [optional] [readonly] 
**name** | [**MetricName**](MetricName.md) |  | [optional] 
**quotaPeriod** | **String** | The quota period used to summarize the usage values. | [optional] [readonly] 
**unit** | [**UnitType**](UnitType.md) |  | [optional] 


