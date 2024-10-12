# ContentApiForShopping.ProductCluster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **String** | Brand of the product cluster. | [optional] 
**brandInventoryStatus** | **String** | Tells if there is at least one product of the brand currently &#x60;IN_STOCK&#x60; in your product feed across multiple countries, all products are &#x60;OUT_OF_STOCK&#x60; in your product feed, or &#x60;NOT_IN_INVENTORY&#x60;. The field doesn&#39;t take the Best Sellers report country filter into account. | [optional] 
**categoryL1** | **String** | Product category (1st level) of the product cluster, represented in Google&#39;s product taxonomy. | [optional] 
**categoryL2** | **String** | Product category (2nd level) of the product cluster, represented in Google&#39;s product taxonomy. | [optional] 
**categoryL3** | **String** | Product category (3rd level) of the product cluster, represented in Google&#39;s product taxonomy. | [optional] 
**categoryL4** | **String** | Product category (4th level) of the product cluster, represented in Google&#39;s product taxonomy. | [optional] 
**categoryL5** | **String** | Product category (5th level) of the product cluster, represented in Google&#39;s product taxonomy. | [optional] 
**inventoryStatus** | **String** | Tells whether the product cluster is &#x60;IN_STOCK&#x60; in your product feed across multiple countries, &#x60;OUT_OF_STOCK&#x60; in your product feed, or &#x60;NOT_IN_INVENTORY&#x60; at all. The field doesn&#39;t take the Best Sellers report country filter into account. | [optional] 
**title** | **String** | Title of the product cluster. | [optional] 
**variantGtins** | **[String]** | GTINs of example variants of the product cluster. | [optional] 



## Enum: BrandInventoryStatusEnum


* `INVENTORY_STATUS_UNSPECIFIED` (value: `"INVENTORY_STATUS_UNSPECIFIED"`)

* `IN_STOCK` (value: `"IN_STOCK"`)

* `OUT_OF_STOCK` (value: `"OUT_OF_STOCK"`)

* `NOT_IN_INVENTORY` (value: `"NOT_IN_INVENTORY"`)





## Enum: InventoryStatusEnum


* `INVENTORY_STATUS_UNSPECIFIED` (value: `"INVENTORY_STATUS_UNSPECIFIED"`)

* `IN_STOCK` (value: `"IN_STOCK"`)

* `OUT_OF_STOCK` (value: `"OUT_OF_STOCK"`)

* `NOT_IN_INVENTORY` (value: `"NOT_IN_INVENTORY"`)




