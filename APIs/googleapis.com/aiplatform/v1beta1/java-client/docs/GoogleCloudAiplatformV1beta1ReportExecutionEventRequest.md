

# GoogleCloudAiplatformV1beta1ReportExecutionEventRequest

Request message for NotebookInternalService.ReportExecutionEvent.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventType** | [**EventTypeEnum**](#EventTypeEnum) | Required. The type of the event. |  [optional] |
|**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  |  [optional] |
|**vmToken** | **String** | Required. The VM identity token (a JWT) for authenticating the VM. https://cloud.google.com/compute/docs/instances/verifying-instance-identity |  [optional] |



## Enum: EventTypeEnum

| Name | Value |
|---- | -----|
| EVENT_TYPE_UNSPECIFIED | &quot;EVENT_TYPE_UNSPECIFIED&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| DONE | &quot;DONE&quot; |
| FAILED | &quot;FAILED&quot; |



