

# GoogleCloudAiplatformV1beta1SearchNearestEntitiesRequest

The request message for FeatureOnlineStoreService.SearchNearestEntities.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**query** | [**GoogleCloudAiplatformV1beta1NearestNeighborQuery**](GoogleCloudAiplatformV1beta1NearestNeighborQuery.md) |  |  [optional] |
|**returnFullEntity** | **Boolean** | Optional. If set to true, the full entities (including all vector values and metadata) of the nearest neighbors are returned; otherwise only entity id of the nearest neighbors will be returned. Note that returning full entities will significantly increase the latency and cost of the query. |  [optional] |



