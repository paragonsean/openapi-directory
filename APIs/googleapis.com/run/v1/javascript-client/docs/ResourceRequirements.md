# CloudRunAdminApi.ResourceRequirements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limits** | **{String: String}** | Limits describes the maximum amount of compute resources allowed. Only &#39;cpu&#39; and &#39;memory&#39; keys are supported. * For supported &#39;cpu&#39; values, go to https://cloud.google.com/run/docs/configuring/cpu. * For supported &#39;memory&#39; values and syntax, go to https://cloud.google.com/run/docs/configuring/memory-limits | [optional] 
**requests** | **{String: String}** | Requests describes the minimum amount of compute resources required. Only &#x60;cpu&#x60; and &#x60;memory&#x60; are supported. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. * For supported &#39;cpu&#39; values, go to https://cloud.google.com/run/docs/configuring/cpu. * For supported &#39;memory&#39; values and syntax, go to https://cloud.google.com/run/docs/configuring/memory-limits | [optional] 


