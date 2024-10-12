# InfermedicaApi.ParseApi

All URIs are relative to *https://api.infermedica.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getMentions**](ParseApi.md#getMentions) | **POST** /parse | Find mentions of observations in given text



## getMentions

> ParseResponse getMentions(body)

Find mentions of observations in given text

Returns list of mentions of observation found in given text.

### Example

```javascript
import InfermedicaApi from 'infermedica_api';

let apiInstance = new InfermedicaApi.ParseApi();
let body = new InfermedicaApi.ParseRequest(); // ParseRequest | 
apiInstance.getMentions(body, (error, data, response) => {
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
 **body** | [**ParseRequest**](ParseRequest.md)|  | 

### Return type

[**ParseResponse**](ParseResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

