# MagentoB2B.CartsMineCollectionPointSearchResultApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temandoShippingCollectionPointCartCollectionPointManagementV1GetCollectionPointsGet**](CartsMineCollectionPointSearchResultApi.md#temandoShippingCollectionPointCartCollectionPointManagementV1GetCollectionPointsGet) | **GET** /V1/carts/mine/collection-point/search-result | carts/mine/collection-point/search-result



## temandoShippingCollectionPointCartCollectionPointManagementV1GetCollectionPointsGet

> [TemandoShippingDataCollectionPointQuoteCollectionPointInterface] temandoShippingCollectionPointCartCollectionPointManagementV1GetCollectionPointsGet()

carts/mine/collection-point/search-result



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineCollectionPointSearchResultApi();
apiInstance.temandoShippingCollectionPointCartCollectionPointManagementV1GetCollectionPointsGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[TemandoShippingDataCollectionPointQuoteCollectionPointInterface]**](TemandoShippingDataCollectionPointQuoteCollectionPointInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

