

# ListenerCreate


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**domainKeys** | **List&lt;String&gt;** |  |  [optional] |
|**ip** | **String** | the interface this listener should bind to. |  [optional] |
|**name** | **String** |  |  |
|**port** | **Integer** | the port this listener should bind to. |  |
|**protocol** | [**ProtocolEnum**](#ProtocolEnum) | the protocol this listener will handle. http and http2 configure the listener to only process requests of that type. http_auto will adapt to HTTP/1.1 and HTTP/2 as needed. tcp configures the listener to be a tcp proxy  |  |
|**tracingConfig** | [**TracingConfig**](TracingConfig.md) |  |  [optional] |
|**zoneKey** | **String** |  |  [optional] |



## Enum: ProtocolEnum

| Name | Value |
|---- | -----|
| HTTP | &quot;http&quot; |
| HTTP2 | &quot;http2&quot; |
| HTTP_AUTO | &quot;http_auto&quot; |
| TCP | &quot;tcp&quot; |



