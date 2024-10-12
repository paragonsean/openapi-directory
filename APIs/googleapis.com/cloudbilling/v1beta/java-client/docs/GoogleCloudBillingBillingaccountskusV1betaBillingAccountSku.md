

# GoogleCloudBillingBillingaccountskusV1betaBillingAccountSku

Encapsulates a stock keeping unit (SKU) visible to a billing account. A SKU distinctly identifies a resource that you can purchase, such as `Nvidia Tesla K80 GPU attached to Spot Preemptible VMs running in Warsaw`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAccountService** | **String** | BillingAccountService that the BillingAccountSku belongs to. |  [optional] |
|**displayName** | **String** | Description of the BillingAccountSku. Example: \&quot;A2 Instance Core running in Hong Kong\&quot;. |  [optional] |
|**geoTaxonomy** | [**GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomy**](GoogleCloudBillingBillingaccountskusV1betaGeoTaxonomy.md) |  |  [optional] |
|**name** | **String** | Resource name for the BillingAccountSku. Example: \&quot;billingAccounts/012345-567890-ABCDEF/skus/AA95-CD31-42FE\&quot;. |  [optional] |
|**productTaxonomy** | [**GoogleCloudBillingBillingaccountskusV1betaProductTaxonomy**](GoogleCloudBillingBillingaccountskusV1betaProductTaxonomy.md) |  |  [optional] |
|**skuId** | **String** | Unique identifier for the SKU. It is the string after the collection identifier \&quot;skus/\&quot; Example: \&quot;AA95-CD31-42FE\&quot;. |  [optional] |



