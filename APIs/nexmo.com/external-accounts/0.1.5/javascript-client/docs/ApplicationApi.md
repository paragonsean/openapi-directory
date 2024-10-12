# ExternalAccountsApi.ApplicationApi

All URIs are relative to *https://api.nexmo.com/beta/chatapp-accounts*

Method | HTTP request | Description
------------- | ------------- | -------------
[**linkApplication**](ApplicationApi.md#linkApplication) | **POST** /{provider}/{external_id}/applications | Link application to an account
[**unliWithoutApplicationnkApplication**](ApplicationApi.md#unliWithoutApplicationnkApplication) | **DELETE** /{provider}/{external_id}/applications/{application_id} | Unlink application from an account



## linkApplication

> AccountResponse linkApplication(provider, externalId, linkApplicationRequest)

Link application to an account

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

let apiInstance = new ExternalAccountsApi.ApplicationApi();
let provider = "provider_example"; // String | Provider of the account you want to assign an application to
let externalId = "externalId_example"; // String | External id of the account you want to assign an application to. This is channel dependent. For Facebook it will be your Facebook Page ID, for Viber your Viber Service Message ID and for WhatsApp your WhatsApp number.
let linkApplicationRequest = new ExternalAccountsApi.LinkApplicationRequest(); // LinkApplicationRequest | Request body can contain any of the following. Please note, the only one application can be linked to the account.
apiInstance.linkApplication(provider, externalId, linkApplicationRequest, (error, data, response) => {
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
 **provider** | **String**| Provider of the account you want to assign an application to | 
 **externalId** | **String**| External id of the account you want to assign an application to. This is channel dependent. For Facebook it will be your Facebook Page ID, for Viber your Viber Service Message ID and for WhatsApp your WhatsApp number. | 
 **linkApplicationRequest** | [**LinkApplicationRequest**](LinkApplicationRequest.md)| Request body can contain any of the following. Please note, the only one application can be linked to the account. | 

### Return type

[**AccountResponse**](AccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## unliWithoutApplicationnkApplication

> unliWithoutApplicationnkApplication(provider, externalId, applicationId)

Unlink application from an account

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

let apiInstance = new ExternalAccountsApi.ApplicationApi();
let provider = "provider_example"; // String | Provider of the account you want to unlink an application from
let externalId = "externalId_example"; // String | External id of the account you want to unlink an application from
let applicationId = "applicationId_example"; // String | Id of the application you want to unlink
apiInstance.unliWithoutApplicationnkApplication(provider, externalId, applicationId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **String**| Provider of the account you want to unlink an application from | 
 **externalId** | **String**| External id of the account you want to unlink an application from | 
 **applicationId** | **String**| Id of the application you want to unlink | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

