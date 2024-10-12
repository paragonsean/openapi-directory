# SevenIoApi.VoiceApi

All URIs are relative to *https://gateway.seven.io/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**voice**](VoiceApi.md#voice) | **POST** /voice | 



## voice

> String voice(to, text, opts)



### Example

```javascript
import SevenIoApi from 'seven_io_api';
let defaultClient = SevenIoApi.ApiClient.instance;
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new SevenIoApi.VoiceApi();
let to = "to_example"; // String | Determines the receiver. Must be a valid phone number or contact from the address book.
let text = "text_example"; // String | The text to convert to a voice message. Accepts valid XML too.
let opts = {
  'xml': 3.4, // Number | Decides whether the parameter \"text\" is plain text or XML. The default value is 0.
  'from': "from_example" // String | Sets the sender. Must be a verified sender. Use an inbound number of yours or one of ours.
};
apiInstance.voice(to, text, opts, (error, data, response) => {
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
 **to** | **String**| Determines the receiver. Must be a valid phone number or contact from the address book. | 
 **text** | **String**| The text to convert to a voice message. Accepts valid XML too. | 
 **xml** | **Number**| Decides whether the parameter \&quot;text\&quot; is plain text or XML. The default value is 0. | [optional] 
 **from** | **String**| Sets the sender. Must be a verified sender. Use an inbound number of yours or one of ours. | [optional] 

### Return type

**String**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

