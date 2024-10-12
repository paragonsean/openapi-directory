# ServiceBroker.ProjectsApi

All URIs are relative to *https://servicebroker.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicebrokerProjectsBrokersInstancesServiceBindingsList**](ProjectsApi.md#servicebrokerProjectsBrokersInstancesServiceBindingsList) | **GET** /v1alpha1/{parent}/service_bindings | 
[**servicebrokerProjectsBrokersServiceInstancesList**](ProjectsApi.md#servicebrokerProjectsBrokersServiceInstancesList) | **GET** /v1alpha1/{parent}/service_instances | 
[**servicebrokerProjectsBrokersV2CatalogList**](ProjectsApi.md#servicebrokerProjectsBrokersV2CatalogList) | **GET** /v1alpha1/{parent}/v2/catalog | 
[**servicebrokerProjectsBrokersV2ServiceInstancesCreate**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesCreate) | **PUT** /v1alpha1/{parent}/v2/service_instances/{instance_id} | 
[**servicebrokerProjectsBrokersV2ServiceInstancesDelete**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesDelete) | **DELETE** /v1alpha1/{parent}/v2/service_instances/{instanceId} | 
[**servicebrokerProjectsBrokersV2ServiceInstancesGet**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesGet) | **GET** /v1alpha1/{name} | 
[**servicebrokerProjectsBrokersV2ServiceInstancesGetLastOperation**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesGetLastOperation) | **GET** /v1alpha1/{parent}/v2/service_instances/{instanceId}/last_operation | 
[**servicebrokerProjectsBrokersV2ServiceInstancesPatch**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesPatch) | **PATCH** /v1alpha1/{parent}/v2/service_instances/{instance_id} | 
[**servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate) | **PUT** /v1alpha1/{parent}/v2/service_instances/{instanceId}/service_bindings/{binding_id} | 
[**servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet) | **GET** /v1alpha1/{parent}/v2/service_instances/{instanceId}/service_bindings/{bindingId} | 
[**servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation) | **GET** /v1alpha1/{parent}/v2/service_instances/{instanceId}/service_bindings/{bindingId}/last_operation | 



## servicebrokerProjectsBrokersInstancesServiceBindingsList

> GoogleCloudServicebrokerV1alpha1ListBindingsResponse servicebrokerProjectsBrokersInstancesServiceBindingsList(parent, opts)



Lists all the bindings in the instance

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

let apiInstance = new ServiceBroker.ProjectsApi();
let parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]/instances/[INSTANCE_ID]`.
let opts = {
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'pageSize': 56, // Number | Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. If unset or 0, all the results will be returned.
  'pageToken': "pageToken_example" // String | Specifies a page token to use. Set `pageToken` to a `nextPageToken` returned by a previous list request to get the next page of results.
};
apiInstance.servicebrokerProjectsBrokersInstancesServiceBindingsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/instances/[INSTANCE_ID]&#x60;. | 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **pageSize** | **Number**| Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. If unset or 0, all the results will be returned. | [optional] 
 **pageToken** | **String**| Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1alpha1ListBindingsResponse**](GoogleCloudServicebrokerV1alpha1ListBindingsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerProjectsBrokersServiceInstancesList

> GoogleCloudServicebrokerV1alpha1ListServiceInstancesResponse servicebrokerProjectsBrokersServiceInstancesList(parent, opts)



Lists all the instances in the brokers This API is an extension and not part of the OSB spec. Hence the path is a standard Google API URL.

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

let apiInstance = new ServiceBroker.ProjectsApi();
let parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
let opts = {
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'pageSize': 56, // Number | Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. If unset or 0, all the results will be returned.
  'pageToken': "pageToken_example" // String | Specifies a page token to use. Set `pageToken` to a `nextPageToken` returned by a previous list request to get the next page of results.
};
apiInstance.servicebrokerProjectsBrokersServiceInstancesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;. | 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **pageSize** | **Number**| Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. If unset or 0, all the results will be returned. | [optional] 
 **pageToken** | **String**| Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1alpha1ListServiceInstancesResponse**](GoogleCloudServicebrokerV1alpha1ListServiceInstancesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerProjectsBrokersV2CatalogList

> GoogleCloudServicebrokerV1alpha1ListCatalogResponse servicebrokerProjectsBrokersV2CatalogList(parent, opts)



Lists all the Services registered with this broker for consumption for given service registry broker, which contains an set of services. Note, that Service producer API is separate from Broker API.

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

let apiInstance = new ServiceBroker.ProjectsApi();
let parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
let opts = {
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'pageSize': 56, // Number | Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. If unset or 0, all the results will be returned.
  'pageToken': "pageToken_example" // String | Specifies a page token to use. Set `pageToken` to a `nextPageToken` returned by a previous list request to get the next page of results.
};
apiInstance.servicebrokerProjectsBrokersV2CatalogList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;. | 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **pageSize** | **Number**| Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. If unset or 0, all the results will be returned. | [optional] 
 **pageToken** | **String**| Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1alpha1ListCatalogResponse**](GoogleCloudServicebrokerV1alpha1ListCatalogResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesCreate

> GoogleCloudServicebrokerV1alpha1CreateServiceInstanceResponse servicebrokerProjectsBrokersV2ServiceInstancesCreate(parent, instanceId, opts)



Provisions a service instance. If &#x60;request.accepts_incomplete&#x60; is false and Broker cannot execute request synchronously HTTP 422 error will be returned along with FAILED_PRECONDITION status. If &#x60;request.accepts_incomplete&#x60; is true and the Broker decides to execute resource asynchronously then HTTP 202 response code will be returned and a valid polling operation in the response will be included. If Broker executes the request synchronously and it succeeds HTTP 201 response will be furnished. If identical instance exists, then HTTP 200 response will be returned. If an instance with identical ID but mismatching parameters exists, then HTTP 409 status code will be returned.

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

let apiInstance = new ServiceBroker.ProjectsApi();
let parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
let instanceId = "instanceId_example"; // String | The id of the service instance. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required.
let opts = {
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'acceptsIncomplete': true, // Boolean | Value indicating that API client supports asynchronous operations. If Broker cannot execute the request synchronously HTTP 422 code will be returned to HTTP clients along with FAILED_PRECONDITION error. If true and broker will execute request asynchronously 202 HTTP code will be returned. This broker always requires this to be true as all mutator operations are asynchronous.
  'googleCloudServicebrokerV1alpha1ServiceInstance': new ServiceBroker.GoogleCloudServicebrokerV1alpha1ServiceInstance() // GoogleCloudServicebrokerV1alpha1ServiceInstance | 
};
apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesCreate(parent, instanceId, opts, (error, data, response) => {
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
 **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;. | 
 **instanceId** | **String**| The id of the service instance. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required. | 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **acceptsIncomplete** | **Boolean**| Value indicating that API client supports asynchronous operations. If Broker cannot execute the request synchronously HTTP 422 code will be returned to HTTP clients along with FAILED_PRECONDITION error. If true and broker will execute request asynchronously 202 HTTP code will be returned. This broker always requires this to be true as all mutator operations are asynchronous. | [optional] 
 **googleCloudServicebrokerV1alpha1ServiceInstance** | [**GoogleCloudServicebrokerV1alpha1ServiceInstance**](GoogleCloudServicebrokerV1alpha1ServiceInstance.md)|  | [optional] 

### Return type

[**GoogleCloudServicebrokerV1alpha1CreateServiceInstanceResponse**](GoogleCloudServicebrokerV1alpha1CreateServiceInstanceResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesDelete

> GoogleCloudServicebrokerV1alpha1DeleteServiceInstanceResponse servicebrokerProjectsBrokersV2ServiceInstancesDelete(parent, instanceId, opts)



Deprovisions a service instance. For synchronous/asynchronous request details see CreateServiceInstance method. If service instance does not exist HTTP 410 status will be returned.

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

let apiInstance = new ServiceBroker.ProjectsApi();
let parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
let instanceId = "instanceId_example"; // String | The instance id to deprovision.
let opts = {
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'acceptsIncomplete': true, // Boolean | See CreateServiceInstanceRequest for details.
  'planId': "planId_example", // String | The plan id of the service instance.
  'serviceId': "serviceId_example" // String | The service id of the service instance.
};
apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesDelete(parent, instanceId, opts, (error, data, response) => {
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
 **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;. | 
 **instanceId** | **String**| The instance id to deprovision. | 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **acceptsIncomplete** | **Boolean**| See CreateServiceInstanceRequest for details. | [optional] 
 **planId** | **String**| The plan id of the service instance. | [optional] 
 **serviceId** | **String**| The service id of the service instance. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1alpha1DeleteServiceInstanceResponse**](GoogleCloudServicebrokerV1alpha1DeleteServiceInstanceResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesGet

> GoogleCloudServicebrokerV1alpha1ServiceInstance servicebrokerProjectsBrokersV2ServiceInstancesGet(name, opts)



Gets the given service instance from the system. This API is an extension and not part of the OSB spec. Hence the path is a standard Google API URL.

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

let apiInstance = new ServiceBroker.ProjectsApi();
let name = "name_example"; // String | The resource name of the instance to return.
let opts = {
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example" // String | OAuth access token.
};
apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesGet(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource name of the instance to return. | 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1alpha1ServiceInstance**](GoogleCloudServicebrokerV1alpha1ServiceInstance.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesGetLastOperation

> GoogleCloudServicebrokerV1alpha1Operation servicebrokerProjectsBrokersV2ServiceInstancesGetLastOperation(parent, instanceId, opts)



Returns the state of the last operation for the service instance. Only last (or current) operation can be polled.

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

let apiInstance = new ServiceBroker.ProjectsApi();
let parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
let instanceId = "instanceId_example"; // String | The instance id for which to return the last operation status.
let opts = {
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'operation': "operation_example", // String | If `operation` was returned during mutation operation, this field must be populated with the provided value.
  'planId': "planId_example", // String | Plan id.
  'serviceId': "serviceId_example" // String | Service id.
};
apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesGetLastOperation(parent, instanceId, opts, (error, data, response) => {
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
 **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;. | 
 **instanceId** | **String**| The instance id for which to return the last operation status. | 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **operation** | **String**| If &#x60;operation&#x60; was returned during mutation operation, this field must be populated with the provided value. | [optional] 
 **planId** | **String**| Plan id. | [optional] 
 **serviceId** | **String**| Service id. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1alpha1Operation**](GoogleCloudServicebrokerV1alpha1Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesPatch

> GoogleCloudServicebrokerV1alpha1UpdateServiceInstanceResponse servicebrokerProjectsBrokersV2ServiceInstancesPatch(parent, instanceId, opts)



Updates an existing service instance. See CreateServiceInstance for possible response codes.

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

let apiInstance = new ServiceBroker.ProjectsApi();
let parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
let instanceId = "instanceId_example"; // String | The id of the service instance. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required.
let opts = {
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'acceptsIncomplete': true, // Boolean | See CreateServiceInstanceRequest for details.
  'googleCloudServicebrokerV1alpha1ServiceInstance': new ServiceBroker.GoogleCloudServicebrokerV1alpha1ServiceInstance() // GoogleCloudServicebrokerV1alpha1ServiceInstance | 
};
apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesPatch(parent, instanceId, opts, (error, data, response) => {
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
 **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;. | 
 **instanceId** | **String**| The id of the service instance. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required. | 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **acceptsIncomplete** | **Boolean**| See CreateServiceInstanceRequest for details. | [optional] 
 **googleCloudServicebrokerV1alpha1ServiceInstance** | [**GoogleCloudServicebrokerV1alpha1ServiceInstance**](GoogleCloudServicebrokerV1alpha1ServiceInstance.md)|  | [optional] 

### Return type

[**GoogleCloudServicebrokerV1alpha1UpdateServiceInstanceResponse**](GoogleCloudServicebrokerV1alpha1UpdateServiceInstanceResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate

> GoogleCloudServicebrokerV1alpha1CreateBindingResponse servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate(parent, instanceId, bindingId, opts)



CreateBinding generates a service binding to an existing service instance. See ProviServiceInstance for async operation details.

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

let apiInstance = new ServiceBroker.ProjectsApi();
let parent = "parent_example"; // String | The GCP container. Must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
let instanceId = "instanceId_example"; // String | The service instance to which to bind.
let bindingId = "bindingId_example"; // String | The id of the binding. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required.
let opts = {
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'acceptsIncomplete': true, // Boolean | See CreateServiceInstanceRequest for details.
  'googleCloudServicebrokerV1alpha1Binding': new ServiceBroker.GoogleCloudServicebrokerV1alpha1Binding() // GoogleCloudServicebrokerV1alpha1Binding | 
};
apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate(parent, instanceId, bindingId, opts, (error, data, response) => {
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
 **parent** | **String**| The GCP container. Must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;. | 
 **instanceId** | **String**| The service instance to which to bind. | 
 **bindingId** | **String**| The id of the binding. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required. | 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **acceptsIncomplete** | **Boolean**| See CreateServiceInstanceRequest for details. | [optional] 
 **googleCloudServicebrokerV1alpha1Binding** | [**GoogleCloudServicebrokerV1alpha1Binding**](GoogleCloudServicebrokerV1alpha1Binding.md)|  | [optional] 

### Return type

[**GoogleCloudServicebrokerV1alpha1CreateBindingResponse**](GoogleCloudServicebrokerV1alpha1CreateBindingResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet

> GoogleCloudServicebrokerV1alpha1GetBindingResponse servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet(parent, instanceId, bindingId, opts)



GetBinding returns the binding information.

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

let apiInstance = new ServiceBroker.ProjectsApi();
let parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
let instanceId = "instanceId_example"; // String | Instance id to which the binding is bound.
let bindingId = "bindingId_example"; // String | The binding id.
let opts = {
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'planId': "planId_example", // String | Plan id.
  'serviceId': "serviceId_example" // String | Service id.
};
apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet(parent, instanceId, bindingId, opts, (error, data, response) => {
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
 **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;. | 
 **instanceId** | **String**| Instance id to which the binding is bound. | 
 **bindingId** | **String**| The binding id. | 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **planId** | **String**| Plan id. | [optional] 
 **serviceId** | **String**| Service id. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1alpha1GetBindingResponse**](GoogleCloudServicebrokerV1alpha1GetBindingResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation

> GoogleCloudServicebrokerV1alpha1Operation servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation(parent, instanceId, bindingId, opts)



Returns the state of the last operation for the binding. Only last (or current) operation can be polled.

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

let apiInstance = new ServiceBroker.ProjectsApi();
let parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]`.
let instanceId = "instanceId_example"; // String | The instance id that the binding is bound to.
let bindingId = "bindingId_example"; // String | The binding id for which to return the last operation
let opts = {
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'operation': "operation_example", // String | If `operation` was returned during mutation operation, this field must be populated with the provided value.
  'planId': "planId_example", // String | Plan id.
  'serviceId': "serviceId_example" // String | Service id.
};
apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation(parent, instanceId, bindingId, opts, (error, data, response) => {
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
 **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]&#x60;. | 
 **instanceId** | **String**| The instance id that the binding is bound to. | 
 **bindingId** | **String**| The binding id for which to return the last operation | 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **operation** | **String**| If &#x60;operation&#x60; was returned during mutation operation, this field must be populated with the provided value. | [optional] 
 **planId** | **String**| Plan id. | [optional] 
 **serviceId** | **String**| Service id. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1alpha1Operation**](GoogleCloudServicebrokerV1alpha1Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

