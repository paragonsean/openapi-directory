# VertexAiApi.GoogleCloudAiplatformV1beta1FeaturestoreOnlineServingConfigScaling

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpuUtilizationTarget** | **Number** | Optional. The cpu utilization that the Autoscaler should be trying to achieve. This number is on a scale from 0 (no utilization) to 100 (total utilization), and is limited between 10 and 80. When a cluster&#39;s CPU utilization exceeds the target that you have set, Bigtable immediately adds nodes to the cluster. When CPU utilization is substantially lower than the target, Bigtable removes nodes. If not set or set to 0, default to 50. | [optional] 
**maxNodeCount** | **Number** | The maximum number of nodes to scale up to. Must be greater than min_node_count, and less than or equal to 10 times of &#39;min_node_count&#39;. | [optional] 
**minNodeCount** | **Number** | Required. The minimum number of nodes to scale down to. Must be greater than or equal to 1. | [optional] 


