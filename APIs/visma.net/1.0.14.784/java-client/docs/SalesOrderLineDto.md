

# SalesOrderLineDto


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attachments** | [**List&lt;AttachmentDto&gt;**](AttachmentDto.md) | The attachments associated with this sales order line |  [optional] |
|**baseOrderQuantity** | **Double** | The base order quantity for this line |  [optional] |
|**billedQuantity** | **Double** | The billed quantity for this line |  [optional] |
|**branch** | [**CdDescriptionPairDto**](CdDescriptionPairDto.md) |  |  [optional] |
|**commissionable** | **Boolean** | Indicates if line is comissionable |  [optional] |
|**completed** | **Boolean** | Whether this order line is completed or not |  [optional] |
|**description** | **String** | Any description for this order line |  [optional] |
|**discountAmount** | **Double** | The discount amount for this line |  [optional] |
|**discountCode** | **String** | Code of discount applied to this line |  [optional] |
|**discountPercent** | **Double** | Discount percentage applied to this line |  [optional] |
|**discountSequenceId** | **String** | Id of discount sequence applied to this line |  [optional] |
|**extendedPrice** | **Double** | The extended price for this sales order line |  [optional] |
|**externalLink** | **String** | Any external link for this sales order line |  [optional] |
|**freeItem** | **Boolean** | Whether these item(s) are free or not |  [optional] |
|**hasManualDiscount** | **Boolean** | Discount is applied manually |  [optional] |
|**hasManualPrice** | **Boolean** | Unit price is applied manually |  [optional] |
|**inventory** | [**SalesOrderLineInventoryDto**](SalesOrderLineInventoryDto.md) |  |  [optional] |
|**inventoryAlternateId** | **String** |  |  [optional] |
|**lineId** | **Integer** | The line number of the sales order line |  [optional] |
|**lineTotalBeforeDiscount** | **Double** | The line total before any discounts are applied |  [optional] |
|**lineType** | **String** | The type of sales order line |  [optional] |
|**note** | **String** | Any note that has been applied to this order line |  [optional] |
|**openLine** | **Boolean** | Indicates if line has quantity left to be shipped |  [optional] |
|**openQuantity** | **Double** | The open quantity for this line |  [optional] |
|**operation** | **String** | The type of operation the line represents to the order |  [optional] |
|**orderDate** | **OffsetDateTime** | The date the order line was added  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**overshipThreshold** | **Double** | The overship threshold value (%) |  [optional] |
|**projectTaskId** | **String** | The project task with which this sales order line is associated |  [optional] |
|**purchaseOrderSource** | **String** | Information about line purchase order source |  [optional] |
|**quantity** | **Double** | The quantity of unit of measure this line represents |  [optional] |
|**quantityOnShipments** | **Double** | The quantity on shipments for this line |  [optional] |
|**reasonCode** | **String** | The reason code |  [optional] |
|**replacementUnitCost** | **Double** | The replacement unit cost of an item. This is set based on the supplier price.  If no supplier price found, the last price of the item&#39;s default supplier will be used.  If no default supplier is set, the last cost of the item will be used. |  [optional] |
|**requestDate** | **OffsetDateTime** | The request date for this order line  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**salesAccountId** | **String** | The general ledger account this line applies to |  [optional] |
|**salesPerson** | [**SalesPersonDto**](SalesPersonDto.md) |  |  [optional] |
|**shipDate** | **OffsetDateTime** | The expected shipping date for this order line  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T00:00:00+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**shippingRule** | **String** | The shipping rule code for this order line |  [optional] |
|**sortOrder** | **Integer** | Used to apply sort order to a set of lines |  [optional] |
|**subaccount** | **Map&lt;String, String&gt;** | The general ledger subaccount this line applies to |  [optional] |
|**supplier** | [**SupplierDto**](SupplierDto.md) |  |  [optional] |
|**supplierPrice** | **Double** |  |  [optional] |
|**taxCategoryId** | **String** | The Tax Category Id applying to this order line |  [optional] |
|**undershipThreshold** | **Double** | The undership threshold value (%) |  [optional] |
|**unitCost** | **Double** | The unit cost of items on this order line |  [optional] |
|**unitOfMeasure** | **String** | The unit of measure (UOM) for the sales order line |  [optional] |
|**unitPrice** | **Double** | The unit price for items on this order line |  [optional] |
|**warehouseId** | **String** | The Site Id for items on this line |  [optional] |
|**warehouseLocation** | [**LocationDto**](LocationDto.md) |  |  [optional] |



