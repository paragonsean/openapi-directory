# ManagementApi.TerminalsTerminalLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getTerminals**](TerminalsTerminalLevelApi.md#getTerminals) | **GET** /terminals | Get a list of terminals
[**postTerminalsTerminalIdReassign**](TerminalsTerminalLevelApi.md#postTerminalsTerminalIdReassign) | **POST** /terminals/{terminalId}/reassign | Reassign a terminal



## getTerminals

> ListTerminalsResponse getTerminals(opts)

Get a list of terminals

Returns the payment terminals that the API credential has access to and that match the query parameters.  To make this request, your API credential must have the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API — Terminal actions read

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalsTerminalLevelApi();
let opts = {
  'searchQuery': "searchQuery_example", // String | Returns terminals with an ID that contains the specified string. If present, other query parameters are ignored.
  'otpQuery': "otpQuery_example", // String | Returns one or more terminals associated with the one-time passwords specified in the request. If this query parameter is used, other query parameters are ignored.
  'countries': "countries_example", // String | Returns terminals located in the countries specified by their [two-letter country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2).
  'merchantIds': "merchantIds_example", // String | Returns terminals that belong to the merchant accounts specified by their unique merchant account ID.
  'storeIds': "storeIds_example", // String | Returns terminals that are assigned to the [stores](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores) specified by their unique store ID.
  'brandModels': "brandModels_example", // String | Returns terminals of the [models](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels) specified in the format *brand.model*.
  'pageNumber': 56, // Number | The number of the page to fetch.
  'pageSize': 56 // Number | The number of items to have on a page, maximum 100. The default is 20 items on a page.
};
apiInstance.getTerminals(opts, (error, data, response) => {
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
 **searchQuery** | **String**| Returns terminals with an ID that contains the specified string. If present, other query parameters are ignored. | [optional] 
 **otpQuery** | **String**| Returns one or more terminals associated with the one-time passwords specified in the request. If this query parameter is used, other query parameters are ignored. | [optional] 
 **countries** | **String**| Returns terminals located in the countries specified by their [two-letter country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). | [optional] 
 **merchantIds** | **String**| Returns terminals that belong to the merchant accounts specified by their unique merchant account ID. | [optional] 
 **storeIds** | **String**| Returns terminals that are assigned to the [stores](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores) specified by their unique store ID. | [optional] 
 **brandModels** | **String**| Returns terminals of the [models](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels) specified in the format *brand.model*. | [optional] 
 **pageNumber** | **Number**| The number of the page to fetch. | [optional] 
 **pageSize** | **Number**| The number of items to have on a page, maximum 100. The default is 20 items on a page. | [optional] 

### Return type

[**ListTerminalsResponse**](ListTerminalsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postTerminalsTerminalIdReassign

> postTerminalsTerminalIdReassign(terminalId, opts)

Reassign a terminal

Reassigns a payment terminal to a company account, merchant account, merchant account inventory, or a store.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Assign Terminal

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalsTerminalLevelApi();
let terminalId = "terminalId_example"; // String | The unique identifier of the payment terminal.
let opts = {
  'terminalReassignmentRequest': new ManagementApi.TerminalReassignmentRequest() // TerminalReassignmentRequest | 
};
apiInstance.postTerminalsTerminalIdReassign(terminalId, opts, (error, data, response) => {
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
 **terminalId** | **String**| The unique identifier of the payment terminal. | 
 **terminalReassignmentRequest** | [**TerminalReassignmentRequest**](TerminalReassignmentRequest.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

