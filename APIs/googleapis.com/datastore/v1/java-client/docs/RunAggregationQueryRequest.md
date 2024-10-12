

# RunAggregationQueryRequest

The request for Datastore.RunAggregationQuery.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationQuery** | [**AggregationQuery**](AggregationQuery.md) |  |  [optional] |
|**databaseId** | **String** | The ID of the database against which to make the request. &#39;(default)&#39; is not allowed; please use empty string &#39;&#39; to refer the default database. |  [optional] |
|**gqlQuery** | [**GqlQuery**](GqlQuery.md) |  |  [optional] |
|**partitionId** | [**PartitionId**](PartitionId.md) |  |  [optional] |
|**readOptions** | [**ReadOptions**](ReadOptions.md) |  |  [optional] |



