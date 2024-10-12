# ServiceBroker.V1Api

All URIs are relative to *https://servicebroker.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicebrokerGetIamPolicy**](V1Api.md#servicebrokerGetIamPolicy) | **GET** /v1/{resource}:getIamPolicy | 
[**servicebrokerSetIamPolicy**](V1Api.md#servicebrokerSetIamPolicy) | **POST** /v1/{resource}:setIamPolicy | 
[**servicebrokerTestIamPermissions**](V1Api.md#servicebrokerTestIamPermissions) | **POST** /v1/{resource}:testIamPermissions | 



## servicebrokerGetIamPolicy

> GoogleIamV1Policy servicebrokerGetIamPolicy(resource, opts)



Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

### Example

```javascript
import ServiceBroker from 'service_broker';
let defaultClient = ServiceBroker.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBroker.V1Api();
let resource = "resource_example"; // String | REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'optionsRequestedPolicyVersion': 56 // Number | Optional. The policy format version to be returned.  Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected.  Requests for policies with any conditional bindings must specify version 3. Policies without any conditional bindings may specify any valid value or leave the field unset.
};
apiInstance.servicebrokerGetIamPolicy(resource, opts, (error, data, response) => {
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
 **resource** | **String**| REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **optionsRequestedPolicyVersion** | **Number**| Optional. The policy format version to be returned.  Valid values are 0, 1, and 3. Requests specifying an invalid value will be rejected.  Requests for policies with any conditional bindings must specify version 3. Policies without any conditional bindings may specify any valid value or leave the field unset. | [optional] 

### Return type

[**GoogleIamV1Policy**](GoogleIamV1Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerSetIamPolicy

> GoogleIamV1Policy servicebrokerSetIamPolicy(resource, opts)



Sets the access control policy on the specified resource. Replaces any existing policy.  Can return Public Errors: NOT_FOUND, INVALID_ARGUMENT and PERMISSION_DENIED

### Example

```javascript
import ServiceBroker from 'service_broker';
let defaultClient = ServiceBroker.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBroker.V1Api();
let resource = "resource_example"; // String | REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleIamV1SetIamPolicyRequest': new ServiceBroker.GoogleIamV1SetIamPolicyRequest() // GoogleIamV1SetIamPolicyRequest | 
};
apiInstance.servicebrokerSetIamPolicy(resource, opts, (error, data, response) => {
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
 **resource** | **String**| REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleIamV1SetIamPolicyRequest** | [**GoogleIamV1SetIamPolicyRequest**](GoogleIamV1SetIamPolicyRequest.md)|  | [optional] 

### Return type

[**GoogleIamV1Policy**](GoogleIamV1Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## servicebrokerTestIamPermissions

> GoogleIamV1TestIamPermissionsResponse servicebrokerTestIamPermissions(resource, opts)



Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a NOT_FOUND error.  Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may \&quot;fail open\&quot; without warning.

### Example

```javascript
import ServiceBroker from 'service_broker';
let defaultClient = ServiceBroker.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceBroker.V1Api();
let resource = "resource_example"; // String | REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'callback': "callback_example", // String | JSONP
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'googleIamV1TestIamPermissionsRequest': new ServiceBroker.GoogleIamV1TestIamPermissionsRequest() // GoogleIamV1TestIamPermissionsRequest | 
};
apiInstance.servicebrokerTestIamPermissions(resource, opts, (error, data, response) => {
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
 **resource** | **String**| REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **googleIamV1TestIamPermissionsRequest** | [**GoogleIamV1TestIamPermissionsRequest**](GoogleIamV1TestIamPermissionsRequest.md)|  | [optional] 

### Return type

[**GoogleIamV1TestIamPermissionsResponse**](GoogleIamV1TestIamPermissionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*

