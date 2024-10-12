# MagentoB2B.CustomerGroupsDefaultApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerGroupManagementV1GetDefaultGroupGet**](CustomerGroupsDefaultApi.md#customerGroupManagementV1GetDefaultGroupGet) | **GET** /V1/customerGroups/default | customerGroups/default



## customerGroupManagementV1GetDefaultGroupGet

> CustomerDataGroupInterface customerGroupManagementV1GetDefaultGroupGet(opts)

customerGroups/default

Get default customer group.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomerGroupsDefaultApi();
let opts = {
  'storeId': 56 // Number | 
};
apiInstance.customerGroupManagementV1GetDefaultGroupGet(opts, (error, data, response) => {
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
 **storeId** | **Number**|  | [optional] 

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

