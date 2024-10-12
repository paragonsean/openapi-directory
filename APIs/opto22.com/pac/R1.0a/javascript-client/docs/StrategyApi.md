# PacControlRestApi.StrategyApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**readStrategyDetails_0**](StrategyApi.md#readStrategyDetails_0) | **GET** /device/strategy | 



## readStrategyDetails_0

> StrategyResponse readStrategyDetails_0()



Returns the name, date, time, and CRC of the strategy currently in the controller, and the number of charts currently running. Empty strings and a 0 will be returned when there is no strategy.

### Example

```javascript
import PacControlRestApi from 'pac_control_rest_api';
let defaultClient = PacControlRestApi.ApiClient.instance;
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new PacControlRestApi.StrategyApi();
apiInstance.readStrategyDetails_0((error, data, response) => {
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

[**StrategyResponse**](StrategyResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

