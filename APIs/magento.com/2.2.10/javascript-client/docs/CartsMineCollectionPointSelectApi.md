# MagentoB2B.CartsMineCollectionPointSelectApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPost**](CartsMineCollectionPointSelectApi.md#temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPost) | **POST** /V1/carts/mine/collection-point/select | carts/mine/collection-point/select



## temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPost

> Boolean temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPost(opts)

carts/mine/collection-point/select



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CartsMineCollectionPointSelectApi();
let opts = {
  'temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest': new MagentoB2B.TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest() // TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest | 
};
apiInstance.temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPost(opts, (error, data, response) => {
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
 **temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest** | [**TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest**](TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

