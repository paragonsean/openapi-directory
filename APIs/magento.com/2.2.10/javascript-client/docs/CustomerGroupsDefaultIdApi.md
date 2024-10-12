# MagentoB2B.CustomerGroupsDefaultIdApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerCustomerGroupConfigV1SetDefaultCustomerGroupPut**](CustomerGroupsDefaultIdApi.md#customerCustomerGroupConfigV1SetDefaultCustomerGroupPut) | **PUT** /V1/customerGroups/default/{id} | customerGroups/default/{id}



## customerCustomerGroupConfigV1SetDefaultCustomerGroupPut

> Number customerCustomerGroupConfigV1SetDefaultCustomerGroupPut(id)

customerGroups/default/{id}

Set system default customer group.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomerGroupsDefaultIdApi();
let id = 56; // Number | 
apiInstance.customerCustomerGroupConfigV1SetDefaultCustomerGroupPut(id, (error, data, response) => {
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

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

