# VismaNetErpSalesOrdersApi.LocationAvailabilityDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | The description of the location | [optional] 
**internalLocationId** | **Number** | The internal id used by the sytem for this location | [optional] 
**lastModified** | **Date** | Date and time this entry for this location was modified  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T12:15:14+02:00&#39;), the date is considered to be in the UTC time zone. | [optional] 
**locationId** | **String** | The location id (LocationCd) for this location | [optional] 
**quantityAvailable** | **Number** | You can configure the way this estimated quantity is calculated by using availability  calculation rules. The available quantity may include anticipated transactions and therefore  may be less than or greater than the QuantityOnHand. Anticipated transactions correspond  to the documents and transactions that have been entered in the system but not yet  processed to the end.  In the availability calculation settings of an item class, you specify which anticipated  transactions affect the available quantity. Thus, the available quantity may include  goods on purchase orders and exclude the goods allocated for sales orders. You can use  the available quantity as an indicator of demand.  Note: For quantities on warehouse location level, only quantities added specifically for the location are taken into consideration in quantityAvailable | [optional] 
**quantityAvailableForShipment** | **Number** | Estimated quantity calculated by using the following formula: the QuantityOnHand minus the quantity on unreleased inventory  issues, minus the quantity allocated for shipping. Thus, the QuantityAvailableForShipment can be less than the QuantityOnHand.  Note: For quantities on warehouse location level, only quantities added specifically for the location are taken into consideration in quantityAvailableForShipment | [optional] 
**quantityNotAvailable** | **Number** | The quantity stored at locations not included in the availability calculation.  For each warehouse location, the &#39;Include in Qty. Available&#39; check box on the  Warehouses(IN204000) screen defines whether the quantity of items stored at this  location is included in the quantity of available items. | [optional] 
**quantityOnHand** | **Number** | Physical quantity on-hand of items in the specific location | [optional] 
**quantityPurchaseOrders** | **Number** | The quantity of the inventory item included in open purchase orders.  Note: For quantities on warehouse location level, only quantities added specifically for the location are taken into consideration | [optional] 


