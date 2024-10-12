# MagentoB2B.CustomersCustomerIdPermissionsReadonlyApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1IsReadonlyGet**](CustomersCustomerIdPermissionsReadonlyApi.md#customerAccountManagementV1IsReadonlyGet) | **GET** /V1/customers/{customerId}/permissions/readonly | customers/{customerId}/permissions/readonly



## customerAccountManagementV1IsReadonlyGet

> Boolean customerAccountManagementV1IsReadonlyGet(customerId)

customers/{customerId}/permissions/readonly

Check if customer can be deleted.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersCustomerIdPermissionsReadonlyApi();
let customerId = 56; // Number | 
apiInstance.customerAccountManagementV1IsReadonlyGet(customerId, (error, data, response) => {
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
 **customerId** | **Number**|  | 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

