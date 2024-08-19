# Netatmo.HealthyhomecoachApi

All URIs are relative to *https://api.netatmo.net/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**gethomecoachsdata**](HealthyhomecoachApi.md#gethomecoachsdata) | **GET** /gethomecoachsdata | 



## gethomecoachsdata

> NAHealthyHomeCoachDataResponse gethomecoachsdata(opts)



The method gethomecoachsdata Returns data from a user Healthy Home Coach Station (measures and device specific data).

### Example

```javascript
import Netatmo from 'netatmo';
let defaultClient = Netatmo.ApiClient.instance;
// Configure OAuth2 access token for authorization: code_oauth
let code_oauth = defaultClient.authentications['code_oauth'];
code_oauth.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: password_oauth
let password_oauth = defaultClient.authentications['password_oauth'];
password_oauth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new Netatmo.HealthyhomecoachApi();
let opts = {
  'deviceId': "deviceId_example" // String | Id of the device you want to retrieve information of
};
apiInstance.gethomecoachsdata(opts, (error, data, response) => {
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
 **deviceId** | **String**| Id of the device you want to retrieve information of | [optional] 

### Return type

[**NAHealthyHomeCoachDataResponse**](NAHealthyHomeCoachDataResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

