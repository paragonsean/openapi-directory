# ExternalAccountsApi.ViberServiceMessageApi

All URIs are relative to *https://api.nexmo.com/beta/chatapp-accounts*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getVSMAccount**](ViberServiceMessageApi.md#getVSMAccount) | **GET** /viber_service_msg/{external_id} | Retrieve a Viber Service Message account



## getVSMAccount

> VSMAccountResponse getVSMAccount(externalId)

Retrieve a Viber Service Message account

### Example

```javascript
import ExternalAccountsApi from 'external_accounts_api';
let defaultClient = ExternalAccountsApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ExternalAccountsApi.ViberServiceMessageApi();
let externalId = "externalId_example"; // String | External id of the account you want to retrieve. In this case it will be your Viber Service Message ID.
apiInstance.getVSMAccount(externalId, (error, data, response) => {
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
 **externalId** | **String**| External id of the account you want to retrieve. In this case it will be your Viber Service Message ID. | 

### Return type

[**VSMAccountResponse**](VSMAccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

