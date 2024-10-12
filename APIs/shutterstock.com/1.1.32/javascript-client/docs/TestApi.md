# ShutterstockApiExplorer.TestApi

All URIs are relative to *https://api.shutterstock.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**echo**](TestApi.md#echo) | **GET** /v2/test | Echo text
[**validate**](TestApi.md#validate) | **GET** /v2/test/validate | Validate input



## echo

> TestEcho echo(opts)

Echo text

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';

let apiInstance = new ShutterstockApiExplorer.TestApi();
let opts = {
  'text': "'ok'" // String | Text to echo
};
apiInstance.echo(opts, (error, data, response) => {
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
 **text** | **String**| Text to echo | [optional] [default to &#39;ok&#39;]

### Return type

[**TestEcho**](TestEcho.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## validate

> TestValidate validate(id, opts)

Validate input

### Example

```javascript
import ShutterstockApiExplorer from 'shutterstock_api_explorer';

let apiInstance = new ShutterstockApiExplorer.TestApi();
let id = 123; // Number | Integer ID
let opts = {
  'tag': ["null"], // [String] | List of tags
  'userAgent': "userAgent_example" // String | User agent
};
apiInstance.validate(id, opts, (error, data, response) => {
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
 **id** | **Number**| Integer ID | 
 **tag** | [**[String]**](String.md)| List of tags | [optional] 
 **userAgent** | **String**| User agent | [optional] 

### Return type

[**TestValidate**](TestValidate.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

