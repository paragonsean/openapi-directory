# Events.EventsApi

All URIs are relative to *https://api.hubapi.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEventsV3EventsGetPage**](EventsApi.md#getEventsV3EventsGetPage) | **GET** /events/v3/events/ | 



## getEventsV3EventsGetPage

> CollectionResponseExternalUnifiedEvent getEventsV3EventsGetPage(opts)



### Example

```javascript
import Events from 'events';
let defaultClient = Events.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2_legacy
let oauth2_legacy = defaultClient.authentications['oauth2_legacy'];
oauth2_legacy.accessToken = 'YOUR ACCESS TOKEN';
// Configure API key authorization: private_apps_legacy
let private_apps_legacy = defaultClient.authentications['private_apps_legacy'];
private_apps_legacy.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//private_apps_legacy.apiKeyPrefix = 'Token';

let apiInstance = new Events.EventsApi();
let opts = {
  'objectType': "objectType_example", // String | 
  'eventType': "eventType_example", // String | 
  'occurredAfter': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'occurredBefore': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'objectId': 789, // Number | 
  'indexTableName': "indexTableName_example", // String | 
  'indexSpecificMetadata': "indexSpecificMetadata_example", // String | 
  'after': "after_example", // String | The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
  'before': "before_example", // String | 
  'limit': 56, // Number | The maximum number of results to display per page.
  'sort': ["null"], // [String] | 
  'objectPropertyPropname': {key: null}, // Object | 
  'propertyPropname': {key: null}, // Object | 
  'id': ["null"] // [String] | 
};
apiInstance.getEventsV3EventsGetPage(opts, (error, data, response) => {
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
 **objectType** | **String**|  | [optional] 
 **eventType** | **String**|  | [optional] 
 **occurredAfter** | **Date**|  | [optional] 
 **occurredBefore** | **Date**|  | [optional] 
 **objectId** | **Number**|  | [optional] 
 **indexTableName** | **String**|  | [optional] 
 **indexSpecificMetadata** | **String**|  | [optional] 
 **after** | **String**| The paging cursor token of the last successfully read resource will be returned as the &#x60;paging.next.after&#x60; JSON property of a paged response containing more results. | [optional] 
 **before** | **String**|  | [optional] 
 **limit** | **Number**| The maximum number of results to display per page. | [optional] 
 **sort** | [**[String]**](String.md)|  | [optional] 
 **objectPropertyPropname** | [**Object**](.md)|  | [optional] 
 **propertyPropname** | [**Object**](.md)|  | [optional] 
 **id** | [**[String]**](String.md)|  | [optional] 

### Return type

[**CollectionResponseExternalUnifiedEvent**](CollectionResponseExternalUnifiedEvent.md)

### Authorization

[oauth2_legacy](../README.md#oauth2_legacy), [private_apps_legacy](../README.md#private_apps_legacy)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, */*

