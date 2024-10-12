

# ListStreamsRequestStreamNameCondition

Specifies the condition that streams must satisfy to be returned when you list streams (see the <code>ListStreams</code> API). A condition has a comparison operation and a value. Currently, you can specify only the <code>BEGINS_WITH</code> operator, which finds streams whose names start with a given prefix. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**comparisonOperator** | [**ComparisonOperator**](ComparisonOperator.md) |  |  [optional] |
|**comparisonValue** | [**String**](String.md) |  |  [optional] |



