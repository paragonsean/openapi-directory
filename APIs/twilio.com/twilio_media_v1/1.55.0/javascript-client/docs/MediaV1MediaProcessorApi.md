# TwilioMedia.MediaV1MediaProcessorApi

All URIs are relative to *https://media.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMediaProcessor**](MediaV1MediaProcessorApi.md#createMediaProcessor) | **POST** /v1/MediaProcessors | 
[**fetchMediaProcessor**](MediaV1MediaProcessorApi.md#fetchMediaProcessor) | **GET** /v1/MediaProcessors/{Sid} | 
[**listMediaProcessor**](MediaV1MediaProcessorApi.md#listMediaProcessor) | **GET** /v1/MediaProcessors | 
[**updateMediaProcessor**](MediaV1MediaProcessorApi.md#updateMediaProcessor) | **POST** /v1/MediaProcessors/{Sid} | 



## createMediaProcessor

> MediaV1MediaProcessor createMediaProcessor(extension, extensionContext, opts)





### Example

```javascript
import TwilioMedia from 'twilio_media';
let defaultClient = TwilioMedia.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMedia.MediaV1MediaProcessorApi();
let extension = "extension_example"; // String | The [Media Extension](/docs/live/media-extensions-overview) name or URL. Ex: `video-composer-v2`
let extensionContext = "extensionContext_example"; // String | The context of the Media Extension, represented as a JSON dictionary. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about the context to send.
let opts = {
  'extensionEnvironment': null, // Object | User-defined environment variables for the Media Extension, represented as a JSON dictionary of key/value strings. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about whether you need to provide this.
  'maxDuration': 56, // Number | The maximum time, in seconds, that the MediaProcessor can run before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the MediaProcessor, regardless of whether media is still streaming.
  'statusCallback': "statusCallback_example", // String | The URL to which Twilio will send asynchronous webhook requests for every MediaProcessor event. See [Status Callbacks](/docs/live/api/status-callbacks) for details.
  'statusCallbackMethod': "statusCallbackMethod_example" // String | The HTTP method Twilio should use to call the `status_callback` URL. Can be `POST` or `GET` and the default is `POST`.
};
apiInstance.createMediaProcessor(extension, extensionContext, opts, (error, data, response) => {
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
 **extension** | **String**| The [Media Extension](/docs/live/media-extensions-overview) name or URL. Ex: &#x60;video-composer-v2&#x60; | 
 **extensionContext** | **String**| The context of the Media Extension, represented as a JSON dictionary. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about the context to send. | 
 **extensionEnvironment** | [**Object**](Object.md)| User-defined environment variables for the Media Extension, represented as a JSON dictionary of key/value strings. See the documentation for the specific [Media Extension](/docs/live/media-extensions-overview) you are using for more information about whether you need to provide this. | [optional] 
 **maxDuration** | **Number**| The maximum time, in seconds, that the MediaProcessor can run before automatically ends. The default value is 300 seconds, and the maximum value is 90000 seconds. Once this maximum duration is reached, Twilio will end the MediaProcessor, regardless of whether media is still streaming. | [optional] 
 **statusCallback** | **String**| The URL to which Twilio will send asynchronous webhook requests for every MediaProcessor event. See [Status Callbacks](/docs/live/api/status-callbacks) for details. | [optional] 
 **statusCallbackMethod** | **String**| The HTTP method Twilio should use to call the &#x60;status_callback&#x60; URL. Can be &#x60;POST&#x60; or &#x60;GET&#x60; and the default is &#x60;POST&#x60;. | [optional] 

### Return type

[**MediaV1MediaProcessor**](MediaV1MediaProcessor.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchMediaProcessor

> MediaV1MediaProcessor fetchMediaProcessor(sid)



Returns a single MediaProcessor resource identified by a SID.

### Example

```javascript
import TwilioMedia from 'twilio_media';
let defaultClient = TwilioMedia.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMedia.MediaV1MediaProcessorApi();
let sid = "sid_example"; // String | The SID of the MediaProcessor resource to fetch.
apiInstance.fetchMediaProcessor(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the MediaProcessor resource to fetch. | 

### Return type

[**MediaV1MediaProcessor**](MediaV1MediaProcessor.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMediaProcessor

> ListMediaProcessorResponse listMediaProcessor(opts)



Returns a list of MediaProcessors.

### Example

```javascript
import TwilioMedia from 'twilio_media';
let defaultClient = TwilioMedia.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMedia.MediaV1MediaProcessorApi();
let opts = {
  'order': "order_example", // MediaProcessorEnumOrder | The sort order of the list by `date_created`. Can be: `asc` (ascending) or `desc` (descending) with `desc` as the default.
  'status': "status_example", // MediaProcessorEnumStatus | Status to filter by, with possible values `started`, `ended` or `failed`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listMediaProcessor(opts, (error, data, response) => {
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
 **order** | **MediaProcessorEnumOrder**| The sort order of the list by &#x60;date_created&#x60;. Can be: &#x60;asc&#x60; (ascending) or &#x60;desc&#x60; (descending) with &#x60;desc&#x60; as the default. | [optional] 
 **status** | **MediaProcessorEnumStatus**| Status to filter by, with possible values &#x60;started&#x60;, &#x60;ended&#x60; or &#x60;failed&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListMediaProcessorResponse**](ListMediaProcessorResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMediaProcessor

> MediaV1MediaProcessor updateMediaProcessor(sid, status)



Updates a MediaProcessor resource identified by a SID.

### Example

```javascript
import TwilioMedia from 'twilio_media';
let defaultClient = TwilioMedia.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioMedia.MediaV1MediaProcessorApi();
let sid = "sid_example"; // String | The SID of the MediaProcessor resource to update.
let status = "status_example"; // MediaProcessorEnumUpdateStatus | 
apiInstance.updateMediaProcessor(sid, status, (error, data, response) => {
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
 **sid** | **String**| The SID of the MediaProcessor resource to update. | 
 **status** | **MediaProcessorEnumUpdateStatus**|  | 

### Return type

[**MediaV1MediaProcessor**](MediaV1MediaProcessor.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

