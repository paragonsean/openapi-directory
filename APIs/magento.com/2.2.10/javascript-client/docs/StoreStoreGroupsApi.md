# MagentoB2B.StoreStoreGroupsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storeGroupRepositoryV1GetListGet**](StoreStoreGroupsApi.md#storeGroupRepositoryV1GetListGet) | **GET** /V1/store/storeGroups | store/storeGroups



## storeGroupRepositoryV1GetListGet

> [StoreDataGroupInterface] storeGroupRepositoryV1GetListGet()

store/storeGroups

Retrieve list of all groups

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.StoreStoreGroupsApi();
apiInstance.storeGroupRepositoryV1GetListGet((error, data, response) => {
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

[**[StoreDataGroupInterface]**](StoreDataGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

