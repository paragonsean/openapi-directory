

# GkeNodePoolTarget

GKE node pools that Dataproc workloads run on.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**nodePool** | **String** | Required. The target GKE node pool. Format: &#39;projects/{project}/locations/{location}/clusters/{cluster}/nodePools/{node_pool}&#39; |  [optional] |
|**nodePoolConfig** | [**GkeNodePoolConfig**](GkeNodePoolConfig.md) |  |  [optional] |
|**roles** | [**List&lt;RolesEnum&gt;**](#List&lt;RolesEnum&gt;) | Required. The roles associated with the GKE node pool. |  [optional] |



## Enum: List&lt;RolesEnum&gt;

| Name | Value |
|---- | -----|
| ROLE_UNSPECIFIED | &quot;ROLE_UNSPECIFIED&quot; |
| DEFAULT | &quot;DEFAULT&quot; |
| CONTROLLER | &quot;CONTROLLER&quot; |
| SPARK_DRIVER | &quot;SPARK_DRIVER&quot; |
| SPARK_EXECUTOR | &quot;SPARK_EXECUTOR&quot; |



