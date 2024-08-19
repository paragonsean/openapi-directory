# ZappitiPlayerApi.ZappitiServiceApi

All URIs are relative to *http://192.168.1.5:8990*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkZappitiServicePost**](ZappitiServiceApi.md#checkZappitiServicePost) | **POST** /CheckZappitiService | Check if Zappiti Service app status on the player
[**installZappitiServicePost**](ZappitiServiceApi.md#installZappitiServicePost) | **POST** /InstallZappitiService | Open a popup that allow the user to install Zappiti Service, if not already installed
[**startZappitiServicePost**](ZappitiServiceApi.md#startZappitiServicePost) | **POST** /StartZappitiService | Start Zappiti Service if not started yet



## checkZappitiServicePost

> CheckZappitiServiceResult checkZappitiServicePost(body)

Check if Zappiti Service app status on the player

ErrorCode.NotInstalled ErrorCode.NotRunning ErrorCode.Running 

### Example

```javascript
import ZappitiPlayerApi from 'zappiti_player_api';

let apiInstance = new ZappitiPlayerApi.ZappitiServiceApi();
let body = new ZappitiPlayerApi.CheckZappitiServiceRequest(); // CheckZappitiServiceRequest | 
apiInstance.checkZappitiServicePost(body, (error, data, response) => {
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
 **body** | [**CheckZappitiServiceRequest**](CheckZappitiServiceRequest.md)|  | 

### Return type

[**CheckZappitiServiceResult**](CheckZappitiServiceResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## installZappitiServicePost

> InstallZappitiServiceResult installZappitiServicePost(body)

Open a popup that allow the user to install Zappiti Service, if not already installed

### Example

```javascript
import ZappitiPlayerApi from 'zappiti_player_api';

let apiInstance = new ZappitiPlayerApi.ZappitiServiceApi();
let body = new ZappitiPlayerApi.InstallZappitiServiceRequest(); // InstallZappitiServiceRequest | 
apiInstance.installZappitiServicePost(body, (error, data, response) => {
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
 **body** | [**InstallZappitiServiceRequest**](InstallZappitiServiceRequest.md)|  | 

### Return type

[**InstallZappitiServiceResult**](InstallZappitiServiceResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startZappitiServicePost

> StartZappitiServiceResult startZappitiServicePost(body)

Start Zappiti Service if not started yet

### Example

```javascript
import ZappitiPlayerApi from 'zappiti_player_api';

let apiInstance = new ZappitiPlayerApi.ZappitiServiceApi();
let body = new ZappitiPlayerApi.StartZappitiServiceRequest(); // StartZappitiServiceRequest | 
apiInstance.startZappitiServicePost(body, (error, data, response) => {
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
 **body** | [**StartZappitiServiceRequest**](StartZappitiServiceRequest.md)|  | 

### Return type

[**StartZappitiServiceResult**](StartZappitiServiceResult.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

