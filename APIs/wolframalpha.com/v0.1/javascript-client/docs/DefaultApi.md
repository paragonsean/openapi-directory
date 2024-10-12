# Wolfram.DefaultApi

All URIs are relative to *https://www.wolframalpha.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getWolframAlphaResults**](DefaultApi.md#getWolframAlphaResults) | **GET** /api/v1/llm-api | Get Wolfram|Alpha results
[**getWolframCloudResults**](DefaultApi.md#getWolframCloudResults) | **GET** /api/v1/cloud-plugin | Evaluate Wolfram Language code



## getWolframAlphaResults

> getWolframAlphaResults(input)

Get Wolfram|Alpha results

### Example

```javascript
import Wolfram from 'wolfram';

let apiInstance = new Wolfram.DefaultApi();
let input = "input_example"; // String | the input
apiInstance.getWolframAlphaResults(input, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | **String**| the input | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain


## getWolframCloudResults

> getWolframCloudResults(input)

Evaluate Wolfram Language code

### Example

```javascript
import Wolfram from 'wolfram';

let apiInstance = new Wolfram.DefaultApi();
let input = "input_example"; // String | the input expression
apiInstance.getWolframCloudResults(input, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **input** | **String**| the input expression | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain

