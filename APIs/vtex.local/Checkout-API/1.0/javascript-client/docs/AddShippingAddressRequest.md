# CheckoutApi.AddShippingAddressRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clearAddressIfPostalCodeNotFound** | **Boolean** | This field should be sent as &#x60;false&#x60; to prevent the address information from being filled in automatically based on the &#x60;postalCode&#x60; information. | [optional] 
**logisticsInfo** | [**[AddShippingAddressRequestLogisticsInfoInner]**](AddShippingAddressRequestLogisticsInfoInner.md) | Array with logistics information on each item of the &#x60;items&#x60; array in the &#x60;orderForm&#x60;. | [optional] 
**selectedAddresses** | [**[AddShippingAddressRequestSelectedAddressesInner]**](AddShippingAddressRequestSelectedAddressesInner.md) | List of objects with addresses information. | [optional] 


