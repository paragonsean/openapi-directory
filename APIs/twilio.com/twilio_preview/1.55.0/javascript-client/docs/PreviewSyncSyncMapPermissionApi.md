# TwilioPreview.PreviewSyncSyncMapPermissionApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSyncSyncMapPermission**](PreviewSyncSyncMapPermissionApi.md#deleteSyncSyncMapPermission) | **DELETE** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity} | 
[**fetchSyncSyncMapPermission**](PreviewSyncSyncMapPermissionApi.md#fetchSyncSyncMapPermission) | **GET** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity} | 
[**listSyncSyncMapPermission**](PreviewSyncSyncMapPermissionApi.md#listSyncSyncMapPermission) | **GET** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Permissions | 
[**updateSyncSyncMapPermission**](PreviewSyncSyncMapPermissionApi.md#updateSyncSyncMapPermission) | **POST** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Permissions/{Identity} | 



## deleteSyncSyncMapPermission

> deleteSyncSyncMapPermission(serviceSid, mapSid, identity)



Delete a specific Sync Map Permission.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncMapPermissionApi();
let serviceSid = "serviceSid_example"; // String | 
let mapSid = "mapSid_example"; // String | Identifier of the Sync Map. Either a SID or a unique name.
let identity = "identity_example"; // String | Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
apiInstance.deleteSyncSyncMapPermission(serviceSid, mapSid, identity, (error, data, response) => {
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
 **mapSid** | **String**| Identifier of the Sync Map. Either a SID or a unique name. | 
 **identity** | **String**| Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSyncSyncMapPermission

> PreviewSyncServiceSyncMapSyncMapPermission fetchSyncSyncMapPermission(serviceSid, mapSid, identity)



Fetch a specific Sync Map Permission.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncMapPermissionApi();
let serviceSid = "serviceSid_example"; // String | 
let mapSid = "mapSid_example"; // String | Identifier of the Sync Map. Either a SID or a unique name.
let identity = "identity_example"; // String | Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
apiInstance.fetchSyncSyncMapPermission(serviceSid, mapSid, identity, (error, data, response) => {
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
 **mapSid** | **String**| Identifier of the Sync Map. Either a SID or a unique name. | 
 **identity** | **String**| Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer. | 

### Return type

[**PreviewSyncServiceSyncMapSyncMapPermission**](PreviewSyncServiceSyncMapSyncMapPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncSyncMapPermission

> ListSyncSyncMapPermissionResponse listSyncSyncMapPermission(serviceSid, mapSid, opts)



Retrieve a list of all Permissions applying to a Sync Map.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncMapPermissionApi();
let serviceSid = "serviceSid_example"; // String | 
let mapSid = "mapSid_example"; // String | Identifier of the Sync Map. Either a SID or a unique name.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSyncSyncMapPermission(serviceSid, mapSid, opts, (error, data, response) => {
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
 **mapSid** | **String**| Identifier of the Sync Map. Either a SID or a unique name. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSyncSyncMapPermissionResponse**](ListSyncSyncMapPermissionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSyncSyncMapPermission

> PreviewSyncServiceSyncMapSyncMapPermission updateSyncSyncMapPermission(serviceSid, mapSid, identity, manage, read, write)



Update an identity&#39;s access to a specific Sync Map.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncMapPermissionApi();
let serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Sync Service Instance.
let mapSid = "mapSid_example"; // String | Identifier of the Sync Map. Either a SID or a unique name.
let identity = "identity_example"; // String | Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer.
let manage = true; // Boolean | Boolean flag specifying whether the identity can delete the Sync Map.
let read = true; // Boolean | Boolean flag specifying whether the identity can read the Sync Map.
let write = true; // Boolean | Boolean flag specifying whether the identity can create, update and delete Items of the Sync Map.
apiInstance.updateSyncSyncMapPermission(serviceSid, mapSid, identity, manage, read, write, (error, data, response) => {
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
 **mapSid** | **String**| Identifier of the Sync Map. Either a SID or a unique name. | 
 **identity** | **String**| Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer. | 
 **manage** | **Boolean**| Boolean flag specifying whether the identity can delete the Sync Map. | 
 **read** | **Boolean**| Boolean flag specifying whether the identity can read the Sync Map. | 
 **write** | **Boolean**| Boolean flag specifying whether the identity can create, update and delete Items of the Sync Map. | 

### Return type

[**PreviewSyncServiceSyncMapSyncMapPermission**](PreviewSyncServiceSyncMapSyncMapPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

