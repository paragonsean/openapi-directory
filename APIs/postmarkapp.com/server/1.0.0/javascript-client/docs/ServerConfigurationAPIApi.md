# PostmarkApi.ServerConfigurationAPIApi

All URIs are relative to *http://api.postmarkapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**editCurrentServerConfiguration**](ServerConfigurationAPIApi.md#editCurrentServerConfiguration) | **PUT** /server | Edit Server Configuration
[**getCurrentServerConfiguration**](ServerConfigurationAPIApi.md#getCurrentServerConfiguration) | **GET** /server | Get Server Configuration



## editCurrentServerConfiguration

> ServerConfigurationResponse editCurrentServerConfiguration(xPostmarkServerToken, opts)

Edit Server Configuration

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.ServerConfigurationAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
let opts = {
  'body': new PostmarkApi.EditServerConfigurationRequest() // EditServerConfigurationRequest | The settings that should be modified for the current server.
};
apiInstance.editCurrentServerConfiguration(xPostmarkServerToken, opts, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 
 **body** | [**EditServerConfigurationRequest**](EditServerConfigurationRequest.md)| The settings that should be modified for the current server. | [optional] 

### Return type

[**ServerConfigurationResponse**](ServerConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCurrentServerConfiguration

> ServerConfigurationResponse getCurrentServerConfiguration(xPostmarkServerToken)

Get Server Configuration

### Example

```javascript
import PostmarkApi from 'postmark_api';

let apiInstance = new PostmarkApi.ServerConfigurationAPIApi();
let xPostmarkServerToken = "xPostmarkServerToken_example"; // String | The token associated with the Server on which this request will operate.
apiInstance.getCurrentServerConfiguration(xPostmarkServerToken, (error, data, response) => {
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
 **xPostmarkServerToken** | **String**| The token associated with the Server on which this request will operate. | 

### Return type

[**ServerConfigurationResponse**](ServerConfigurationResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

