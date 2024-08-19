

# GoogleCloudServicebrokerV1alpha1Binding

Describes the binding.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bindResource** | **Map&lt;String, Object&gt;** | A JSON object that contains data for platform resources associated with the binding to be created. |  [optional] |
|**bindingId** | **String** | The id of the binding. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required. |  [optional] |
|**createTime** | **String** | Output only. Timestamp for when the binding was created. |  [optional] |
|**parameters** | **Map&lt;String, Object&gt;** | Configuration options for the service binding. |  [optional] |
|**planId** | **String** | The ID of the plan. See &#x60;Service&#x60; and &#x60;Plan&#x60; resources for details. Maximum length is 64, GUID recommended. Required. |  [optional] |
|**serviceId** | **String** | The id of the service. Must be a valid identifier of a service contained in the list from a &#x60;ListServices()&#x60; call. Maximum length is 64, GUID recommended. Required. |  [optional] |



