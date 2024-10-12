# CleverCloudApi.GithubApi

All URIs are relative to *https://api.clever-cloud.com/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteGithubLink_0**](GithubApi.md#deleteGithubLink_0) | **DELETE** /github/link | 
[**getGithubApplications_1**](GithubApi.md#getGithubApplications_1) | **GET** /github/applications | 
[**getGithubCallback_0**](GithubApi.md#getGithubCallback_0) | **GET** /github/callback | 
[**getGithubEmails_0**](GithubApi.md#getGithubEmails_0) | **GET** /github/emails | 
[**getGithubKeys_0**](GithubApi.md#getGithubKeys_0) | **GET** /github/keys | 
[**getGithubLink_0**](GithubApi.md#getGithubLink_0) | **GET** /github/link | 
[**getGithubLogin_0**](GithubApi.md#getGithubLogin_0) | **GET** /github/login | 
[**getGithubSignup_0**](GithubApi.md#getGithubSignup_0) | **GET** /github/signup | 
[**getGithubUsername_0**](GithubApi.md#getGithubUsername_0) | **GET** /github/username | 
[**getGithub_0**](GithubApi.md#getGithub_0) | **GET** /github | 
[**postGithubRedeploy_0**](GithubApi.md#postGithubRedeploy_0) | **POST** /github/redeploy | 
[**postGithubSignup_0**](GithubApi.md#postGithubSignup_0) | **POST** /github/signup | 



## deleteGithubLink_0

> deleteGithubLink_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.GithubApi();
apiInstance.deleteGithubLink_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGithubApplications_1

> [Application] getGithubApplications_1()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.GithubApi();
apiInstance.getGithubApplications_1((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Application]**](Application.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGithubCallback_0

> getGithubCallback_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.GithubApi();
let opts = {
  'code': "code_example", // String | 
  'state': "state_example", // String | 
  'error': "error_example", // String | 
  'errorDescription': "errorDescription_example", // String | 
  'errorUri': "errorUri_example", // String | 
  'cookie': "cookie_example" // String | 
};
apiInstance.getGithubCallback_0(opts, (error, data, response) => {
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
 **code** | **String**|  | [optional] 
 **state** | **String**|  | [optional] 
 **error** | **String**|  | [optional] 
 **errorDescription** | **String**|  | [optional] 
 **errorUri** | **String**|  | [optional] 
 **cookie** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGithubEmails_0

> [String] getGithubEmails_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.GithubApi();
apiInstance.getGithubEmails_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**[String]**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGithubKeys_0

> [Key] getGithubKeys_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.GithubApi();
apiInstance.getGithubKeys_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**[Key]**](Key.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGithubLink_0

> getGithubLink_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.GithubApi();
let opts = {
  'transactionId': "transactionId_example", // String | From GET /github
  'redirectUrl': "redirectUrl_example" // String | 
};
apiInstance.getGithubLink_0(opts, (error, data, response) => {
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
 **transactionId** | **String**| From GET /github | [optional] 
 **redirectUrl** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGithubLogin_0

> getGithubLogin_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.GithubApi();
let opts = {
  'redirectUrl': "redirectUrl_example", // String | 
  'fromAuthorize': "fromAuthorize_example" // String | 
};
apiInstance.getGithubLogin_0(opts, (error, data, response) => {
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
 **redirectUrl** | **String**|  | [optional] 
 **fromAuthorize** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGithubSignup_0

> getGithubSignup_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.GithubApi();
let opts = {
  'redirectUrl': "redirectUrl_example", // String | 
  'fromAuthorize': "fromAuthorize_example" // String | 
};
apiInstance.getGithubSignup_0(opts, (error, data, response) => {
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
 **redirectUrl** | **String**|  | [optional] 
 **fromAuthorize** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getGithubUsername_0

> String getGithubUsername_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.GithubApi();
apiInstance.getGithubUsername_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## getGithub_0

> TransactionId getGithub_0()



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.GithubApi();
apiInstance.getGithub_0((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**TransactionId**](TransactionId.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postGithubRedeploy_0

> postGithubRedeploy_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.GithubApi();
let opts = {
  'userAgent': "userAgent_example", // String | 
  'xGithubEvent': "xGithubEvent_example", // String | 
  'xHubSignature': "xHubSignature_example" // String | 
};
apiInstance.postGithubRedeploy_0(opts, (error, data, response) => {
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
 **userAgent** | **String**|  | [optional] 
 **xGithubEvent** | **String**|  | [optional] 
 **xHubSignature** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## postGithubSignup_0

> postGithubSignup_0(opts)



### Example

```javascript
import CleverCloudApi from 'clever_cloud_api';

let apiInstance = new CleverCloudApi.GithubApi();
let opts = {
  'transactionId': "transactionId_example", // String | 
  'name': "name_example", // String | 
  'otherId': "otherId_example", // String | 
  'otherEmail': "otherEmail_example", // String | 
  'password': "password_example", // String | 
  'autoLink': "autoLink_example", // String | 
  'terms': "terms_example" // String | 
};
apiInstance.postGithubSignup_0(opts, (error, data, response) => {
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
 **transactionId** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **otherId** | **String**|  | [optional] 
 **otherEmail** | **String**|  | [optional] 
 **password** | **String**|  | [optional] 
 **autoLink** | **String**|  | [optional] 
 **terms** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

