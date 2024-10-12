# MagentoB2B.CustomerGroupsIdPermissionsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerGroupManagementV1IsReadonlyGet**](CustomerGroupsIdPermissionsApi.md#customerGroupManagementV1IsReadonlyGet) | **GET** /V1/customerGroups/{id}/permissions | customerGroups/{id}/permissions



## customerGroupManagementV1IsReadonlyGet

> Boolean customerGroupManagementV1IsReadonlyGet(id)

customerGroups/{id}/permissions

Check if customer group can be deleted.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomerGroupsIdPermissionsApi();
let id = 56; // Number | 
apiInstance.customerGroupManagementV1IsReadonlyGet(id, (error, data, response) => {
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

