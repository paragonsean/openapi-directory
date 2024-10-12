

# GoogleCloudServicebrokerV1beta1GetBindingResponse

Response for the `GetBinding()` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**credentials** | **Map&lt;String, Object&gt;** | Credentials to use the binding. |  [optional] |
|**deploymentName** | **String** | String containing the Deployment Manager deployment name that was created for this binding, |  [optional] |
|**description** | **String** | Used to communicate description of the response. Usually for non-standard error codes. https://github.com/openservicebrokerapi/servicebroker/blob/master/spec.md#service-broker-errors |  [optional] |
|**resourceName** | **String** | Output only. The resource name of the binding, e.g. projects/project_id/brokers/broker_id/service_instances/instance_id/bindings/binding_id. |  [optional] |
|**routeServiceUrl** | **String** | A URL to which the platform may proxy requests for the address sent with bind_resource.route |  [optional] |
|**syslogDrainUrl** | **String** | From where to read system logs. |  [optional] |
|**volumeMounts** | **List&lt;Map&lt;String, Object&gt;&gt;** | An array of configurations for mounting volumes. |  [optional] |



