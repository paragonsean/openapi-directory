# MagentoB2B.CustomerGroupsDefaultStoreIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1CustomerGroupsDefaultStoreIdGet**](CustomerGroupsDefaultStoreIdApi.md#v1CustomerGroupsDefaultStoreIdGet) | **GET** /V1/customerGroups/default/{storeId} | customerGroups/default/{storeId}



## v1CustomerGroupsDefaultStoreIdGet

> CustomerDataGroupInterface v1CustomerGroupsDefaultStoreIdGet(storeId)

customerGroups/default/{storeId}

Get default customer group.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomerGroupsDefaultStoreIdApi();
let storeId = 56; // Number | 
apiInstance.v1CustomerGroupsDefaultStoreIdGet(storeId, (error, data, response) => {
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
 **storeId** | **Number**|  | 

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

