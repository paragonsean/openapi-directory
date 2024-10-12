

# CloudRunConfig

Configuration options for the Cloud Run feature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disabled** | **Boolean** | Whether Cloud Run addon is enabled for this cluster. |  [optional] |
|**loadBalancerType** | [**LoadBalancerTypeEnum**](#LoadBalancerTypeEnum) | Which load balancer type is installed for Cloud Run. |  [optional] |



## Enum: LoadBalancerTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;LOAD_BALANCER_TYPE_UNSPECIFIED&quot; |
| EXTERNAL | &quot;LOAD_BALANCER_TYPE_EXTERNAL&quot; |
| INTERNAL | &quot;LOAD_BALANCER_TYPE_INTERNAL&quot; |



