# CloudMonitoringApi.MonitoredResource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **{String: String}** | Required. Values for all of the labels listed in the associated monitored resource descriptor. For example, Compute Engine VM instances use the labels \&quot;project_id\&quot;, \&quot;instance_id\&quot;, and \&quot;zone\&quot;. | [optional] 
**type** | **String** | Required. The monitored resource type. This field must match the type field of a MonitoredResourceDescriptor object. For example, the type of a Compute Engine VM instance is gce_instance. For a list of types, see Monitoring resource types (https://cloud.google.com/monitoring/api/resources) and Logging resource types (https://cloud.google.com/logging/docs/api/v2/resource-list). | [optional] 


