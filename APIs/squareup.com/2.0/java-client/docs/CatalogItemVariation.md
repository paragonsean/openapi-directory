

# CatalogItemVariation

An item variation (i.e., product) in the Catalog object model. Each item may have a maximum of 250 item variations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableForBooking** | **Boolean** | If the &#x60;CatalogItem&#x60; that owns this item variation is of type &#x60;APPOINTMENTS_SERVICE&#x60;, a bool representing whether this service is available for booking. |  [optional] |
|**inventoryAlertThreshold** | **Long** | If the inventory quantity for the variation is less than or equal to this value and &#x60;inventory_alert_type&#x60; is &#x60;LOW_QUANTITY&#x60;, the variation displays an alert in the merchant dashboard.  This value is always an integer. |  [optional] |
|**inventoryAlertType** | **String** | Indicates whether the item variation displays an alert when its inventory quantity is less than or equal to its &#x60;inventory_alert_threshold&#x60;. |  [optional] |
|**itemId** | **String** | The ID of the &#x60;CatalogItem&#x60; associated with this item variation. |  [optional] |
|**itemOptionValues** | [**List&lt;CatalogItemOptionValueForItemVariation&gt;**](CatalogItemOptionValueForItemVariation.md) | List of item option values associated with this item variation. Listed in the same order as the item options of the parent item. |  [optional] |
|**locationOverrides** | [**List&lt;ItemVariationLocationOverrides&gt;**](ItemVariationLocationOverrides.md) | Per-location price and inventory overrides. |  [optional] |
|**measurementUnitId** | **String** | ID of the ‘CatalogMeasurementUnit’ that is used to measure the quantity sold of this item variation. If left unset, the item will be sold in whole quantities. |  [optional] |
|**name** | **String** | The item variation&#39;s name. This is a searchable attribute for use in applicable query filters, and its value length is of Unicode code points. |  [optional] |
|**ordinal** | **Integer** | The order in which this item variation should be displayed. This value is read-only. On writes, the ordinal for each item variation within a parent &#x60;CatalogItem&#x60; is set according to the item variations&#39;s position. On reads, the value is not guaranteed to be sequential or unique. |  [optional] |
|**priceMoney** | [**Money**](Money.md) |  |  [optional] |
|**pricingType** | **String** | Indicates whether the item variation&#39;s price is fixed or determined at the time of sale. |  [optional] |
|**serviceDuration** | **Long** | If the &#x60;CatalogItem&#x60; that owns this item variation is of type &#x60;APPOINTMENTS_SERVICE&#x60;, then this is the duration of the service in milliseconds. For example, a 30 minute appointment would have the value &#x60;1800000&#x60;, which is equal to 30 (minutes) * 60 (seconds per minute) * 1000 (milliseconds per second). |  [optional] |
|**sku** | **String** | The item variation&#39;s SKU, if any. This is a searchable attribute for use in applicable query filters. |  [optional] |
|**stockable** | **Boolean** | Whether stock is counted directly on this variation (TRUE) or only on its components (FALSE). For backward compatibility missing values will be interpreted as TRUE. |  [optional] |
|**stockableConversion** | [**CatalogStockConversion**](CatalogStockConversion.md) |  |  [optional] |
|**teamMemberIds** | **List&lt;String&gt;** | Tokens of employees that can perform the service represented by this variation. Only valid for variations of type &#x60;APPOINTMENTS_SERVICE&#x60;. |  [optional] |
|**trackInventory** | **Boolean** | If &#x60;true&#x60;, inventory tracking is active for the variation. |  [optional] |
|**upc** | **String** | The universal product code (UPC) of the item variation, if any. This is a searchable attribute for use in applicable query filters.  The value of this attribute should be a number of 12-14 digits long.  This restriction is enforced on the Square Seller Dashboard, Square Point of Sale or Retail Point of Sale apps, where this attribute shows in the GTIN field. If a non-compliant UPC value is assigned to this attribute using the API, the value is not editable on the Seller Dashboard, Square Point of Sale or Retail Point of Sale apps unless it is updated to fit the expected format. |  [optional] |
|**userData** | **String** | Arbitrary user metadata to associate with the item variation. This attribute value length is of Unicode code points. |  [optional] |



