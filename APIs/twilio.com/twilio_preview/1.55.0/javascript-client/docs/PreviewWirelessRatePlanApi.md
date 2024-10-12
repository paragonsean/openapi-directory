# TwilioPreview.PreviewWirelessRatePlanApi

All URIs are relative to *https://preview.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createWirelessRatePlan**](PreviewWirelessRatePlanApi.md#createWirelessRatePlan) | **POST** /wireless/RatePlans | 
[**deleteWirelessRatePlan**](PreviewWirelessRatePlanApi.md#deleteWirelessRatePlan) | **DELETE** /wireless/RatePlans/{Sid} | 
[**fetchWirelessRatePlan**](PreviewWirelessRatePlanApi.md#fetchWirelessRatePlan) | **GET** /wireless/RatePlans/{Sid} | 
[**listWirelessRatePlan**](PreviewWirelessRatePlanApi.md#listWirelessRatePlan) | **GET** /wireless/RatePlans | 
[**updateWirelessRatePlan**](PreviewWirelessRatePlanApi.md#updateWirelessRatePlan) | **POST** /wireless/RatePlans/{Sid} | 



## createWirelessRatePlan

> PreviewWirelessRatePlan createWirelessRatePlan(opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewWirelessRatePlanApi();
let opts = {
  'commandsEnabled': true, // Boolean | 
  'dataEnabled': true, // Boolean | 
  'dataLimit': 56, // Number | 
  'dataMetering': "dataMetering_example", // String | 
  'friendlyName': "friendlyName_example", // String | 
  'internationalRoaming': ["null"], // [String] | 
  'messagingEnabled': true, // Boolean | 
  'nationalRoamingEnabled': true, // Boolean | 
  'uniqueName': "uniqueName_example", // String | 
  'voiceEnabled': true // Boolean | 
};
apiInstance.createWirelessRatePlan(opts, (error, data, response) => {
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
 **commandsEnabled** | **Boolean**|  | [optional] 
 **dataEnabled** | **Boolean**|  | [optional] 
 **dataLimit** | **Number**|  | [optional] 
 **dataMetering** | **String**|  | [optional] 
 **friendlyName** | **String**|  | [optional] 
 **internationalRoaming** | [**[String]**](String.md)|  | [optional] 
 **messagingEnabled** | **Boolean**|  | [optional] 
 **nationalRoamingEnabled** | **Boolean**|  | [optional] 
 **uniqueName** | **String**|  | [optional] 
 **voiceEnabled** | **Boolean**|  | [optional] 

### Return type

[**PreviewWirelessRatePlan**](PreviewWirelessRatePlan.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteWirelessRatePlan

> deleteWirelessRatePlan(sid)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewWirelessRatePlanApi();
let sid = "sid_example"; // String | 
apiInstance.deleteWirelessRatePlan(sid, (error, data, response) => {
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
 **sid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchWirelessRatePlan

> PreviewWirelessRatePlan fetchWirelessRatePlan(sid)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewWirelessRatePlanApi();
let sid = "sid_example"; // String | 
apiInstance.fetchWirelessRatePlan(sid, (error, data, response) => {
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
 **sid** | **String**|  | 

### Return type

[**PreviewWirelessRatePlan**](PreviewWirelessRatePlan.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listWirelessRatePlan

> ListWirelessRatePlanResponse listWirelessRatePlan(opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewWirelessRatePlanApi();
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listWirelessRatePlan(opts, (error, data, response) => {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListWirelessRatePlanResponse**](ListWirelessRatePlanResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateWirelessRatePlan

> PreviewWirelessRatePlan updateWirelessRatePlan(sid, opts)





### Example

```javascript
import TwilioPreview from 'twilio_preview';
let defaultClient = TwilioPreview.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioPreview.PreviewWirelessRatePlanApi();
let sid = "sid_example"; // String | 
let opts = {
  'friendlyName': "friendlyName_example", // String | 
  'uniqueName': "uniqueName_example" // String | 
};
apiInstance.updateWirelessRatePlan(sid, opts, (error, data, response) => {
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
 **sid** | **String**|  | 
 **friendlyName** | **String**|  | [optional] 
 **uniqueName** | **String**|  | [optional] 

### Return type

[**PreviewWirelessRatePlan**](PreviewWirelessRatePlan.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

