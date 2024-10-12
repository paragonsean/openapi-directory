# CloudMonitoringApi.MonitoredResourceMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**systemLabels** | **{String: Object}** | Output only. Values for predefined system metadata labels. System labels are a kind of metadata extracted by Google, including \&quot;machine_image\&quot;, \&quot;vpc\&quot;, \&quot;subnet_id\&quot;, \&quot;security_group\&quot;, \&quot;name\&quot;, etc. System label values can be only strings, Boolean values, or a list of strings. For example: { \&quot;name\&quot;: \&quot;my-test-instance\&quot;, \&quot;security_group\&quot;: [\&quot;a\&quot;, \&quot;b\&quot;, \&quot;c\&quot;], \&quot;spot_instance\&quot;: false }  | [optional] 
**userLabels** | **{String: String}** | Output only. A map of user-defined metadata labels. | [optional] 


