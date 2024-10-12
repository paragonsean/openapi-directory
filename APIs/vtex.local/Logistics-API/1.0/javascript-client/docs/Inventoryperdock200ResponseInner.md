# LogisticsApi.Inventoryperdock200ResponseInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availableQuantity** | **Number** | Amount of items available for sale. Difference between total quantity and reserved quantity. | [optional] 
**dateOfSupplyUtc** | **String** | Date of supply lot in UTC. | [optional] 
**deliveryChannel** | **[String]** | List of delivery channels available. | [optional] 
**dockId** | **String** | Dock ID. | [optional] 
**isUnlimited** | **Boolean** | Indicates whether the SKU&#39;s availability is unlimited (\&quot;infinite inventory\&quot;). | [optional] 
**keepSellingAfterExpiration** | **Boolean** | Indicates whether SKU can continue to be sold after the available quantity gets to 0. | [optional] 
**reservedQuantity** | **Number** | Reserved quantity of the SKU. | [optional] 
**salesChannel** | **[String]** | List of sales channels associated. | [optional] 
**skuId** | **String** | SKU ID. | [optional] 
**timeToRefill** | **String** | Time to refill (deprecated). | [optional] 
**totalQuantity** | **Number** | Total quantity of SKU. | [optional] 
**transfer** | **String** | Transfer. | [optional] 
**warehouseId** | **String** | Warehouse ID. | [optional] 


