

# NodeAffinity

Specifies the NodeAffinity key, values, and affinity operator according to [shared sole tenant node group affinities](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**key** | **String** | Key for NodeAffinity. |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | Operator for NodeAffinity. |  [optional] |
|**values** | **List&lt;String&gt;** | Values for NodeAffinity. |  [optional] |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| OPERATOR_UNSPECIFIED | &quot;OPERATOR_UNSPECIFIED&quot; |
| IN | &quot;IN&quot; |
| NOT_IN | &quot;NOT_IN&quot; |



