# AccountApi.DefaultApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/provisioning*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accountCtrlGetAccountServicesByAccountID**](DefaultApi.md#accountCtrlGetAccountServicesByAccountID) | **GET** /api/accounts/{account_id} | Get account data by ID
[**accountCtrlGetLocationByID**](DefaultApi.md#accountCtrlGetLocationByID) | **GET** /api/accounts/{account_id}/locations/{location_id} | Get location data by account ID and location ID
[**accountCtrlGetLocationsByAccountID**](DefaultApi.md#accountCtrlGetLocationsByAccountID) | **GET** /api/accounts/{account_id}/locations | Get account locations data by account ID



## accountCtrlGetAccountServicesByAccountID

> AccountHalResponse accountCtrlGetAccountServicesByAccountID(accountId)

Get account data by ID

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure Bearer (OAuth) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AccountApi.DefaultApi();
let accountId = 571700; // Number | The Vonage Business Cloud account ID
apiInstance.accountCtrlGetAccountServicesByAccountID(accountId, (error, data, response) => {
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
 **accountId** | **Number**| The Vonage Business Cloud account ID | 

### Return type

[**AccountHalResponse**](AccountHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountCtrlGetLocationByID

> LocationHalResponse accountCtrlGetLocationByID(accountId, locationId)

Get location data by account ID and location ID

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure Bearer (OAuth) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AccountApi.DefaultApi();
let accountId = 571700; // Number | The Vonage Business Cloud account ID
let locationId = 327910; // Number | The Vonage Business Cloud location ID
apiInstance.accountCtrlGetLocationByID(accountId, locationId, (error, data, response) => {
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
 **accountId** | **Number**| The Vonage Business Cloud account ID | 
 **locationId** | **Number**| The Vonage Business Cloud location ID | 

### Return type

[**LocationHalResponse**](LocationHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## accountCtrlGetLocationsByAccountID

> LocationsHalResponse accountCtrlGetLocationsByAccountID(accountId)

Get account locations data by account ID

### Example

```javascript
import AccountApi from 'account_api';
let defaultClient = AccountApi.ApiClient.instance;
// Configure Bearer (OAuth) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AccountApi.DefaultApi();
let accountId = 571700; // Number | The Vonage Business Cloud account ID
apiInstance.accountCtrlGetLocationsByAccountID(accountId, (error, data, response) => {
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
 **accountId** | **Number**| The Vonage Business Cloud account ID | 

### Return type

[**LocationsHalResponse**](LocationsHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

