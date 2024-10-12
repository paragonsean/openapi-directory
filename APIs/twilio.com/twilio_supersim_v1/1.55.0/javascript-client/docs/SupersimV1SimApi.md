# TwilioSupersim.SupersimV1SimApi

All URIs are relative to *https://supersim.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSim**](SupersimV1SimApi.md#createSim) | **POST** /v1/Sims | 
[**fetchSim**](SupersimV1SimApi.md#fetchSim) | **GET** /v1/Sims/{Sid} | 
[**listSim**](SupersimV1SimApi.md#listSim) | **GET** /v1/Sims | 
[**updateSim**](SupersimV1SimApi.md#updateSim) | **POST** /v1/Sims/{Sid} | 



## createSim

> SupersimV1Sim createSim(iccid, registrationCode)



Register a Super SIM to your Account

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1SimApi();
let iccid = "iccid_example"; // String | The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) of the Super SIM to be added to your Account.
let registrationCode = "registrationCode_example"; // String | The 10-digit code required to claim the Super SIM for your Account.
apiInstance.createSim(iccid, registrationCode, (error, data, response) => {
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
 **iccid** | **String**| The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) of the Super SIM to be added to your Account. | 
 **registrationCode** | **String**| The 10-digit code required to claim the Super SIM for your Account. | 

### Return type

[**SupersimV1Sim**](SupersimV1Sim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchSim

> SupersimV1Sim fetchSim(sid)



Fetch a Super SIM instance from your account.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1SimApi();
let sid = "sid_example"; // String | The SID of the Sim resource to fetch.
apiInstance.fetchSim(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Sim resource to fetch. | 

### Return type

[**SupersimV1Sim**](SupersimV1Sim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSim

> ListSimResponse listSim(opts)



Retrieve a list of Super SIMs from your account.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1SimApi();
let opts = {
  'status': "status_example", // SimEnumStatus | The status of the Sim resources to read. Can be `new`, `ready`, `active`, `inactive`, or `scheduled`.
  'fleet': "fleet_example", // String | The SID or unique name of the Fleet to which a list of Sims are assigned.
  'iccid': "iccid_example", // String | The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listSim(opts, (error, data, response) => {
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
 **status** | **SimEnumStatus**| The status of the Sim resources to read. Can be &#x60;new&#x60;, &#x60;ready&#x60;, &#x60;active&#x60;, &#x60;inactive&#x60;, or &#x60;scheduled&#x60;. | [optional] 
 **fleet** | **String**| The SID or unique name of the Fleet to which a list of Sims are assigned. | [optional] 
 **iccid** | **String**| The [ICCID](https://en.wikipedia.org/wiki/Subscriber_identity_module#ICCID) associated with a Super SIM to filter the list by. Passing this parameter will always return a list containing zero or one SIMs. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListSimResponse**](ListSimResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSim

> SupersimV1Sim updateSim(sid, opts)



Updates the given properties of a Super SIM instance from your account.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1SimApi();
let sid = "sid_example"; // String | The SID of the Sim resource to update.
let opts = {
  'accountSid': "accountSid_example", // String | The SID of the Account to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a Subaccount of the requesting Account. Only valid when the Sim resource's status is new.
  'callbackMethod': "callbackMethod_example", // String | The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
  'callbackUrl': "callbackUrl_example", // String | The URL we should call using the `callback_method` after an asynchronous update has finished.
  'fleet': "fleet_example", // String | The SID or unique name of the Fleet to which the SIM resource should be assigned.
  'status': "status_example", // SimEnumStatusUpdate | 
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
};
apiInstance.updateSim(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the Sim resource to update. | 
 **accountSid** | **String**| The SID of the Account to which the Sim resource should belong. The Account SID can only be that of the requesting Account or that of a Subaccount of the requesting Account. Only valid when the Sim resource&#39;s status is new. | [optional] 
 **callbackMethod** | **String**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is POST. | [optional] 
 **callbackUrl** | **String**| The URL we should call using the &#x60;callback_method&#x60; after an asynchronous update has finished. | [optional] 
 **fleet** | **String**| The SID or unique name of the Fleet to which the SIM resource should be assigned. | [optional] 
 **status** | **SimEnumStatusUpdate**|  | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. | [optional] 

### Return type

[**SupersimV1Sim**](SupersimV1Sim.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

