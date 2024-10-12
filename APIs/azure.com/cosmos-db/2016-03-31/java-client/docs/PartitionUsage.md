

# PartitionUsage

The partition level usage data for a usage request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**partitionId** | **String** | The partition id (GUID identifier) of the usages. |  [optional] [readonly] |
|**partitionKeyRangeId** | **String** | The partition key range id (integer identifier) of the usages. |  [optional] [readonly] |
|**currentValue** | **Long** | Current value for this metric |  [optional] [readonly] |
|**limit** | **Long** | Maximum value for this metric |  [optional] [readonly] |
|**name** | [**MetricName**](MetricName.md) |  |  [optional] |
|**quotaPeriod** | **String** | The quota period used to summarize the usage values. |  [optional] [readonly] |
|**unit** | **UnitType** |  |  [optional] |



