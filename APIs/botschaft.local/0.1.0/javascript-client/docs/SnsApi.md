# FastApi.SnsApi

All URIs are relative to *http://botschaft.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**snsGetSnsGet**](SnsApi.md#snsGetSnsGet) | **GET** /sns | Sns Get
[**snsPostSnsPost**](SnsApi.md#snsPostSnsPost) | **POST** /sns | Sns Post



## snsGetSnsGet

> Object snsGetSnsGet(opts)

Sns Get

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.SnsApi();
let opts = {
  'message': "message_example", // String | 
  'base64Message': "base64Message_example", // String | 
  'authorization': "authorization_example" // String | 
};
apiInstance.snsGetSnsGet(opts, (error, data, response) => {
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


## snsPostSnsPost

> Object snsPostSnsPost(snsMessageRequest, opts)

Sns Post

### Example

```javascript
import FastApi from 'fast_api';

let apiInstance = new FastApi.SnsApi();
let snsMessageRequest = new FastApi.SnsMessageRequest(); // SnsMessageRequest | 
let opts = {
  'authorization': "authorization_example" // String | 
};
apiInstance.snsPostSnsPost(snsMessageRequest, opts, (error, data, response) => {
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
 **snsMessageRequest** | [**SnsMessageRequest**](SnsMessageRequest.md)|  | 
 **authorization** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

