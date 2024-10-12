# OnSchedApiUtility.HealthApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**utilityV1HealthHeartbeatGet**](HealthApi.md#utilityV1HealthHeartbeatGet) | **GET** /utility/v1/health/heartbeat | 
[**utilityV1HealthThreadinfoGet**](HealthApi.md#utilityV1HealthThreadinfoGet) | **GET** /utility/v1/health/threadinfo | 



## utilityV1HealthHeartbeatGet

> String utilityV1HealthHeartbeatGet()



### Example

```javascript
import OnSchedApiUtility from 'on_sched_api_utility';
let defaultClient = OnSchedApiUtility.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedApiUtility.HealthApi();
apiInstance.utilityV1HealthHeartbeatGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## utilityV1HealthThreadinfoGet

> ThreadPoolInfo utilityV1HealthThreadinfoGet()



### Example

```javascript
import OnSchedApiUtility from 'on_sched_api_utility';
let defaultClient = OnSchedApiUtility.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedApiUtility.HealthApi();
apiInstance.utilityV1HealthThreadinfoGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ThreadPoolInfo**](ThreadPoolInfo.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

