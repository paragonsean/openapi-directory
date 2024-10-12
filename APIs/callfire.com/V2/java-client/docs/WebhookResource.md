

# WebhookResource

WebhookResource describes a resource and a list of supported events, once event is triggered CallFire performs an HTTP POST request to a client's endpoint

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**resource** | **String** | A name of a webhook resource (ex: InboundCall, OutboundCall, InboundText, OutboundText, CallBroadcast, TextBroadcast, etc...) |  [optional] |
|**supportedEvents** | **Set&lt;String&gt;** | A list of event names which are supported by webhook resource (ex: Started, Stopped, Finished, etc.) |  [optional] |



