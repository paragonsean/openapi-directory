# MagentoB2B.StoreStoreViewsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storeStoreRepositoryV1GetListGet**](StoreStoreViewsApi.md#storeStoreRepositoryV1GetListGet) | **GET** /V1/store/storeViews | store/storeViews



## storeStoreRepositoryV1GetListGet

> [StoreDataStoreInterface] storeStoreRepositoryV1GetListGet()

store/storeViews

Retrieve list of all stores

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.StoreStoreViewsApi();
apiInstance.storeStoreRepositoryV1GetListGet((error, data, response) => {
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

[**[StoreDataStoreInterface]**](StoreDataStoreInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

