# EDrvApi.SmartChargingApi

All URIs are relative to *http://api.edrv.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletechargingschedule**](SmartChargingApi.md#deletechargingschedule) | **DELETE** /v1/commands/chargingschedule | 
[**setchargingschedule**](SmartChargingApi.md#setchargingschedule) | **POST** /v1/commands/chargingschedule | 



## deletechargingschedule

> Setchargingschedule201Response deletechargingschedule(deletechargingscheduleRequest)



Delete a smart charging schedule

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.SmartChargingApi();
let deletechargingscheduleRequest = new EDrvApi.DeletechargingscheduleRequest(); // DeletechargingscheduleRequest | 
apiInstance.deletechargingschedule(deletechargingscheduleRequest, (error, data, response) => {
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
 **deletechargingscheduleRequest** | [**DeletechargingscheduleRequest**](DeletechargingscheduleRequest.md)|  | 

### Return type

[**Setchargingschedule201Response**](Setchargingschedule201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setchargingschedule

> Setchargingschedule201Response setchargingschedule(setchargingscheduleRequest)



Set one of charging power or current of a specific chargestation connector

### Example

```javascript
import EDrvApi from 'e_drv_api';
let defaultClient = EDrvApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new EDrvApi.SmartChargingApi();
let setchargingscheduleRequest = new EDrvApi.SetchargingscheduleRequest(); // SetchargingscheduleRequest | 
apiInstance.setchargingschedule(setchargingscheduleRequest, (error, data, response) => {
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
 **setchargingscheduleRequest** | [**SetchargingscheduleRequest**](SetchargingscheduleRequest.md)|  | 

### Return type

[**Setchargingschedule201Response**](Setchargingschedule201Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

