# CloudLoggingApi.MonitoredResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **{String: String}** | Required. Values for all of the labels listed in the associated monitored resource descriptor. For example, Compute Engine VM instances use the labels \&quot;project_id\&quot;, \&quot;instance_id\&quot;, and \&quot;zone\&quot;. | [optional] 
**type** | **String** | Required. The monitored resource type. This field must match the type field of a MonitoredResourceDescriptor object. For example, the type of a Compute Engine VM instance is gce_instance. Some descriptors include the service name in the type; for example, the type of a Datastream stream is datastream.googleapis.com/Stream. | [optional] 


