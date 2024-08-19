

# GoogleCloudServicebrokerV1alpha1ListBindingsResponse

The response for the `ListBindings()` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bindings** | [**List&lt;GoogleCloudServicebrokerV1alpha1Binding&gt;**](GoogleCloudServicebrokerV1alpha1Binding.md) | The list of the bindings in the instance. |  [optional] |
|**description** | **String** | Used to communicate description of the response. Usually for non-standard error codes. https://github.com/openservicebrokerapi/servicebroker/blob/master/spec.md#service-broker-errors |  [optional] |
|**nextPageToken** | **String** | This token allows you to get the next page of results for list requests. If the number of results is larger than &#x60;pageSize&#x60;, use the &#x60;nextPageToken&#x60; as a value for the query parameter &#x60;pageToken&#x60; in the next list request. Subsequent list requests will have their own &#x60;nextPageToken&#x60; to continue paging through the results |  [optional] |



