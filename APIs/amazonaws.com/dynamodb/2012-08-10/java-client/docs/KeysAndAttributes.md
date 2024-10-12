

# KeysAndAttributes

<p>Represents a set of primary keys and, for each key, the attributes to retrieve from the table.</p> <p>For each primary key, you must provide <i>all</i> of the key attributes. For example, with a simple primary key, you only need to provide the partition key. For a composite primary key, you must provide <i>both</i> the partition key and the sort key.</p>

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**keys** | [**List**](List.md) |  |  |
|**attributesToGet** | [**List**](List.md) |  |  [optional] |
|**consistentRead** | [**Boolean**](Boolean.md) |  |  [optional] |
|**projectionExpression** | [**String**](String.md) |  |  [optional] |
|**expressionAttributeNames** | [**Map**](Map.md) |  |  [optional] |



