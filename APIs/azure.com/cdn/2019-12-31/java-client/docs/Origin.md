

# Origin

CDN origin is the source of the content being delivered via CDN. When the edge nodes represented by an endpoint do not have the requested content cached, they attempt to fetch it from one or more of the configured origins.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**OriginProperties**](OriginProperties.md) |  |  [optional] |
|**location** | **String** | Resource location. |  |
|**tags** | **Map&lt;String, String&gt;** | Resource tags. |  [optional] |
|**id** | **String** | Resource ID. |  [optional] [readonly] |
|**name** | **String** | Resource name. |  [optional] [readonly] |
|**type** | **String** | Resource type. |  [optional] [readonly] |



