# SlackWebApi.PinsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**pinsAdd**](PinsApi.md#pinsAdd) | **POST** /pins.add | 
[**pinsList**](PinsApi.md#pinsList) | **GET** /pins.list | 
[**pinsRemove**](PinsApi.md#pinsRemove) | **POST** /pins.remove | 



## pinsAdd

> PinsAddSchema pinsAdd(token, channel, opts)



Pins an item to a channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.PinsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `pins:write`
let channel = "channel_example"; // String | Channel to pin the item in.
let opts = {
  'timestamp': "timestamp_example" // String | Timestamp of the message to pin.
};
apiInstance.pinsAdd(token, channel, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;pins:write&#x60; | 
 **channel** | **String**| Channel to pin the item in. | 
 **timestamp** | **String**| Timestamp of the message to pin. | [optional] 

### Return type

[**PinsAddSchema**](PinsAddSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## pinsList

> [PinsListSuccessSchemaInner] pinsList(token, channel)



Lists items pinned to a channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.PinsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `pins:read`
let channel = "channel_example"; // String | Channel to get pinned items for.
apiInstance.pinsList(token, channel, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;pins:read&#x60; | 
 **channel** | **String**| Channel to get pinned items for. | 

### Return type

[**[PinsListSuccessSchemaInner]**](PinsListSuccessSchemaInner.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## pinsRemove

> PinsRemoveSchema pinsRemove(token, channel, opts)



Un-pins an item from a channel.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.PinsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `pins:write`
let channel = "channel_example"; // String | Channel where the item is pinned to.
let opts = {
  'timestamp': "timestamp_example" // String | Timestamp of the message to un-pin.
};
apiInstance.pinsRemove(token, channel, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;pins:write&#x60; | 
 **channel** | **String**| Channel where the item is pinned to. | 
 **timestamp** | **String**| Timestamp of the message to un-pin. | [optional] 

### Return type

[**PinsRemoveSchema**](PinsRemoveSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

