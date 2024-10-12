# TwilioServerless.ServerlessV1EnvironmentApi

All URIs are relative to *https://serverless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createEnvironment**](ServerlessV1EnvironmentApi.md#createEnvironment) | **POST** /v1/Services/{ServiceSid}/Environments | 
[**deleteEnvironment**](ServerlessV1EnvironmentApi.md#deleteEnvironment) | **DELETE** /v1/Services/{ServiceSid}/Environments/{Sid} | 
[**fetchEnvironment**](ServerlessV1EnvironmentApi.md#fetchEnvironment) | **GET** /v1/Services/{ServiceSid}/Environments/{Sid} | 
[**listEnvironment**](ServerlessV1EnvironmentApi.md#listEnvironment) | **GET** /v1/Services/{ServiceSid}/Environments | 



## createEnvironment

> ServerlessV1ServiceEnvironment createEnvironment(serviceSid, uniqueName, opts)



Create a new environment.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1EnvironmentApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to create the Environment resource under.
let uniqueName = "uniqueName_example"; // String | A user-defined string that uniquely identifies the Environment resource. It can be a maximum of 100 characters.
let opts = {
  'domainSuffix': "domainSuffix_example" // String | A URL-friendly name that represents the environment and forms part of the domain name. It can be a maximum of 16 characters.
};
apiInstance.createEnvironment(serviceSid, uniqueName, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to create the Environment resource under. | 
 **uniqueName** | **String**| A user-defined string that uniquely identifies the Environment resource. It can be a maximum of 100 characters. | 
 **domainSuffix** | **String**| A URL-friendly name that represents the environment and forms part of the domain name. It can be a maximum of 16 characters. | [optional] 

### Return type

[**ServerlessV1ServiceEnvironment**](ServerlessV1ServiceEnvironment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteEnvironment

> deleteEnvironment(serviceSid, sid)



Delete a specific environment.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1EnvironmentApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to delete the Environment resource from.
let sid = "sid_example"; // String | The SID of the Environment resource to delete.
apiInstance.deleteEnvironment(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to delete the Environment resource from. | 
 **sid** | **String**| The SID of the Environment resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchEnvironment

> ServerlessV1ServiceEnvironment fetchEnvironment(serviceSid, sid)



Retrieve a specific environment.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1EnvironmentApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Environment resource from.
let sid = "sid_example"; // String | The SID of the Environment resource to fetch.
apiInstance.fetchEnvironment(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to fetch the Environment resource from. | 
 **sid** | **String**| The SID of the Environment resource to fetch. | 

### Return type

[**ServerlessV1ServiceEnvironment**](ServerlessV1ServiceEnvironment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEnvironment

> ListEnvironmentResponse listEnvironment(serviceSid, opts)



Retrieve a list of all environments.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1EnvironmentApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Environment resources from.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listEnvironment(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to read the Environment resources from. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListEnvironmentResponse**](ListEnvironmentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

