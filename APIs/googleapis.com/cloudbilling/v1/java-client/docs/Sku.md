

# Sku

Encapsulates a single SKU in Google Cloud Platform

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**Category**](Category.md) |  |  [optional] |
|**description** | **String** | A human readable description of the SKU, has a maximum length of 256 characters. |  [optional] |
|**geoTaxonomy** | [**GeoTaxonomy**](GeoTaxonomy.md) |  |  [optional] |
|**name** | **String** | The resource name for the SKU. Example: \&quot;services/DA34-426B-A397/skus/AA95-CD31-42FE\&quot; |  [optional] |
|**pricingInfo** | [**List&lt;PricingInfo&gt;**](PricingInfo.md) | A timeline of pricing info for this SKU in chronological order. |  [optional] |
|**serviceProviderName** | **String** | Identifies the service provider. This is &#39;Google&#39; for first party services in Google Cloud Platform. |  [optional] |
|**serviceRegions** | **List&lt;String&gt;** | List of service regions this SKU is offered at. Example: \&quot;asia-east1\&quot; Service regions can be found at https://cloud.google.com/about/locations/ |  [optional] |
|**skuId** | **String** | The identifier for the SKU. Example: \&quot;AA95-CD31-42FE\&quot; |  [optional] |



