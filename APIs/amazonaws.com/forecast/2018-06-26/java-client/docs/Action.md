

# Action

Defines the modifications that you are making to an attribute for a what-if forecast. For example, you can use this operation to create a what-if forecast that investigates a 10% off sale on all shoes. To do this, you specify <code>\"AttributeName\": \"shoes\"</code>, <code>\"Operation\": \"MULTIPLY\"</code>, and <code>\"Value\": \"0.90\"</code>. Pair this operation with the <a>TimeSeriesCondition</a> operation within the <a>CreateWhatIfForecastRequest$TimeSeriesTransformations</a> operation to define a subset of attribute items that are modified.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributeName** | [**String**](String.md) |  |  |
|**operation** | [**Operation**](Operation.md) |  |  |
|**value** | [**Double**](Double.md) |  |  |



