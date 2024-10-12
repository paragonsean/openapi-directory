# TwilioApi.Api20100401ShortCodeApi

All URIs are relative to *https://api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchShortCode**](Api20100401ShortCodeApi.md#fetchShortCode) | **GET** /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json | 
[**listShortCode**](Api20100401ShortCodeApi.md#listShortCode) | **GET** /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes.json | 
[**updateShortCode**](Api20100401ShortCodeApi.md#updateShortCode) | **POST** /2010-04-01/Accounts/{AccountSid}/SMS/ShortCodes/{Sid}.json | 



## fetchShortCode

> ApiV2010AccountShortCode fetchShortCode(accountSid, sid)



Fetch an instance of a short code

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401ShortCodeApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to fetch.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ShortCode resource to fetch
apiInstance.fetchShortCode(accountSid, sid, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to fetch. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the ShortCode resource to fetch | 

### Return type

[**ApiV2010AccountShortCode**](ApiV2010AccountShortCode.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listShortCode

> ListShortCodeResponse listShortCode(accountSid, opts)



Retrieve a list of short-codes belonging to the account used to make the request

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401ShortCodeApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to read.
let opts = {
  'friendlyName': "friendlyName_example", // String | The string that identifies the ShortCode resources to read.
  'shortCode': "shortCode_example", // String | Only show the ShortCode resources that match this pattern. You can specify partial numbers and use '*' as a wildcard for any digit.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listShortCode(accountSid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to read. | 
 **friendlyName** | **String**| The string that identifies the ShortCode resources to read. | [optional] 
 **shortCode** | **String**| Only show the ShortCode resources that match this pattern. You can specify partial numbers and use &#39;*&#39; as a wildcard for any digit. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListShortCodeResponse**](ListShortCodeResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateShortCode

> ApiV2010AccountShortCode updateShortCode(accountSid, sid, opts)



Update a short code with the following parameters

### Example

```javascript
import TwilioApi from 'twilio_api';
let defaultClient = TwilioApi.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioApi.Api20100401ShortCodeApi();
let accountSid = "accountSid_example"; // String | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to update.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ShortCode resource to update
let opts = {
  'apiVersion': "apiVersion_example", // String | The API version to use to start a new TwiML session. Can be: `2010-04-01` or `2008-08-01`.
  'friendlyName': "friendlyName_example", // String | A descriptive string that you created to describe this resource. It can be up to 64 characters long. By default, the `FriendlyName` is the short code.
  'smsFallbackMethod': "smsFallbackMethod_example", // String | The HTTP method that we should use to call the `sms_fallback_url`. Can be: `GET` or `POST`.
  'smsFallbackUrl': "smsFallbackUrl_example", // String | The URL that we should call if an error occurs while retrieving or executing the TwiML from `sms_url`.
  'smsMethod': "smsMethod_example", // String | The HTTP method we should use when calling the `sms_url`. Can be: `GET` or `POST`.
  'smsUrl': "smsUrl_example" // String | The URL we should call when receiving an incoming SMS message to this short code.
};
apiInstance.updateShortCode(accountSid, sid, opts, (error, data, response) => {
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
 **accountSid** | **String**| The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to update. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the ShortCode resource to update | 
 **apiVersion** | **String**| The API version to use to start a new TwiML session. Can be: &#x60;2010-04-01&#x60; or &#x60;2008-08-01&#x60;. | [optional] 
 **friendlyName** | **String**| A descriptive string that you created to describe this resource. It can be up to 64 characters long. By default, the &#x60;FriendlyName&#x60; is the short code. | [optional] 
 **smsFallbackMethod** | **String**| The HTTP method that we should use to call the &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **smsFallbackUrl** | **String**| The URL that we should call if an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;. | [optional] 
 **smsMethod** | **String**| The HTTP method we should use when calling the &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;. | [optional] 
 **smsUrl** | **String**| The URL we should call when receiving an incoming SMS message to this short code. | [optional] 

### Return type

[**ApiV2010AccountShortCode**](ApiV2010AccountShortCode.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

