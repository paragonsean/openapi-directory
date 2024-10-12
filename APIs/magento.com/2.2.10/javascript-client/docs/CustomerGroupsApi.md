# MagentoB2B.CustomerGroupsApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerGroupRepositoryV1SavePost**](CustomerGroupsApi.md#customerGroupRepositoryV1SavePost) | **POST** /V1/customerGroups | customerGroups



## customerGroupRepositoryV1SavePost

> CustomerDataGroupInterface customerGroupRepositoryV1SavePost(opts)

customerGroups

Save customer group.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomerGroupsApi();
let opts = {
  'customerGroupRepositoryV1SavePostRequest': new MagentoB2B.CustomerGroupRepositoryV1SavePostRequest() // CustomerGroupRepositoryV1SavePostRequest | 
};
apiInstance.customerGroupRepositoryV1SavePost(opts, (error, data, response) => {
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
 **customerGroupRepositoryV1SavePostRequest** | [**CustomerGroupRepositoryV1SavePostRequest**](CustomerGroupRepositoryV1SavePostRequest.md)|  | [optional] 

### Return type

[**CustomerDataGroupInterface**](CustomerDataGroupInterface.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

