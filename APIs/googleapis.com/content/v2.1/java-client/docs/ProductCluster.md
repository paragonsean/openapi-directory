

# ProductCluster

Product cluster fields. A product cluster is a grouping for different offers that represent the same product. Values are only set for fields requested explicitly in the request's search query.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**brand** | **String** | Brand of the product cluster. |  [optional] |
|**brandInventoryStatus** | [**BrandInventoryStatusEnum**](#BrandInventoryStatusEnum) | Tells if there is at least one product of the brand currently &#x60;IN_STOCK&#x60; in your product feed across multiple countries, all products are &#x60;OUT_OF_STOCK&#x60; in your product feed, or &#x60;NOT_IN_INVENTORY&#x60;. The field doesn&#39;t take the Best Sellers report country filter into account. |  [optional] |
|**categoryL1** | **String** | Product category (1st level) of the product cluster, represented in Google&#39;s product taxonomy. |  [optional] |
|**categoryL2** | **String** | Product category (2nd level) of the product cluster, represented in Google&#39;s product taxonomy. |  [optional] |
|**categoryL3** | **String** | Product category (3rd level) of the product cluster, represented in Google&#39;s product taxonomy. |  [optional] |
|**categoryL4** | **String** | Product category (4th level) of the product cluster, represented in Google&#39;s product taxonomy. |  [optional] |
|**categoryL5** | **String** | Product category (5th level) of the product cluster, represented in Google&#39;s product taxonomy. |  [optional] |
|**inventoryStatus** | [**InventoryStatusEnum**](#InventoryStatusEnum) | Tells whether the product cluster is &#x60;IN_STOCK&#x60; in your product feed across multiple countries, &#x60;OUT_OF_STOCK&#x60; in your product feed, or &#x60;NOT_IN_INVENTORY&#x60; at all. The field doesn&#39;t take the Best Sellers report country filter into account. |  [optional] |
|**title** | **String** | Title of the product cluster. |  [optional] |
|**variantGtins** | **List&lt;String&gt;** | GTINs of example variants of the product cluster. |  [optional] |



## Enum: BrandInventoryStatusEnum

| Name | Value |
|---- | -----|
| INVENTORY_STATUS_UNSPECIFIED | &quot;INVENTORY_STATUS_UNSPECIFIED&quot; |
| IN_STOCK | &quot;IN_STOCK&quot; |
| OUT_OF_STOCK | &quot;OUT_OF_STOCK&quot; |
| NOT_IN_INVENTORY | &quot;NOT_IN_INVENTORY&quot; |



## Enum: InventoryStatusEnum

| Name | Value |
|---- | -----|
| INVENTORY_STATUS_UNSPECIFIED | &quot;INVENTORY_STATUS_UNSPECIFIED&quot; |
| IN_STOCK | &quot;IN_STOCK&quot; |
| OUT_OF_STOCK | &quot;OUT_OF_STOCK&quot; |
| NOT_IN_INVENTORY | &quot;NOT_IN_INVENTORY&quot; |



