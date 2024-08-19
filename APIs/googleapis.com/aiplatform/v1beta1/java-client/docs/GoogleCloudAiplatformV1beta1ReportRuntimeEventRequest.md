

# GoogleCloudAiplatformV1beta1ReportRuntimeEventRequest

Request message for NotebookInternalService.ReportRuntimeEvent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventDetails** | **Map&lt;String, String&gt;** | Optional. The details of the request for debug. |  [optional] |
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | Required. The type of the event. |  [optional] |
|**internalOsServiceStateInstance** | [**List&lt;GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance&gt;**](GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance.md) | The details of the internal os service states. |  [optional] |
|**internalOsServiceStateInstances** | [**List&lt;GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance&gt;**](GoogleCloudAiplatformV1beta1InternalOsServiceStateInstance.md) | Optional. The details of the internal os service states. |  [optional] |
|**vmToken** | **String** | Required. The VM identity token (a JWT) for authenticating the VM. https://cloud.google.com/compute/docs/instances/verifying-instance-identity |  [optional] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| EVENT_TYPE_UNSPECIFIED | &quot;EVENT_TYPE_UNSPECIFIED&quot; |
| HEARTBEAT | &quot;HEARTBEAT&quot; |
| IDLE | &quot;IDLE&quot; |



