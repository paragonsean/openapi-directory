# SevenIoApi.ValidateForVoiceApi

All URIs are relative to *https://gateway.seven.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validateForVoice**](ValidateForVoiceApi.md#validateForVoice) | **POST** /validate_for_voice | 



## validateForVoice

> ValidateForVoice200Response validateForVoice(number, opts)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.ValidateForVoiceApi();
let number = "number_example"; // String | Determines the recipient. Can only be a number, not a contact from your address book.
let opts = {
  'callback': "callback_example" // String | The callback URL which gets queried right after validation.
};
apiInstance.validateForVoice(number, opts, (error, data, response) => {
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
 **number** | **String**| Determines the recipient. Can only be a number, not a contact from your address book. | 
 **callback** | **String**| The callback URL which gets queried right after validation. | [optional] 

### Return type

[**ValidateForVoice200Response**](ValidateForVoice200Response.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

