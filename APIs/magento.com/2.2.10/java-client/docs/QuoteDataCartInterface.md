

# QuoteDataCartInterface

Interface CartInterface

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAddress** | [**QuoteDataAddressInterface**](QuoteDataAddressInterface.md) |  |  [optional] |
|**convertedAt** | **String** | Cart conversion date and time. Otherwise, null. |  [optional] |
|**createdAt** | **String** | Cart creation date and time. Otherwise, null. |  [optional] |
|**currency** | [**QuoteDataCurrencyInterface**](QuoteDataCurrencyInterface.md) |  |  [optional] |
|**customer** | [**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md) |  |  |
|**customerIsGuest** | **Boolean** | For guest customers, false for logged in customers |  [optional] |
|**customerNote** | **String** | Notice text |  [optional] |
|**customerNoteNotify** | **Boolean** | Customer notification flag |  [optional] |
|**customerTaxClassId** | **Integer** | Customer tax class ID. |  [optional] |
|**extensionAttributes** | [**QuoteDataCartExtensionInterface**](QuoteDataCartExtensionInterface.md) |  |  [optional] |
|**id** | **Integer** | Cart/quote ID. |  |
|**isActive** | **Boolean** | Active status flag value. Otherwise, null. |  [optional] |
|**isVirtual** | **Boolean** | Virtual flag value. Otherwise, null. |  [optional] |
|**items** | [**List&lt;QuoteDataCartItemInterface&gt;**](QuoteDataCartItemInterface.md) | Array of items. Otherwise, null. |  [optional] |
|**itemsCount** | **Integer** | Number of different items or products in the cart. Otherwise, null. |  [optional] |
|**itemsQty** | **BigDecimal** | Total quantity of all cart items. Otherwise, null. |  [optional] |
|**origOrderId** | **Integer** | Original order ID. Otherwise, null. |  [optional] |
|**reservedOrderId** | **String** | Reserved order ID. Otherwise, null. |  [optional] |
|**storeId** | **Integer** | Store identifier |  |
|**updatedAt** | **String** | Cart last update date and time. Otherwise, null. |  [optional] |



