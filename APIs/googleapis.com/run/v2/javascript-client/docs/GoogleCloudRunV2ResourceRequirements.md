# CloudRunAdminApi.GoogleCloudRunV2ResourceRequirements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpuIdle** | **Boolean** | Determines whether CPU is only allocated during requests (true by default). However, if ResourceRequirements is set, the caller must explicitly set this field to true to preserve the default behavior. | [optional] 
**limits** | **{String: String}** | Only &#x60;memory&#x60; and &#x60;cpu&#x60; keys in the map are supported. Notes: * The only supported values for CPU are &#39;1&#39;, &#39;2&#39;, &#39;4&#39;, and &#39;8&#39;. Setting 4 CPU requires at least 2Gi of memory. For more information, go to https://cloud.google.com/run/docs/configuring/cpu. * For supported &#39;memory&#39; values and syntax, go to https://cloud.google.com/run/docs/configuring/memory-limits | [optional] 
**startupCpuBoost** | **Boolean** | Determines whether CPU should be boosted on startup of a new container instance above the requested CPU threshold, this can help reduce cold-start latency. | [optional] 


