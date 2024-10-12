# TwilioSync.SyncV1DocumentPermissionApi

All URIs are relative to *https://sync.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteDocumentPermission**](SyncV1DocumentPermissionApi.md#deleteDocumentPermission) | **DELETE** /v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity} | 
[**fetchDocumentPermission**](SyncV1DocumentPermissionApi.md#fetchDocumentPermission) | **GET** /v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity} | 
[**listDocumentPermission**](SyncV1DocumentPermissionApi.md#listDocumentPermission) | **GET** /v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions | 
[**updateDocumentPermission**](SyncV1DocumentPermissionApi.md#updateDocumentPermission) | **POST** /v1/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity} | 



## deleteDocumentPermission

> deleteDocumentPermission(serviceSid, documentSid, identity)



Delete a specific Sync Document Permission.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1DocumentPermissionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to delete.
let documentSid = "documentSid_example"; // String | The SID of the Sync Document with the Document Permission resource to delete. Can be the Document resource's `sid` or its `unique_name`.
let identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Document Permission resource to delete.
apiInstance.deleteDocumentPermission(serviceSid, documentSid, identity, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to delete. | 
 **documentSid** | **String**| The SID of the Sync Document with the Document Permission resource to delete. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Document Permission resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchDocumentPermission

> SyncV1ServiceDocumentDocumentPermission fetchDocumentPermission(serviceSid, documentSid, identity)



Fetch a specific Sync Document Permission.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1DocumentPermissionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to fetch.
let documentSid = "documentSid_example"; // String | The SID of the Sync Document with the Document Permission resource to fetch. Can be the Document resource's `sid` or its `unique_name`.
let identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Document Permission resource to fetch.
apiInstance.fetchDocumentPermission(serviceSid, documentSid, identity, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to fetch. | 
 **documentSid** | **String**| The SID of the Sync Document with the Document Permission resource to fetch. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Document Permission resource to fetch. | 

### Return type

[**SyncV1ServiceDocumentDocumentPermission**](SyncV1ServiceDocumentDocumentPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDocumentPermission

> ListDocumentPermissionResponse listDocumentPermission(serviceSid, documentSid, opts)



Retrieve a list of all Permissions applying to a Sync Document.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1DocumentPermissionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resources to read.
let documentSid = "documentSid_example"; // String | The SID of the Sync Document with the Document Permission resources to read. Can be the Document resource's `sid` or its `unique_name`.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDocumentPermission(serviceSid, documentSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resources to read. | 
 **documentSid** | **String**| The SID of the Sync Document with the Document Permission resources to read. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListDocumentPermissionResponse**](ListDocumentPermissionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateDocumentPermission

> SyncV1ServiceDocumentDocumentPermission updateDocumentPermission(serviceSid, documentSid, identity, manage, read, write)



Update an identity&#39;s access to a specific Sync Document.

### Example

```javascript
import TwilioSync from 'twilio_sync';
let defaultClient = TwilioSync.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSync.SyncV1DocumentPermissionApi();
let serviceSid = "serviceSid_example"; // String | The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to update.
let documentSid = "documentSid_example"; // String | The SID of the Sync Document with the Document Permission resource to update. Can be the Document resource's `sid` or its `unique_name`.
let identity = "identity_example"; // String | The application-defined string that uniquely identifies the User's Document Permission resource to update.
let manage = true; // Boolean | Whether the identity can delete the Sync Document. Default value is `false`.
let read = true; // Boolean | Whether the identity can read the Sync Document. Default value is `false`.
let write = true; // Boolean | Whether the identity can update the Sync Document. Default value is `false`.
apiInstance.updateDocumentPermission(serviceSid, documentSid, identity, manage, read, write, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the [Sync Service](https://www.twilio.com/docs/sync/api/service) with the Document Permission resource to update. | 
 **documentSid** | **String**| The SID of the Sync Document with the Document Permission resource to update. Can be the Document resource&#39;s &#x60;sid&#x60; or its &#x60;unique_name&#x60;. | 
 **identity** | **String**| The application-defined string that uniquely identifies the User&#39;s Document Permission resource to update. | 
 **manage** | **Boolean**| Whether the identity can delete the Sync Document. Default value is &#x60;false&#x60;. | 
 **read** | **Boolean**| Whether the identity can read the Sync Document. Default value is &#x60;false&#x60;. | 
 **write** | **Boolean**| Whether the identity can update the Sync Document. Default value is &#x60;false&#x60;. | 

### Return type

[**SyncV1ServiceDocumentDocumentPermission**](SyncV1ServiceDocumentDocumentPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

