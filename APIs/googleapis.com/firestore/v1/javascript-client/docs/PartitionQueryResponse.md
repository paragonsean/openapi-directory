# CloudFirestoreApi.PartitionQueryResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nextPageToken** | **String** | A page token that may be used to request an additional set of results, up to the number specified by &#x60;partition_count&#x60; in the PartitionQuery request. If blank, there are no more results. | [optional] 
**partitions** | [**[Cursor]**](Cursor.md) | Partition results. Each partition is a split point that can be used by RunQuery as a starting or end point for the query results. The RunQuery requests must be made with the same query supplied to this PartitionQuery request. The partition cursors will be ordered according to same ordering as the results of the query supplied to PartitionQuery. For example, if a PartitionQuery request returns partition cursors A and B, running the following three queries will return the entire result set of the original query: * query, end_at A * query, start_at A, end_at B * query, start_at B An empty result may indicate that the query has too few results to be partitioned, or that the query is not yet supported for partitioning. | [optional] 


