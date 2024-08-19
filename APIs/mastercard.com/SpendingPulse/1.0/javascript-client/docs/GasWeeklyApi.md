# SpendingPulse.GasWeeklyApi

All URIs are relative to *https://api.mastercard.com/spendingpulse/v1/spulse.svc*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gasweeklyGet**](GasWeeklyApi.md#gasweeklyGet) | **GET** /gasweekly | Returns the weekly gasoline report. This resource pulls back the report with ProductLine &#x3D; \&quot;US Weekly Gasoline Demand Report\&quot;. Keep in mind that you must be subscribed to the gasoline weekly report to be able to receive data back from this resource.



## gasweeklyGet

> GasWeeklyListResponse gasweeklyGet(opts)

Returns the weekly gasoline report. This resource pulls back the report with ProductLine &#x3D; \&quot;US Weekly Gasoline Demand Report\&quot;. Keep in mind that you must be subscribed to the gasoline weekly report to be able to receive data back from this resource.

Returns the weekly gasoline report. This resource pulls back the report with ProductLine &#x3D; \&quot;US Weekly Gasoline Demand Report\&quot;. Keep in mind that you must be subscribed to the gasoline weekly report to be able to receive data back from this resource. 

### Example

```javascript
import SpendingPulse from 'spending_pulse';

let apiInstance = new SpendingPulse.GasWeeklyApi();
let opts = {
  'currentRow': "1", // String | Starting record number to return.
  'offset': "25" // String | Used to restrict the number of records returned if needed to be less than max.
};
apiInstance.gasweeklyGet(opts, (error, data, response) => {
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

[**GasWeeklyListResponse**](GasWeeklyListResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

