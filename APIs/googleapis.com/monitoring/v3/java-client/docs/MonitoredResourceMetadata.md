

# MonitoredResourceMetadata

Auxiliary metadata for a MonitoredResource object. MonitoredResource objects contain the minimum set of information to uniquely identify a monitored resource instance. There is some other useful auxiliary metadata. Monitoring and Logging use an ingestion pipeline to extract metadata for cloud resources of all types, and store the metadata in this message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**systemLabels** | **Map&lt;String, Object&gt;** | Output only. Values for predefined system metadata labels. System labels are a kind of metadata extracted by Google, including \&quot;machine_image\&quot;, \&quot;vpc\&quot;, \&quot;subnet_id\&quot;, \&quot;security_group\&quot;, \&quot;name\&quot;, etc. System label values can be only strings, Boolean values, or a list of strings. For example: { \&quot;name\&quot;: \&quot;my-test-instance\&quot;, \&quot;security_group\&quot;: [\&quot;a\&quot;, \&quot;b\&quot;, \&quot;c\&quot;], \&quot;spot_instance\&quot;: false }  |  [optional] |
|**userLabels** | **Map&lt;String, String&gt;** | Output only. A map of user-defined metadata labels. |  [optional] |



