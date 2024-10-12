

# BillbeeInterfacesBillbeeAPIModelOrderItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**List&lt;BillbeeInterfacesBillbeeAPIModelOrderItemAttribute&gt;**](BillbeeInterfacesBillbeeAPIModelOrderItemAttribute.md) | A list of product attributes for this position |  [optional] |
|**billbeeId** | **Long** | The billbee id of this item |  [optional] |
|**discount** | **Double** | Sets the discount in percent |  [optional] |
|**dontAdjustStock** | **Boolean** | If true, the import of this order won&#39;t adjust the stock level at billbee. |  [optional] |
|**getPriceFromArticleIfAny** | **Boolean** | If true, the price will be overwritten by the known article price in billbee if available |  [optional] |
|**invoiceSKU** | **String** | Contains the SKU from OrderDetail (if available) or from Product |  [optional] |
|**isCoupon** | **Boolean** | Determines if it is a coupon, which is interpreted as tax-free payment |  [optional] |
|**product** | [**BillbeeInterfacesBillbeeAPIModelSoldProduct**](BillbeeInterfacesBillbeeAPIModelSoldProduct.md) |  |  [optional] |
|**quantity** | **Double** | The sold quantity |  [optional] |
|**serialNumber** | **String** | Contains the used serial number |  [optional] |
|**shippingProfileId** | **String** | Determines if it is a coupon, which is interpreted as tax-free payment |  [optional] |
|**taxAmount** | **Double** | The tax amount in the total price |  [optional] |
|**taxIndex** | **Integer** | The tax index. |  [optional] |
|**totalPrice** | **Double** | The total price (unit price * quantity) |  [optional] |
|**transactionId** | **String** | Id of the individual transaction. Only required by Ebay to detect aggregated orders |  [optional] |
|**unrebatedTotalPrice** | **Double** | Is just used for the billbee api |  [optional] |



