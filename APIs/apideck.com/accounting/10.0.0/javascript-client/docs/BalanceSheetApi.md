# AccountingApi.BalanceSheetApi

All URIs are relative to *https://unify.apideck.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**balanceSheetOne**](BalanceSheetApi.md#balanceSheetOne) | **GET** /accounting/balance-sheet | Get BalanceSheet



## balanceSheetOne

> GetBalanceSheetResponse balanceSheetOne(xApideckConsumerId, xApideckAppId, opts)

Get BalanceSheet

Get BalanceSheet

### Example

```javascript
import AccountingApi from 'accounting_api';
let defaultClient = AccountingApi.ApiClient.instance;
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new AccountingApi.BalanceSheetApi();
let xApideckConsumerId = "xApideckConsumerId_example"; // String | ID of the consumer which you want to get or push data from
let xApideckAppId = "dSBdXd2H6Mqwfg0atXHXYcysLJE9qyn1VwBtXHX"; // String | The ID of your Unify application
let opts = {
  'xApideckServiceId': "xApideckServiceId_example", // String | Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
  'passThrough': {key: {"search":"San Francisco"}}, // PassThroughQuery | Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]=leads becomes ?search=leads
  'filter': new AccountingApi.BalanceSheetFilter(), // BalanceSheetFilter | Apply filters
  'raw': false // Boolean | Include raw response. Mostly used for debugging purposes
};
apiInstance.balanceSheetOne(xApideckConsumerId, xApideckAppId, opts, (error, data, response) => {
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
 **xApideckConsumerId** | **String**| ID of the consumer which you want to get or push data from | 
 **xApideckAppId** | **String**| The ID of your Unify application | 
 **xApideckServiceId** | **String**| Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API. | [optional] 
 **passThrough** | [**PassThroughQuery**](Object.md)| Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads | [optional] 
 **filter** | [**BalanceSheetFilter**](.md)| Apply filters | [optional] 
 **raw** | **Boolean**| Include raw response. Mostly used for debugging purposes | [optional] [default to false]

### Return type

[**GetBalanceSheetResponse**](GetBalanceSheetResponse.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

