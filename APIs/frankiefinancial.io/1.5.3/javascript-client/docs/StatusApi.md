# FrankieFinancialApi.StatusApi

All URIs are relative to *https://api.demo.frankiefinancial.io/compliance/v1.2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**statusCheck**](StatusApi.md#statusCheck) | **GET** /ruok | Service Status



## statusCheck

> PuppyObject statusCheck(opts)

Service Status

Simple check to see if the service is running smoothly.

### Example

```javascript
import FrankieFinancialApi from 'frankie_financial_api';

let apiInstance = new FrankieFinancialApi.StatusApi();
let opts = {
  'askingNicely': true // Boolean | If set to true, the request is being made politely. 
};
apiInstance.statusCheck(opts, (error, data, response) => {
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
 **askingNicely** | **Boolean**| If set to true, the request is being made politely.  | [optional] 

### Return type

[**PuppyObject**](PuppyObject.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

