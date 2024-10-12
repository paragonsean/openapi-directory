# MagentoB2B.GuestCartsCartIdCollectionPointSearchRequestApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temandoShippingCollectionPointGuestCartCollectionPointManagementV1DeleteSearchRequestDelete**](GuestCartsCartIdCollectionPointSearchRequestApi.md#temandoShippingCollectionPointGuestCartCollectionPointManagementV1DeleteSearchRequestDelete) | **DELETE** /V1/guest-carts/{cartId}/collection-point/search-request | guest-carts/{cartId}/collection-point/search-request
[**temandoShippingCollectionPointGuestCartCollectionPointManagementV1SaveSearchRequestPut**](GuestCartsCartIdCollectionPointSearchRequestApi.md#temandoShippingCollectionPointGuestCartCollectionPointManagementV1SaveSearchRequestPut) | **PUT** /V1/guest-carts/{cartId}/collection-point/search-request | guest-carts/{cartId}/collection-point/search-request



## temandoShippingCollectionPointGuestCartCollectionPointManagementV1DeleteSearchRequestDelete

> Boolean temandoShippingCollectionPointGuestCartCollectionPointManagementV1DeleteSearchRequestDelete(cartId)

guest-carts/{cartId}/collection-point/search-request



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdCollectionPointSearchRequestApi();
let cartId = "cartId_example"; // String | 
apiInstance.temandoShippingCollectionPointGuestCartCollectionPointManagementV1DeleteSearchRequestDelete(cartId, (error, data, response) => {
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

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## temandoShippingCollectionPointGuestCartCollectionPointManagementV1SaveSearchRequestPut

> TemandoShippingDataCollectionPointSearchRequestInterface temandoShippingCollectionPointGuestCartCollectionPointManagementV1SaveSearchRequestPut(cartId, opts)

guest-carts/{cartId}/collection-point/search-request



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdCollectionPointSearchRequestApi();
let cartId = "cartId_example"; // String | 
let opts = {
  'temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest': new MagentoB2B.TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest() // TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest | 
};
apiInstance.temandoShippingCollectionPointGuestCartCollectionPointManagementV1SaveSearchRequestPut(cartId, opts, (error, data, response) => {
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
 **temandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest** | [**TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest**](TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest.md)|  | [optional] 

### Return type

[**TemandoShippingDataCollectionPointSearchRequestInterface**](TemandoShippingDataCollectionPointSearchRequestInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

