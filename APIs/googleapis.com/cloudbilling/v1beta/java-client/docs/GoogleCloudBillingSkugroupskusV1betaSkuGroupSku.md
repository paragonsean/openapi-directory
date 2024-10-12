

# GoogleCloudBillingSkugroupskusV1betaSkuGroupSku

Encapsulates a publicly listed stock keeping unit (SKU) that is part of a publicly listed SKU group. A SKU group represents a collection of SKUs that are related to each other. For example, the `AI Platform APIs` SKU group includes SKUs from the Cloud Dialogflow API, the Cloud Text-to-Speech API, and additional related APIs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Description of the SkuGroupSku. Example: \&quot;A2 Instance Core running in Hong Kong\&quot;. |  [optional] |
|**geoTaxonomy** | [**GoogleCloudBillingSkugroupskusV1betaGeoTaxonomy**](GoogleCloudBillingSkugroupskusV1betaGeoTaxonomy.md) |  |  [optional] |
|**name** | **String** | Resource name for the SkuGroupSku. Example: \&quot;skuGroups/0e6403d1-4694-44d2-a696-7a78b1a69301/skus/AA95-CD31-42FE\&quot;. |  [optional] |
|**productTaxonomy** | [**GoogleCloudBillingSkugroupskusV1betaProductTaxonomy**](GoogleCloudBillingSkugroupskusV1betaProductTaxonomy.md) |  |  [optional] |
|**service** | **String** | Service that the SkuGroupSku belongs to. |  [optional] |
|**skuId** | **String** | Unique identifier for the SKU. It is the string after the collection identifier \&quot;skus/\&quot; Example: \&quot;AA95-CD31-42FE\&quot;. |  [optional] |



