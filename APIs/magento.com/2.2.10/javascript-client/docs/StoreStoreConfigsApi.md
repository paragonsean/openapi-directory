# MagentoB2B.StoreStoreConfigsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**storeStoreConfigManagerV1GetStoreConfigsGet**](StoreStoreConfigsApi.md#storeStoreConfigManagerV1GetStoreConfigsGet) | **GET** /V1/store/storeConfigs | store/storeConfigs



## storeStoreConfigManagerV1GetStoreConfigsGet

> [StoreDataStoreConfigInterface] storeStoreConfigManagerV1GetStoreConfigsGet(opts)

store/storeConfigs



### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.StoreStoreConfigsApi();
let opts = {
  'storeCodes': ["null"] // [String] | 
};
apiInstance.storeStoreConfigManagerV1GetStoreConfigsGet(opts, (error, data, response) => {
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
 **storeCodes** | [**[String]**](String.md)|  | [optional] 

### Return type

[**[StoreDataStoreConfigInterface]**](StoreDataStoreConfigInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

