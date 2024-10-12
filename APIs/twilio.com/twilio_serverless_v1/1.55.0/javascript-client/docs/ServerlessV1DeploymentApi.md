# TwilioServerless.ServerlessV1DeploymentApi

All URIs are relative to *https://serverless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createDeployment**](ServerlessV1DeploymentApi.md#createDeployment) | **POST** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Deployments | 
[**fetchDeployment**](ServerlessV1DeploymentApi.md#fetchDeployment) | **GET** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Deployments/{Sid} | 
[**listDeployment**](ServerlessV1DeploymentApi.md#listDeployment) | **GET** /v1/Services/{ServiceSid}/Environments/{EnvironmentSid}/Deployments | 



## createDeployment

> ServerlessV1ServiceEnvironmentDeployment createDeployment(serviceSid, environmentSid, opts)



Create a new Deployment.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1DeploymentApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to create the Deployment resource under.
let environmentSid = "environmentSid_example"; // String | The SID of the Environment for the Deployment.
let opts = {
  'buildSid': "buildSid_example" // String | The SID of the Build for the Deployment.
};
apiInstance.createDeployment(serviceSid, environmentSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to create the Deployment resource under. | 
 **environmentSid** | **String**| The SID of the Environment for the Deployment. | 
 **buildSid** | **String**| The SID of the Build for the Deployment. | [optional] 

### Return type

[**ServerlessV1ServiceEnvironmentDeployment**](ServerlessV1ServiceEnvironmentDeployment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## fetchDeployment

> ServerlessV1ServiceEnvironmentDeployment fetchDeployment(serviceSid, environmentSid, sid)



Retrieve a specific Deployment.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1DeploymentApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Deployment resource from.
let environmentSid = "environmentSid_example"; // String | The SID of the Environment used by the Deployment to fetch.
let sid = "sid_example"; // String | The SID that identifies the Deployment resource to fetch.
apiInstance.fetchDeployment(serviceSid, environmentSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to fetch the Deployment resource from. | 
 **environmentSid** | **String**| The SID of the Environment used by the Deployment to fetch. | 
 **sid** | **String**| The SID that identifies the Deployment resource to fetch. | 

### Return type

[**ServerlessV1ServiceEnvironmentDeployment**](ServerlessV1ServiceEnvironmentDeployment.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeployment

> ListDeploymentResponse listDeployment(serviceSid, environmentSid, opts)



Retrieve a list of all Deployments.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1DeploymentApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Deployment resources from.
let environmentSid = "environmentSid_example"; // String | The SID of the Environment used by the Deployment resources to read.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listDeployment(serviceSid, environmentSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to read the Deployment resources from. | 
 **environmentSid** | **String**| The SID of the Environment used by the Deployment resources to read. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListDeploymentResponse**](ListDeploymentResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

