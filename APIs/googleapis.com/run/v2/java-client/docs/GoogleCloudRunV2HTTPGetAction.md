

# GoogleCloudRunV2HTTPGetAction

HTTPGetAction describes an action based on HTTP Get requests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**httpHeaders** | [**List&lt;GoogleCloudRunV2HTTPHeader&gt;**](GoogleCloudRunV2HTTPHeader.md) | Custom headers to set in the request. HTTP allows repeated headers. |  [optional] |
|**path** | **String** | Path to access on the HTTP server. Defaults to &#39;/&#39;. |  [optional] |
|**port** | **Integer** | Port number to access on the container. Must be in the range 1 to 65535. If not specified, defaults to the exposed port of the container, which is the value of container.ports[0].containerPort. |  [optional] |



