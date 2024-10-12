# TwilioSupersim.SupersimV1BillingPeriodApi

All URIs are relative to *https://supersim.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**listBillingPeriod**](SupersimV1BillingPeriodApi.md#listBillingPeriod) | **GET** /v1/Sims/{SimSid}/BillingPeriods | 



## listBillingPeriod

> ListBillingPeriodResponse listBillingPeriod(simSid, opts)



Retrieve a list of Billing Periods for a Super SIM.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1BillingPeriodApi();
let simSid = "simSid_example"; // String | The SID of the Super SIM to list Billing Periods for.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listBillingPeriod(simSid, opts, (error, data, response) => {
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
 **simSid** | **String**| The SID of the Super SIM to list Billing Periods for. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListBillingPeriodResponse**](ListBillingPeriodResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

