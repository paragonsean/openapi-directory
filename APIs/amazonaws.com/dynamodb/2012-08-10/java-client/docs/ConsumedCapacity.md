

# ConsumedCapacity

The capacity units consumed by an operation. The data returned includes the total provisioned throughput consumed, along with statistics for the table and any indexes involved in the operation. <code>ConsumedCapacity</code> is only returned if the request asked for it. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughputIntro.html\">Provisioned Throughput</a> in the <i>Amazon DynamoDB Developer Guide</i>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**tableName** | [**String**](String.md) |  |  [optional] |
|**capacityUnits** | [**Double**](Double.md) |  |  [optional] |
|**readCapacityUnits** | [**Double**](Double.md) |  |  [optional] |
|**writeCapacityUnits** | [**Double**](Double.md) |  |  [optional] |
|**table** | [**ConsumedCapacityTable**](ConsumedCapacityTable.md) |  |  [optional] |
|**localSecondaryIndexes** | [**Map**](Map.md) |  |  [optional] |
|**globalSecondaryIndexes** | [**Map**](Map.md) |  |  [optional] |



