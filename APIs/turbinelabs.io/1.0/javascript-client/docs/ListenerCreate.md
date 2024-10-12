# TurbineLabsApi.ListenerCreate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domainKeys** | **[String]** |  | [optional] 
**ip** | **String** | the interface this listener should bind to. | [optional] 
**name** | **String** |  | 
**port** | **Number** | the port this listener should bind to. | 
**protocol** | **String** | the protocol this listener will handle. http and http2 configure the listener to only process requests of that type. http_auto will adapt to HTTP/1.1 and HTTP/2 as needed. tcp configures the listener to be a tcp proxy  | 
**tracingConfig** | [**TracingConfig**](TracingConfig.md) |  | [optional] 
**zoneKey** | **String** |  | [optional] 



## Enum: ProtocolEnum


* `http` (value: `"http"`)

* `http2` (value: `"http2"`)

* `http_auto` (value: `"http_auto"`)

* `tcp` (value: `"tcp"`)




