

# GoogleCloudAiplatformV1FindNeighborsRequestQuery

A query to find a number of the nearest neighbors (most similar vectors) of a vector.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approximateNeighborCount** | **Integer** | The number of neighbors to find via approximate search before exact reordering is performed. If not set, the default value from scam config is used; if set, this value must be &gt; 0. |  [optional] |
|**datapoint** | [**GoogleCloudAiplatformV1IndexDatapoint**](GoogleCloudAiplatformV1IndexDatapoint.md) |  |  [optional] |
|**fractionLeafNodesToSearchOverride** | **Double** | The fraction of the number of leaves to search, set at query time allows user to tune search performance. This value increase result in both search accuracy and latency increase. The value should be between 0.0 and 1.0. If not set or set to 0.0, query uses the default value specified in NearestNeighborSearchConfig.TreeAHConfig.fraction_leaf_nodes_to_search. |  [optional] |
|**neighborCount** | **Integer** | The number of nearest neighbors to be retrieved from database for each query. If not set, will use the default from the service configuration (https://cloud.google.com/vertex-ai/docs/matching-engine/configuring-indexes#nearest-neighbor-search-config). |  [optional] |
|**perCrowdingAttributeNeighborCount** | **Integer** | Crowding is a constraint on a neighbor list produced by nearest neighbor search requiring that no more than some value k&#39; of the k neighbors returned have the same value of crowding_attribute. It&#39;s used for improving result diversity. This field is the maximum number of matches with the same crowding tag. |  [optional] |



