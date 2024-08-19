

# GoogleCloudServicebrokerV1beta1Plan

Plan message describes a Service Plan.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bindable** | **Boolean** | Specifies whether instances of the service can be bound to applications. If not specified, &#x60;Service.bindable&#x60; will be presumed. |  [optional] |
|**description** | **String** | Textual description of the plan. Optional. |  [optional] |
|**free** | **Boolean** | Whether the service is free. |  [optional] |
|**id** | **String** | ID is a globally unique identifier used to uniquely identify the plan. User must make no presumption about the format of this field. |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** | A list of metadata for a service offering. Metadata is an arbitrary JSON object. |  [optional] |
|**name** | **String** | User friendly name of the plan. The name must be globally unique within GCP project. Note, which is different from (\&quot;This must be globally unique within a platform marketplace\&quot;). |  [optional] |
|**schemas** | **Map&lt;String, Object&gt;** | Schema definitions for service instances and bindings for the plan. |  [optional] |



