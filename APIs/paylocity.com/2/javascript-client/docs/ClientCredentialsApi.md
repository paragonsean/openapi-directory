# PaylocityApi.ClientCredentialsApi

All URIs are relative to *https://api.paylocity.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addClientSecret**](ClientCredentialsApi.md#addClientSecret) | **POST** /v2/credentials/secrets | Obtain new client secret.



## addClientSecret

> [ClientCredentialsResponse] addClientSecret(addClientSecret)

Obtain new client secret.

Obtain new client secret for Paylocity-issued client id. See Setup section for details.

### Example

```javascript
import PaylocityApi from 'paylocity_api';
let defaultClient = PaylocityApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: paylocity_auth
let paylocity_auth = defaultClient.authentications['paylocity_auth'];
paylocity_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new PaylocityApi.ClientCredentialsApi();
let addClientSecret = new PaylocityApi.AddClientSecret(); // AddClientSecret | Add Client Secret Model
apiInstance.addClientSecret(addClientSecret, (error, data, response) => {
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
 **addClientSecret** | [**AddClientSecret**](AddClientSecret.md)| Add Client Secret Model | 

### Return type

[**[ClientCredentialsResponse]**](ClientCredentialsResponse.md)

### Authorization

[paylocity_auth](../README.md#paylocity_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

