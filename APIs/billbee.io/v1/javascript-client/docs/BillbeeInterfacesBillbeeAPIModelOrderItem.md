# BillbeeApi.BillbeeInterfacesBillbeeAPIModelOrderItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**[BillbeeInterfacesBillbeeAPIModelOrderItemAttribute]**](BillbeeInterfacesBillbeeAPIModelOrderItemAttribute.md) | A list of product attributes for this position | [optional] 
**billbeeId** | **Number** | The billbee id of this item | [optional] 
**discount** | **Number** | Sets the discount in percent | [optional] 
**dontAdjustStock** | **Boolean** | If true, the import of this order won&#39;t adjust the stock level at billbee. | [optional] 
**getPriceFromArticleIfAny** | **Boolean** | If true, the price will be overwritten by the known article price in billbee if available | [optional] 
**invoiceSKU** | **String** | Contains the SKU from OrderDetail (if available) or from Product | [optional] 
**isCoupon** | **Boolean** | Determines if it is a coupon, which is interpreted as tax-free payment | [optional] 
**product** | [**BillbeeInterfacesBillbeeAPIModelSoldProduct**](BillbeeInterfacesBillbeeAPIModelSoldProduct.md) |  | [optional] 
**quantity** | **Number** | The sold quantity | [optional] 
**serialNumber** | **String** | Contains the used serial number | [optional] 
**shippingProfileId** | **String** | Determines if it is a coupon, which is interpreted as tax-free payment | [optional] 
**taxAmount** | **Number** | The tax amount in the total price | [optional] 
**taxIndex** | **Number** | The tax index. | [optional] 
**totalPrice** | **Number** | The total price (unit price * quantity) | [optional] 
**transactionId** | **String** | Id of the individual transaction. Only required by Ebay to detect aggregated orders | [optional] 
**unrebatedTotalPrice** | **Number** | Is just used for the billbee api | [optional] 


