

# LicenseAssignment

Representation of a license assignment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etags** | **String** | ETag of the resource. |  [optional] |
|**kind** | **String** | Identifies the resource as a LicenseAssignment, which is &#x60;licensing#licenseAssignment&#x60;. |  [optional] |
|**productId** | **String** | A product&#39;s unique identifier. For more information about products in this version of the API, see Product and SKU IDs. |  [optional] |
|**productName** | **String** | Display Name of the product. |  [optional] |
|**selfLink** | **String** | Link to this page. |  [optional] |
|**skuId** | **String** | A product SKU&#39;s unique identifier. For more information about available SKUs in this version of the API, see Products and SKUs. |  [optional] |
|**skuName** | **String** | Display Name of the sku of the product. |  [optional] |
|**userId** | **String** | The user&#39;s current primary email address. If the user&#39;s email address changes, use the new email address in your API requests. Since a &#x60;userId&#x60; is subject to change, do not use a &#x60;userId&#x60; value as a key for persistent data. This key could break if the current user&#39;s email address changes. If the &#x60;userId&#x60; is suspended, the license status changes. |  [optional] |



