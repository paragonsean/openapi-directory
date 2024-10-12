# MagentoB2B.GuestCartsCartIdCollectionPointSelectApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**temandoShippingCollectionPointGuestCartCollectionPointManagementV1SelectCollectionPointPost**](GuestCartsCartIdCollectionPointSelectApi.md#temandoShippingCollectionPointGuestCartCollectionPointManagementV1SelectCollectionPointPost) | **POST** /V1/guest-carts/{cartId}/collection-point/select | guest-carts/{cartId}/collection-point/select



## temandoShippingCollectionPointGuestCartCollectionPointManagementV1SelectCollectionPointPost

> Boolean temandoShippingCollectionPointGuestCartCollectionPointManagementV1SelectCollectionPointPost(cartId, opts)

guest-carts/{cartId}/collection-point/select



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GuestCartsCartIdCollectionPointSelectApi();
let cartId = "cartId_example"; // String | 
let opts = {
  'temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest': new MagentoB2B.TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest() // TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest | 
};
apiInstance.temandoShippingCollectionPointGuestCartCollectionPointManagementV1SelectCollectionPointPost(cartId, opts, (error, data, response) => {
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
 **temandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest** | [**TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest**](TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

