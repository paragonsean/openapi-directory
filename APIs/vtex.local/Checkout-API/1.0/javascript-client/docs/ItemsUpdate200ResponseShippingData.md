# CheckoutApi.ItemsUpdate200ResponseShippingData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**ItemsUpdate200ResponseShippingDataAddress**](ItemsUpdate200ResponseShippingDataAddress.md) |  | [optional] 
**availableAddresses** | [**[ItemsUpdate200ResponseShippingDataAvailableAddressesInner]**](ItemsUpdate200ResponseShippingDataAvailableAddressesInner.md) | Array with information on the available addresses for the order. | [optional] 
**logisticsInfo** | [**[ItemsUpdate200ResponseShippingDataLogisticsInfoInner]**](ItemsUpdate200ResponseShippingDataLogisticsInfoInner.md) | Array with logistics information. Each object in this array corresponds to an object in the &#x60;items&#x60; array, based on the respective &#x60;itemIndex&#x60;. | [optional] 
**selectedAddresses** | [**[ItemsUpdate200ResponseShippingDataAvailableAddressesInner]**](ItemsUpdate200ResponseShippingDataAvailableAddressesInner.md) | Array with information on the selected addresses for the order. | [optional] 


