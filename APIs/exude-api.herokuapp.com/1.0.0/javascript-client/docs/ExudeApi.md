# ExudeApiService.ExudeApi

All URIs are relative to *https://exude-api.herokuapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filterFileDataStoppings**](ExudeApi.md#filterFileDataStoppings) | **POST** /exude/{type}/file | Filter the stopping words from the provided input file
[**filterStoppings**](ExudeApi.md#filterStoppings) | **POST** /exude/{type}/data | Filter the stopping words from the provided input data or links



## filterFileDataStoppings

> ExudeResponseBean filterFileDataStoppings(type, opts)

Filter the stopping words from the provided input file

### Example

```javascript
import ExudeApiService from 'exude_api_service';

let apiInstance = new ExudeApiService.ExudeApi();
let type = "type_example"; // String | provide the type of filtering required stopping/swear
let opts = {
  'file': "/path/to/file" // File | 
};
apiInstance.filterFileDataStoppings(type, opts, (error, data, response) => {
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
 **type** | **String**| provide the type of filtering required stopping/swear | 
 **file** | **File**|  | [optional] 

### Return type

[**ExudeResponseBean**](ExudeResponseBean.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## filterStoppings

> ExudeResponseBean filterStoppings(type, opts)

Filter the stopping words from the provided input data or links

### Example

```javascript
import ExudeApiService from 'exude_api_service';

let apiInstance = new ExudeApiService.ExudeApi();
let type = "stopping"; // String | provide the type of filtering required stopping/swear
let opts = {
  'data': "data_example", // String | 
  'links': ["null"] // [String] | 
};
apiInstance.filterStoppings(type, opts, (error, data, response) => {
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
 **type** | **String**| provide the type of filtering required stopping/swear | 
 **data** | **String**|  | [optional] 
 **links** | [**[String]**](String.md)|  | [optional] 

### Return type

[**ExudeResponseBean**](ExudeResponseBean.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json

