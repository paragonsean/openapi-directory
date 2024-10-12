

# HTTPGetAction

HTTPGetAction describes an action based on HTTP Get requests.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**host** | **String** | Not supported by Cloud Run. |  [optional] |
|**httpHeaders** | [**List&lt;HTTPHeader&gt;**](HTTPHeader.md) | Custom headers to set in the request. HTTP allows repeated headers. |  [optional] |
|**path** | **String** | Path to access on the HTTP server. |  [optional] |
|**port** | **Integer** | Port number to access on the container. Number must be in the range 1 to 65535. |  [optional] |
|**scheme** | **String** | Not supported by Cloud Run. |  [optional] |



