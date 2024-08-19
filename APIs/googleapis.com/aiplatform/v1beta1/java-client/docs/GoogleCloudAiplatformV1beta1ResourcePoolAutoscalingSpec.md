

# GoogleCloudAiplatformV1beta1ResourcePoolAutoscalingSpec

The min/max number of replicas allowed if enabling autoscaling

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxReplicaCount** | **String** | Optional. max replicas in the node pool, must be ≥ replica_count and &gt; min_replica_count or will throw error |  [optional] |
|**minReplicaCount** | **String** | Optional. min replicas in the node pool, must be ≤ replica_count and &lt; max_replica_count or will throw error |  [optional] |



