# VertexAiApi.GoogleCloudAiplatformV1beta1FindNeighborsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployedIndexId** | **String** | The ID of the DeployedIndex that will serve the request. This request is sent to a specific IndexEndpoint, as per the IndexEndpoint.network. That IndexEndpoint also has IndexEndpoint.deployed_indexes, and each such index has a DeployedIndex.id field. The value of the field below must equal one of the DeployedIndex.id fields of the IndexEndpoint that is being called for this request. | [optional] 
**queries** | [**[GoogleCloudAiplatformV1beta1FindNeighborsRequestQuery]**](GoogleCloudAiplatformV1beta1FindNeighborsRequestQuery.md) | The list of queries. | [optional] 
**returnFullDatapoint** | **Boolean** | If set to true, the full datapoints (including all vector values and restricts) of the nearest neighbors are returned. Note that returning full datapoint will significantly increase the latency and cost of the query. | [optional] 


