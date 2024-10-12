# TwilioApi.Api20100401NotificationApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchCallNotification**](Api20100401NotificationApi.md#fetchCallNotification) | **GET** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Notifications/{Sid}.json | 
[**fetchNotification**](Api20100401NotificationApi.md#fetchNotification) | **GET** /2010-04-01/Accounts/{AccountSid}/Notifications/{Sid}.json | 
[**listCallNotification**](Api20100401NotificationApi.md#listCallNotification) | **GET** /2010-04-01/Accounts/{AccountSid}/Calls/{CallSid}/Notifications.json | 
[**listNotification**](Api20100401NotificationApi.md#listNotification) | **GET** /2010-04-01/Accounts/{AccountSid}/Notifications.json | 



## fetchCallNotification

> ApiV2010AccountCallCallNotificationInstance fetchCallNotification(accountSid, callSid, sid)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401NotificationApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resource to fetch.
let callSid = "callSid_example"; // String | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Call Notification resource to fetch.
apiInstance.fetchCallNotification(accountSid, callSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resource to fetch. | 
 **callSid** | **String**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resource to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Call Notification resource to fetch. | 

### Return type

[**ApiV2010AccountCallCallNotificationInstance**](ApiV2010AccountCallCallNotificationInstance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## fetchNotification

> ApiV2010AccountNotificationInstance fetchNotification(accountSid, sid)



Fetch a notification belonging to the account used to make the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401NotificationApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Notification resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the Notification resource to fetch.
apiInstance.fetchNotification(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Notification resource to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the Notification resource to fetch. | 

### Return type

[**ApiV2010AccountNotificationInstance**](ApiV2010AccountNotificationInstance.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCallNotification

> ListCallNotificationResponse listCallNotification(accountSid, callSid, opts)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401NotificationApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resources to read.
let callSid = "callSid_example"; // String | The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resources to read.
let opts = {
  'log': 56, // Number | Only read notifications of the specified log level. Can be:  `0` to read only ERROR notifications or `1` to read only WARNING notifications. By default, all notifications are read.
  'messageDate': new Date("2013-10-20"), // Date | Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
  'messageDate2': new Date("2013-10-20"), // Date | Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
  'messageDate3': new Date("2013-10-20"), // Date | Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listCallNotification(accountSid, callSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Call Notification resources to read. | 
 **callSid** | **String**| The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the Call Notification resources to read. | 
 **log** | **Number**| Only read notifications of the specified log level. Can be:  &#x60;0&#x60; to read only ERROR notifications or &#x60;1&#x60; to read only WARNING notifications. By default, all notifications are read. | [optional] 
 **messageDate** | **Date**| Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date. | [optional] 
 **messageDate2** | **Date**| Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date. | [optional] 
 **messageDate3** | **Date**| Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListCallNotificationResponse**](ListCallNotificationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listNotification

> ListNotificationResponse listNotification(accountSid, opts)



Retrieve a list of notifications belonging to the account used to make the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401NotificationApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Notification resources to read.
let opts = {
  'log': 56, // Number | Only read notifications of the specified log level. Can be:  `0` to read only ERROR notifications or `1` to read only WARNING notifications. By default, all notifications are read.
  'messageDate': new Date("2013-10-20"), // Date | Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
  'messageDate2': new Date("2013-10-20"), // Date | Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
  'messageDate3': new Date("2013-10-20"), // Date | Only show notifications for the specified date, formatted as `YYYY-MM-DD`. You can also specify an inequality, such as `<=YYYY-MM-DD` for messages logged at or before midnight on a date, or `>=YYYY-MM-DD` for messages logged at or after midnight on a date.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listNotification(accountSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Notification resources to read. | 
 **log** | **Number**| Only read notifications of the specified log level. Can be:  &#x60;0&#x60; to read only ERROR notifications or &#x60;1&#x60; to read only WARNING notifications. By default, all notifications are read. | [optional] 
 **messageDate** | **Date**| Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date. | [optional] 
 **messageDate2** | **Date**| Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date. | [optional] 
 **messageDate3** | **Date**| Only show notifications for the specified date, formatted as &#x60;YYYY-MM-DD&#x60;. You can also specify an inequality, such as &#x60;&lt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or before midnight on a date, or &#x60;&gt;&#x3D;YYYY-MM-DD&#x60; for messages logged at or after midnight on a date. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListNotificationResponse**](ListNotificationResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

