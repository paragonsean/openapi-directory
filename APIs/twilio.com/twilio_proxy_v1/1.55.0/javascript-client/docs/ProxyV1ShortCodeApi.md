# TwilioProxy.ProxyV1ShortCodeApi

All URIs are relative to *https://proxy.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createShortCode**](ProxyV1ShortCodeApi.md#createShortCode) | **POST** /v1/Services/{ServiceSid}/ShortCodes | 
[**deleteShortCode**](ProxyV1ShortCodeApi.md#deleteShortCode) | **DELETE** /v1/Services/{ServiceSid}/ShortCodes/{Sid} | 
[**fetchShortCode**](ProxyV1ShortCodeApi.md#fetchShortCode) | **GET** /v1/Services/{ServiceSid}/ShortCodes/{Sid} | 
[**listShortCode**](ProxyV1ShortCodeApi.md#listShortCode) | **GET** /v1/Services/{ServiceSid}/ShortCodes | 
[**updateShortCode**](ProxyV1ShortCodeApi.md#updateShortCode) | **POST** /v1/Services/{ServiceSid}/ShortCodes/{Sid} | 



## createShortCode

> ProxyV1ServiceShortCode createShortCode(serviceSid, sid)



Add a Short Code to the Proxy Number Pool for the Service.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ShortCodeApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource.
let sid = "sid_example"; // String | The SID of a Twilio [ShortCode](https://www.twilio.com/en-us/messaging/channels/sms/short-codes) resource that represents the short code you would like to assign to your Proxy Service.
apiInstance.createShortCode(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource. | 
 **sid** | **String**| The SID of a Twilio [ShortCode](https://www.twilio.com/en-us/messaging/channels/sms/short-codes) resource that represents the short code you would like to assign to your Proxy Service. | 

### Return type

[**ProxyV1ServiceShortCode**](ProxyV1ServiceShortCode.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteShortCode

> deleteShortCode(serviceSid, sid)



Delete a specific Short Code from a Service.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ShortCodeApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource to delete the ShortCode resource from.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ShortCode resource to delete.
apiInstance.deleteShortCode(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) resource to delete the ShortCode resource from. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the ShortCode resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchShortCode

> ProxyV1ServiceShortCode fetchShortCode(serviceSid, sid)



Fetch a specific Short Code.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ShortCodeApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to fetch the resource from.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ShortCode resource to fetch.
apiInstance.fetchShortCode(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to fetch the resource from. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the ShortCode resource to fetch. | 

### Return type

[**ProxyV1ServiceShortCode**](ProxyV1ServiceShortCode.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listShortCode

> ListShortCodeResponse listShortCode(serviceSid, opts)



Retrieve a list of all Short Codes in the Proxy Number Pool for the Service. A maximum of 100 records will be returned per page.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ShortCodeApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listShortCode(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) to read the resources from. | 
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

> ProxyV1ServiceShortCode updateShortCode(serviceSid, sid, opts)



Update a specific Short Code.

### Example

```javascript
import TwilioProxy from 'twilio_proxy';
let defaultClient = TwilioProxy.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioProxy.ProxyV1ShortCodeApi();
let serviceSid = "serviceSid_example"; // String | The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to update.
let sid = "sid_example"; // String | The Twilio-provided string that uniquely identifies the ShortCode resource to update.
let opts = {
  'isReserved': true // Boolean | Whether the short code should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information.
};
apiInstance.updateShortCode(serviceSid, sid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the parent [Service](https://www.twilio.com/docs/proxy/api/service) of the resource to update. | 
 **sid** | **String**| The Twilio-provided string that uniquely identifies the ShortCode resource to update. | 
 **isReserved** | **Boolean**| Whether the short code should be reserved and not be assigned to a participant using proxy pool logic. See [Reserved Phone Numbers](https://www.twilio.com/docs/proxy/reserved-phone-numbers) for more information. | [optional] 

### Return type

[**ProxyV1ServiceShortCode**](ProxyV1ServiceShortCode.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

