# ConnectorsApi.RuntimeConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conndSubscription** | **String** | Output only. Pub/Sub subscription for connd to receive message. E.g. projects/{project-id}/subscriptions/{topic-id} | [optional] [readonly] 
**conndTopic** | **String** | Output only. Pub/Sub topic for connd to send message. E.g. projects/{project-id}/topics/{topic-id} | [optional] [readonly] 
**controlPlaneSubscription** | **String** | Output only. Pub/Sub subscription for control plane to receive message. E.g. projects/{project-id}/subscriptions/{topic-id} | [optional] [readonly] 
**controlPlaneTopic** | **String** | Output only. Pub/Sub topic for control plne to send message. communication. E.g. projects/{project-id}/topics/{topic-id} | [optional] [readonly] 
**locationId** | **String** | Output only. location_id of the runtime location. E.g. \&quot;us-west1\&quot;. | [optional] [readonly] 
**name** | **String** | Output only. Name of the runtimeConfig resource. Format: projects/{project}/locations/{location}/runtimeConfig | [optional] [readonly] 
**runtimeEndpoint** | **String** | Output only. The endpoint of the connectors runtime ingress. | [optional] [readonly] 
**schemaGcsBucket** | **String** | Output only. The Cloud Storage bucket that stores connector&#39;s schema reports. | [optional] [readonly] 
**serviceDirectory** | **String** | Output only. The name of the Service Directory service name. | [optional] [readonly] 
**state** | **String** | Output only. The state of the location. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `INACTIVE` (value: `"INACTIVE"`)

* `ACTIVATING` (value: `"ACTIVATING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `CREATING` (value: `"CREATING"`)

* `DELETING` (value: `"DELETING"`)

* `UPDATING` (value: `"UPDATING"`)




