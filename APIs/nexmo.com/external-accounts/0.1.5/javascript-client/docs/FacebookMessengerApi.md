# ExternalAccountsApi.FacebookMessengerApi

All URIs are relative to *https://api.nexmo.com/beta/chatapp-accounts*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMessengerAccount**](FacebookMessengerApi.md#createMessengerAccount) | **POST** /messenger | Create a Messenger account
[**deleteMessengerAccount**](FacebookMessengerApi.md#deleteMessengerAccount) | **DELETE** /messenger/{external_id} | Delete a Messenger account
[**getMessengerAccount**](FacebookMessengerApi.md#getMessengerAccount) | **GET** /messenger/{external_id} | Retrieve a Messenger account
[**updateMessengerAccount**](FacebookMessengerApi.md#updateMessengerAccount) | **PATCH** /messenger/{external_id} | Update a Messenger account



## createMessengerAccount

> MessengerAccountResponse createMessengerAccount(createMessengerAccountRequest)

Create a Messenger account

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

let apiInstance = new ExternalAccountsApi.FacebookMessengerApi();
let createMessengerAccountRequest = new ExternalAccountsApi.CreateMessengerAccountRequest(); // CreateMessengerAccountRequest | 
apiInstance.createMessengerAccount(createMessengerAccountRequest, (error, data, response) => {
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
 **createMessengerAccountRequest** | [**CreateMessengerAccountRequest**](CreateMessengerAccountRequest.md)|  | 

### Return type

[**MessengerAccountResponse**](MessengerAccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteMessengerAccount

> deleteMessengerAccount(externalId)

Delete a Messenger account

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

let apiInstance = new ExternalAccountsApi.FacebookMessengerApi();
let externalId = "externalId_example"; // String | External id of the account you want to delete. In this case it is the Facebook Page ID.
apiInstance.deleteMessengerAccount(externalId, (error, data, response) => {
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
 **externalId** | **String**| External id of the account you want to delete. In this case it is the Facebook Page ID. | 

### Return type

null (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMessengerAccount

> MessengerAccountResponse getMessengerAccount(externalId)

Retrieve a Messenger account

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

let apiInstance = new ExternalAccountsApi.FacebookMessengerApi();
let externalId = "externalId_example"; // String | External id of the account you want to retrieve. In this case it is the Facebook Page ID.
apiInstance.getMessengerAccount(externalId, (error, data, response) => {
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
 **externalId** | **String**| External id of the account you want to retrieve. In this case it is the Facebook Page ID. | 

### Return type

[**MessengerAccountResponse**](MessengerAccountResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMessengerAccount

> UpdateMessengerAccount200Response updateMessengerAccount(externalId, updateMessengerAccountRequest)

Update a Messenger account

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

let apiInstance = new ExternalAccountsApi.FacebookMessengerApi();
let externalId = "externalId_example"; // String | External id of the account you want to update. In this case it is the Facebook Page ID.
let updateMessengerAccountRequest = new ExternalAccountsApi.UpdateMessengerAccountRequest(); // UpdateMessengerAccountRequest | Request body can contain any of the following
apiInstance.updateMessengerAccount(externalId, updateMessengerAccountRequest, (error, data, response) => {
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
 **externalId** | **String**| External id of the account you want to update. In this case it is the Facebook Page ID. | 
 **updateMessengerAccountRequest** | [**UpdateMessengerAccountRequest**](UpdateMessengerAccountRequest.md)| Request body can contain any of the following | 

### Return type

[**UpdateMessengerAccount200Response**](UpdateMessengerAccount200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth), [bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

