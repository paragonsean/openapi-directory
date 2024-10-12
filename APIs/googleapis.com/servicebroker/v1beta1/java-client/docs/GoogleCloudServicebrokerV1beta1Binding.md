

# GoogleCloudServicebrokerV1beta1Binding

Describes the binding.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bindResource** | **Map&lt;String, Object&gt;** | A JSON object that contains data for platform resources associated with the binding to be created. |  [optional] |
|**bindingId** | **String** | The id of the binding. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required. |  [optional] |
|**createTime** | **String** | Output only. Timestamp for when the binding was created. |  [optional] |
|**deploymentName** | **String** | Output only. String containing the Deployment Manager deployment name that was created for this binding, |  [optional] |
|**parameters** | **Map&lt;String, Object&gt;** | Configuration options for the service binding. |  [optional] |
|**planId** | **String** | The ID of the plan. See &#x60;Service&#x60; and &#x60;Plan&#x60; resources for details. Maximum length is 64, GUID recommended. Required. |  [optional] |
|**resourceName** | **String** | Output only. The resource name of the binding, e.g. projects/project_id/brokers/broker_id/service_instances/instance_id/bindings/binding_id. |  [optional] |
|**serviceId** | **String** | The id of the service. Must be a valid identifier of a service contained in the list from a &#x60;ListServices()&#x60; call. Maximum length is 64, GUID recommended. Required. |  [optional] |



