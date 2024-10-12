

# PipeEnrichmentHttpParameters

These are custom parameter to be used when the target is an API Gateway REST APIs or EventBridge ApiDestinations. In the latter case, these are merged with any InvocationParameters specified on the Connection, with any values from the Connection taking precedence.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**headerParameters** | [**Map**](Map.md) |  |  [optional] |
|**pathParameterValues** | [**List**](List.md) |  |  [optional] |
|**queryStringParameters** | [**Map**](Map.md) |  |  [optional] |



