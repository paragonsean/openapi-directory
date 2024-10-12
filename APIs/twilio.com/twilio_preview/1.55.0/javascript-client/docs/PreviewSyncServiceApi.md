# TwilioPreview.PreviewSyncServiceApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSyncService**](PreviewSyncServiceApi.md#createSyncService) | **POST** /Sync/Services | 
[**deleteSyncService**](PreviewSyncServiceApi.md#deleteSyncService) | **DELETE** /Sync/Services/{Sid} | 
[**fetchSyncService**](PreviewSyncServiceApi.md#fetchSyncService) | **GET** /Sync/Services/{Sid} | 
[**listSyncService**](PreviewSyncServiceApi.md#listSyncService) | **GET** /Sync/Services | 
[**updateSyncService**](PreviewSyncServiceApi.md#updateSyncService) | **POST** /Sync/Services/{Sid} | 



## createSyncService

> PreviewSyncService createSyncService(opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncServiceApi();
let opts = {
  'aclEnabled': true, // Boolean | 
  'friendlyName': "friendlyName_example", // String | 
  'reachabilityWebhooksEnabled': true, // Boolean | 
  'webhookUrl': "webhookUrl_example" // String | 
};
apiInstance.createSyncService(opts, (error, data, response) => {
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
 **aclEnabled** | **Boolean**|  | [optional] 
 **friendlyName** | **String**|  | [optional] 
 **reachabilityWebhooksEnabled** | **Boolean**|  | [optional] 
 **webhookUrl** | **String**|  | [optional] 

### Return type

[**PreviewSyncService**](PreviewSyncService.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSyncService

> deleteSyncService(sid)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncServiceApi();
let sid = "sid_example"; // String | 
apiInstance.deleteSyncService(sid, (error, data, response) => {
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
 **sid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSyncService

> PreviewSyncService fetchSyncService(sid)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncServiceApi();
let sid = "sid_example"; // String | 
apiInstance.fetchSyncService(sid, (error, data, response) => {
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
 **sid** | **String**|  | 

### Return type

[**PreviewSyncService**](PreviewSyncService.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncService

> ListSyncServiceResponse listSyncService(opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncServiceApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSyncService(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSyncServiceResponse**](ListSyncServiceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSyncService

> PreviewSyncService updateSyncService(sid, opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncServiceApi();
let sid = "sid_example"; // String | 
let opts = {
  'aclEnabled': true, // Boolean | 
  'friendlyName': "friendlyName_example", // String | 
  'reachabilityWebhooksEnabled': true, // Boolean | 
  'webhookUrl': "webhookUrl_example" // String | 
};
apiInstance.updateSyncService(sid, opts, (error, data, response) => {
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
 **sid** | **String**|  | 
 **aclEnabled** | **Boolean**|  | [optional] 
 **friendlyName** | **String**|  | [optional] 
 **reachabilityWebhooksEnabled** | **Boolean**|  | [optional] 
 **webhookUrl** | **String**|  | [optional] 

### Return type

[**PreviewSyncService**](PreviewSyncService.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

