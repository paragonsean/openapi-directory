# TrafficDirectorApi.Pipe

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **Number** | The mode for the Pipe. Not applicable for abstract sockets. | [optional] 
**path** | **String** | Unix Domain Socket path. On Linux, paths starting with &#39;@&#39; will use the abstract namespace. The starting &#39;@&#39; is replaced by a null byte by Envoy. Paths starting with &#39;@&#39; will result in an error in environments other than Linux. | [optional] 


