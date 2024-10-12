

# RuntimeConfig

RuntimeConfig is the singleton resource of each location. It includes generic resource configs consumed by control plane and runtime plane like: pub/sub topic/subscription resource name, Cloud Storage location storing schema etc.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**conndSubscription** | **String** | Output only. Pub/Sub subscription for connd to receive message. E.g. projects/{project-id}/subscriptions/{topic-id} |  [optional] [readonly] |
|**conndTopic** | **String** | Output only. Pub/Sub topic for connd to send message. E.g. projects/{project-id}/topics/{topic-id} |  [optional] [readonly] |
|**controlPlaneSubscription** | **String** | Output only. Pub/Sub subscription for control plane to receive message. E.g. projects/{project-id}/subscriptions/{topic-id} |  [optional] [readonly] |
|**controlPlaneTopic** | **String** | Output only. Pub/Sub topic for control plne to send message. communication. E.g. projects/{project-id}/topics/{topic-id} |  [optional] [readonly] |
|**locationId** | **String** | Output only. location_id of the runtime location. E.g. \&quot;us-west1\&quot;. |  [optional] [readonly] |
|**name** | **String** | Output only. Name of the runtimeConfig resource. Format: projects/{project}/locations/{location}/runtimeConfig |  [optional] [readonly] |
|**runtimeEndpoint** | **String** | Output only. The endpoint of the connectors runtime ingress. |  [optional] [readonly] |
|**schemaGcsBucket** | **String** | Output only. The Cloud Storage bucket that stores connector&#39;s schema reports. |  [optional] [readonly] |
|**serviceDirectory** | **String** | Output only. The name of the Service Directory service name. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the location. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| INACTIVE | &quot;INACTIVE&quot; |
| ACTIVATING | &quot;ACTIVATING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| CREATING | &quot;CREATING&quot; |
| DELETING | &quot;DELETING&quot; |
| UPDATING | &quot;UPDATING&quot; |



