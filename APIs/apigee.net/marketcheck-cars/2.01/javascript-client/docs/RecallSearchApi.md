# MarketcheckApis.RecallSearchApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getRecallHistory**](RecallSearchApi.md#getRecallHistory) | **GET** /car/recall/{vin} | Recall info by vin



## getRecallHistory

> SearchResponse getRecallHistory(vin, opts)

Recall info by vin

Get a particular recall information for a vin

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.RecallSearchApi();
let vin = "vin_example"; // String | The VIN to identify the car. Must be a valid 17 char VIN
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'page': 3.4 // Number | Page number to fetch the results for the given criteria. Default is 1.
};
apiInstance.getRecallHistory(vin, opts, (error, data, response) => {
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
 **vin** | **String**| The VIN to identify the car. Must be a valid 17 char VIN | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **page** | **Number**| Page number to fetch the results for the given criteria. Default is 1. | [optional] 

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

