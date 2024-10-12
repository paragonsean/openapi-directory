# TwilioSync.SyncV1SyncMapApi

All URIs are relative to *https://sync.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSyncMap**](SyncV1SyncMapApi.md#createSyncMap) | **POST** /v1/Services/{ServiceSid}/Maps | 
[**deleteSyncMap**](SyncV1SyncMapApi.md#deleteSyncMap) | **DELETE** /v1/Services/{ServiceSid}/Maps/{Sid} | 
[**fetchSyncMap**](SyncV1SyncMapApi.md#fetchSyncMap) | **GET** /v1/Services/{ServiceSid}/Maps/{Sid} | 
[**listSyncMap**](SyncV1SyncMapApi.md#listSyncMap) | **GET** /v1/Services/{ServiceSid}/Maps | 
[**updateSyncMap**](SyncV1SyncMapApi.md#updateSyncMap) | **POST** /v1/Services/{ServiceSid}/Maps/{Sid} | 



## createSyncMap

> SyncV1ServiceSyncMap createSyncMap(serviceSid, opts)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the Sync Map in.
let opts = {
  'collectionTtl': 56, // Number | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Sync Map expires (time-to-live) and is deleted.
  'ttl': 56, // Number | An alias for `collection_ttl`. If both parameters are provided, this value is ignored.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used as an alternative to the `sid` in the URL path to address the resource.
};
apiInstance.createSyncMap(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the Sync Map in. | 
 **collectionTtl** | **Number**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Sync Map expires (time-to-live) and is deleted. | [optional] 
 **ttl** | **Number**| An alias for &#x60;collection_ttl&#x60;. If both parameters are provided, this value is ignored. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. | [optional] 

### Return type

[**SyncV1ServiceSyncMap**](SyncV1ServiceSyncMap.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSyncMap

> deleteSyncMap(serviceSid, sid)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to delete.
let sid = "sid_example"; // String | The SID of the Sync Map resource to delete. Can be the Sync Map's `sid` or its `unique_name`.
apiInstance.deleteSyncMap(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to delete. | 
 **sid** | **String**| The SID of the Sync Map resource to delete. Can be the Sync Map&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSyncMap

> SyncV1ServiceSyncMap fetchSyncMap(serviceSid, sid)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to fetch.
let sid = "sid_example"; // String | The SID of the Sync Map resource to fetch. Can be the Sync Map's `sid` or its `unique_name`.
apiInstance.fetchSyncMap(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to fetch. | 
 **sid** | **String**| The SID of the Sync Map resource to fetch. Can be the Sync Map&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 

### Return type

[**SyncV1ServiceSyncMap**](SyncV1ServiceSyncMap.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncMap

> ListSyncMapResponse listSyncMap(serviceSid, opts)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSyncMap(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSyncMapResponse**](ListSyncMapResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSyncMap

> SyncV1ServiceSyncMap updateSyncMap(serviceSid, sid, opts)





### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to update.
let sid = "sid_example"; // String | The SID of the Sync Map resource to update. Can be the Sync Map's `sid` or its `unique_name`.
let opts = {
  'collectionTtl': 56, // Number | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Sync Map expires (time-to-live) and is deleted.
  'ttl': 56 // Number | An alias for `collection_ttl`. If both parameters are provided, this value is ignored.
};
apiInstance.updateSyncMap(serviceSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map resource to update. | 
 **sid** | **String**| The SID of the Sync Map resource to update. Can be the Sync Map&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **collectionTtl** | **Number**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Sync Map expires (time-to-live) and is deleted. | [optional] 
 **ttl** | **Number**| An alias for &#x60;collection_ttl&#x60;. If both parameters are provided, this value is ignored. | [optional] 

### Return type

[**SyncV1ServiceSyncMap**](SyncV1ServiceSyncMap.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

