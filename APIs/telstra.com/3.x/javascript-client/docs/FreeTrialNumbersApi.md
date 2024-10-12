# MessagingApiV3X.FreeTrialNumbersApi

All URIs are relative to *https://products.api.telstra.com/messaging/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createTrialNumbers**](FreeTrialNumbersApi.md#createTrialNumbers) | **POST** /free-trial-numbers | create free trial number list
[**getTrialNumbers**](FreeTrialNumbersApi.md#getTrialNumbers) | **GET** /free-trial-numbers | get all free trial numbers



## createTrialNumbers

> FreeTrialNumbers createTrialNumbers(contentLanguage, authorization, accept, acceptCharset, contentType, createTrialNumbersRequest, opts)

create free trial number list

Your Free Trial Numbers are the 10 recipient mobile numbers that you can message during the Free Trial. The first five numbers you send an SMS/MMS to will automatically be added to your Free Trial Numbers list. After that, you can use this endpoint to register another five. Alternatively, you can use this endpoint to register all 10 numbers.    Use this endpoint to register a Free Trial Number to your account. To test out all the features that the trial has to offer, we recommend registering your own mobile number to your Free Trial Numbers list.   Note that you can only message mobile numbers that have been added to your Free Trial list and once registered, a Free Trial Number cannot be removed or replaced. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.FreeTrialNumbersApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let createTrialNumbersRequest = new MessagingApiV3X.CreateTrialNumbersRequest(); // CreateTrialNumbersRequest | 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.createTrialNumbers(contentLanguage, authorization, accept, acceptCharset, contentType, createTrialNumbersRequest, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **createTrialNumbersRequest** | [**CreateTrialNumbersRequest**](CreateTrialNumbersRequest.md)|  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

[**FreeTrialNumbers**](FreeTrialNumbers.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTrialNumbers

> FreeTrialNumbers getTrialNumbers(contentLanguage, authorization, accept, acceptCharset, contentType, opts)

get all free trial numbers

Use this endpoint to fetch the Free Trial Number(s) currently assigned to your account. These are the mobile numbers that you can message during the Free Trial.  If you&#39;re using a paid plan, there&#39;s no limit to the number of recipients that you can message, so you don&#39;t need to register Free Trial Numbers. 

### Example

```javascript
import MessagingApiV3X from 'messaging_api_v3_x';
let defaultClient = MessagingApiV3X.ApiClient.instance;
// Configure OAuth2 access token for authorization: bearer_auth
let bearer_auth = defaultClient.authentications['bearer_auth'];
bearer_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MessagingApiV3X.FreeTrialNumbersApi();
let contentLanguage = "en-au"; // String | 
let authorization = "Bearer <access_token>"; // String | 
let accept = "application/json"; // String | 
let acceptCharset = "utf-8"; // String | 
let contentType = "application/json"; // String | 
let opts = {
  'telstraApiVersion': "3.1.0" // String | 
};
apiInstance.getTrialNumbers(contentLanguage, authorization, accept, acceptCharset, contentType, opts, (error, data, response) => {
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
 **contentLanguage** | **String**|  | 
 **authorization** | **String**|  | 
 **accept** | **String**|  | 
 **acceptCharset** | **String**|  | 
 **contentType** | **String**|  | 
 **telstraApiVersion** | **String**|  | [optional] 

### Return type

[**FreeTrialNumbers**](FreeTrialNumbers.md)

### Authorization

[bearer_auth](../README.md#bearer_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

