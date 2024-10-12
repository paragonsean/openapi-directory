

# PatchSalesOrderLineDto

The sales order line which is set to patch

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**branchId** | **String** | Sets the branch with which this line is associated.  If &#x60;BranchId&#x60; is provided as (null), the value will be set from from order &#x60;BranchId&#x60; |  [optional] |
|**commissionable** | **Boolean** | Indicates if line is comissionable. |  [optional] |
|**description** | **String** | Sets the description of the order line item. This will override the default description from the inventory item  &lt;br&gt;Note that text fields should not contain any personally identifiable or otherwise sensitive data |  [optional] |
|**discountAmount** | **Double** | Sets the manual currency discount amount for the line.  &lt;remarks&gt;  Note that the behavior of the &#39;discountAmount&#39; field is affected by the &#39;hasManualDiscount&#39; option.  If &#39;hasManualDiscount&#39; is provided and set to \&quot;false\&quot;, and &#39;discountAmount&#39; is provided, the system will set the discountAmount according to the predefined rules.  &lt;/remarks&gt; |  [optional] |
|**discountCode** | **String** | Sets the discount for the line if applicable. This must be one of the selectable discount codes.  &lt;remarks&gt;  Note that the behavior of the &#39;discountCode&#39; field is affected by the &#39;hasManualDiscount&#39; option.  If &#39;hasManualDiscount&#39; is provided and set to \&quot;false\&quot;, and &#39;discountCode&#39; is provided, the system will set the discountCode according to the predefined rules.  &lt;/remarks&gt; |  [optional] |
|**discountPercent** | **Double** | Sets the manual percentage discount for the line.  &lt;remarks&gt;  Note that the behavior of the &#39;discountPercent&#39; field is affected by the &#39;hasManualDiscount&#39; option.  If &#39;hasManualDiscount&#39; is provided and set to \&quot;false\&quot;, and &#39;discountPercent&#39; is provided, the system will set the discountPercent according to the predefined rules.  &lt;/remarks&gt; |  [optional] |
|**externalLink** | **String** | Sets the external link for the line |  [optional] |
|**hasManualDiscount** | **Boolean** | Indicates that line level discount is applied manually.  &lt;remarks&gt;  Note that the behavior of the fields &#39;discountCode&#39;, &#39;discountPercent&#39; and &#39;discountAmount&#39; is affected by this option.  If &#39;hasManualDiscount&#39; is provided and set to \&quot;false\&quot;, and discount field(s) is provided, the system will set the line level discounts according to the predefined rules.  &lt;/remarks&gt; |  [optional] |
|**hasManualPrice** | **Boolean** | Indicates that the &#x60;unitPrice&#x60; in this line has been specified manually.  If set to \&quot;false\&quot;, the system updates the unit price in the line according to predefined rules.  Note that the behavior of the field &#x60;unitPrice&#x60; is affected by this option.  If &#x60;hasManualPrice&#x60; is provided and set to \&quot;false\&quot;, and &#x60;unitPrice&#x60; is provided, the system will set the &#x60;unitPrice&#x60; according to the predefined rules. |  [optional] |
|**lineId** | **Integer** | The line id of the line. |  |
|**note** | **String** | Any note to apply to the order header. |  [optional] |
|**operation** | **String** | The type of operation the line represents to the order. Acceptable values are &#39;Issue&#39; or &#39;Receipt&#39;. This must be a valid operation for sales order type. |  [optional] |
|**overshipThreshold** | **Double** | Sets the overship threshold in percent. If not set, information from the inventory item is used |  [optional] |
|**projectTaskId** | **String** | The project task with which this sales order line is associated |  [optional] |
|**purchaseOrderSource** | **String** | Sets the purchase source of the line.  Accepted values are &#x60;dropShip&#x60; or &#x60;purchaseToOrder&#x60;, when null provided, value will be set from default value from the inventory item.  If the value was provided as &#39;&#39; (empty string), the value will set to null. |  [optional] |
|**quantity** | **Double** | Sets the quantity of items on the order line |  [optional] |
|**reasonCode** | **String** | Patch the reason code for the line. This must be one of the selectable reason codes |  [optional] |
|**requestDate** | **OffsetDateTime** | Sets the date the order line is requested (Requested On)  Unless a specific time zone offset is specified with the date (e.g. &#39;2012-12-24T13:30:23+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**salesAccountId** | **String** | Overrides the Sales Account Id of the line. The value must be one of the selectable Accounts.  If not set, a value based on the rules is used |  [optional] |
|**salesPersonId** | **String** | Sets the sales person for the line.  If &#x60;SalesPersonId&#x60; is provided as (null), the value will be set from from order &#x60;SalesPersonId&#x60; |  [optional] |
|**shipDate** | **OffsetDateTime** | Sets the day the order line should be shipped, so that the customer gets it on the requested date (Ship On).  Unless a specific time zone offset is specified with the date (e.g. &#39;2012-12-24T13:30:23+02:00&#39;), the passed date is considered to be in the UTC time zone. |  [optional] |
|**shippingRule** | **String** | The way the line item should be shipped.  &lt;br&gt;One of the following options can be set:&lt;br&gt;&lt;list type&#x3D;\&quot;bullet\&quot;&gt;&lt;item&gt;&lt;term&gt;CancelRemainder: &lt;/term&gt;&lt;description&gt;The ordered quantity should be delivered in one shipment&lt;/description&gt;&lt;/item&gt;&lt;item&gt;&lt;term&gt;BackOrderAllowed: &lt;/term&gt;&lt;description&gt;The ordered quantity can be delivered in multiple shipments.&lt;/description&gt;&lt;/item&gt;&lt;item&gt;&lt;term&gt;ShipComplete: &lt;/term&gt;&lt;description&gt;The ordered quantity should be delivered in one shipment.&lt;/description&gt;&lt;/item&gt;&lt;/list&gt; |  [optional] |
|**sortOrder** | **Integer** |  |  [optional] |
|**subaccount** | **Map&lt;String, String&gt;** | Overrides the Subaccount setup for the line.  Each entry corresponds to a subaccount id/value pair |  [optional] |
|**supplierId** | **String** | Sets the Purchase Order Vendor for the line, can be set if the purchase order source is &#x60;purchaseToOrder&#x60; or &#x60;dropShip&#x60;. |  [optional] |
|**supplierPrice** | **Double** | Sets the supplier price for the line item. |  [optional] |
|**taxCategoryId** | **String** | Overrides the default tax category id. The value must be one of the selectable Tax Categories |  [optional] |
|**undershipThreshold** | **Double** | Sets the undership threshold in percent. If not set, information from the inventory item is used |  [optional] |
|**unitCost** | **Double** | Sets the unit cost of the product on the line. |  [optional] |
|**unitOfMeasure** | **String** | Sets the Unit of measure for the line item. This will override the default UOM for the inventory item |  [optional] |
|**unitPrice** | **Double** | Sets the unit price for the product on the line.  If no price is set(null or omitted) the price will be set according to predefined rules based on the inventoryId and the customer.  Note that the behavior of the &#x60;unitPrice&#x60; field is affected by the &#x60;hasManualPrice&#x60; option.  If &#x60;hasManualPrice&#x60; is provided and set to \&quot;false\&quot;, and &#x60;unitPrice&#x60; is provided, the system will set the &#x60;unitPrice&#x60; according to the predefined rules. |  [optional] |
|**warehouseId** | **String** | Sets the warehouse the item should be shipped from. This will override the default, or the one set on the order head. |  [optional] |
|**warehouseLocationId** | **String** | Sets the warehouse location that will be used for the shipment generated for the order the warehouse location Id for this line.  This must be a valid location for &#x60;warehouseId&#x60; and will override the default if set. |  [optional] |



