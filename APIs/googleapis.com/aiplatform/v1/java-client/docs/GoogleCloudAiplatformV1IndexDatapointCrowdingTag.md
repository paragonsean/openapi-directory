

# GoogleCloudAiplatformV1IndexDatapointCrowdingTag

Crowding tag is a constraint on a neighbor list produced by nearest neighbor search requiring that no more than some value k' of the k neighbors returned have the same value of crowding_attribute.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**crowdingAttribute** | **String** | The attribute value used for crowding. The maximum number of neighbors to return per crowding attribute value (per_crowding_attribute_num_neighbors) is configured per-query. This field is ignored if per_crowding_attribute_num_neighbors is larger than the total number of neighbors to return for a given query. |  [optional] |



