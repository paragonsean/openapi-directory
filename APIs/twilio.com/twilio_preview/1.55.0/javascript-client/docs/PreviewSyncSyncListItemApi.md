# TwilioPreview.PreviewSyncSyncListItemApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSyncSyncListItem**](PreviewSyncSyncListItemApi.md#createSyncSyncListItem) | **POST** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Items | 
[**deleteSyncSyncListItem**](PreviewSyncSyncListItemApi.md#deleteSyncSyncListItem) | **DELETE** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index} | 
[**fetchSyncSyncListItem**](PreviewSyncSyncListItemApi.md#fetchSyncSyncListItem) | **GET** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index} | 
[**listSyncSyncListItem**](PreviewSyncSyncListItemApi.md#listSyncSyncListItem) | **GET** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Items | 
[**updateSyncSyncListItem**](PreviewSyncSyncListItemApi.md#updateSyncSyncListItem) | **POST** /Sync/Services/{ServiceSid}/Lists/{ListSid}/Items/{Index} | 



## createSyncSyncListItem

> PreviewSyncServiceSyncListSyncListItem createSyncSyncListItem(serviceSid, listSid, data)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncListItemApi();
let serviceSid = "serviceSid_example"; // String | 
let listSid = "listSid_example"; // String | 
let data = null; // Object | 
apiInstance.createSyncSyncListItem(serviceSid, listSid, data, (error, data, response) => {
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
 **listSid** | **String**|  | 
 **data** | [**Object**](Object.md)|  | 

### Return type

[**PreviewSyncServiceSyncListSyncListItem**](PreviewSyncServiceSyncListSyncListItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteSyncSyncListItem

> deleteSyncSyncListItem(serviceSid, listSid, index, opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncListItemApi();
let serviceSid = "serviceSid_example"; // String | 
let listSid = "listSid_example"; // String | 
let index = 56; // Number | 
let opts = {
  'ifMatch': "ifMatch_example" // String | The If-Match HTTP request header
};
apiInstance.deleteSyncSyncListItem(serviceSid, listSid, index, opts, (error, data, response) => {
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
 **listSid** | **String**|  | 
 **index** | **Number**|  | 
 **ifMatch** | **String**| The If-Match HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchSyncSyncListItem

> PreviewSyncServiceSyncListSyncListItem fetchSyncSyncListItem(serviceSid, listSid, index)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncListItemApi();
let serviceSid = "serviceSid_example"; // String | 
let listSid = "listSid_example"; // String | 
let index = 56; // Number | 
apiInstance.fetchSyncSyncListItem(serviceSid, listSid, index, (error, data, response) => {
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
 **listSid** | **String**|  | 
 **index** | **Number**|  | 

### Return type

[**PreviewSyncServiceSyncListSyncListItem**](PreviewSyncServiceSyncListSyncListItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSyncSyncListItem

> ListSyncSyncListItemResponse listSyncSyncListItem(serviceSid, listSid, opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncListItemApi();
let serviceSid = "serviceSid_example"; // String | 
let listSid = "listSid_example"; // String | 
let opts = {
  'order': "order_example", // SyncListItemEnumQueryResultOrder | 
  'from': "from_example", // String | 
  'bounds': "bounds_example", // SyncListItemEnumQueryFromBoundType | 
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSyncSyncListItem(serviceSid, listSid, opts, (error, data, response) => {
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
 **listSid** | **String**|  | 
 **order** | **SyncListItemEnumQueryResultOrder**|  | [optional] 
 **from** | **String**|  | [optional] 
 **bounds** | **SyncListItemEnumQueryFromBoundType**|  | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSyncSyncListItemResponse**](ListSyncSyncListItemResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSyncSyncListItem

> PreviewSyncServiceSyncListSyncListItem updateSyncSyncListItem(serviceSid, listSid, index, data, opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewSyncSyncListItemApi();
let serviceSid = "serviceSid_example"; // String | 
let listSid = "listSid_example"; // String | 
let index = 56; // Number | 
let data = null; // Object | 
let opts = {
  'ifMatch': "ifMatch_example" // String | The If-Match HTTP request header
};
apiInstance.updateSyncSyncListItem(serviceSid, listSid, index, data, opts, (error, data, response) => {
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
 **listSid** | **String**|  | 
 **index** | **Number**|  | 
 **data** | [**Object**](Object.md)|  | 
 **ifMatch** | **String**| The If-Match HTTP request header | [optional] 

### Return type

[**PreviewSyncServiceSyncListSyncListItem**](PreviewSyncServiceSyncListSyncListItem.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

