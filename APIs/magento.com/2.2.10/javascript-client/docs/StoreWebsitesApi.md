# MagentoB2B.StoreWebsitesApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storeWebsiteRepositoryV1GetListGet**](StoreWebsitesApi.md#storeWebsiteRepositoryV1GetListGet) | **GET** /V1/store/websites | store/websites



## storeWebsiteRepositoryV1GetListGet

> [StoreDataWebsiteInterface] storeWebsiteRepositoryV1GetListGet()

store/websites

Retrieve list of all websites

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.StoreWebsitesApi();
apiInstance.storeWebsiteRepositoryV1GetListGet((error, data, response) => {
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

[**[StoreDataWebsiteInterface]**](StoreDataWebsiteInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

