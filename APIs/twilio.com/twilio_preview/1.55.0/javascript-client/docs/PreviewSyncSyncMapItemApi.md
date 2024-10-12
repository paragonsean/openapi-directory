# TwilioPreview.PreviewSyncSyncMapItemApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSyncSyncMapItem**](PreviewSyncSyncMapItemApi.md#createSyncSyncMapItem) | **POST** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Items | 
[**deleteSyncSyncMapItem**](PreviewSyncSyncMapItemApi.md#deleteSyncSyncMapItem) | **DELETE** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key} | 
[**fetchSyncSyncMapItem**](PreviewSyncSyncMapItemApi.md#fetchSyncSyncMapItem) | **GET** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key} | 
[**listSyncSyncMapItem**](PreviewSyncSyncMapItemApi.md#listSyncSyncMapItem) | **GET** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Items | 
[**updateSyncSyncMapItem**](PreviewSyncSyncMapItemApi.md#updateSyncSyncMapItem) | **POST** /Sync/Services/{ServiceSid}/Maps/{MapSid}/Items/{Key} | 



## createSyncSyncMapItem

> PreviewSyncServiceSyncMapSyncMapItem createSyncSyncMapItem(serviceSid, mapSid, data, key)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncMapItemApi();
let serviceSid = "serviceSid_example"; // String | 
let mapSid = "mapSid_example"; // String | 
let data = null; // Object | 
let key = "key_example"; // String | 
apiInstance.createSyncSyncMapItem(serviceSid, mapSid, data, key, (error, data, response) => {
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
 **mapSid** | **String**|  | 
 **data** | [**Object**](Object.md)|  | 
 **key** | **String**|  | 

### Return type

[**PreviewSyncServiceSyncMapSyncMapItem**](PreviewSyncServiceSyncMapSyncMapItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSyncSyncMapItem

> deleteSyncSyncMapItem(serviceSid, mapSid, key, opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncMapItemApi();
let serviceSid = "serviceSid_example"; // String | 
let mapSid = "mapSid_example"; // String | 
let key = "key_example"; // String | 
let opts = {
  'ifMatch': "ifMatch_example" // String | The If-Match HTTP request header
};
apiInstance.deleteSyncSyncMapItem(serviceSid, mapSid, key, opts, (error, data, response) => {
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
 **mapSid** | **String**|  | 
 **key** | **String**|  | 
 **ifMatch** | **String**| The If-Match HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSyncSyncMapItem

> PreviewSyncServiceSyncMapSyncMapItem fetchSyncSyncMapItem(serviceSid, mapSid, key)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncMapItemApi();
let serviceSid = "serviceSid_example"; // String | 
let mapSid = "mapSid_example"; // String | 
let key = "key_example"; // String | 
apiInstance.fetchSyncSyncMapItem(serviceSid, mapSid, key, (error, data, response) => {
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
 **mapSid** | **String**|  | 
 **key** | **String**|  | 

### Return type

[**PreviewSyncServiceSyncMapSyncMapItem**](PreviewSyncServiceSyncMapSyncMapItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncSyncMapItem

> ListSyncSyncMapItemResponse listSyncSyncMapItem(serviceSid, mapSid, opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncMapItemApi();
let serviceSid = "serviceSid_example"; // String | 
let mapSid = "mapSid_example"; // String | 
let opts = {
  'order': "order_example", // SyncMapItemEnumQueryResultOrder | 
  'from': "from_example", // String | 
  'bounds': "bounds_example", // SyncMapItemEnumQueryFromBoundType | 
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSyncSyncMapItem(serviceSid, mapSid, opts, (error, data, response) => {
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
 **mapSid** | **String**|  | 
 **order** | **SyncMapItemEnumQueryResultOrder**|  | [optional] 
 **from** | **String**|  | [optional] 
 **bounds** | **SyncMapItemEnumQueryFromBoundType**|  | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSyncSyncMapItemResponse**](ListSyncSyncMapItemResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSyncSyncMapItem

> PreviewSyncServiceSyncMapSyncMapItem updateSyncSyncMapItem(serviceSid, mapSid, key, data, opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncMapItemApi();
let serviceSid = "serviceSid_example"; // String | 
let mapSid = "mapSid_example"; // String | 
let key = "key_example"; // String | 
let data = null; // Object | 
let opts = {
  'ifMatch': "ifMatch_example" // String | The If-Match HTTP request header
};
apiInstance.updateSyncSyncMapItem(serviceSid, mapSid, key, data, opts, (error, data, response) => {
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
 **mapSid** | **String**|  | 
 **key** | **String**|  | 
 **data** | [**Object**](Object.md)|  | 
 **ifMatch** | **String**| The If-Match HTTP request header | [optional] 

### Return type

[**PreviewSyncServiceSyncMapSyncMapItem**](PreviewSyncServiceSyncMapSyncMapItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

