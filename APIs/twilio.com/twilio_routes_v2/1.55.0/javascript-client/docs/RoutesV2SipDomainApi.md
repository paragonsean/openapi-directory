# TwilioRoutes.RoutesV2SipDomainApi

All URIs are relative to *https://routes.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchSipDomain**](RoutesV2SipDomainApi.md#fetchSipDomain) | **GET** /v2/SipDomains/{SipDomain} | 
[**updateSipDomain**](RoutesV2SipDomainApi.md#updateSipDomain) | **POST** /v2/SipDomains/{SipDomain} | 



## fetchSipDomain

> RoutesV2SipDomain fetchSipDomain(sipDomain)





### Example

```javascript
import TwilioRoutes from 'twilio_routes';
let defaultClient = TwilioRoutes.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioRoutes.RoutesV2SipDomainApi();
let sipDomain = "sipDomain_example"; // String | 
apiInstance.fetchSipDomain(sipDomain, (error, data, response) => {
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
 **sipDomain** | **String**|  | 

### Return type

[**RoutesV2SipDomain**](RoutesV2SipDomain.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSipDomain

> RoutesV2SipDomain updateSipDomain(sipDomain, opts)





### Example

```javascript
import TwilioRoutes from 'twilio_routes';
let defaultClient = TwilioRoutes.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioRoutes.RoutesV2SipDomainApi();
let sipDomain = "sipDomain_example"; // String | 
let opts = {
  'friendlyName': "friendlyName_example", // String | 
  'voiceRegion': "voiceRegion_example" // String | 
};
apiInstance.updateSipDomain(sipDomain, opts, (error, data, response) => {
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
 **sipDomain** | **String**|  | 
 **friendlyName** | **String**|  | [optional] 
 **voiceRegion** | **String**|  | [optional] 

### Return type

[**RoutesV2SipDomain**](RoutesV2SipDomain.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

