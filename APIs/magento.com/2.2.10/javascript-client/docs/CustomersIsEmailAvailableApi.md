# MagentoB2B.CustomersIsEmailAvailableApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customerAccountManagementV1IsEmailAvailablePost**](CustomersIsEmailAvailableApi.md#customerAccountManagementV1IsEmailAvailablePost) | **POST** /V1/customers/isEmailAvailable | customers/isEmailAvailable



## customerAccountManagementV1IsEmailAvailablePost

> Boolean customerAccountManagementV1IsEmailAvailablePost(opts)

customers/isEmailAvailable

Check if given email is associated with a customer account in given website.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.CustomersIsEmailAvailableApi();
let opts = {
  'customerAccountManagementV1IsEmailAvailablePostRequest': new MagentoB2B.CustomerAccountManagementV1IsEmailAvailablePostRequest() // CustomerAccountManagementV1IsEmailAvailablePostRequest | 
};
apiInstance.customerAccountManagementV1IsEmailAvailablePost(opts, (error, data, response) => {
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
 **customerAccountManagementV1IsEmailAvailablePostRequest** | [**CustomerAccountManagementV1IsEmailAvailablePostRequest**](CustomerAccountManagementV1IsEmailAvailablePostRequest.md)|  | [optional] 

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

