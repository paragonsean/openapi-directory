# TwilioPreview.PreviewSyncDocumentPermissionApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSyncDocumentPermission**](PreviewSyncDocumentPermissionApi.md#deleteSyncDocumentPermission) | **DELETE** /Sync/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity} | 
[**fetchSyncDocumentPermission**](PreviewSyncDocumentPermissionApi.md#fetchSyncDocumentPermission) | **GET** /Sync/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity} | 
[**listSyncDocumentPermission**](PreviewSyncDocumentPermissionApi.md#listSyncDocumentPermission) | **GET** /Sync/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions | 
[**updateSyncDocumentPermission**](PreviewSyncDocumentPermissionApi.md#updateSyncDocumentPermission) | **POST** /Sync/Services/{ServiceSid}/Documents/{DocumentSid}/Permissions/{Identity} | 



## deleteSyncDocumentPermission

> deleteSyncDocumentPermission(serviceSid, documentSid, identity)



Delete a specific Sync Document Permission.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncDocumentPermissionApi();
let serviceSid = "serviceSid_example"; // String | 
let documentSid = "documentSid_example"; // String | Identifier of the Sync Document. Either a SID or a unique name.
let identity = "identity_example"; // String | Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
apiInstance.deleteSyncDocumentPermission(serviceSid, documentSid, identity, (error, data, response) => {
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
 **serviceSid** | **String**|  | 
 **documentSid** | **String**| Identifier of the Sync Document. Either a SID or a unique name. | 
 **identity** | **String**| Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSyncDocumentPermission

> PreviewSyncServiceDocumentDocumentPermission fetchSyncDocumentPermission(serviceSid, documentSid, identity)



Fetch a specific Sync Document Permission.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncDocumentPermissionApi();
let serviceSid = "serviceSid_example"; // String | 
let documentSid = "documentSid_example"; // String | Identifier of the Sync Document. Either a SID or a unique name.
let identity = "identity_example"; // String | Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
apiInstance.fetchSyncDocumentPermission(serviceSid, documentSid, identity, (error, data, response) => {
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
 **serviceSid** | **String**|  | 
 **documentSid** | **String**| Identifier of the Sync Document. Either a SID or a unique name. | 
 **identity** | **String**| Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer. | 

### Return type

[**PreviewSyncServiceDocumentDocumentPermission**](PreviewSyncServiceDocumentDocumentPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncDocumentPermission

> ListSyncDocumentPermissionResponse listSyncDocumentPermission(serviceSid, documentSid, opts)



Retrieve a list of all Permissions applying to a Sync Document.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncDocumentPermissionApi();
let serviceSid = "serviceSid_example"; // String | 
let documentSid = "documentSid_example"; // String | Identifier of the Sync Document. Either a SID or a unique name.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSyncDocumentPermission(serviceSid, documentSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**|  | 
 **documentSid** | **String**| Identifier of the Sync Document. Either a SID or a unique name. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSyncDocumentPermissionResponse**](ListSyncDocumentPermissionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSyncDocumentPermission

> PreviewSyncServiceDocumentDocumentPermission updateSyncDocumentPermission(serviceSid, documentSid, identity, manage, read, write)



Update an identity&#39;s access to a specific Sync Document.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncDocumentPermissionApi();
let serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Sync Service Instance.
let documentSid = "documentSid_example"; // String | Identifier of the Sync Document. Either a SID or a unique name.
let identity = "identity_example"; // String | Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer.
let manage = true; // Boolean | Boolean flag specifying whether the identity can delete the Sync Document.
let read = true; // Boolean | Boolean flag specifying whether the identity can read the Sync Document.
let write = true; // Boolean | Boolean flag specifying whether the identity can update the Sync Document.
apiInstance.updateSyncDocumentPermission(serviceSid, documentSid, identity, manage, read, write, (error, data, response) => {
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
 **serviceSid** | **String**| The unique SID identifier of the Sync Service Instance. | 
 **documentSid** | **String**| Identifier of the Sync Document. Either a SID or a unique name. | 
 **identity** | **String**| Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer. | 
 **manage** | **Boolean**| Boolean flag specifying whether the identity can delete the Sync Document. | 
 **read** | **Boolean**| Boolean flag specifying whether the identity can read the Sync Document. | 
 **write** | **Boolean**| Boolean flag specifying whether the identity can update the Sync Document. | 

### Return type

[**PreviewSyncServiceDocumentDocumentPermission**](PreviewSyncServiceDocumentDocumentPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

