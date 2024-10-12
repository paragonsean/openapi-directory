# TwilioSync.SyncV1SyncListPermissionApi

All URIs are relative to *https://sync.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSyncListPermission**](SyncV1SyncListPermissionApi.md#deleteSyncListPermission) | **DELETE** /v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity} | 
[**fetchSyncListPermission**](SyncV1SyncListPermissionApi.md#fetchSyncListPermission) | **GET** /v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity} | 
[**listSyncListPermission**](SyncV1SyncListPermissionApi.md#listSyncListPermission) | **GET** /v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions | 
[**updateSyncListPermission**](SyncV1SyncListPermissionApi.md#updateSyncListPermission) | **POST** /v1/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity} | 



## deleteSyncListPermission

> deleteSyncListPermission(serviceSid, listSid, identity)



Delete a specific Sync List Permission.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncListPermissionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to delete.
let listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Permission resource to delete. Can be the Sync List resource's `sid` or its `unique_name`.
let identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Sync List Permission resource to delete.
apiInstance.deleteSyncListPermission(serviceSid, listSid, identity, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to delete. | 
 **listSid** | **String**| The SID of the Sync List with the Sync List Permission resource to delete. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Sync List Permission resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSyncListPermission

> SyncV1ServiceSyncListSyncListPermission fetchSyncListPermission(serviceSid, listSid, identity)



Fetch a specific Sync List Permission.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncListPermissionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to fetch.
let listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Permission resource to fetch. Can be the Sync List resource's `sid` or its `unique_name`.
let identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Sync List Permission resource to fetch.
apiInstance.fetchSyncListPermission(serviceSid, listSid, identity, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to fetch. | 
 **listSid** | **String**| The SID of the Sync List with the Sync List Permission resource to fetch. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Sync List Permission resource to fetch. | 

### Return type

[**SyncV1ServiceSyncListSyncListPermission**](SyncV1ServiceSyncListSyncListPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncListPermission

> ListSyncListPermissionResponse listSyncListPermission(serviceSid, listSid, opts)



Retrieve a list of all Permissions applying to a Sync List.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncListPermissionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resources to read.
let listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Permission resources to read. Can be the Sync List resource's `sid` or its `unique_name`.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSyncListPermission(serviceSid, listSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resources to read. | 
 **listSid** | **String**| The SID of the Sync List with the Sync List Permission resources to read. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSyncListPermissionResponse**](ListSyncListPermissionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSyncListPermission

> SyncV1ServiceSyncListSyncListPermission updateSyncListPermission(serviceSid, listSid, identity, manage, read, write)



Update an identity&#39;s access to a specific Sync List.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1SyncListPermissionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to update.
let listSid = "listSid_example"; // String | The SID of the Sync List with the Sync List Permission resource to update. Can be the Sync List resource's `sid` or its `unique_name`.
let identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Sync List Permission resource to update.
let manage = true; // Boolean | Whether the identity can delete the Sync List. Default value is `false`.
let read = true; // Boolean | Whether the identity can read the Sync List and its Items. Default value is `false`.
let write = true; // Boolean | Whether the identity can create, update, and delete Items in the Sync List. Default value is `false`.
apiInstance.updateSyncListPermission(serviceSid, listSid, identity, manage, read, write, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Sync List Permission resource to update. | 
 **listSid** | **String**| The SID of the Sync List with the Sync List Permission resource to update. Can be the Sync List resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Sync List Permission resource to update. | 
 **manage** | **Boolean**| Whether the identity can delete the Sync List. Default value is &#x60;false&#x60;. | 
 **read** | **Boolean**| Whether the identity can read the Sync List and its Items. Default value is &#x60;false&#x60;. | 
 **write** | **Boolean**| Whether the identity can create, update, and delete Items in the Sync List. Default value is &#x60;false&#x60;. | 

### Return type

[**SyncV1ServiceSyncListSyncListPermission**](SyncV1ServiceSyncListSyncListPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

