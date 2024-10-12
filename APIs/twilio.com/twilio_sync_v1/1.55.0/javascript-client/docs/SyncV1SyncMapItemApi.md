# TwilioSync.SyncV1SyncMapItemApi

All URIs are relative to *https://sync.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSyncMapItem**](SyncV1SyncMapItemApi.md#createSyncMapItem) | **POST** /v1/Services/{ServiceSid}/Maps/{MapSid}/Items | 
[**deleteSyncMapItem**](SyncV1SyncMapItemApi.md#deleteSyncMapItem) | **DELETE** /v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key} | 
[**fetchSyncMapItem**](SyncV1SyncMapItemApi.md#fetchSyncMapItem) | **GET** /v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key} | 
[**listSyncMapItem**](SyncV1SyncMapItemApi.md#listSyncMapItem) | **GET** /v1/Services/{ServiceSid}/Maps/{MapSid}/Items | 
[**updateSyncMapItem**](SyncV1SyncMapItemApi.md#updateSyncMapItem) | **POST** /v1/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key} | 



## createSyncMapItem

> SyncV1ServiceSyncMapSyncMapItem createSyncMapItem(serviceSid, mapSid, data, key, opts)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapItemApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the Map Item in.
let mapSid = "mapSid_example"; // String | The SID of the Sync Map to add the new Map Item to. Can be the Sync Map resource's `sid` or its `unique_name`.
let data = null; // Object | A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to 16 KiB in length.
let key = "key_example"; // String | The unique, user-defined key for the Map Item. Can be up to 320 characters long.
let opts = {
  'collectionTtl': 56, // Number | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item's parent Sync Map expires (time-to-live) and is deleted.
  'itemTtl': 56, // Number | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item expires (time-to-live) and is deleted.
  'ttl': 56 // Number | An alias for `item_ttl`. If both parameters are provided, this value is ignored.
};
apiInstance.createSyncMapItem(serviceSid, mapSid, data, key, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the Map Item in. | 
 **mapSid** | **String**| The SID of the Sync Map to add the new Map Item to. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **data** | [**Object**](Object.md)| A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to 16 KiB in length. | 
 **key** | **String**| The unique, user-defined key for the Map Item. Can be up to 320 characters long. | 
 **collectionTtl** | **Number**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item&#39;s parent Sync Map expires (time-to-live) and is deleted. | [optional] 
 **itemTtl** | **Number**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item expires (time-to-live) and is deleted. | [optional] 
 **ttl** | **Number**| An alias for &#x60;item_ttl&#x60;. If both parameters are provided, this value is ignored. | [optional] 

### Return type

[**SyncV1ServiceSyncMapSyncMapItem**](SyncV1ServiceSyncMapSyncMapItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSyncMapItem

> deleteSyncMapItem(serviceSid, mapSid, key, opts)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapItemApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to delete.
let mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Item resource to delete. Can be the Sync Map resource's `sid` or its `unique_name`.
let key = "key_example"; // String | The `key` value of the Sync Map Item resource to delete.
let opts = {
  'ifMatch': "ifMatch_example" // String | If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
};
apiInstance.deleteSyncMapItem(serviceSid, mapSid, key, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to delete. | 
 **mapSid** | **String**| The SID of the Sync Map with the Sync Map Item resource to delete. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **key** | **String**| The &#x60;key&#x60; value of the Sync Map Item resource to delete. | 
 **ifMatch** | **String**| If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match). | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSyncMapItem

> SyncV1ServiceSyncMapSyncMapItem fetchSyncMapItem(serviceSid, mapSid, key)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapItemApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to fetch.
let mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource's `sid` or its `unique_name`.
let key = "key_example"; // String | The `key` value of the Sync Map Item resource to fetch.
apiInstance.fetchSyncMapItem(serviceSid, mapSid, key, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to fetch. | 
 **mapSid** | **String**| The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **key** | **String**| The &#x60;key&#x60; value of the Sync Map Item resource to fetch. | 

### Return type

[**SyncV1ServiceSyncMapSyncMapItem**](SyncV1ServiceSyncMapSyncMapItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncMapItem

> ListSyncMapItemResponse listSyncMapItem(serviceSid, mapSid, opts)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapItemApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Map Item resources to read.
let mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource's `sid` or its `unique_name`.
let opts = {
  'order': "order_example", // SyncMapItemEnumQueryResultOrder | How to order the Map Items returned by their `key` value. Can be: `asc` (ascending) or `desc` (descending) and the default is ascending. Map Items are [ordered lexicographically](https://en.wikipedia.org/wiki/Lexicographical_order) by Item key.
  'from': "from_example", // String | The `key` of the first Sync Map Item resource to read. See also `bounds`.
  'bounds': "bounds_example", // SyncMapItemEnumQueryFromBoundType | Whether to include the Map Item referenced by the `from` parameter. Can be: `inclusive` to include the Map Item referenced by the `from` parameter or `exclusive` to start with the next Map Item. The default value is `inclusive`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSyncMapItem(serviceSid, mapSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Map Item resources to read. | 
 **mapSid** | **String**| The SID of the Sync Map with the Sync Map Item resource to fetch. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **order** | **SyncMapItemEnumQueryResultOrder**| How to order the Map Items returned by their &#x60;key&#x60; value. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) and the default is ascending. Map Items are [ordered lexicographically](https://en.wikipedia.org/wiki/Lexicographical_order) by Item key. | [optional] 
 **from** | **String**| The &#x60;key&#x60; of the first Sync Map Item resource to read. See also &#x60;bounds&#x60;. | [optional] 
 **bounds** | **SyncMapItemEnumQueryFromBoundType**| Whether to include the Map Item referenced by the &#x60;from&#x60; parameter. Can be: &#x60;inclusive&#x60; to include the Map Item referenced by the &#x60;from&#x60; parameter or &#x60;exclusive&#x60; to start with the next Map Item. The default value is &#x60;inclusive&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSyncMapItemResponse**](ListSyncMapItemResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSyncMapItem

> SyncV1ServiceSyncMapSyncMapItem updateSyncMapItem(serviceSid, mapSid, key, opts)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapItemApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to update.
let mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Item resource to update. Can be the Sync Map resource's `sid` or its `unique_name`.
let key = "key_example"; // String | The `key` value of the Sync Map Item resource to update. 
let opts = {
  'ifMatch': "ifMatch_example", // String | If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match).
  'collectionTtl': 56, // Number | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item's parent Sync Map expires (time-to-live) and is deleted. This parameter can only be used when the Map Item's `data` or `ttl` is updated in the same request.
  'data': null, // Object | A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to 16 KiB in length.
  'itemTtl': 56, // Number | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item expires (time-to-live) and is deleted.
  'ttl': 56 // Number | An alias for `item_ttl`. If both parameters are provided, this value is ignored.
};
apiInstance.updateSyncMapItem(serviceSid, mapSid, key, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Item resource to update. | 
 **mapSid** | **String**| The SID of the Sync Map with the Sync Map Item resource to update. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **key** | **String**| The &#x60;key&#x60; value of the Sync Map Item resource to update.  | 
 **ifMatch** | **String**| If provided, applies this mutation if (and only if) the “revision” field of this [map item] matches the provided value. This matches the semantics of (and is implemented with) the HTTP [If-Match header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match). | [optional] 
 **collectionTtl** | **Number**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item&#39;s parent Sync Map expires (time-to-live) and is deleted. This parameter can only be used when the Map Item&#39;s &#x60;data&#x60; or &#x60;ttl&#x60; is updated in the same request. | [optional] 
 **data** | [**Object**](Object.md)| A JSON string that represents an arbitrary, schema-less object that the Map Item stores. Can be up to 16 KiB in length. | [optional] 
 **itemTtl** | **Number**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Map Item expires (time-to-live) and is deleted. | [optional] 
 **ttl** | **Number**| An alias for &#x60;item_ttl&#x60;. If both parameters are provided, this value is ignored. | [optional] 

### Return type

[**SyncV1ServiceSyncMapSyncMapItem**](SyncV1ServiceSyncMapSyncMapItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

