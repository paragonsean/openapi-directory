# ServiceBroker.GoogleCloudServicebrokerV1alpha1GetBindingResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | **{String: Object}** | Credentials to use the binding. | [optional] 
**description** | **String** | Used to communicate description of the response. Usually for non-standard error codes. https://github.com/openservicebrokerapi/servicebroker/blob/master/spec.md#service-broker-errors | [optional] 
**routeServiceUrl** | **String** | A URL to which the platform may proxy requests for the address sent with bind_resource.route | [optional] 
**syslogDrainUrl** | **String** | From where to read system logs. | [optional] 
**volumeMounts** | **[{String: Object}]** | An array of configuration for mounting volumes. | [optional] 


