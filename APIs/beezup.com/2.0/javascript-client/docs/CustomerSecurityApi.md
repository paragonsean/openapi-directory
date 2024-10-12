# BeezUpMerchantApi.CustomerSecurityApi

All URIs are relative to *https://api.beezup.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**logout**](CustomerSecurityApi.md#logout) | **POST** /v2/user/customer/security/logout | Log out the current user from go2
[**zendeskToken**](CustomerSecurityApi.md#zendeskToken) | **GET** /v2/user/customer/zendeskToken | Zendesk token



## logout

> logout()

Log out the current user from go2

Log out the current user from go2

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerSecurityApi();
apiInstance.logout((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## zendeskToken

> ZendeskToken zendeskToken()

Zendesk token

Zendesk token - Generates a JWT token to access BeezUP restricted Help Center in SSO as described here: https://support.zendesk.com/hc/en-us/articles/222874768-Using-restricted-Help-Center-content-with-the-Web-Widget

### Example

```javascript
import BeezUpMerchantApi from 'beez_up_merchant_api_';

let apiInstance = new BeezUpMerchantApi.CustomerSecurityApi();
apiInstance.zendeskToken((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ZendeskToken**](ZendeskToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

