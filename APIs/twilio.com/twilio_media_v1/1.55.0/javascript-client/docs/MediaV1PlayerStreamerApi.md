# TwilioMedia.MediaV1PlayerStreamerApi

All URIs are relative to *https://media.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createPlayerStreamer**](MediaV1PlayerStreamerApi.md#createPlayerStreamer) | **POST** /v1/PlayerStreamers | 
[**fetchPlayerStreamer**](MediaV1PlayerStreamerApi.md#fetchPlayerStreamer) | **GET** /v1/PlayerStreamers/{Sid} | 
[**listPlayerStreamer**](MediaV1PlayerStreamerApi.md#listPlayerStreamer) | **GET** /v1/PlayerStreamers | 
[**updatePlayerStreamer**](MediaV1PlayerStreamerApi.md#updatePlayerStreamer) | **POST** /v1/PlayerStreamers/{Sid} | 



## createPlayerStreamer

> MediaV1PlayerStreamer createPlayerStreamer(opts)





### Example

```javascript
import TwilioMedia from 'twilio_media';
let defaultClient = TwilioMedia.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMedia.MediaV1PlayerStreamerApi();
let opts = {
  'maxDuration': 56, // Number | The maximum time, in seconds, that the PlayerStreamer is active (`created` or `started`) before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the PlayerStreamer, regardless of whether media is still streaming.
  'statusCallback': "statusCallback_example", // String | The URL to which Twilio will send asynchronous webhook requests for every PlayerStreamer event. See [Status Callbacks](/docs/live/api/status-callbacks) for more details.
  'statusCallbackMethod': "statusCallbackMethod_example", // String | The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
  'video': true // Boolean | Specifies whether the PlayerStreamer is configured to stream video. Defaults to `true`.
};
apiInstance.createPlayerStreamer(opts, (error, data, response) => {
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
 **maxDuration** | **Number**| The maximum time, in seconds, that the PlayerStreamer is active (&#x60;created&#x60; or &#x60;started&#x60;) before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the PlayerStreamer, regardless of whether media is still streaming. | [optional] 
 **statusCallback** | **String**| The URL to which Twilio will send asynchronous webhook requests for every PlayerStreamer event. See [Status Callbacks](/docs/live/api/status-callbacks) for more details. | [optional] 
 **statusCallbackMethod** | **String**| The HTTP method Twilio should use to call the &#x60;status_callback&#x60; URL. Can be &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. | [optional] 
 **video** | **Boolean**| Specifies whether the PlayerStreamer is configured to stream video. Defaults to &#x60;true&#x60;. | [optional] 

### Return type

[**MediaV1PlayerStreamer**](MediaV1PlayerStreamer.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchPlayerStreamer

> MediaV1PlayerStreamer fetchPlayerStreamer(sid)



Returns a single PlayerStreamer resource identified by a SID.

### Example

```javascript
import TwilioMedia from 'twilio_media';
let defaultClient = TwilioMedia.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMedia.MediaV1PlayerStreamerApi();
let sid = "sid_example"; // String | The SID of the PlayerStreamer resource to fetch.
apiInstance.fetchPlayerStreamer(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the PlayerStreamer resource to fetch. | 

### Return type

[**MediaV1PlayerStreamer**](MediaV1PlayerStreamer.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPlayerStreamer

> ListPlayerStreamerResponse listPlayerStreamer(opts)



Returns a list of PlayerStreamers.

### Example

```javascript
import TwilioMedia from 'twilio_media';
let defaultClient = TwilioMedia.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMedia.MediaV1PlayerStreamerApi();
let opts = {
  'order': "order_example", // PlayerStreamerEnumOrder | The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
  'status': "status_example", // PlayerStreamerEnumStatus | Status to filter by, with possible values `created`, `started`, `ended`, or `failed`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listPlayerStreamer(opts, (error, data, response) => {
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
 **order** | **PlayerStreamerEnumOrder**| The sort order of the list by &#x60;date_created&#x60;. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) with &#x60;desc&#x60; as the default. | [optional] 
 **status** | **PlayerStreamerEnumStatus**| Status to filter by, with possible values &#x60;created&#x60;, &#x60;started&#x60;, &#x60;ended&#x60;, or &#x60;failed&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListPlayerStreamerResponse**](ListPlayerStreamerResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updatePlayerStreamer

> MediaV1PlayerStreamer updatePlayerStreamer(sid, status)



Updates a PlayerStreamer resource identified by a SID.

### Example

```javascript
import TwilioMedia from 'twilio_media';
let defaultClient = TwilioMedia.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMedia.MediaV1PlayerStreamerApi();
let sid = "sid_example"; // String | The SID of the PlayerStreamer resource to update.
let status = "status_example"; // PlayerStreamerEnumUpdateStatus | 
apiInstance.updatePlayerStreamer(sid, status, (error, data, response) => {
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
 **sid** | **String**| The SID of the PlayerStreamer resource to update. | 
 **status** | **PlayerStreamerEnumUpdateStatus**|  | 

### Return type

[**MediaV1PlayerStreamer**](MediaV1PlayerStreamer.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

