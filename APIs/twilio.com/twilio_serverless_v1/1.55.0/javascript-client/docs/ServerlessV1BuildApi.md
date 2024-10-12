# TwilioServerless.ServerlessV1BuildApi

All URIs are relative to *https://serverless.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createBuild**](ServerlessV1BuildApi.md#createBuild) | **POST** /v1/Services/{ServiceSid}/Builds | 
[**deleteBuild**](ServerlessV1BuildApi.md#deleteBuild) | **DELETE** /v1/Services/{ServiceSid}/Builds/{Sid} | 
[**fetchBuild**](ServerlessV1BuildApi.md#fetchBuild) | **GET** /v1/Services/{ServiceSid}/Builds/{Sid} | 
[**listBuild**](ServerlessV1BuildApi.md#listBuild) | **GET** /v1/Services/{ServiceSid}/Builds | 



## createBuild

> ServerlessV1ServiceBuild createBuild(serviceSid, opts)



Create a new Build resource. At least one function version or asset version is required.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1BuildApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to create the Build resource under.
let opts = {
  'assetVersions': ["null"], // [String] | The list of Asset Version resource SIDs to include in the Build.
  'dependencies': "dependencies_example", // String | A list of objects that describe the Dependencies included in the Build. Each object contains the `name` and `version` of the dependency.
  'functionVersions': ["null"], // [String] | The list of the Function Version resource SIDs to include in the Build.
  'runtime': "runtime_example" // String | The Runtime version that will be used to run the Build resource when it is deployed.
};
apiInstance.createBuild(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to create the Build resource under. | 
 **assetVersions** | [**[String]**](String.md)| The list of Asset Version resource SIDs to include in the Build. | [optional] 
 **dependencies** | **String**| A list of objects that describe the Dependencies included in the Build. Each object contains the &#x60;name&#x60; and &#x60;version&#x60; of the dependency. | [optional] 
 **functionVersions** | [**[String]**](String.md)| The list of the Function Version resource SIDs to include in the Build. | [optional] 
 **runtime** | **String**| The Runtime version that will be used to run the Build resource when it is deployed. | [optional] 

### Return type

[**ServerlessV1ServiceBuild**](ServerlessV1ServiceBuild.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteBuild

> deleteBuild(serviceSid, sid)



Delete a Build resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1BuildApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to delete the Build resource from.
let sid = "sid_example"; // String | The SID of the Build resource to delete.
apiInstance.deleteBuild(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to delete the Build resource from. | 
 **sid** | **String**| The SID of the Build resource to delete. | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchBuild

> ServerlessV1ServiceBuild fetchBuild(serviceSid, sid)



Retrieve a specific Build resource.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1BuildApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to fetch the Build resource from.
let sid = "sid_example"; // String | The SID of the Build resource to fetch.
apiInstance.fetchBuild(serviceSid, sid, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to fetch the Build resource from. | 
 **sid** | **String**| The SID of the Build resource to fetch. | 

### Return type

[**ServerlessV1ServiceBuild**](ServerlessV1ServiceBuild.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listBuild

> ListBuildResponse listBuild(serviceSid, opts)



Retrieve a list of all Builds.

### Example

```javascript
import TwilioServerless from 'twilio_serverless';
let defaultClient = TwilioServerless.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioServerless.ServerlessV1BuildApi();
let serviceSid = "serviceSid_example"; // String | The SID of the Service to read the Build resources from.
let opts = {
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listBuild(serviceSid, opts, (error, data, response) => {
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
 **serviceSid** | **String**| The SID of the Service to read the Build resources from. | 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListBuildResponse**](ListBuildResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

