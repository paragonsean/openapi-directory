# MarketcheckApis.CRMCleanseAPIApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**crmCheck**](CRMCleanseAPIApi.md#crmCheck) | **GET** /crm_check/car/{vin} | CRM check of a particular vin



## crmCheck

> CRMResponse crmCheck(vin, saleDate, opts)

CRM check of a particular vin

Check whether particular vin has had a listing after stipulated date or not

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CRMCleanseAPIApi();
let vin = "vin_example"; // String | The VIN to identify the car. Must be a valid 17 char VIN
let saleDate = "saleDate_example"; // String | sale date to check whether after this listing has appeared or not. Must be 8 character long, with YYYYMMDD format
let opts = {
  'apiKey': "apiKey_example" // String | The API Authentication Key. Mandatory with all API calls.
};
apiInstance.crmCheck(vin, saleDate, opts, (error, data, response) => {
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
 **saleDate** | **String**| sale date to check whether after this listing has appeared or not. Must be 8 character long, with YYYYMMDD format | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 

### Return type

[**CRMResponse**](CRMResponse.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

