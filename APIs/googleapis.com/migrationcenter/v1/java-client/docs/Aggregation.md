

# Aggregation

Message describing an aggregation. The message includes the aggregation type, parameters, and the field on which to perform the aggregation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Object** | Object count. |  [optional] |
|**field** | **String** | The name of the field on which to aggregate. |  [optional] |
|**frequency** | **Object** | Frequency distribution of all field values. |  [optional] |
|**histogram** | [**AggregationHistogram**](AggregationHistogram.md) |  |  [optional] |
|**sum** | **Object** | Sum of field values. |  [optional] |



