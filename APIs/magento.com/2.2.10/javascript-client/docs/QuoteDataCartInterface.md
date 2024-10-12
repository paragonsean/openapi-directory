# MagentoB2B.QuoteDataCartInterface

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAddress** | [**QuoteDataAddressInterface**](QuoteDataAddressInterface.md) |  | [optional] 
**convertedAt** | **String** | Cart conversion date and time. Otherwise, null. | [optional] 
**createdAt** | **String** | Cart creation date and time. Otherwise, null. | [optional] 
**currency** | [**QuoteDataCurrencyInterface**](QuoteDataCurrencyInterface.md) |  | [optional] 
**customer** | [**CustomerDataCustomerInterface**](CustomerDataCustomerInterface.md) |  | 
**customerIsGuest** | **Boolean** | For guest customers, false for logged in customers | [optional] 
**customerNote** | **String** | Notice text | [optional] 
**customerNoteNotify** | **Boolean** | Customer notification flag | [optional] 
**customerTaxClassId** | **Number** | Customer tax class ID. | [optional] 
**extensionAttributes** | [**QuoteDataCartExtensionInterface**](QuoteDataCartExtensionInterface.md) |  | [optional] 
**id** | **Number** | Cart/quote ID. | 
**isActive** | **Boolean** | Active status flag value. Otherwise, null. | [optional] 
**isVirtual** | **Boolean** | Virtual flag value. Otherwise, null. | [optional] 
**items** | [**[QuoteDataCartItemInterface]**](QuoteDataCartItemInterface.md) | Array of items. Otherwise, null. | [optional] 
**itemsCount** | **Number** | Number of different items or products in the cart. Otherwise, null. | [optional] 
**itemsQty** | **Number** | Total quantity of all cart items. Otherwise, null. | [optional] 
**origOrderId** | **Number** | Original order ID. Otherwise, null. | [optional] 
**reservedOrderId** | **String** | Reserved order ID. Otherwise, null. | [optional] 
**storeId** | **Number** | Store identifier | 
**updatedAt** | **String** | Cart last update date and time. Otherwise, null. | [optional] 


