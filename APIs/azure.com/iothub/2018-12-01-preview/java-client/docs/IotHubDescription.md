

# IotHubDescription

The description of the IoT hub.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **String** | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |  [optional] |
|**properties** | [**IotHubProperties**](IotHubProperties.md) |  |  [optional] |
|**sku** | [**IotHubSkuInfo**](IotHubSkuInfo.md) |  |  |
|**id** | **String** | The resource identifier. |  [optional] [readonly] |
|**location** | **String** | The resource location. |  |
|**name** | **String** | The resource name. |  [optional] [readonly] |
|**tags** | **Map&lt;String, String&gt;** | The resource tags. |  [optional] |
|**type** | **String** | The resource type. |  [optional] [readonly] |



