# CloudRunAdminApi.HTTPGetAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host** | **String** | (Optional) Host name to connect to, defaults to the pod IP. You probably want to set \&quot;Host\&quot; in httpHeaders instead. | [optional] 
**httpHeaders** | [**[HTTPHeader]**](HTTPHeader.md) | (Optional) Custom headers to set in the request. HTTP allows repeated headers. | [optional] 
**path** | **String** | (Optional) Path to access on the HTTP server. | [optional] 
**scheme** | **String** | (Optional) Scheme to use for connecting to the host. Defaults to HTTP. | [optional] 


