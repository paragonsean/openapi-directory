# UebermapsApiEndpoints.ShareApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shareMapIdGet**](ShareApi.md#shareMapIdGet) | **GET** /share/map/{id} | Get secret access token to share map



## shareMapIdGet

> MapWithAuthToken shareMapIdGet(id)

Get secret access token to share map

Get secret access token of an uebermap with access set to &#39;Secret link&#39;. Pass the &#39;token&#39; on every request you make to access this uebermap and its resources. F.e. token&#x3D;1-x_gqu7eLBe3uKoAGAGXy

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.ShareApi();
let id = 56; // Number | Id of map
apiInstance.shareMapIdGet(id, (error, data, response) => {
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
 **id** | **Number**| Id of map | 

### Return type

[**MapWithAuthToken**](MapWithAuthToken.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

