# TwilioApi.Api20100401TriggerApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createUsageTrigger**](Api20100401TriggerApi.md#createUsageTrigger) | **POST** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json | 
[**deleteUsageTrigger**](Api20100401TriggerApi.md#deleteUsageTrigger) | **DELETE** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json | 
[**fetchUsageTrigger**](Api20100401TriggerApi.md#fetchUsageTrigger) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json | 
[**listUsageTrigger**](Api20100401TriggerApi.md#listUsageTrigger) | **GET** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers.json | 
[**updateUsageTrigger**](Api20100401TriggerApi.md#updateUsageTrigger) | **POST** /2010-04-01/Accounts/{AccountSid}/Usage/Triggers/{Sid}.json | 



## createUsageTrigger

> ApiV2010AccountUsageUsageTrigger createUsageTrigger(accountSid, callbackUrl, triggerValue, usageCategory, opts)



Create a new UsageTrigger

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401TriggerApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
let callbackUrl = "callbackUrl_example"; // String | The URL we should call using `callback_method` when the trigger fires.
let triggerValue = "triggerValue_example"; // String | The usage value at which the trigger should fire.  For convenience, you can use an offset value such as `+30` to specify a trigger_value that is 30 units more than the current usage value. Be sure to urlencode a `+` as `%2B`.
let usageCategory = "usageCategory_example"; // UsageTriggerEnumUsageCategory | 
let opts = {
  'callbackMethod': "callbackMethod_example", // String | The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is `POST`.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
  'recurring': "recurring_example", // UsageTriggerEnumRecurring | 
  'triggerBy': "triggerBy_example" // UsageTriggerEnumTriggerField | 
};
apiInstance.createUsageTrigger(accountSid, callbackUrl, triggerValue, usageCategory, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource. | 
 **callbackUrl** | **String**| The URL we should call using &#x60;callback_method&#x60; when the trigger fires. | 
 **triggerValue** | **String**| The usage value at which the trigger should fire.  For convenience, you can use an offset value such as &#x60;+30&#x60; to specify a trigger_value that is 30 units more than the current usage value. Be sure to urlencode a &#x60;+&#x60; as &#x60;%2B&#x60;. | 
 **usageCategory** | **UsageTriggerEnumUsageCategory**|  | 
 **callbackMethod** | **String**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 
 **recurring** | **UsageTriggerEnumRecurring**|  | [optional] 
 **triggerBy** | **UsageTriggerEnumTriggerField**|  | [optional] 

### Return type

[**ApiV2010AccountUsageUsageTrigger**](ApiV2010AccountUsageUsageTrigger.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteUsageTrigger

> deleteUsageTrigger(accountSid, sid)





### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401TriggerApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to delete.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the UsageTrigger resource to delete.
apiInstance.deleteUsageTrigger(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to delete. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the UsageTrigger resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchUsageTrigger

> ApiV2010AccountUsageUsageTrigger fetchUsageTrigger(accountSid, sid)



Fetch and instance of a usage-trigger

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401TriggerApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resource to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the UsageTrigger resource to fetch.
apiInstance.fetchUsageTrigger(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resource to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the UsageTrigger resource to fetch. | 

### Return type

[**ApiV2010AccountUsageUsageTrigger**](ApiV2010AccountUsageUsageTrigger.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listUsageTrigger

> ListUsageTriggerResponse listUsageTrigger(accountSid, opts)



Retrieve a list of usage-triggers belonging to the account used to make the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401TriggerApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to read.
let opts = {
  'recurring': "recurring_example", // UsageTriggerEnumRecurring | The frequency of recurring UsageTriggers to read. Can be: `daily`, `monthly`, or `yearly` to read recurring UsageTriggers. An empty value or a value of `alltime` reads non-recurring UsageTriggers.
  'triggerBy': "triggerBy_example", // UsageTriggerEnumTriggerField | The trigger field of the UsageTriggers to read.  Can be: `count`, `usage`, or `price` as described in the [UsageRecords documentation](https://www.twilio.com/docs/usage/api/usage-record#usage-count-price).
  'usageCategory': "usageCategory_example", // UsageTriggerEnumUsageCategory | The usage category of the UsageTriggers to read. Must be a supported [usage categories](https://www.twilio.com/docs/usage/api/usage-record#usage-categories).
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listUsageTrigger(accountSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to read. | 
 **recurring** | **UsageTriggerEnumRecurring**| The frequency of recurring UsageTriggers to read. Can be: &#x60;daily&#x60;, &#x60;monthly&#x60;, or &#x60;yearly&#x60; to read recurring UsageTriggers. An empty value or a value of &#x60;alltime&#x60; reads non-recurring UsageTriggers. | [optional] 
 **triggerBy** | **UsageTriggerEnumTriggerField**| The trigger field of the UsageTriggers to read.  Can be: &#x60;count&#x60;, &#x60;usage&#x60;, or &#x60;price&#x60; as described in the [UsageRecords documentation](https://www.twilio.com/docs/usage/api/usage-record#usage-count-price). | [optional] 
 **usageCategory** | **UsageTriggerEnumUsageCategory**| The usage category of the UsageTriggers to read. Must be a supported [usage categories](https://www.twilio.com/docs/usage/api/usage-record#usage-categories). | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListUsageTriggerResponse**](ListUsageTriggerResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateUsageTrigger

> ApiV2010AccountUsageUsageTrigger updateUsageTrigger(accountSid, sid, opts)



Update an instance of a usage trigger

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401TriggerApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to update.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the UsageTrigger resource to update.
let opts = {
  'callbackMethod': "callbackMethod_example", // String | The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is `POST`.
  'callbackUrl': "callbackUrl_example", // String | The URL we should call using `callback_method` when the trigger fires.
  'friendlyName': "friendlyName_example" // String | A descriptive string that you create to describe the resource. It can be up to 64 characters long.
};
apiInstance.updateUsageTrigger(accountSid, sid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the UsageTrigger resources to update. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the UsageTrigger resource to update. | 
 **callbackMethod** | **String**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. | [optional] 
 **callbackUrl** | **String**| The URL we should call using &#x60;callback_method&#x60; when the trigger fires. | [optional] 
 **friendlyName** | **String**| A descriptive string that you create to describe the resource. It can be up to 64 characters long. | [optional] 

### Return type

[**ApiV2010AccountUsageUsageTrigger**](ApiV2010AccountUsageUsageTrigger.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

