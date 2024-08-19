# VertexAiApi.GoogleCloudAiplatformV1beta1NearestNeighborQuery

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedding** | [**GoogleCloudAiplatformV1beta1NearestNeighborQueryEmbedding**](GoogleCloudAiplatformV1beta1NearestNeighborQueryEmbedding.md) |  | [optional] 
**entityId** | **String** | Optional. The entity id whose similar entities should be searched for. If embedding is set, search will use embedding instead of entity_id. | [optional] 
**neighborCount** | **Number** | Optional. The number of similar entities to be retrieved from feature view for each query. | [optional] 
**parameters** | [**GoogleCloudAiplatformV1beta1NearestNeighborQueryParameters**](GoogleCloudAiplatformV1beta1NearestNeighborQueryParameters.md) |  | [optional] 
**perCrowdingAttributeNeighborCount** | **Number** | Optional. Crowding is a constraint on a neighbor list produced by nearest neighbor search requiring that no more than sper_crowding_attribute_neighbor_count of the k neighbors returned have the same value of crowding_attribute. It&#39;s used for improving result diversity. | [optional] 
**stringFilters** | [**[GoogleCloudAiplatformV1beta1NearestNeighborQueryStringFilter]**](GoogleCloudAiplatformV1beta1NearestNeighborQueryStringFilter.md) | Optional. The list of string filters. | [optional] 


