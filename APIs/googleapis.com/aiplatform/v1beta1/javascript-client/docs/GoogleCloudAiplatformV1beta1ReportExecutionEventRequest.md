# VertexAiApi.GoogleCloudAiplatformV1beta1ReportExecutionEventRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventType** | **String** | Required. The type of the event. | [optional] 
**status** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 
**vmToken** | **String** | Required. The VM identity token (a JWT) for authenticating the VM. https://cloud.google.com/compute/docs/instances/verifying-instance-identity | [optional] 



## Enum: EventTypeEnum


* `EVENT_TYPE_UNSPECIFIED` (value: `"EVENT_TYPE_UNSPECIFIED"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `DONE` (value: `"DONE"`)

* `FAILED` (value: `"FAILED"`)




