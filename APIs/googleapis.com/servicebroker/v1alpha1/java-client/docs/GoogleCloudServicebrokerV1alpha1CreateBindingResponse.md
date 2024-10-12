

# GoogleCloudServicebrokerV1alpha1CreateBindingResponse

Response for the `CreateBinding()` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**credentials** | **Map&lt;String, Object&gt;** | Credentials to use the binding. |  [optional] |
|**description** | **String** | Used to communicate description of the response. Usually for non-standard error codes. https://github.com/openservicebrokerapi/servicebroker/blob/master/spec.md#service-broker-errors |  [optional] |
|**operation** | **String** | If broker executes operation asynchronously, this is the operation ID that can be polled to check the completion status of said operation. This broker always executes all create/delete operations asynchronously. |  [optional] |
|**routeServiceUrl** | **String** | A URL to which the platform may proxy requests for the address sent with bind_resource.route |  [optional] |
|**syslogDrainUrl** | **String** | From where to read system logs. |  [optional] |
|**volumeMounts** | **List&lt;Map&lt;String, Object&gt;&gt;** | An array of configuration for mounting volumes. |  [optional] |



