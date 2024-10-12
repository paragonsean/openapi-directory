# FastApi.TwilioApi

All URIs are relative to *http://botschaft.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**twilioMessageGetTwilioGet**](TwilioApi.md#twilioMessageGetTwilioGet) | **GET** /twilio | Twilio Message Get
[**twilioMessagePostTwilioPost**](TwilioApi.md#twilioMessagePostTwilioPost) | **POST** /twilio | Twilio Message Post



## twilioMessageGetTwilioGet

> Object twilioMessageGetTwilioGet(to, opts)

Twilio Message Get

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.TwilioApi();
let to = "to_example"; // String | 
let opts = {
  'message': "message_example", // String | 
  'base64Message': "base64Message_example", // String | 
  'authorization': "authorization_example" // String | 
};
apiInstance.twilioMessageGetTwilioGet(to, opts, (error, data, response) => {
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
 **to** | **String**|  | 
 **message** | **String**|  | [optional] 
 **base64Message** | **String**|  | [optional] 
 **authorization** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## twilioMessagePostTwilioPost

> Object twilioMessagePostTwilioPost(twilioMessageRequest, opts)

Twilio Message Post

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.TwilioApi();
let twilioMessageRequest = new FastApi.TwilioMessageRequest(); // TwilioMessageRequest | 
let opts = {
  'authorization': "authorization_example" // String | 
};
apiInstance.twilioMessagePostTwilioPost(twilioMessageRequest, opts, (error, data, response) => {
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
 **twilioMessageRequest** | [**TwilioMessageRequest**](TwilioMessageRequest.md)|  | 
 **authorization** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

