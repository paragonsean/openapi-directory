

# GoogleCloudAiplatformV1beta1NearestNeighborQueryParameters

Parameters that can be overrided in each query to tune query latency and recall.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**approximateNeighborCandidates** | **Integer** | Optional. The number of neighbors to find via approximate search before exact reordering is performed; if set, this value must be &gt; neighbor_count. |  [optional] |
|**leafNodesSearchFraction** | **Double** | Optional. The fraction of the number of leaves to search, set at query time allows user to tune search performance. This value increase result in both search accuracy and latency increase. The value should be between 0.0 and 1.0. |  [optional] |



