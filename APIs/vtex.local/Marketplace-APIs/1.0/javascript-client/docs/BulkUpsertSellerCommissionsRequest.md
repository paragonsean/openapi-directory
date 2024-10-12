# MarketplaceApi.BulkUpsertSellerCommissionsRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categoryFullPath** | **String** | Full path to the SKU&#39;s category. It should be written as {department}/{category}. For example: if the department is **Appliances** and the category is **Oven**, the full path should be &#39;Appliances/Oven&#39;. | [default to &#39;Appliances/Oven&#39;]
**categoryId** | **String** | Marketplace&#39;s Category ID that the product belongs to, configured in the Catalog. | [default to &#39;6&#39;]
**freightCommissionPercentage** | **Number** | Percentage of the comission applied to the freight in decimals. | [default to 2.43]
**productCommissionPercentage** | **Number** | Percentage of the comission applied to the product in decimals. | [default to 9.85]


