# AgcoApi.UpdateGroupSubscriptionsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateGroupSubscriptionsDeleteUpdateGroupSubscription**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsDeleteUpdateGroupSubscription) | **DELETE** /api/v2/UpdateGroupSubscriptions/{UpdateGroupSubscriptionID} | Delete an Update Group Subscription
[**updateGroupSubscriptionsGetUpdateGroupSubscription**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsGetUpdateGroupSubscription) | **GET** /api/v2/UpdateGroupSubscriptions/{UpdateGroupSubscriptionID} | Get an Update Group Subscription
[**updateGroupSubscriptionsGetUpdateGroupSubscriptions**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsGetUpdateGroupSubscriptions) | **GET** /api/v2/UpdateGroupSubscriptions | Get Update Group Subscriptions
[**updateGroupSubscriptionsPostUpdateGroupSubscription**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsPostUpdateGroupSubscription) | **POST** /api/v2/UpdateGroupSubscriptions | Add an Update Group Subscription
[**updateGroupSubscriptionsPostUpdateGroupSubscriptions**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsPostUpdateGroupSubscriptions) | **POST** /api/v2/UpdateGroupSubscriptions/Batch | No Documentation Found.
[**updateGroupSubscriptionsPutUpdateGroupSubscription**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsPutUpdateGroupSubscription) | **PUT** /api/v2/UpdateGroupSubscriptions/{UpdateGroupSubscriptionID} | Update an Update Group Subscription
[**updateGroupSubscriptionsPutUpdateGroupSubscriptions**](UpdateGroupSubscriptionsApi.md#updateGroupSubscriptionsPutUpdateGroupSubscriptions) | **PUT** /api/v2/UpdateGroupSubscriptions/Batch | No Documentation Found.



## updateGroupSubscriptionsDeleteUpdateGroupSubscription

> updateGroupSubscriptionsDeleteUpdateGroupSubscription(updateGroupSubscriptionID)

Delete an Update Group Subscription

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupSubscriptionsApi();
let updateGroupSubscriptionID = 56; // Number | The Update Group Subscription ID to delete
apiInstance.updateGroupSubscriptionsDeleteUpdateGroupSubscription(updateGroupSubscriptionID, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateGroupSubscriptionID** | **Number**| The Update Group Subscription ID to delete | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## updateGroupSubscriptionsGetUpdateGroupSubscription

> UpdateSystemModelsUpdateGroupSubscription updateGroupSubscriptionsGetUpdateGroupSubscription(updateGroupSubscriptionID)

Get an Update Group Subscription

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupSubscriptionsApi();
let updateGroupSubscriptionID = 56; // Number | The Update Group Subscription ID
apiInstance.updateGroupSubscriptionsGetUpdateGroupSubscription(updateGroupSubscriptionID, (error, data, response) => {
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
 **updateGroupSubscriptionID** | **Number**| The Update Group Subscription ID | 

### Return type

[**UpdateSystemModelsUpdateGroupSubscription**](UpdateSystemModelsUpdateGroupSubscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## updateGroupSubscriptionsGetUpdateGroupSubscriptions

> APIPagedResponseUpdateSystemModelsUpdateGroupSubscription updateGroupSubscriptionsGetUpdateGroupSubscriptions(opts)

Get Update Group Subscriptions

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupSubscriptionsApi();
let opts = {
  'updateGroupID': "updateGroupID_example", // String | Optional. Filter by Update Group ID.
  'packageTypeID': "packageTypeID_example", // String | Optional. Filter by Package Type ID.
  'clientID': "clientID_example", // String | Optional. Filter by Client ID.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.updateGroupSubscriptionsGetUpdateGroupSubscriptions(opts, (error, data, response) => {
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
 **updateGroupID** | **String**| Optional. Filter by Update Group ID. | [optional] 
 **packageTypeID** | **String**| Optional. Filter by Package Type ID. | [optional] 
 **clientID** | **String**| Optional. Filter by Client ID. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsUpdateGroupSubscription**](APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## updateGroupSubscriptionsPostUpdateGroupSubscription

> Number updateGroupSubscriptionsPostUpdateGroupSubscription(updateSystemModelsUpdateGroupSubscription)

Add an Update Group Subscription

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupSubscriptionsApi();
let updateSystemModelsUpdateGroupSubscription = new AgcoApi.UpdateSystemModelsUpdateGroupSubscription(); // UpdateSystemModelsUpdateGroupSubscription | The Update Group Subscription to add
apiInstance.updateGroupSubscriptionsPostUpdateGroupSubscription(updateSystemModelsUpdateGroupSubscription, (error, data, response) => {
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
 **updateSystemModelsUpdateGroupSubscription** | [**UpdateSystemModelsUpdateGroupSubscription**](UpdateSystemModelsUpdateGroupSubscription.md)| The Update Group Subscription to add | 

### Return type

**Number**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## updateGroupSubscriptionsPostUpdateGroupSubscriptions

> updateGroupSubscriptionsPostUpdateGroupSubscriptions(updateSystemModelsUpdateGroupSubscription)

No Documentation Found.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupSubscriptionsApi();
let updateSystemModelsUpdateGroupSubscription = [new AgcoApi.UpdateSystemModelsUpdateGroupSubscription()]; // [UpdateSystemModelsUpdateGroupSubscription] | 
apiInstance.updateGroupSubscriptionsPostUpdateGroupSubscriptions(updateSystemModelsUpdateGroupSubscription, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateSystemModelsUpdateGroupSubscription** | [**[UpdateSystemModelsUpdateGroupSubscription]**](UpdateSystemModelsUpdateGroupSubscription.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## updateGroupSubscriptionsPutUpdateGroupSubscription

> updateGroupSubscriptionsPutUpdateGroupSubscription(updateGroupSubscriptionID, updateSystemModelsUpdateGroupSubscription)

Update an Update Group Subscription

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupSubscriptionsApi();
let updateGroupSubscriptionID = 56; // Number | The Update Group Subscription ID
let updateSystemModelsUpdateGroupSubscription = new AgcoApi.UpdateSystemModelsUpdateGroupSubscription(); // UpdateSystemModelsUpdateGroupSubscription | The updated Update Group Subscription
apiInstance.updateGroupSubscriptionsPutUpdateGroupSubscription(updateGroupSubscriptionID, updateSystemModelsUpdateGroupSubscription, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateGroupSubscriptionID** | **Number**| The Update Group Subscription ID | 
 **updateSystemModelsUpdateGroupSubscription** | [**UpdateSystemModelsUpdateGroupSubscription**](UpdateSystemModelsUpdateGroupSubscription.md)| The updated Update Group Subscription | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## updateGroupSubscriptionsPutUpdateGroupSubscriptions

> updateGroupSubscriptionsPutUpdateGroupSubscriptions(updateSystemModelsUpdateGroupSubscription)

No Documentation Found.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupSubscriptionsApi();
let updateSystemModelsUpdateGroupSubscription = [new AgcoApi.UpdateSystemModelsUpdateGroupSubscription()]; // [UpdateSystemModelsUpdateGroupSubscription] | 
apiInstance.updateGroupSubscriptionsPutUpdateGroupSubscriptions(updateSystemModelsUpdateGroupSubscription, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateSystemModelsUpdateGroupSubscription** | [**[UpdateSystemModelsUpdateGroupSubscription]**](UpdateSystemModelsUpdateGroupSubscription.md)|  | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

