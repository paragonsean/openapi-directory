# EnodeApi.StatisticsApi

All URIs are relative to *https://api.test.enode.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getStatisticsCharging**](StatisticsApi.md#getStatisticsCharging) | **GET** /statistics/charging | Get User Charging Statistics



## getStatisticsCharging

> [GetStatisticsCharging200ResponseInner] getStatisticsCharging(startDate, opts)

Get User Charging Statistics

Returns a normalized timeseries of statistics about power consumption and price for the User.

### Example

```javascript
import EnodeApi from 'enode_api';
let defaultClient = EnodeApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: UserAccessToken
let UserAccessToken = defaultClient.authentications['UserAccessToken'];
UserAccessToken.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EnodeApi.StatisticsApi();
let startDate = new Date("2013-10-20"); // Date | Earliest date to include in the response
let opts = {
  'resolution': "'DAY'", // String | The unit of time the data will be cut into before aggregate statistics are applied. For instance if you choose DAY, then each item in the returned array will cover 1 day.
  'endDate': new Date("2013-10-20"), // Date | Latest date to include in the response (defaults to current date/time)
  'vehicleId': "vehicleId_example", // String | Filter statistics to only include this vehicle
  'chargingLocationId': "chargingLocationId_example" // String | Filter statistics to only include this charging location
};
apiInstance.getStatisticsCharging(startDate, opts, (error, data, response) => {
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
 **startDate** | **Date**| Earliest date to include in the response | 
 **resolution** | **String**| The unit of time the data will be cut into before aggregate statistics are applied. For instance if you choose DAY, then each item in the returned array will cover 1 day. | [optional] [default to &#39;DAY&#39;]
 **endDate** | **Date**| Latest date to include in the response (defaults to current date/time) | [optional] 
 **vehicleId** | **String**| Filter statistics to only include this vehicle | [optional] 
 **chargingLocationId** | **String**| Filter statistics to only include this charging location | [optional] 

### Return type

[**[GetStatisticsCharging200ResponseInner]**](GetStatisticsCharging200ResponseInner.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

