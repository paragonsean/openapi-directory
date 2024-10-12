# CloudDataprocApi.GkeNodePoolTarget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nodePool** | **String** | Required. The target GKE node pool. Format: &#39;projects/{project}/locations/{location}/clusters/{cluster}/nodePools/{node_pool}&#39; | [optional] 
**nodePoolConfig** | [**GkeNodePoolConfig**](GkeNodePoolConfig.md) |  | [optional] 
**roles** | **[String]** | Required. The roles associated with the GKE node pool. | [optional] 



## Enum: [RolesEnum]


* `ROLE_UNSPECIFIED` (value: `"ROLE_UNSPECIFIED"`)

* `DEFAULT` (value: `"DEFAULT"`)

* `CONTROLLER` (value: `"CONTROLLER"`)

* `SPARK_DRIVER` (value: `"SPARK_DRIVER"`)

* `SPARK_EXECUTOR` (value: `"SPARK_EXECUTOR"`)




