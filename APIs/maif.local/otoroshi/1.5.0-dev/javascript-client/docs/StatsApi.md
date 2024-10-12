# OtoroshiAdminApi.StatsApi

All URIs are relative to *http://otoroshi-api.oto.tools*

Method | HTTP request | Description
------------- | ------------- | -------------
[**globalLiveStats**](StatsApi.md#globalLiveStats) | **GET** /api/live | Get global otoroshi stats
[**serviceLiveStats**](StatsApi.md#serviceLiveStats) | **GET** /api/live/{id} | Get live feed of otoroshi stats



## globalLiveStats

> Stats globalLiveStats()

Get global otoroshi stats

Get global otoroshi stats

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.StatsApi();
apiInstance.globalLiveStats((error, data, response) => {
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

[**Stats**](Stats.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceLiveStats

> Stats serviceLiveStats(id)

Get live feed of otoroshi stats

Get live feed of global otoroshi stats (global) or for a service {id}

### Example

```javascript
import OtoroshiAdminApi from 'otoroshi_admin_api';
let defaultClient = OtoroshiAdminApi.ApiClient.instance;
// Configure HTTP basic authorization: otoroshi_auth
let otoroshi_auth = defaultClient.authentications['otoroshi_auth'];
otoroshi_auth.username = 'YOUR USERNAME';
otoroshi_auth.password = 'YOUR PASSWORD';

let apiInstance = new OtoroshiAdminApi.StatsApi();
let id = "id_example"; // String | The service id or global for otoroshi stats
apiInstance.serviceLiveStats(id, (error, data, response) => {
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
 **id** | **String**| The service id or global for otoroshi stats | 

### Return type

[**Stats**](Stats.md)

### Authorization

[otoroshi_auth](../README.md#otoroshi_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/event-stream

