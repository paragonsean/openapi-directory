# MagentoB2B.CartsMineCollectionPointSearchRequestApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temandoShippingCollectionPointCartCollectionPointManagementV1DeleteSearchRequestDelete**](CartsMineCollectionPointSearchRequestApi.md#temandoShippingCollectionPointCartCollectionPointManagementV1DeleteSearchRequestDelete) | **DELETE** /V1/carts/mine/collection-point/search-request | carts/mine/collection-point/search-request
[**temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPut**](CartsMineCollectionPointSearchRequestApi.md#temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPut) | **PUT** /V1/carts/mine/collection-point/search-request | carts/mine/collection-point/search-request



## temandoShippingCollectionPointCartCollectionPointManagementV1DeleteSearchRequestDelete

> Boolean temandoShippingCollectionPointCartCollectionPointManagementV1DeleteSearchRequestDelete()

carts/mine/collection-point/search-request



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineCollectionPointSearchRequestApi();
apiInstance.temandoShippingCollectionPointCartCollectionPointManagementV1DeleteSearchRequestDelete((error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPut

> TemandoShippingDataCollectionPointSearchRequestInterface temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPut(opts)

carts/mine/collection-point/search-request



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineCollectionPointSearchRequestApi();
let opts = {
  'temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest': new MagentoB2B.TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest() // TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest | 
};
apiInstance.temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPut(opts, (error, data, response) => {
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
 **temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest** | [**TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest**](TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest.md)|  | [optional] 

### Return type

[**TemandoShippingDataCollectionPointSearchRequestInterface**](TemandoShippingDataCollectionPointSearchRequestInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

