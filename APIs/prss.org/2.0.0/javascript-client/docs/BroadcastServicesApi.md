# ContentDepot.BroadcastServicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2BroadcastservicesGet**](BroadcastServicesApi.md#apiV2BroadcastservicesGet) | **GET** /api/v2/broadcastservices | Gets broadcast services matching the given criteria.
[**apiV2BroadcastservicesIdGet**](BroadcastServicesApi.md#apiV2BroadcastservicesIdGet) | **GET** /api/v2/broadcastservices/{id} | Returns the broadcast service matching the given ID.



## apiV2BroadcastservicesGet

> [Episode] apiV2BroadcastservicesGet(opts)

Gets broadcast services matching the given criteria.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.BroadcastServicesApi();
let opts = {
  'pageStart': 0, // Number | The start page of the results to return. The first item is indexed at 0.
  'pageSize': 500, // Number | The number of items to return. Must be between 0 and 500, inclusive.
  'orderById': "orderById_example" // String | The sort order of the list of broadcast services, based on broadcast service ID. If unspecified, the broadcast services are returned in random order. If using paging to iterate through the results, sort order should be specified.
};
apiInstance.apiV2BroadcastservicesGet(opts, (error, data, response) => {
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
 **pageStart** | **Number**| The start page of the results to return. The first item is indexed at 0. | [optional] [default to 0]
 **pageSize** | **Number**| The number of items to return. Must be between 0 and 500, inclusive. | [optional] [default to 500]
 **orderById** | **String**| The sort order of the list of broadcast services, based on broadcast service ID. If unspecified, the broadcast services are returned in random order. If using paging to iterate through the results, sort order should be specified. | [optional] 

### Return type

[**[Episode]**](Episode.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## apiV2BroadcastservicesIdGet

> BroadcastService apiV2BroadcastservicesIdGet(id)

Returns the broadcast service matching the given ID.

### Example

```javascript
import ContentDepot from 'content_depot';
let defaultClient = ContentDepot.ApiClient.instance;
// Configure OAuth2 access token for authorization: cd_oauth2
let cd_oauth2 = defaultClient.authentications['cd_oauth2'];
cd_oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ContentDepot.BroadcastServicesApi();
let id = 789; // Number | The ID of the broadcast service to find.
apiInstance.apiV2BroadcastservicesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| The ID of the broadcast service to find. | 

### Return type

[**BroadcastService**](BroadcastService.md)

### Authorization

[cd_oauth2](../README.md#cd_oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

