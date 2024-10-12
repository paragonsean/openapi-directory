# ServiceBroker.GoogleCloudServicebrokerV1beta1CreateBindingResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | **{String: Object}** | Credentials to use the binding. | [optional] 
**description** | **String** | Used to communicate description of the response. Usually for non-standard error codes. https://github.com/openservicebrokerapi/servicebroker/blob/master/spec.md#service-broker-errors | [optional] 
**operation** | **String** | If broker executes operation asynchronously, this is the operation ID that can be polled to check the completion status of said operation. This broker always executes all create/delete operations asynchronously. | [optional] 
**routeServiceUrl** | **String** | A URL to which the platform may proxy requests for the address sent with bind_resource.route | [optional] 
**syslogDrainUrl** | **String** | From where to read system logs. | [optional] 
**volumeMounts** | **[{String: Object}]** | An array of configuration for mounting volumes. | [optional] 


