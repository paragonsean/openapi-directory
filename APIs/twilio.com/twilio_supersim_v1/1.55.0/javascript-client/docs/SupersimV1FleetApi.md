# TwilioSupersim.SupersimV1FleetApi

All URIs are relative to *https://supersim.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createFleet**](SupersimV1FleetApi.md#createFleet) | **POST** /v1/Fleets | 
[**fetchFleet**](SupersimV1FleetApi.md#fetchFleet) | **GET** /v1/Fleets/{Sid} | 
[**listFleet**](SupersimV1FleetApi.md#listFleet) | **GET** /v1/Fleets | 
[**updateFleet**](SupersimV1FleetApi.md#updateFleet) | **POST** /v1/Fleets/{Sid} | 



## createFleet

> SupersimV1Fleet createFleet(networkAccessProfile, opts)



Create a Fleet

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1FleetApi();
let networkAccessProfile = "networkAccessProfile_example"; // String | The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
let opts = {
  'dataEnabled': true, // Boolean | Defines whether SIMs in the Fleet are capable of using 2G/3G/4G/LTE/CAT-M data connectivity. Defaults to `true`.
  'dataLimit': 56, // Number | The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).
  'ipCommandsMethod': "ipCommandsMethod_example", // String | A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
  'ipCommandsUrl': "ipCommandsUrl_example", // String | The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
  'smsCommandsEnabled': true, // Boolean | Defines whether SIMs in the Fleet are capable of sending and receiving machine-to-machine SMS via Commands. Defaults to `true`.
  'smsCommandsMethod': "smsCommandsMethod_example", // String | A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
  'smsCommandsUrl': "smsCommandsUrl_example", // String | The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
};
apiInstance.createFleet(networkAccessProfile, opts, (error, data, response) => {
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
 **networkAccessProfile** | **String**| The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet&#39;s SIMs can connect to. | 
 **dataEnabled** | **Boolean**| Defines whether SIMs in the Fleet are capable of using 2G/3G/4G/LTE/CAT-M data connectivity. Defaults to &#x60;true&#x60;. | [optional] 
 **dataLimit** | **Number**| The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000). | [optional] 
 **ipCommandsMethod** | **String**| A string representing the HTTP method to use when making a request to &#x60;ip_commands_url&#x60;. Can be one of &#x60;POST&#x60; or &#x60;GET&#x60;. Defaults to &#x60;POST&#x60;. | [optional] 
 **ipCommandsUrl** | **String**| The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored. | [optional] 
 **smsCommandsEnabled** | **Boolean**| Defines whether SIMs in the Fleet are capable of sending and receiving machine-to-machine SMS via Commands. Defaults to &#x60;true&#x60;. | [optional] 
 **smsCommandsMethod** | **String**| A string representing the HTTP method to use when making a request to &#x60;sms_commands_url&#x60;. Can be one of &#x60;POST&#x60; or &#x60;GET&#x60;. Defaults to &#x60;POST&#x60;. | [optional] 
 **smsCommandsUrl** | **String**| The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. | [optional] 

### Return type

[**SupersimV1Fleet**](SupersimV1Fleet.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchFleet

> SupersimV1Fleet fetchFleet(sid)



Fetch a Fleet instance from your account.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1FleetApi();
let sid = "sid_example"; // String | The SID of the Fleet resource to fetch.
apiInstance.fetchFleet(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Fleet resource to fetch. | 

### Return type

[**SupersimV1Fleet**](SupersimV1Fleet.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listFleet

> ListFleetResponse listFleet(opts)



Retrieve a list of Fleets from your account.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1FleetApi();
let opts = {
  'networkAccessProfile': "networkAccessProfile_example", // String | The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet's SIMs can connect to.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listFleet(opts, (error, data, response) => {
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
 **networkAccessProfile** | **String**| The SID or unique name of the Network Access Profile that controls which cellular networks the Fleet&#39;s SIMs can connect to. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListFleetResponse**](ListFleetResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateFleet

> SupersimV1Fleet updateFleet(sid, opts)



Updates the given properties of a Super SIM Fleet instance from your account.

### Example

```javascript
import TwilioSupersim from 'twilio_supersim';
let defaultClient = TwilioSupersim.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioSupersim.SupersimV1FleetApi();
let sid = "sid_example"; // String | The SID of the Fleet resource to update.
let opts = {
  'dataLimit': 56, // Number | The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000).
  'ipCommandsMethod': "ipCommandsMethod_example", // String | A string representing the HTTP method to use when making a request to `ip_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
  'ipCommandsUrl': "ipCommandsUrl_example", // String | The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
  'networkAccessProfile': "networkAccessProfile_example", // String | The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet's SIMs can connect to.
  'smsCommandsMethod': "smsCommandsMethod_example", // String | A string representing the HTTP method to use when making a request to `sms_commands_url`. Can be one of `POST` or `GET`. Defaults to `POST`.
  'smsCommandsUrl': "smsCommandsUrl_example", // String | The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored.
  'uniqueName': "uniqueName_example" // String | An application-defined string that uniquely identifies the resource. It can be used in place of the resource's `sid` in the URL to address the resource.
};
apiInstance.updateFleet(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the Fleet resource to update. | 
 **dataLimit** | **Number**| The total data usage (download and upload combined) in Megabytes that each Super SIM assigned to the Fleet can consume during a billing period (normally one month). Value must be between 1MB (1) and 2TB (2,000,000). Defaults to 1GB (1,000). | [optional] 
 **ipCommandsMethod** | **String**| A string representing the HTTP method to use when making a request to &#x60;ip_commands_url&#x60;. Can be one of &#x60;POST&#x60; or &#x60;GET&#x60;. Defaults to &#x60;POST&#x60;. | [optional] 
 **ipCommandsUrl** | **String**| The URL that will receive a webhook when a Super SIM in the Fleet is used to send an IP Command from your device to a special IP address. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored. | [optional] 
 **networkAccessProfile** | **String**| The SID or unique name of the Network Access Profile that will control which cellular networks the Fleet&#39;s SIMs can connect to. | [optional] 
 **smsCommandsMethod** | **String**| A string representing the HTTP method to use when making a request to &#x60;sms_commands_url&#x60;. Can be one of &#x60;POST&#x60; or &#x60;GET&#x60;. Defaults to &#x60;POST&#x60;. | [optional] 
 **smsCommandsUrl** | **String**| The URL that will receive a webhook when a Super SIM in the Fleet is used to send an SMS from your device to the SMS Commands number. Your server should respond with an HTTP status code in the 200 range; any response body will be ignored. | [optional] 
 **uniqueName** | **String**| An application-defined string that uniquely identifies the resource. It can be used in place of the resource&#39;s &#x60;sid&#x60; in the URL to address the resource. | [optional] 

### Return type

[**SupersimV1Fleet**](SupersimV1Fleet.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

