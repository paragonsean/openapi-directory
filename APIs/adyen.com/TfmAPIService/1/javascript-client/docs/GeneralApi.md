# PosTerminalManagementApi.GeneralApi

All URIs are relative to *https://postfmapi-test.adyen.com/postfmapi/terminal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**postAssignTerminals**](GeneralApi.md#postAssignTerminals) | **POST** /assignTerminals | Assign terminals
[**postFindTerminal**](GeneralApi.md#postFindTerminal) | **POST** /findTerminal | Get the account or store of a terminal
[**postGetStoresUnderAccount**](GeneralApi.md#postGetStoresUnderAccount) | **POST** /getStoresUnderAccount | Get the stores of an account
[**postGetTerminalDetails**](GeneralApi.md#postGetTerminalDetails) | **POST** /getTerminalDetails | Get the details of a terminal
[**postGetTerminalsUnderAccount**](GeneralApi.md#postGetTerminalsUnderAccount) | **POST** /getTerminalsUnderAccount | Get the list of terminals



## postAssignTerminals

> AssignTerminalsResponse postAssignTerminals(opts)

Assign terminals

Assigns one or more payment terminals to a merchant account or a store. You can also use this endpoint to reassign terminals between merchant accounts or stores, and to unassign a terminal and return it to company inventory.

### Example

```javascript
import PosTerminalManagementApi from 'pos_terminal_management_api';
let defaultClient = PosTerminalManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new PosTerminalManagementApi.GeneralApi();
let opts = {
  'assignTerminalsRequest': new PosTerminalManagementApi.AssignTerminalsRequest() // AssignTerminalsRequest | 
};
apiInstance.postAssignTerminals(opts, (error, data, response) => {
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
 **assignTerminalsRequest** | [**AssignTerminalsRequest**](AssignTerminalsRequest.md)|  | [optional] 

### Return type

[**AssignTerminalsResponse**](AssignTerminalsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postFindTerminal

> FindTerminalResponse postFindTerminal(opts)

Get the account or store of a terminal

Returns the company account, merchant account, or store that a payment terminal is assigned to.

### Example

```javascript
import PosTerminalManagementApi from 'pos_terminal_management_api';
let defaultClient = PosTerminalManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new PosTerminalManagementApi.GeneralApi();
let opts = {
  'findTerminalRequest': new PosTerminalManagementApi.FindTerminalRequest() // FindTerminalRequest | 
};
apiInstance.postFindTerminal(opts, (error, data, response) => {
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
 **findTerminalRequest** | [**FindTerminalRequest**](FindTerminalRequest.md)|  | [optional] 

### Return type

[**FindTerminalResponse**](FindTerminalResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postGetStoresUnderAccount

> GetStoresUnderAccountResponse postGetStoresUnderAccount(opts)

Get the stores of an account

Returns a list of stores associated with a company account or a merchant account, including the status of each store.

### Example

```javascript
import PosTerminalManagementApi from 'pos_terminal_management_api';
let defaultClient = PosTerminalManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new PosTerminalManagementApi.GeneralApi();
let opts = {
  'getStoresUnderAccountRequest': new PosTerminalManagementApi.GetStoresUnderAccountRequest() // GetStoresUnderAccountRequest | 
};
apiInstance.postGetStoresUnderAccount(opts, (error, data, response) => {
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
 **getStoresUnderAccountRequest** | [**GetStoresUnderAccountRequest**](GetStoresUnderAccountRequest.md)|  | [optional] 

### Return type

[**GetStoresUnderAccountResponse**](GetStoresUnderAccountResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postGetTerminalDetails

> GetTerminalDetailsResponse postGetTerminalDetails(opts)

Get the details of a terminal

Returns the details of a payment terminal, including where the terminal is assigned to. The response returns the same details that are provided in the terminal list in your Customer Area and in the Terminal Fleet report.

### Example

```javascript
import PosTerminalManagementApi from 'pos_terminal_management_api';
let defaultClient = PosTerminalManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new PosTerminalManagementApi.GeneralApi();
let opts = {
  'getTerminalDetailsRequest': new PosTerminalManagementApi.GetTerminalDetailsRequest() // GetTerminalDetailsRequest | 
};
apiInstance.postGetTerminalDetails(opts, (error, data, response) => {
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
 **getTerminalDetailsRequest** | [**GetTerminalDetailsRequest**](GetTerminalDetailsRequest.md)|  | [optional] 

### Return type

[**GetTerminalDetailsResponse**](GetTerminalDetailsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## postGetTerminalsUnderAccount

> GetTerminalsUnderAccountResponse postGetTerminalsUnderAccount(opts)

Get the list of terminals

Returns a list of payment terminals associated with a company account, merchant account, or store. The response shows whether the terminals are in the inventory, or in-store (ready for boarding or already boarded).

### Example

```javascript
import PosTerminalManagementApi from 'pos_terminal_management_api';
let defaultClient = PosTerminalManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new PosTerminalManagementApi.GeneralApi();
let opts = {
  'getTerminalsUnderAccountRequest': new PosTerminalManagementApi.GetTerminalsUnderAccountRequest() // GetTerminalsUnderAccountRequest | 
};
apiInstance.postGetTerminalsUnderAccount(opts, (error, data, response) => {
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
 **getTerminalsUnderAccountRequest** | [**GetTerminalsUnderAccountRequest**](GetTerminalsUnderAccountRequest.md)|  | [optional] 

### Return type

[**GetTerminalsUnderAccountResponse**](GetTerminalsUnderAccountResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

