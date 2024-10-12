# TwilioPreview.PreviewSyncSyncListPermissionApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteSyncSyncListPermission**](PreviewSyncSyncListPermissionApi.md#deleteSyncSyncListPermission) | **DELETE** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity} | 
[**fetchSyncSyncListPermission**](PreviewSyncSyncListPermissionApi.md#fetchSyncSyncListPermission) | **GET** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity} | 
[**listSyncSyncListPermission**](PreviewSyncSyncListPermissionApi.md#listSyncSyncListPermission) | **GET** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Permissions | 
[**updateSyncSyncListPermission**](PreviewSyncSyncListPermissionApi.md#updateSyncSyncListPermission) | **POST** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Permissions/{Identity} | 



## deleteSyncSyncListPermission

> deleteSyncSyncListPermission(serviceSid, listSid, identity)



Delete a specific Sync List Permission.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncListPermissionApi();
let serviceSid = "serviceSid_example"; // String | 
let listSid = "listSid_example"; // String | Identifier of the Sync List. Either a SID or a unique name.
let identity = "identity_example"; // String | Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
apiInstance.deleteSyncSyncListPermission(serviceSid, listSid, identity, (error, data, response) => {
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
 **listSid** | **String**| Identifier of the Sync List. Either a SID or a unique name. | 
 **identity** | **String**| Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSyncSyncListPermission

> PreviewSyncServiceSyncListSyncListPermission fetchSyncSyncListPermission(serviceSid, listSid, identity)



Fetch a specific Sync List Permission.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncListPermissionApi();
let serviceSid = "serviceSid_example"; // String | 
let listSid = "listSid_example"; // String | Identifier of the Sync List. Either a SID or a unique name.
let identity = "identity_example"; // String | Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer.
apiInstance.fetchSyncSyncListPermission(serviceSid, listSid, identity, (error, data, response) => {
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
 **listSid** | **String**| Identifier of the Sync List. Either a SID or a unique name. | 
 **identity** | **String**| Arbitrary string identifier representing a user associated with an FPA token, assigned by the developer. | 

### Return type

[**PreviewSyncServiceSyncListSyncListPermission**](PreviewSyncServiceSyncListSyncListPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncSyncListPermission

> ListSyncSyncListPermissionResponse listSyncSyncListPermission(serviceSid, listSid, opts)



Retrieve a list of all Permissions applying to a Sync List.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncListPermissionApi();
let serviceSid = "serviceSid_example"; // String | 
let listSid = "listSid_example"; // String | Identifier of the Sync List. Either a SID or a unique name.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSyncSyncListPermission(serviceSid, listSid, opts, (error, data, response) => {
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
 **listSid** | **String**| Identifier of the Sync List. Either a SID or a unique name. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSyncSyncListPermissionResponse**](ListSyncSyncListPermissionResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSyncSyncListPermission

> PreviewSyncServiceSyncListSyncListPermission updateSyncSyncListPermission(serviceSid, listSid, identity, manage, read, write)



Update an identity&#39;s access to a specific Sync List.

### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncListPermissionApi();
let serviceSid = "serviceSid_example"; // String | The unique SID identifier of the Sync Service Instance.
let listSid = "listSid_example"; // String | Identifier of the Sync List. Either a SID or a unique name.
let identity = "identity_example"; // String | Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer.
let manage = true; // Boolean | Boolean flag specifying whether the identity can delete the Sync List.
let read = true; // Boolean | Boolean flag specifying whether the identity can read the Sync List.
let write = true; // Boolean | Boolean flag specifying whether the identity can create, update and delete Items of the Sync List.
apiInstance.updateSyncSyncListPermission(serviceSid, listSid, identity, manage, read, write, (error, data, response) => {
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
 **listSid** | **String**| Identifier of the Sync List. Either a SID or a unique name. | 
 **identity** | **String**| Arbitrary string identifier representing a human user associated with an FPA token, assigned by the developer. | 
 **manage** | **Boolean**| Boolean flag specifying whether the identity can delete the Sync List. | 
 **read** | **Boolean**| Boolean flag specifying whether the identity can read the Sync List. | 
 **write** | **Boolean**| Boolean flag specifying whether the identity can create, update and delete Items of the Sync List. | 

### Return type

[**PreviewSyncServiceSyncListSyncListPermission**](PreviewSyncServiceSyncListSyncListPermission.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

