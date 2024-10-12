

# GoogleCloudApigeeV1DebugSession


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | Optional. The number of request to be traced. Min &#x3D; 1, Max &#x3D; 15, Default &#x3D; 10. |  [optional] |
|**createTime** | **String** | Output only. The first transaction creation timestamp, recorded by UAP. |  [optional] [readonly] |
|**filter** | **String** | Optional. A conditional statement which is evaluated against the request message to determine if it should be traced. Syntax matches that of on API Proxy bundle flow Condition. |  [optional] |
|**name** | **String** | A unique ID for this DebugSession. |  [optional] |
|**timeout** | **String** | Optional. The time in seconds after which this DebugSession should end. This value will override the value in query param, if both are provided. |  [optional] |
|**tracesize** | **Integer** | Optional. The maximum number of bytes captured from the response payload. Min &#x3D; 0, Max &#x3D; 5120, Default &#x3D; 5120. |  [optional] |
|**validity** | **Integer** | Optional. The length of time, in seconds, that this debug session is valid, starting from when it&#39;s received in the control plane. Min &#x3D; 1, Max &#x3D; 15, Default &#x3D; 10. |  [optional] |



