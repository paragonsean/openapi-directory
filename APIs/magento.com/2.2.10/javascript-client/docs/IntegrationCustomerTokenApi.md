# MagentoB2B.IntegrationCustomerTokenApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationCustomerTokenServiceV1CreateCustomerAccessTokenPost**](IntegrationCustomerTokenApi.md#integrationCustomerTokenServiceV1CreateCustomerAccessTokenPost) | **POST** /V1/integration/customer/token | integration/customer/token



## integrationCustomerTokenServiceV1CreateCustomerAccessTokenPost

> String integrationCustomerTokenServiceV1CreateCustomerAccessTokenPost(opts)

integration/customer/token

Create access token for admin given the customer credentials.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.IntegrationCustomerTokenApi();
let opts = {
  'integrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest': new MagentoB2B.IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest() // IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest | 
};
apiInstance.integrationCustomerTokenServiceV1CreateCustomerAccessTokenPost(opts, (error, data, response) => {
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
 **integrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest** | [**IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest**](IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest.md)|  | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

