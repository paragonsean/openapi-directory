# ExternalAccountsApi.WhatsAppApi

All URIs are relative to *https://api.nexmo.com/beta/chatapp-accounts*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getWAAccount**](WhatsAppApi.md#getWAAccount) | **GET** /whatsapp/{external_id} | Retrieve a Whatsapp account



## getWAAccount

> WAAccountResponse getWAAccount(externalId)

Retrieve a Whatsapp account

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

let apiInstance = new ExternalAccountsApi.WhatsAppApi();
let externalId = "externalId_example"; // String | External id of the account you want to retrieve. In this case it will be the WhatsApp number.
apiInstance.getWAAccount(externalId, (error, data, response) => {
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
 **externalId** | **String**| External id of the account you want to retrieve. In this case it will be the WhatsApp number. | 

### Return type

[**WAAccountResponse**](WAAccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

