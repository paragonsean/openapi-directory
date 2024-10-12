# MagentoB2B.GiftWrappingsIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftWrappingWrappingRepositoryV1DeleteByIdDelete**](GiftWrappingsIdApi.md#giftWrappingWrappingRepositoryV1DeleteByIdDelete) | **DELETE** /V1/gift-wrappings/{id} | gift-wrappings/{id}
[**giftWrappingWrappingRepositoryV1GetGet**](GiftWrappingsIdApi.md#giftWrappingWrappingRepositoryV1GetGet) | **GET** /V1/gift-wrappings/{id} | gift-wrappings/{id}



## giftWrappingWrappingRepositoryV1DeleteByIdDelete

> Boolean giftWrappingWrappingRepositoryV1DeleteByIdDelete(id)

gift-wrappings/{id}

Delete gift wrapping

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GiftWrappingsIdApi();
let id = 56; // Number | 
apiInstance.giftWrappingWrappingRepositoryV1DeleteByIdDelete(id, (error, data, response) => {
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
 **id** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## giftWrappingWrappingRepositoryV1GetGet

> GiftWrappingDataWrappingInterface giftWrappingWrappingRepositoryV1GetGet(id, opts)

gift-wrappings/{id}

Return data object for specified wrapping ID and store.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GiftWrappingsIdApi();
let id = 56; // Number | 
let opts = {
  'storeId': 56 // Number | 
};
apiInstance.giftWrappingWrappingRepositoryV1GetGet(id, opts, (error, data, response) => {
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
 **id** | **Number**|  | 
 **storeId** | **Number**|  | [optional] 

### Return type

[**GiftWrappingDataWrappingInterface**](GiftWrappingDataWrappingInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

