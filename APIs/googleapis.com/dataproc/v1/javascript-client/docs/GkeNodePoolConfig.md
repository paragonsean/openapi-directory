# CloudDataprocApi.GkeNodePoolConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscaling** | [**GkeNodePoolAutoscalingConfig**](GkeNodePoolAutoscalingConfig.md) |  | [optional] 
**config** | [**GkeNodeConfig**](GkeNodeConfig.md) |  | [optional] 
**locations** | **[String]** | Optional. The list of Compute Engine zones (https://cloud.google.com/compute/docs/zones#available) where node pool nodes associated with a Dataproc on GKE virtual cluster will be located.Note: All node pools associated with a virtual cluster must be located in the same region as the virtual cluster, and they must be located in the same zone within that region.If a location is not specified during node pool creation, Dataproc on GKE will choose the zone. | [optional] 


