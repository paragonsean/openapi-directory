# ApigeeApi.GoogleCloudApigeeV1ComputeEnvironmentScoresRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**[GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilter]**](GoogleCloudApigeeV1ComputeEnvironmentScoresRequestFilter.md) | Optional. Filters are used to filter scored components. Return all the components if no filter is mentioned. Example: [{ \&quot;scorePath\&quot;: \&quot;/org@myorg/envgroup@myenvgroup/env@myenv/proxies/proxy@myproxy/source\&quot; }, { \&quot;scorePath\&quot;: \&quot;/org@myorg/envgroup@myenvgroup/env@myenv/proxies/proxy@myproxy/target\&quot;, }] This will return components with path: \&quot;/org@myorg/envgroup@myenvgroup/env@myenv/proxies/proxy@myproxy/source\&quot; OR \&quot;/org@myorg/envgroup@myenvgroup/env@myenv/proxies/proxy@myproxy/target\&quot; | [optional] 
**pageSize** | **Number** | Optional. The maximum number of subcomponents to be returned in a single page. The service may return fewer than this value. If unspecified, at most 100 subcomponents will be returned in a single page. | [optional] 
**pageToken** | **String** | Optional. A token that can be sent as &#x60;page_token&#x60; to retrieve the next page. If this field is omitted, there are no subsequent pages. | [optional] 
**timeRange** | [**GoogleTypeInterval**](GoogleTypeInterval.md) |  | [optional] 


