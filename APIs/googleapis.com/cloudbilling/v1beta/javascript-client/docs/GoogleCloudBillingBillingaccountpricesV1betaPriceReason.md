# CloudBillingApi.GoogleCloudBillingBillingaccountpricesV1betaPriceReason

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**defaultPrice** | **Object** | Encapsulates a default price which is the current list price. | [optional] 
**fixedDiscount** | [**GoogleCloudBillingBillingaccountpricesV1betaFixedDiscount**](GoogleCloudBillingBillingaccountpricesV1betaFixedDiscount.md) |  | [optional] 
**fixedPrice** | **Object** | Encapsulates a set fixed price applicable during the terms of a contract agreement. | [optional] 
**floatingDiscount** | [**GoogleCloudBillingBillingaccountpricesV1betaFloatingDiscount**](GoogleCloudBillingBillingaccountpricesV1betaFloatingDiscount.md) |  | [optional] 
**listPriceAsCeiling** | **Object** | Encapsulates a contract feature that the list price (DefaultPrice) will be used for the price if the current list price drops lower than the custom fixed price. Available to new contracts after March 21, 2022. Applies to all fixed price SKUs in the contract, including FixedPrice, FixedDiscount, MigratedPrice, and MergedPrice. | [optional] 
**mergedPrice** | **Object** | Encapsulates a price after merging from multiple sources. With merged tiers, each individual tier can be from a different source with different discount types. | [optional] 
**migratedPrice** | [**GoogleCloudBillingBillingaccountpricesV1betaMigratedPrice**](GoogleCloudBillingBillingaccountpricesV1betaMigratedPrice.md) |  | [optional] 
**type** | **String** | Type of the price reason. It can have values such as &#39;unspecified&#39;, &#39;default-price&#39;, &#39;fixed-price&#39;, &#39;fixed-discount&#39;, &#39;floating-discount&#39;, &#39;migrated-price&#39;, &#39;merged-price&#39;, &#39;list-price-as-ceiling&#39;. | [optional] 


