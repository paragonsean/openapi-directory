# MagentoB2B.GuestCartsCartIdCollectionPointSearchResultApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temandoShippingCollectionPointGuestCartCollectionPointManagementV1GetCollectionPointsGet**](GuestCartsCartIdCollectionPointSearchResultApi.md#temandoShippingCollectionPointGuestCartCollectionPointManagementV1GetCollectionPointsGet) | **GET** /V1/guest-carts/{cartId}/collection-point/search-result | guest-carts/{cartId}/collection-point/search-result



## temandoShippingCollectionPointGuestCartCollectionPointManagementV1GetCollectionPointsGet

> [TemandoShippingDataCollectionPointQuoteCollectionPointInterface] temandoShippingCollectionPointGuestCartCollectionPointManagementV1GetCollectionPointsGet(cartId)

guest-carts/{cartId}/collection-point/search-result



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdCollectionPointSearchResultApi();
let cartId = "cartId_example"; // String | 
apiInstance.temandoShippingCollectionPointGuestCartCollectionPointManagementV1GetCollectionPointsGet(cartId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cartId** | **String**|  | 

### Return type

[**[TemandoShippingDataCollectionPointQuoteCollectionPointInterface]**](TemandoShippingDataCollectionPointQuoteCollectionPointInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

