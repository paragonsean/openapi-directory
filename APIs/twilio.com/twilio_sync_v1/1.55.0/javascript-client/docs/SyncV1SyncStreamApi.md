# TwilioSync.SyncV1SyncStreamApi

All URIs are relative to *https://sync.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSyncStream**](SyncV1SyncStreamApi.md#createSyncStream) | **POST** /v1/Services/{ServiceSid}/Streams | 
[**deleteSyncStream**](SyncV1SyncStreamApi.md#deleteSyncStream) | **DELETE** /v1/Services/{ServiceSid}/Streams/{Sid} | 
[**fetchSyncStream**](SyncV1SyncStreamApi.md#fetchSyncStream) | **GET** /v1/Services/{ServiceSid}/Streams/{Sid} | 
[**listSyncStream**](SyncV1SyncStreamApi.md#listSyncStream) | **GET** /v1/Services/{ServiceSid}/Streams | 
[**updateSyncStream**](SyncV1SyncStreamApi.md#updateSyncStream) | **POST** /v1/Services/{ServiceSid}/Streams/{Sid} | 



## createSyncStream

> SyncV1ServiceSyncStream createSyncStream(serviceSid, opts)



Create a new Stream.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncStreamApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new Stream in.
let opts = {
  'ttl': 56, // Number | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live).
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. This value must be unique within its Service and it can be up to 320 characters long. The `unique_name` value can be used as an alternative to the `sid` in the URL path to address the resource.
};
apiInstance.createSyncStream(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) to create the new Stream in. | 
 **ttl** | **Number**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live). | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. This value must be unique within its Service and it can be up to 320 characters long. The &#x60;unique_name&#x60; value can be used as an alternative to the &#x60;sid&#x60; in the URL path to address the resource. | [optional] 

### Return type

[**SyncV1ServiceSyncStream**](SyncV1ServiceSyncStream.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSyncStream

> deleteSyncStream(serviceSid, sid)



Delete a specific Stream.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncStreamApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Stream resource to delete.
let sid = "sid_example"; // String | The SID of the Stream resource to delete.
apiInstance.deleteSyncStream(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Stream resource to delete. | 
 **sid** | **String**| The SID of the Stream resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSyncStream

> SyncV1ServiceSyncStream fetchSyncStream(serviceSid, sid)



Fetch a specific Stream.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncStreamApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Stream resource to fetch.
let sid = "sid_example"; // String | The SID of the Stream resource to fetch.
apiInstance.fetchSyncStream(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Stream resource to fetch. | 
 **sid** | **String**| The SID of the Stream resource to fetch. | 

### Return type

[**SyncV1ServiceSyncStream**](SyncV1ServiceSyncStream.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncStream

> ListSyncStreamResponse listSyncStream(serviceSid, opts)



Retrieve a list of all Streams in a Service Instance.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncStreamApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Stream resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSyncStream(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Stream resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSyncStreamResponse**](ListSyncStreamResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSyncStream

> SyncV1ServiceSyncStream updateSyncStream(serviceSid, sid, opts)



Update a specific Stream.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncStreamApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Stream resource to update.
let sid = "sid_example"; // String | The SID of the Stream resource to update.
let opts = {
  'ttl': 56 // Number | How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live).
};
apiInstance.updateSyncStream(serviceSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Stream resource to update. | 
 **sid** | **String**| The SID of the Stream resource to update. | 
 **ttl** | **Number**| How long, [in seconds](https://www.twilio.com/docs/sync/limits#sync-payload-limits), before the Stream expires and is deleted (time-to-live). | [optional] 

### Return type

[**SyncV1ServiceSyncStream**](SyncV1ServiceSyncStream.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

