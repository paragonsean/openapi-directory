# GkeHubApi.ServiceMeshType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | A 7 character code matching &#x60;^IST[0-9]{4}$&#x60; or &#x60;^ASM[0-9]{4}$&#x60;, intended to uniquely identify the message type. (e.g. \&quot;IST0001\&quot; is mapped to the \&quot;InternalError\&quot; message type.) | [optional] 
**displayName** | **String** | A human-readable name for the message type. e.g. \&quot;InternalError\&quot;, \&quot;PodMissingProxy\&quot;. This should be the same for all messages of the same type. (This corresponds to the &#x60;name&#x60; field in open-source Istio.) | [optional] 


