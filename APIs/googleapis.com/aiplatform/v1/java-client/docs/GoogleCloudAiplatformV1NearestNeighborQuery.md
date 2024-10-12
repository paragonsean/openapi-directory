

# GoogleCloudAiplatformV1NearestNeighborQuery

A query to find a number of similar entities.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**embedding** | [**GoogleCloudAiplatformV1NearestNeighborQueryEmbedding**](GoogleCloudAiplatformV1NearestNeighborQueryEmbedding.md) |  |  [optional] |
|**entityId** | **String** | Optional. The entity id whose similar entities should be searched for. If embedding is set, search will use embedding instead of entity_id. |  [optional] |
|**neighborCount** | **Integer** | Optional. The number of similar entities to be retrieved from feature view for each query. |  [optional] |
|**parameters** | [**GoogleCloudAiplatformV1NearestNeighborQueryParameters**](GoogleCloudAiplatformV1NearestNeighborQueryParameters.md) |  |  [optional] |
|**perCrowdingAttributeNeighborCount** | **Integer** | Optional. Crowding is a constraint on a neighbor list produced by nearest neighbor search requiring that no more than sper_crowding_attribute_neighbor_count of the k neighbors returned have the same value of crowding_attribute. It&#39;s used for improving result diversity. |  [optional] |
|**stringFilters** | [**List&lt;GoogleCloudAiplatformV1NearestNeighborQueryStringFilter&gt;**](GoogleCloudAiplatformV1NearestNeighborQueryStringFilter.md) | Optional. The list of string filters. |  [optional] |



