# TwilioSupersim.SupersimV1EsimProfileApi

All URIs are relative to *https://supersim.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEsimProfile**](SupersimV1EsimProfileApi.md#createEsimProfile) | **POST** /v1/ESimProfiles | 
[**fetchEsimProfile**](SupersimV1EsimProfileApi.md#fetchEsimProfile) | **GET** /v1/ESimProfiles/{Sid} | 
[**listEsimProfile**](SupersimV1EsimProfileApi.md#listEsimProfile) | **GET** /v1/ESimProfiles | 



## createEsimProfile

> SupersimV1EsimProfile createEsimProfile(opts)



Order an eSIM Profile.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1EsimProfileApi();
let opts = {
  'callbackMethod': "callbackMethod_example", // String | The HTTP method we should use to call `callback_url`. Can be: `GET` or `POST` and the default is POST.
  'callbackUrl': "callbackUrl_example", // String | The URL we should call using the `callback_method` when the status of the eSIM Profile changes. At this stage of the eSIM Profile pilot, the a request to the URL will only be called when the ESimProfile resource changes from `reserving` to `available`.
  'eid': "eid_example", // String | Identifier of the eUICC that will claim the eSIM Profile.
  'generateMatchingId': true // Boolean | When set to `true`, a value for `Eid` does not need to be provided. Instead, when the eSIM profile is reserved, a matching ID will be generated and returned via the `matching_id` property. This identifies the specific eSIM profile that can be used by any capable device to claim and download the profile.
};
apiInstance.createEsimProfile(opts, (error, data, response) => {
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
 **callbackMethod** | **String**| The HTTP method we should use to call &#x60;callback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60; and the default is POST. | [optional] 
 **callbackUrl** | **String**| The URL we should call using the &#x60;callback_method&#x60; when the status of the eSIM Profile changes. At this stage of the eSIM Profile pilot, the a request to the URL will only be called when the ESimProfile resource changes from &#x60;reserving&#x60; to &#x60;available&#x60;. | [optional] 
 **eid** | **String**| Identifier of the eUICC that will claim the eSIM Profile. | [optional] 
 **generateMatchingId** | **Boolean**| When set to &#x60;true&#x60;, a value for &#x60;Eid&#x60; does not need to be provided. Instead, when the eSIM profile is reserved, a matching ID will be generated and returned via the &#x60;matching_id&#x60; property. This identifies the specific eSIM profile that can be used by any capable device to claim and download the profile. | [optional] 

### Return type

[**SupersimV1EsimProfile**](SupersimV1EsimProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchEsimProfile

> SupersimV1EsimProfile fetchEsimProfile(sid)



Fetch an eSIM Profile.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1EsimProfileApi();
let sid = "sid_example"; // String | The SID of the eSIM Profile resource to fetch.
apiInstance.fetchEsimProfile(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the eSIM Profile resource to fetch. | 

### Return type

[**SupersimV1EsimProfile**](SupersimV1EsimProfile.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEsimProfile

> ListEsimProfileResponse listEsimProfile(opts)



Retrieve a list of eSIM Profiles.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1EsimProfileApi();
let opts = {
  'eid': "eid_example", // String | List the eSIM Profiles that have been associated with an EId.
  'simSid': "simSid_example", // String | Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/iot/supersim/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records.
  'status': "status_example", // EsimProfileEnumStatus | List the eSIM Profiles that are in a given status.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listEsimProfile(opts, (error, data, response) => {
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
 **eid** | **String**| List the eSIM Profiles that have been associated with an EId. | [optional] 
 **simSid** | **String**| Find the eSIM Profile resource related to a [Sim](https://www.twilio.com/docs/iot/supersim/api/sim-resource) resource by providing the SIM SID. Will always return an array with either 1 or 0 records. | [optional] 
 **status** | **EsimProfileEnumStatus**| List the eSIM Profiles that are in a given status. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListEsimProfileResponse**](ListEsimProfileResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

