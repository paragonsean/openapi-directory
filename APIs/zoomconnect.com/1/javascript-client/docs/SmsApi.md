# WwwZoomconnectCom.SmsApi

All URIs are relative to *https://www.zoomconnect.com/app*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiRestV1SmsSendBulkGet**](SmsApi.md#apiRestV1SmsSendBulkGet) | **GET** /api/rest/v1/sms/send-bulk | send-bulk
[**apiRestV1SmsSendBulkPost**](SmsApi.md#apiRestV1SmsSendBulkPost) | **POST** /api/rest/v1/sms/send-bulk | send-bulk
[**apiRestV1SmsSendGet**](SmsApi.md#apiRestV1SmsSendGet) | **GET** /api/rest/v1/sms/send | send
[**apiRestV1SmsSendPost**](SmsApi.md#apiRestV1SmsSendPost) | **POST** /api/rest/v1/sms/send | send
[**apiRestV1SmsSendUrlParametersGet**](SmsApi.md#apiRestV1SmsSendUrlParametersGet) | **GET** /api/rest/v1/sms/send-url-parameters | send-url-parameters
[**apiRestV1SmsSendUrlParametersPost**](SmsApi.md#apiRestV1SmsSendUrlParametersPost) | **POST** /api/rest/v1/sms/send-url-parameters | send-url-parameters
[**apiRestV1SmsSendUrlTokenGet**](SmsApi.md#apiRestV1SmsSendUrlTokenGet) | **GET** /api/rest/v1/sms/send-url/{token} | send-url
[**apiRestV1SmsSendUrlTokenPost**](SmsApi.md#apiRestV1SmsSendUrlTokenPost) | **POST** /api/rest/v1/sms/send-url/{token} | send-url



## apiRestV1SmsSendBulkGet

> WebServiceSendSmsRequests apiRestV1SmsSendBulkGet()

send-bulk

Returns an example of the data to POST to send multiple messages in one transaction.

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.SmsApi();
apiInstance.apiRestV1SmsSendBulkGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**WebServiceSendSmsRequests**](WebServiceSendSmsRequests.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1SmsSendBulkPost

> WebServiceSendSmsResponses apiRestV1SmsSendBulkPost(opts)

send-bulk

Send multiple messages in one transaction.

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.SmsApi();
let opts = {
  'body': new WwwZoomconnectCom.WebServiceSendSmsRequests() // WebServiceSendSmsRequests | requests
};
apiInstance.apiRestV1SmsSendBulkPost(opts, (error, data, response) => {
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
 **body** | [**WebServiceSendSmsRequests**](WebServiceSendSmsRequests.md)| requests | [optional] 

### Return type

[**WebServiceSendSmsResponses**](WebServiceSendSmsResponses.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## apiRestV1SmsSendGet

> WebServiceSendSmsRequest apiRestV1SmsSendGet()

send

Returns an example of the data to POST to send a single message.

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.SmsApi();
apiInstance.apiRestV1SmsSendGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**WebServiceSendSmsRequest**](WebServiceSendSmsRequest.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1SmsSendPost

> WebServiceSendSmsResponse apiRestV1SmsSendPost(opts)

send

Sends a single message. The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; fields are required. All other fields are optional.

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.SmsApi();
let opts = {
  'body': new WwwZoomconnectCom.WebServiceSendSmsRequest() // WebServiceSendSmsRequest | request
};
apiInstance.apiRestV1SmsSendPost(opts, (error, data, response) => {
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
 **body** | [**WebServiceSendSmsRequest**](WebServiceSendSmsRequest.md)| request | [optional] 

### Return type

[**WebServiceSendSmsResponse**](WebServiceSendSmsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## apiRestV1SmsSendUrlParametersGet

> String apiRestV1SmsSendUrlParametersGet(recipientNumber, message, opts)

send-url-parameters

Send a single message using URL parameters.The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; parameters are required. All other parameters are optional.

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.SmsApi();
let recipientNumber = "recipientNumber_example"; // String | the phone number of the recipient to send to
let message = "message_example"; // String | the message to send
let opts = {
  'dateToSend': new Date("2013-10-20T19:20:30+01:00"), // Date | date format: yyyyMMddHHmm
  'campaign': "campaign_example", // String | optional campaign name
  'dataField': "dataField_example" // String | optional extra data
};
apiInstance.apiRestV1SmsSendUrlParametersGet(recipientNumber, message, opts, (error, data, response) => {
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
 **recipientNumber** | **String**| the phone number of the recipient to send to | 
 **message** | **String**| the message to send | 
 **dateToSend** | **Date**| date format: yyyyMMddHHmm | [optional] 
 **campaign** | **String**| optional campaign name | [optional] 
 **dataField** | **String**| optional extra data | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1SmsSendUrlParametersPost

> String apiRestV1SmsSendUrlParametersPost(recipientNumber, message, opts)

send-url-parameters

Send a single message using URL parameters.The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; parameters are required. All other parameters are optional.

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.SmsApi();
let recipientNumber = "recipientNumber_example"; // String | the phone number of the recipient to send to
let message = "message_example"; // String | the message to send
let opts = {
  'dateToSend': new Date("2013-10-20T19:20:30+01:00"), // Date | date format: yyyyMMddHHmm
  'campaign': "campaign_example", // String | optional campaign name
  'dataField': "dataField_example" // String | optional extra data
};
apiInstance.apiRestV1SmsSendUrlParametersPost(recipientNumber, message, opts, (error, data, response) => {
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
 **recipientNumber** | **String**| the phone number of the recipient to send to | 
 **message** | **String**| the message to send | 
 **dateToSend** | **Date**| date format: yyyyMMddHHmm | [optional] 
 **campaign** | **String**| optional campaign name | [optional] 
 **dataField** | **String**| optional extra data | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1SmsSendUrlTokenGet

> String apiRestV1SmsSendUrlTokenGet(token, recipientNumber, message, opts)

send-url

Send a single message using your unique URL without having to authenticate using your email address or REST API token. The token required is the URL Sending token available on the developer setting page. The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; parameters are required. All other parameters are optional. Not that the token required here is 

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.SmsApi();
let token = "token_example"; // String | token
let recipientNumber = "recipientNumber_example"; // String | the phone number of the recipient to send to
let message = "message_example"; // String | the message to send
let opts = {
  'dateToSend': new Date("2013-10-20T19:20:30+01:00"), // Date | date format: yyyyMMddHHmm
  'campaign': "campaign_example", // String | optional campaign name
  'dataField': "dataField_example" // String | optional extra data
};
apiInstance.apiRestV1SmsSendUrlTokenGet(token, recipientNumber, message, opts, (error, data, response) => {
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
 **token** | **String**| token | 
 **recipientNumber** | **String**| the phone number of the recipient to send to | 
 **message** | **String**| the message to send | 
 **dateToSend** | **Date**| date format: yyyyMMddHHmm | [optional] 
 **campaign** | **String**| optional campaign name | [optional] 
 **dataField** | **String**| optional extra data | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## apiRestV1SmsSendUrlTokenPost

> String apiRestV1SmsSendUrlTokenPost(token, recipientNumber, message, opts)

send-url

Send a single message using your unique URL without having to authenticate using your email address or REST API token. The token required is the URL Sending token available on the developer setting page. The &lt;i&gt;recipientNumber&lt;/i&gt; and &lt;i&gt;message&lt;/i&gt; parameters are required. All other parameters are optional. Not that the token required here is 

### Example

```javascript
import WwwZoomconnectCom from 'www_zoomconnect_com';

let apiInstance = new WwwZoomconnectCom.SmsApi();
let token = "token_example"; // String | token
let recipientNumber = "recipientNumber_example"; // String | the phone number of the recipient to send to
let message = "message_example"; // String | the message to send
let opts = {
  'dateToSend': new Date("2013-10-20T19:20:30+01:00"), // Date | date format: yyyyMMddHHmm
  'campaign': "campaign_example", // String | optional campaign name
  'dataField': "dataField_example" // String | optional extra data
};
apiInstance.apiRestV1SmsSendUrlTokenPost(token, recipientNumber, message, opts, (error, data, response) => {
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
 **token** | **String**| token | 
 **recipientNumber** | **String**| the phone number of the recipient to send to | 
 **message** | **String**| the message to send | 
 **dateToSend** | **Date**| date format: yyyyMMddHHmm | [optional] 
 **campaign** | **String**| optional campaign name | [optional] 
 **dataField** | **String**| optional extra data | [optional] 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml

