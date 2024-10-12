# MarketcheckApis.CarsHistoryAPIApi

All URIs are relative to *https://marketcheck-prod.apigee.net/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCarHistory**](CarsHistoryAPIApi.md#getCarHistory) | **GET** /history/car/{vin} | Get a cars online listing history
[**historyCarUkVrmGet**](CarsHistoryAPIApi.md#historyCarUkVrmGet) | **GET** /history/car/uk/{vrm} | Get a cars online listing history



## getCarHistory

> [HistoricalListing] getCarHistory(vin, opts)

Get a cars online listing history

The history API returns online listing history for a car identified by its VIN. History listings are sorted in the descending order of the listing date / last seen date

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarsHistoryAPIApi();
let vin = "vin_example"; // String | The VIN to identify the car. Must be a valid 17 char VIN
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'fields': "fields_example", // String | List of fields to fetch, in case the default fields list in the response is to be trimmed down
  'page': 3.4, // Number | Page number to fetch the results for the given criteria. Default is 1.
  'includeDuplicates': true, // Boolean | Flag to indicate whether to include duplicate historical records as well in the response
  'sortOrder': "sortOrder_example" // String | Sort order - asc or desc. Default sort order is asc
};
apiInstance.getCarHistory(vin, opts, (error, data, response) => {
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
 **fields** | **String**| List of fields to fetch, in case the default fields list in the response is to be trimmed down | [optional] 
 **page** | **Number**| Page number to fetch the results for the given criteria. Default is 1. | [optional] 
 **includeDuplicates** | **Boolean**| Flag to indicate whether to include duplicate historical records as well in the response | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 

### Return type

[**[HistoricalListing]**](HistoricalListing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## historyCarUkVrmGet

> [HistoricalListing] historyCarUkVrmGet(vrm, opts)

Get a cars online listing history

The history API returns online listing history for a car identified by its VRM. History listings are sorted in the descending order of the listing date / last seen date

### Example

```javascript
import MarketcheckApis from 'marketcheck_apis';
let defaultClient = MarketcheckApis.ApiClient.instance;
// Configure HTTP basic authorization: authorizeEndpoint
let authorizeEndpoint = defaultClient.authentications['authorizeEndpoint'];
authorizeEndpoint.username = 'YOUR USERNAME';
authorizeEndpoint.password = 'YOUR PASSWORD';

let apiInstance = new MarketcheckApis.CarsHistoryAPIApi();
let vrm = "vrm_example"; // String | The VRM to identify the car.
let opts = {
  'apiKey': "apiKey_example", // String | The API Authentication Key. Mandatory with all API calls.
  'page': 3.4, // Number | Page number to fetch the results for the given criteria. Default is 1.
  'includeDuplicates': true, // Boolean | Flag to indicate whether to include duplicate historical records as well in the response
  'sortOrder': "sortOrder_example" // String | Sort order - asc or desc. Default sort order is asc
};
apiInstance.historyCarUkVrmGet(vrm, opts, (error, data, response) => {
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
 **vrm** | **String**| The VRM to identify the car. | 
 **apiKey** | **String**| The API Authentication Key. Mandatory with all API calls. | [optional] 
 **page** | **Number**| Page number to fetch the results for the given criteria. Default is 1. | [optional] 
 **includeDuplicates** | **Boolean**| Flag to indicate whether to include duplicate historical records as well in the response | [optional] 
 **sortOrder** | **String**| Sort order - asc or desc. Default sort order is asc | [optional] 

### Return type

[**[HistoricalListing]**](HistoricalListing.md)

### Authorization

[authorizeEndpoint](../README.md#authorizeEndpoint)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

