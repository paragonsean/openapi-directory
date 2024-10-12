# MagentoB2B.IntegrationAdminTokenApi

All URIs are relative to *https://example.com/rest/default*

Method | HTTP request | Description
------------- | ------------- | -------------
[**integrationAdminTokenServiceV1CreateAdminAccessTokenPost**](IntegrationAdminTokenApi.md#integrationAdminTokenServiceV1CreateAdminAccessTokenPost) | **POST** /V1/integration/admin/token | integration/admin/token



## integrationAdminTokenServiceV1CreateAdminAccessTokenPost

> String integrationAdminTokenServiceV1CreateAdminAccessTokenPost(opts)

integration/admin/token

Create access token for admin given the admin credentials.

### Example

```javascript
import MagentoB2B from 'magento_b2_b';

let apiInstance = new MagentoB2B.IntegrationAdminTokenApi();
let opts = {
  'integrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest': new MagentoB2B.IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest() // IntegrationAdminTokenServiceV1CreateAdminAccessTokenPostRequest | 
};
apiInstance.integrationAdminTokenServiceV1CreateAdminAccessTokenPost(opts, (error, data, response) => {
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

