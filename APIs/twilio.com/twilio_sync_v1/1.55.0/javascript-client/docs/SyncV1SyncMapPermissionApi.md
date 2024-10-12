# TwilioSync.SyncV1SyncMapPermissionApi

All URIs are relative to *https://sync.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSyncMapPermission**](SyncV1SyncMapPermissionApi.md#deleteSyncMapPermission) | **DELETE** /v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity} | 
[**fetchSyncMapPermission**](SyncV1SyncMapPermissionApi.md#fetchSyncMapPermission) | **GET** /v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity} | 
[**listSyncMapPermission**](SyncV1SyncMapPermissionApi.md#listSyncMapPermission) | **GET** /v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions | 
[**updateSyncMapPermission**](SyncV1SyncMapPermissionApi.md#updateSyncMapPermission) | **POST** /v1/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity} | 



## deleteSyncMapPermission

> deleteSyncMapPermission(serviceSid, mapSid, identity)



Delete a specific Sync Map Permission.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapPermissionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to delete. Can be the Service's `sid` value or `default`.
let mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Permission resource to delete. Can be the Sync Map resource's `sid` or its `unique_name`.
let identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Sync Map Permission resource to delete.
apiInstance.deleteSyncMapPermission(serviceSid, mapSid, identity, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to delete. Can be the Service&#39;s &#x60;sid&#x60; value or &#x60;default&#x60;. | 
 **mapSid** | **String**| The SID of the Sync Map with the Sync Map Permission resource to delete. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Sync Map Permission resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSyncMapPermission

> SyncV1ServiceSyncMapSyncMapPermission fetchSyncMapPermission(serviceSid, mapSid, identity)



Fetch a specific Sync Map Permission.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapPermissionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to fetch. Can be the Service's `sid` value or `default`.
let mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Permission resource to fetch. Can be the Sync Map resource's `sid` or its `unique_name`.
let identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Sync Map Permission resource to fetch.
apiInstance.fetchSyncMapPermission(serviceSid, mapSid, identity, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to fetch. Can be the Service&#39;s &#x60;sid&#x60; value or &#x60;default&#x60;. | 
 **mapSid** | **String**| The SID of the Sync Map with the Sync Map Permission resource to fetch. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Sync Map Permission resource to fetch. | 

### Return type

[**SyncV1ServiceSyncMapSyncMapPermission**](SyncV1ServiceSyncMapSyncMapPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncMapPermission

> ListSyncMapPermissionResponse listSyncMapPermission(serviceSid, mapSid, opts)



Retrieve a list of all Permissions applying to a Sync Map.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapPermissionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resources to read. Can be the Service's `sid` value or `default`.
let mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Permission resources to read. Can be the Sync Map resource's `sid` or its `unique_name`.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSyncMapPermission(serviceSid, mapSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resources to read. Can be the Service&#39;s &#x60;sid&#x60; value or &#x60;default&#x60;. | 
 **mapSid** | **String**| The SID of the Sync Map with the Permission resources to read. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSyncMapPermissionResponse**](ListSyncMapPermissionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSyncMapPermission

> SyncV1ServiceSyncMapSyncMapPermission updateSyncMapPermission(serviceSid, mapSid, identity, manage, read, write)



Update an identity&#39;s access to a specific Sync Map.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncMapPermissionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to update. Can be the Service's `sid` value or `default`.
let mapSid = "mapSid_example"; // String | The SID of the Sync Map with the Sync Map Permission resource to update. Can be the Sync Map resource's `sid` or its `unique_name`.
let identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Sync Map Permission resource to update.
let manage = true; // Boolean | Whether the identity can delete the Sync Map. Default value is `false`.
let read = true; // Boolean | Whether the identity can read the Sync Map and its Items. Default value is `false`.
let write = true; // Boolean | Whether the identity can create, update, and delete Items in the Sync Map. Default value is `false`.
apiInstance.updateSyncMapPermission(serviceSid, mapSid, identity, manage, read, write, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync Map Permission resource to update. Can be the Service&#39;s &#x60;sid&#x60; value or &#x60;default&#x60;. | 
 **mapSid** | **String**| The SID of the Sync Map with the Sync Map Permission resource to update. Can be the Sync Map resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Sync Map Permission resource to update. | 
 **manage** | **Boolean**| Whether the identity can delete the Sync Map. Default value is &#x60;false&#x60;. | 
 **read** | **Boolean**| Whether the identity can read the Sync Map and its Items. Default value is &#x60;false&#x60;. | 
 **write** | **Boolean**| Whether the identity can create, update, and delete Items in the Sync Map. Default value is &#x60;false&#x60;. | 

### Return type

[**SyncV1ServiceSyncMapSyncMapPermission**](SyncV1ServiceSyncMapSyncMapPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

