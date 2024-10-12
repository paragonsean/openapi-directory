

# TimeSeriesCondition

Creates a subset of items within an attribute that are modified. For example, you can use this operation to create a subset of items that cost $5 or less. To do this, you specify <code>\"AttributeName\": \"price\"</code>, <code>\"AttributeValue\": \"5\"</code>, and <code>\"Condition\": \"LESS_THAN\"</code>. Pair this operation with the <a>Action</a> operation within the <a>CreateWhatIfForecastRequest$TimeSeriesTransformations</a> operation to define how the attribute is modified.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeName** | [**String**](String.md) |  |  |
|**attributeValue** | [**String**](String.md) |  |  |
|**condition** | [**Condition**](Condition.md) |  |  |



