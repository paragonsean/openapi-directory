

# WarehouseAvailabilityDto

Warehouse information for a specific inventory item

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | The description of the warehouse |  [optional] |
|**estimatedTotalCost** | **Double** | The total cost for the QuantityOnHand |  [optional] |
|**estimatedUnitCost** | **Double** | The estimated cost per unit, calculated as EstimatedTotalCost/QuantityOnHand |  [optional] |
|**internalWarehouseId** | **Integer** | The internal id used by the system for the warehouse |  [optional] |
|**lastModified** | **OffsetDateTime** | The date and time the entry for this warehouse was modified  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T12:15:14+02:00&#39;), the date is considered to be in the UTC time zone. |  [optional] |
|**locations** | [**List&lt;LocationAvailabilityDto&gt;**](LocationAvailabilityDto.md) | List of locations in the warehouse for the specific inventory item.  Note that this is not returned as part of the response unless expand&#x3D;Location is specified with the request. |  [optional] |
|**quantityAvailable** | **Double** | You can configure the way this estimated quantity is calculated by using availability  calculation rules. The available quantity may include anticipated transactions and therefore  may be less than or greater than the QuantityOnHand. Anticipated transactions correspond  to the documents and transactions that have been entered in the system but not yet  processed to the end.  In the availability calculation settings of an item class, you specify which anticipated  transactions affect the available quantity. Thus, the available quantity may include  goods on purchase orders and exclude the goods allocated for sales orders. You can use  the available quantity as an indicator of demand |  [optional] |
|**quantityAvailableForShipment** | **Double** | Estimated quantity calculated by using the following formula: the QuantityOnHand minus the quantity on unreleased inventory  issues, minus the quantity allocated for shipping. Thus, the QuantityAvailableForShipment can be less than the QuantityOnHand |  [optional] |
|**quantityNotAvailable** | **Double** | The quantity stored at locations not included in the availability calculation.  For each warehouse location, the &#39;Include in Qty. Available&#39; check box on the  Warehouses(IN204000) screen defines whether the quantity of items stored at this  location is included in the quantity of available items. |  [optional] |
|**quantityOnHand** | **Double** | Physical quantity on-hand of items in the specific warehouse |  [optional] |
|**quantityPurchaseOrders** | **Double** | The quantity of the inventory item included in open purchase orders. |  [optional] |
|**warehouseId** | **String** | The id (SiteCd) of the warehouse |  [optional] |



