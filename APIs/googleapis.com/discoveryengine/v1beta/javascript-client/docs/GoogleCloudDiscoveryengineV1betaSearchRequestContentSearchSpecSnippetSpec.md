# DiscoveryEngineApi.GoogleCloudDiscoveryengineV1betaSearchRequestContentSearchSpecSnippetSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maxSnippetCount** | **Number** | [DEPRECATED] This field is deprecated. To control snippet return, use &#x60;return_snippet&#x60; field. For backwards compatibility, we will return snippet if max_snippet_count &gt; 0. | [optional] 
**referenceOnly** | **Boolean** | [DEPRECATED] This field is deprecated and will have no affect on the snippet. | [optional] 
**returnSnippet** | **Boolean** | If &#x60;true&#x60;, then return snippet. If no snippet can be generated, we return \&quot;No snippet is available for this page.\&quot; A &#x60;snippet_status&#x60; with &#x60;SUCCESS&#x60; or &#x60;NO_SNIPPET_AVAILABLE&#x60; will also be returned. | [optional] 


