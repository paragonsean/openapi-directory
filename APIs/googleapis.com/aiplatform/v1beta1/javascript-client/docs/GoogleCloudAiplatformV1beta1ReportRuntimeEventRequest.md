# VertexAiApi.GoogleCloudAiplatformV1beta1ReportRuntimeEventRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventDetails** | **{String: String}** | Optional. The details of the request for debug. | [optional] 
**eventType** | **String** | Required. The type of the event. | [optional] 
**internalOsServiceStateInstance** | [**[GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance]**](GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance.md) | The details of the internal os service states. | [optional] 
**internalOsServiceStateInstances** | [**[GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance]**](GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance.md) | Optional. The details of the internal os service states. | [optional] 
**vmToken** | **String** | Required. The VM identity token (a JWT) for authenticating the VM. https://cloud.google.com/compute/docs/instances/verifying-instance-identity | [optional] 



## Enum: EventTypeEnum


* `EVENT_TYPE_UNSPECIFIED` (value: `"EVENT_TYPE_UNSPECIFIED"`)

* `HEARTBEAT` (value: `"HEARTBEAT"`)

* `IDLE` (value: `"IDLE"`)




