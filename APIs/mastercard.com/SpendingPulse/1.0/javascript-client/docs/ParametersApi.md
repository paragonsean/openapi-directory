# SpendingPulse.ParametersApi

All URIs are relative to *https://api.mastercard.com/spendingpulse/v1/spulse.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parametersGet**](ParametersApi.md#parametersGet) | **GET** /parameters | Returns a distinct list of all reports are available and that one is subscribed to.



## parametersGet

> ParameterListResponse parametersGet(opts)

Returns a distinct list of all reports are available and that one is subscribed to.

Returns a distinct list of all reports are available and that one is subscribed to. 

### Example

```javascript
import SpendingPulse from 'spending_pulse';

let apiInstance = new SpendingPulse.ParametersApi();
let opts = {
  'currentRow': "1", // String | Starting record number to return.
  'offset': "25" // String | Used to restrict the number of records returned if needed to be less than max.
};
apiInstance.parametersGet(opts, (error, data, response) => {
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
 **currentRow** | **String**| Starting record number to return. | [optional] 
 **offset** | **String**| Used to restrict the number of records returned if needed to be less than max. | [optional] 

### Return type

[**ParameterListResponse**](ParameterListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

