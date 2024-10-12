# TwilioSync.SyncV1SyncListItemApi

All URIs are relative to *https://sync.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSyncListItem**](SyncV1SyncListItemApi.md#createSyncListItem) | **POST** /v1/Services/{ServiceSid}/Lists/{ListSid}/Items | 
[**deleteSyncListItem**](SyncV1SyncListItemApi.md#deleteSyncListItem) | **DELETE** /v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index} | 
[**fetchSyncListItem**](SyncV1SyncListItemApi.md#fetchSyncListItem) | **GET** /v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index} | 
[**listSyncListItem**](SyncV1SyncListItemApi.md#listSyncListItem) | **GET** /v1/Services/{ServiceSid}/Lists/{ListSid}/Items | 
[**updateSyncListItem**](SyncV1SyncListItemApi.md#updateSyncListItem) | **POST** /v1/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index} | 



## createSyncListItem

> SyncV1ServiceSyncListSyncListItem createSyncListItem(serviceSid, listSid, data, opts)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncListItemApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new List Item in.
let listSid = "listSid_example"; // String | The SID of the Sync List to add the new List Item to. Can be the Sync List resource's `sid` or its `unique_name`.
let data = null; // Object | A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to 16 KiB in length.
let opts = {
  'collectionTtl': 56, // Number | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item's parent Sync List expires (time-to-live) and is deleted.
  'itemTtl': 56, // Number | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item expires (time-to-live) and is deleted.
  'ttl': 56 // Number | An alias for `item_ttl`. If both parameters are provided, this value is ignored.
};
apiInstance.createSyncListItem(serviceSid, listSid, data, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new List Item in. | 
 **listSid** | **String**| The SID of the Sync List to add the new List Item to. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **data** | [**Object**](Object.md)| A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to 16 KiB in length. | 
 **collectionTtl** | **Number**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item&#39;s parent Sync List expires (time-to-live) and is deleted. | [optional] 
 **itemTtl** | **Number**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item expires (time-to-live) and is deleted. | [optional] 
 **ttl** | **Number**| An alias for &#x60;item_ttl&#x60;. If both parameters are provided, this value is ignored. | [optional] 

### Return type

[**SyncV1ServiceSyncListSyncListItem**](SyncV1ServiceSyncListSyncListItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSyncListItem

> deleteSyncListItem(serviceSid, listSid, index, opts)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncListItemApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to delete.
let listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Item resource to delete. Can be the Sync List resource's `sid` or its `unique_name`.
let index = 56; // Number | The index of the Sync List Item resource to delete.
let opts = {
  'ifMatch': "ifMatch_example" // String | If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
};
apiInstance.deleteSyncListItem(serviceSid, listSid, index, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to delete. | 
 **listSid** | **String**| The SID of the Sync List with the Sync List Item resource to delete. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **index** | **Number**| The index of the Sync List Item resource to delete. | 
 **ifMatch** | **String**| If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match). | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSyncListItem

> SyncV1ServiceSyncListSyncListItem fetchSyncListItem(serviceSid, listSid, index)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncListItemApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to fetch.
let listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Item resource to fetch. Can be the Sync List resource's `sid` or its `unique_name`.
let index = 56; // Number | The index of the Sync List Item resource to fetch.
apiInstance.fetchSyncListItem(serviceSid, listSid, index, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to fetch. | 
 **listSid** | **String**| The SID of the Sync List with the Sync List Item resource to fetch. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **index** | **Number**| The index of the Sync List Item resource to fetch. | 

### Return type

[**SyncV1ServiceSyncListSyncListItem**](SyncV1ServiceSyncListSyncListItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncListItem

> ListSyncListItemResponse listSyncListItem(serviceSid, listSid, opts)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncListItemApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the List Item resources to read.
let listSid = "listSid_example"; // String | The SID of the Sync List with the List Items to read. Can be the Sync List resource's `sid` or its `unique_name`.
let opts = {
  'order': "order_example", // SyncListItemEnumQueryResultOrder | How to order the List Items returned by their `index` value. Can be: `asc` (ascending) or `desc` (descending) and the default is ascending.
  'from': "from_example", // String | The `index` of the first Sync List Item resource to read. See also `bounds`.
  'bounds': "bounds_example", // SyncListItemEnumQueryFromBoundType | Whether to include the List Item referenced by the `from` parameter. Can be: `inclusive` to include the List Item referenced by the `from` parameter or `exclusive` to start with the next List Item. The default value is `inclusive`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSyncListItem(serviceSid, listSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the List Item resources to read. | 
 **listSid** | **String**| The SID of the Sync List with the List Items to read. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **order** | **SyncListItemEnumQueryResultOrder**| How to order the List Items returned by their &#x60;index&#x60; value. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) and the default is ascending. | [optional] 
 **from** | **String**| The &#x60;index&#x60; of the first Sync List Item resource to read. See also &#x60;bounds&#x60;. | [optional] 
 **bounds** | **SyncListItemEnumQueryFromBoundType**| Whether to include the List Item referenced by the &#x60;from&#x60; parameter. Can be: &#x60;inclusive&#x60; to include the List Item referenced by the &#x60;from&#x60; parameter or &#x60;exclusive&#x60; to start with the next List Item. The default value is &#x60;inclusive&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSyncListItemResponse**](ListSyncListItemResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSyncListItem

> SyncV1ServiceSyncListSyncListItem updateSyncListItem(serviceSid, listSid, index, opts)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncListItemApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to update.
let listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Item resource to update. Can be the Sync List resource's `sid` or its `unique_name`.
let index = 56; // Number | The index of the Sync List Item resource to update.
let opts = {
  'ifMatch': "ifMatch_example", // String | If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
  'collectionTtl': 56, // Number | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item's parent Sync List expires (time-to-live) and is deleted. This parameter can only be used when the List Item's `data` or `ttl` is updated in the same request.
  'data': null, // Object | A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to 16 KiB in length.
  'itemTtl': 56, // Number | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item expires (time-to-live) and is deleted.
  'ttl': 56 // Number | An alias for `item_ttl`. If both parameters are provided, this value is ignored.
};
apiInstance.updateSyncListItem(serviceSid, listSid, index, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Item resource to update. | 
 **listSid** | **String**| The SID of the Sync List with the Sync List Item resource to update. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **index** | **Number**| The index of the Sync List Item resource to update. | 
 **ifMatch** | **String**| If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match). | [optional] 
 **collectionTtl** | **Number**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item&#39;s parent Sync List expires (time-to-live) and is deleted. This parameter can only be used when the List Item&#39;s &#x60;data&#x60; or &#x60;ttl&#x60; is updated in the same request. | [optional] 
 **data** | [**Object**](Object.md)| A JSON string that represents an arbitrary, schema-less object that the List Item stores. Can be up to 16 KiB in length. | [optional] 
 **itemTtl** | **Number**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the List Item expires (time-to-live) and is deleted. | [optional] 
 **ttl** | **Number**| An alias for &#x60;item_ttl&#x60;. If both parameters are provided, this value is ignored. | [optional] 

### Return type

[**SyncV1ServiceSyncListSyncListItem**](SyncV1ServiceSyncListSyncListItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

