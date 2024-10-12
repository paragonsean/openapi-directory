# MagentoB2B.GiftWrappingsWrappingIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**giftWrappingWrappingRepositoryV1SavePut**](GiftWrappingsWrappingIdApi.md#giftWrappingWrappingRepositoryV1SavePut) | **PUT** /V1/gift-wrappings/{wrappingId} | gift-wrappings/{wrappingId}



## giftWrappingWrappingRepositoryV1SavePut

> GiftWrappingDataWrappingInterface giftWrappingWrappingRepositoryV1SavePut(wrappingId, opts)

gift-wrappings/{wrappingId}

Create/Update new gift wrapping with data object values

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.GiftWrappingsWrappingIdApi();
let wrappingId = "wrappingId_example"; // String | 
let opts = {
  'giftWrappingWrappingRepositoryV1SavePostRequest': new MagentoB2B.GiftWrappingWrappingRepositoryV1SavePostRequest() // GiftWrappingWrappingRepositoryV1SavePostRequest | 
};
apiInstance.giftWrappingWrappingRepositoryV1SavePut(wrappingId, opts, (error, data, response) => {
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
 **wrappingId** | **String**|  | 
 **giftWrappingWrappingRepositoryV1SavePostRequest** | [**GiftWrappingWrappingRepositoryV1SavePostRequest**](GiftWrappingWrappingRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**GiftWrappingDataWrappingInterface**](GiftWrappingDataWrappingInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

