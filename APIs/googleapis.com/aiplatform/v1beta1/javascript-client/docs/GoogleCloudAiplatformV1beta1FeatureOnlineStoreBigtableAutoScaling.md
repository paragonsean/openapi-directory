# VertexAiApi.GoogleCloudAiplatformV1beta1FeatureOnlineStoreBigtableAutoScaling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpuUtilizationTarget** | **Number** | Optional. A percentage of the cluster&#39;s CPU capacity. Can be from 10% to 80%. When a cluster&#39;s CPU utilization exceeds the target that you have set, Bigtable immediately adds nodes to the cluster. When CPU utilization is substantially lower than the target, Bigtable removes nodes. If not set will default to 50%. | [optional] 
**maxNodeCount** | **Number** | Required. The maximum number of nodes to scale up to. Must be greater than or equal to min_node_count, and less than or equal to 10 times of &#39;min_node_count&#39;. | [optional] 
**minNodeCount** | **Number** | Required. The minimum number of nodes to scale down to. Must be greater than or equal to 1. | [optional] 


