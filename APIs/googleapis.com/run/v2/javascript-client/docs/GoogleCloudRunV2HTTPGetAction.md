# CloudRunAdminApi.GoogleCloudRunV2HTTPGetAction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**httpHeaders** | [**[GoogleCloudRunV2HTTPHeader]**](GoogleCloudRunV2HTTPHeader.md) | Custom headers to set in the request. HTTP allows repeated headers. | [optional] 
**path** | **String** | Path to access on the HTTP server. Defaults to &#39;/&#39;. | [optional] 
**port** | **Number** | Port number to access on the container. Must be in the range 1 to 65535. If not specified, defaults to the exposed port of the container, which is the value of container.ports[0].containerPort. | [optional] 


