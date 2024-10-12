# VertexAiApi.GoogleCloudAiplatformV1beta1ResourcePool

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoscalingSpec** | [**GoogleCloudAiplatformV1beta1ResourcePoolAutoscalingSpec**](GoogleCloudAiplatformV1beta1ResourcePoolAutoscalingSpec.md) |  | [optional] 
**diskSpec** | [**GoogleCloudAiplatformV1beta1DiskSpec**](GoogleCloudAiplatformV1beta1DiskSpec.md) |  | [optional] 
**id** | **String** | Immutable. The unique ID in a PersistentResource for referring to this resource pool. User can specify it if necessary. Otherwise, it&#39;s generated automatically. | [optional] 
**machineSpec** | [**GoogleCloudAiplatformV1beta1MachineSpec**](GoogleCloudAiplatformV1beta1MachineSpec.md) |  | [optional] 
**replicaCount** | **String** | Optional. The total number of machines to use for this resource pool. | [optional] 
**usedReplicaCount** | **String** | Output only. The number of machines currently in use by training jobs for this resource pool. Will replace idle_replica_count. | [optional] [readonly] 


