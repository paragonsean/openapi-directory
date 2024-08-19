# ZappitiPlayerApi.GeneralApi

All URIs are relative to *http://192.168.1.5:8990*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connectionDetailsPost**](GeneralApi.md#connectionDetailsPost) | **POST** /ConnectionDetails | Get user&#39;s login details
[**isAlivePost**](GeneralApi.md#isAlivePost) | **POST** /IsAlive | Get server status



## connectionDetailsPost

> ConnectionDetailsResult connectionDetailsPost(body)

Get user&#39;s login details

### Example

```javascript
import ZappitiPlayerApi from 'zappiti_player_api';

let apiInstance = new ZappitiPlayerApi.GeneralApi();
let body = new ZappitiPlayerApi.ConnectionDetailsRequest(); // ConnectionDetailsRequest | 
apiInstance.connectionDetailsPost(body, (error, data, response) => {
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
 **body** | [**ConnectionDetailsRequest**](ConnectionDetailsRequest.md)|  | 

### Return type

[**ConnectionDetailsResult**](ConnectionDetailsResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## isAlivePost

> IsAliveResult isAlivePost(body)

Get server status

### Example

```javascript
import ZappitiPlayerApi from 'zappiti_player_api';

let apiInstance = new ZappitiPlayerApi.GeneralApi();
let body = new ZappitiPlayerApi.IsAliveRequest(); // IsAliveRequest | 
apiInstance.isAlivePost(body, (error, data, response) => {
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
 **body** | [**IsAliveRequest**](IsAliveRequest.md)|  | 

### Return type

[**IsAliveResult**](IsAliveResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

