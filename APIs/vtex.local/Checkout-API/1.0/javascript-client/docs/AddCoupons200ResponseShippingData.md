# CheckoutApi.AddCoupons200ResponseShippingData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**AddCoupons200ResponseShippingDataAddress**](AddCoupons200ResponseShippingDataAddress.md) |  | [optional] 
**availableAddresses** | [**[AddCoupons200ResponseShippingDataAvailableAddressesInner]**](AddCoupons200ResponseShippingDataAvailableAddressesInner.md) | Array with information on the available addresses for the order. | [optional] 
**logisticsInfo** | [**[AddCoupons200ResponseShippingDataLogisticsInfoInner]**](AddCoupons200ResponseShippingDataLogisticsInfoInner.md) | Array with logistics information. Each object in this array corresponds to an object in the &#x60;items&#x60; array, based on the respective &#x60;itemIndex&#x60;. | [optional] 
**selectedAddresses** | [**[AddCoupons200ResponseShippingDataAvailableAddressesInner]**](AddCoupons200ResponseShippingDataAvailableAddressesInner.md) | Array with information on the selected addresses for the order. | [optional] 


