# UebermapsApiEndpoints.SubscriptionsApi

All URIs are relative to *http://uebermaps.com/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mapsIdSubscriptionsDelete**](SubscriptionsApi.md#mapsIdSubscriptionsDelete) | **DELETE** /maps/{id}/subscriptions | Unsubscribe from map
[**mapsIdSubscriptionsGet**](SubscriptionsApi.md#mapsIdSubscriptionsGet) | **GET** /maps/{id}/subscriptions | List subscriptions for a given map
[**subscriptionsGet**](SubscriptionsApi.md#subscriptionsGet) | **GET** /subscriptions | List subscriptions. Pass no parameters to get own subscriptions
[**subscriptionsPost**](SubscriptionsApi.md#subscriptionsPost) | **POST** /subscriptions | Create map subscription



## mapsIdSubscriptionsDelete

> Subscription mapsIdSubscriptionsDelete(id)

Unsubscribe from map

Unsubscribe from map.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.SubscriptionsApi();
let id = 56; // Number | map id
apiInstance.mapsIdSubscriptionsDelete(id, (error, data, response) => {
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
 **id** | **Number**| map id | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## mapsIdSubscriptionsGet

> [Subscription] mapsIdSubscriptionsGet(id)

List subscriptions for a given map

List subscriptions for a given map.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.SubscriptionsApi();
let id = 56; // Number | Id of map
apiInstance.mapsIdSubscriptionsGet(id, (error, data, response) => {
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

[**[Subscription]**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionsGet

> [Subscription] subscriptionsGet(opts)

List subscriptions. Pass no parameters to get own subscriptions

List subscriptions.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.SubscriptionsApi();
let opts = {
  'userId': 56, // Number | Id of user
  'mapId': 56 // Number | Id of map
};
apiInstance.subscriptionsGet(opts, (error, data, response) => {
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
 **userId** | **Number**| Id of user | [optional] 
 **mapId** | **Number**| Id of map | [optional] 

### Return type

[**[Subscription]**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionsPost

> Subscription subscriptionsPost(mapId)

Create map subscription

Create map subscription.

### Example

```javascript
import UebermapsApiEndpoints from 'uebermaps_api_endpoints';

let apiInstance = new UebermapsApiEndpoints.SubscriptionsApi();
let mapId = 3.4; // Number | map id
apiInstance.subscriptionsPost(mapId, (error, data, response) => {
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
 **mapId** | **Number**| map id | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

