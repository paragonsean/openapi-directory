# RadioMusicServices.BroadcastsApi

All URIs are relative to *https://rms.api.bbc.co.uk*

Method | HTTP request | Description
------------- | ------------- | -------------
[**broadcastsGet**](BroadcastsApi.md#broadcastsGet) | **GET** /broadcasts | Broadcasts
[**broadcastsLatestGet**](BroadcastsApi.md#broadcastsLatestGet) | **GET** /broadcasts/latest | Latest Broadcasts
[**getBroadcastByPid**](BroadcastsApi.md#getBroadcastByPid) | **GET** /broadcasts/{pid} | Broadcasts by PID



## broadcastsGet

> BroadcastsResponse broadcastsGet(xAPIKey, opts)

Broadcasts

All broadcasts 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.BroadcastsApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56, // Number | Paginated results limit
  'serviceId': "serviceId_example", // String | Filter by Service ID. E.g. bbc_radio_fourfm
  'date': "date_example", // String | Filter by date. E.g. 2016-06-17
  'sort': "sort_example" // String | Sort by provided query. E.g. 'start_at' sorts in ascending order, and '-start_at' sorts in descending order
};
apiInstance.broadcastsGet(xAPIKey, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 
 **serviceId** | **String**| Filter by Service ID. E.g. bbc_radio_fourfm | [optional] 
 **date** | **String**| Filter by date. E.g. 2016-06-17 | [optional] 
 **sort** | **String**| Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order | [optional] 

### Return type

[**BroadcastsResponse**](BroadcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## broadcastsLatestGet

> BroadcastsResponse broadcastsLatestGet(xAPIKey, opts)

Latest Broadcasts

Broadcasts for the current day 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.BroadcastsApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let opts = {
  'offset': 56, // Number | Paginated results offset
  'limit': 56, // Number | Paginated results limit
  'serviceId': "serviceId_example", // String | Filter by Service ID. E.g. bbc_radio_fourfm
  'onAir': "onAir_example", // String | Filter what is on air. E.g. 'now' returns current programme being broadcasted.
  'next': "next_example", // String | Filter what will be on air next in minutes. E.g. '240' returns programmes broadcasted in the next four hurs
  'previous': "previous_example", // String | Filter what was on air previously in minutes. E.g. '240' returns programmes broadcasted in the previous four hurs
  'sort': "sort_example" // String | Sort by provided query. E.g. 'start_at' sorts in ascending order, and '-start_at' sorts in descending order
};
apiInstance.broadcastsLatestGet(xAPIKey, opts, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **offset** | **Number**| Paginated results offset | [optional] 
 **limit** | **Number**| Paginated results limit | [optional] 
 **serviceId** | **String**| Filter by Service ID. E.g. bbc_radio_fourfm | [optional] 
 **onAir** | **String**| Filter what is on air. E.g. &#39;now&#39; returns current programme being broadcasted. | [optional] 
 **next** | **String**| Filter what will be on air next in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the next four hurs | [optional] 
 **previous** | **String**| Filter what was on air previously in minutes. E.g. &#39;240&#39; returns programmes broadcasted in the previous four hurs | [optional] 
 **sort** | **String**| Sort by provided query. E.g. &#39;start_at&#39; sorts in ascending order, and &#39;-start_at&#39; sorts in descending order | [optional] 

### Return type

[**BroadcastsResponse**](BroadcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBroadcastByPid

> BroadcastsResponse getBroadcastByPid(xAPIKey, pid)

Broadcasts by PID

Find broadcast by PID 

### Example

```javascript
import RadioMusicServices from 'radio__music_services';

let apiInstance = new RadioMusicServices.BroadcastsApi();
let xAPIKey = "xAPIKey_example"; // String | API_KEY
let pid = "pid_example"; // String | pid
apiInstance.getBroadcastByPid(xAPIKey, pid, (error, data, response) => {
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
 **xAPIKey** | **String**| API_KEY | 
 **pid** | **String**| pid | 

### Return type

[**BroadcastsResponse**](BroadcastsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

