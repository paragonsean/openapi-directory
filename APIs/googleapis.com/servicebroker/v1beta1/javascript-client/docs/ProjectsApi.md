# ServiceBroker.ProjectsApi

All URIs are relative to *https://servicebroker.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicebrokerProjectsBrokersCreate**](ProjectsApi.md#servicebrokerProjectsBrokersCreate) | **POST** /v1beta1/{parent}/brokers | 
[**servicebrokerProjectsBrokersInstancesBindingsList**](ProjectsApi.md#servicebrokerProjectsBrokersInstancesBindingsList) | **GET** /v1beta1/{parent}/bindings | 
[**servicebrokerProjectsBrokersInstancesList**](ProjectsApi.md#servicebrokerProjectsBrokersInstancesList) | **GET** /v1beta1/{parent}/instances | 
[**servicebrokerProjectsBrokersList**](ProjectsApi.md#servicebrokerProjectsBrokersList) | **GET** /v1beta1/{parent}/brokers | 
[**servicebrokerProjectsBrokersV2CatalogList**](ProjectsApi.md#servicebrokerProjectsBrokersV2CatalogList) | **GET** /v1beta1/{parent}/v2/catalog | 
[**servicebrokerProjectsBrokersV2ServiceInstancesCreate**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesCreate) | **PUT** /v1beta1/{parent}/v2/service_instances/{instance_id} | 
[**servicebrokerProjectsBrokersV2ServiceInstancesPatch**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesPatch) | **PATCH** /v1beta1/{name} | 
[**servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate) | **PUT** /v1beta1/{parent}/service_bindings/{binding_id} | 
[**servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsDelete**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsDelete) | **DELETE** /v1beta1/{name} | 
[**servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet) | **GET** /v1beta1/{name} | 
[**servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation**](ProjectsApi.md#servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation) | **GET** /v1beta1/{name}/last_operation | 



## servicebrokerProjectsBrokersCreate

> GoogleCloudServicebrokerV1beta1Broker servicebrokerProjectsBrokersCreate(parent, opts)



CreateBroker creates a Broker.

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
let parent = "parent_example"; // String | The project in which to create broker.
let opts = {
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'googleCloudServicebrokerV1beta1Broker': new ServiceBroker.GoogleCloudServicebrokerV1beta1Broker() // GoogleCloudServicebrokerV1beta1Broker | 
};
apiInstance.servicebrokerProjectsBrokersCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The project in which to create broker. | 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **accessToken** | **String**| OAuth access token. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **googleCloudServicebrokerV1beta1Broker** | [**GoogleCloudServicebrokerV1beta1Broker**](GoogleCloudServicebrokerV1beta1Broker.md)|  | [optional] 

### Return type

[**GoogleCloudServicebrokerV1beta1Broker**](GoogleCloudServicebrokerV1beta1Broker.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## servicebrokerProjectsBrokersInstancesBindingsList

> GoogleCloudServicebrokerV1beta1ListBindingsResponse servicebrokerProjectsBrokersInstancesBindingsList(parent, opts)



Lists all the bindings in the instance.

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
let parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]/` + `v2/service_instances/[INSTANCE_ID]` or `projects/[PROJECT_ID]/brokers/[BROKER_ID]/instances/[INSTANCE_ID]`.
let opts = {
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'pageSize': 56, // Number | Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. Acceptable values are 0 to 200, inclusive. (Default: 100)
  'pageToken': "pageToken_example" // String | Specifies a page token to use. Set `pageToken` to a `nextPageToken` returned by a previous list request to get the next page of results.
};
apiInstance.servicebrokerProjectsBrokersInstancesBindingsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/&#x60; + &#x60;v2/service_instances/[INSTANCE_ID]&#x60; or &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/instances/[INSTANCE_ID]&#x60;. | 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **accessToken** | **String**| OAuth access token. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **pageSize** | **Number**| Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. Acceptable values are 0 to 200, inclusive. (Default: 100) | [optional] 
 **pageToken** | **String**| Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1beta1ListBindingsResponse**](GoogleCloudServicebrokerV1beta1ListBindingsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerProjectsBrokersInstancesList

> GoogleCloudServicebrokerV1beta1ListServiceInstancesResponse servicebrokerProjectsBrokersInstancesList(parent, opts)



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
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'pageSize': 56, // Number | Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. Acceptable values are 0 to 200, inclusive. (Default: 100)
  'pageToken': "pageToken_example" // String | Specifies a page token to use. Set `pageToken` to a `nextPageToken` returned by a previous list request to get the next page of results.
};
apiInstance.servicebrokerProjectsBrokersInstancesList(parent, opts, (error, data, response) => {
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
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **accessToken** | **String**| OAuth access token. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **pageSize** | **Number**| Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. Acceptable values are 0 to 200, inclusive. (Default: 100) | [optional] 
 **pageToken** | **String**| Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1beta1ListServiceInstancesResponse**](GoogleCloudServicebrokerV1beta1ListServiceInstancesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerProjectsBrokersList

> GoogleCloudServicebrokerV1beta1ListBrokersResponse servicebrokerProjectsBrokersList(parent, opts)



ListBrokers lists brokers.

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
let parent = "parent_example"; // String | Parent must match `projects/[PROJECT_ID]/brokers`.
let opts = {
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'pageSize': 56, // Number | Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. Acceptable values are 0 to 200, inclusive. (Default: 100)
  'pageToken': "pageToken_example" // String | Specifies a page token to use. Set `pageToken` to a `nextPageToken` returned by a previous list request to get the next page of results.
};
apiInstance.servicebrokerProjectsBrokersList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Parent must match &#x60;projects/[PROJECT_ID]/brokers&#x60;. | 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **accessToken** | **String**| OAuth access token. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **pageSize** | **Number**| Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. Acceptable values are 0 to 200, inclusive. (Default: 100) | [optional] 
 **pageToken** | **String**| Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1beta1ListBrokersResponse**](GoogleCloudServicebrokerV1beta1ListBrokersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerProjectsBrokersV2CatalogList

> GoogleCloudServicebrokerV1beta1ListCatalogResponse servicebrokerProjectsBrokersV2CatalogList(parent, opts)



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
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
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
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **accessToken** | **String**| OAuth access token. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **pageSize** | **Number**| Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements. Optional. If unset or 0, all the results will be returned. | [optional] 
 **pageToken** | **String**| Specifies a page token to use. Set &#x60;pageToken&#x60; to a &#x60;nextPageToken&#x60; returned by a previous list request to get the next page of results. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1beta1ListCatalogResponse**](GoogleCloudServicebrokerV1beta1ListCatalogResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesCreate

> GoogleCloudServicebrokerV1beta1CreateServiceInstanceResponse servicebrokerProjectsBrokersV2ServiceInstancesCreate(parent, instanceId, opts)



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
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'acceptsIncomplete': true, // Boolean | Value indicating that API client supports asynchronous operations. If Broker cannot execute the request synchronously HTTP 422 code will be returned to HTTP clients along with FAILED_PRECONDITION error. If true and broker will execute request asynchronously 202 HTTP code will be returned. This broker always requires this to be true as all mutator operations are asynchronous.
  'googleCloudServicebrokerV1beta1ServiceInstance': new ServiceBroker.GoogleCloudServicebrokerV1beta1ServiceInstance() // GoogleCloudServicebrokerV1beta1ServiceInstance | 
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
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **accessToken** | **String**| OAuth access token. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **acceptsIncomplete** | **Boolean**| Value indicating that API client supports asynchronous operations. If Broker cannot execute the request synchronously HTTP 422 code will be returned to HTTP clients along with FAILED_PRECONDITION error. If true and broker will execute request asynchronously 202 HTTP code will be returned. This broker always requires this to be true as all mutator operations are asynchronous. | [optional] 
 **googleCloudServicebrokerV1beta1ServiceInstance** | [**GoogleCloudServicebrokerV1beta1ServiceInstance**](GoogleCloudServicebrokerV1beta1ServiceInstance.md)|  | [optional] 

### Return type

[**GoogleCloudServicebrokerV1beta1CreateServiceInstanceResponse**](GoogleCloudServicebrokerV1beta1CreateServiceInstanceResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesPatch

> GoogleCloudServicebrokerV1beta1UpdateServiceInstanceResponse servicebrokerProjectsBrokersV2ServiceInstancesPatch(name, opts)



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
let name = "name_example"; // String | Name must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]`.
let opts = {
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'acceptsIncomplete': true, // Boolean | See CreateServiceInstanceRequest for details.
  'googleCloudServicebrokerV1beta1ServiceInstance': new ServiceBroker.GoogleCloudServicebrokerV1beta1ServiceInstance() // GoogleCloudServicebrokerV1beta1ServiceInstance | 
};
apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesPatch(name, opts, (error, data, response) => {
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
 **name** | **String**| Name must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]&#x60;. | 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **accessToken** | **String**| OAuth access token. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **acceptsIncomplete** | **Boolean**| See CreateServiceInstanceRequest for details. | [optional] 
 **googleCloudServicebrokerV1beta1ServiceInstance** | [**GoogleCloudServicebrokerV1beta1ServiceInstance**](GoogleCloudServicebrokerV1beta1ServiceInstance.md)|  | [optional] 

### Return type

[**GoogleCloudServicebrokerV1beta1UpdateServiceInstanceResponse**](GoogleCloudServicebrokerV1beta1UpdateServiceInstanceResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate

> GoogleCloudServicebrokerV1beta1CreateBindingResponse servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate(parent, bindingId, opts)



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
let parent = "parent_example"; // String | The GCP container. Must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]`.
let bindingId = "bindingId_example"; // String | The id of the binding. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required.
let opts = {
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'acceptsIncomplete': true, // Boolean | See CreateServiceInstanceRequest for details.
  'googleCloudServicebrokerV1beta1Binding': new ServiceBroker.GoogleCloudServicebrokerV1beta1Binding() // GoogleCloudServicebrokerV1beta1Binding | 
};
apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreate(parent, bindingId, opts, (error, data, response) => {
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
 **parent** | **String**| The GCP container. Must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]&#x60;. | 
 **bindingId** | **String**| The id of the binding. Must be unique within GCP project. Maximum length is 64, GUID recommended. Required. | 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **accessToken** | **String**| OAuth access token. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **acceptsIncomplete** | **Boolean**| See CreateServiceInstanceRequest for details. | [optional] 
 **googleCloudServicebrokerV1beta1Binding** | [**GoogleCloudServicebrokerV1beta1Binding**](GoogleCloudServicebrokerV1beta1Binding.md)|  | [optional] 

### Return type

[**GoogleCloudServicebrokerV1beta1CreateBindingResponse**](GoogleCloudServicebrokerV1beta1CreateBindingResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsDelete

> GoogleCloudServicebrokerV1beta1DeleteBindingResponse servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsDelete(name, opts)



Unbinds from a service instance. For synchronous/asynchronous request details see CreateServiceInstance method. If binding does not exist HTTP 410 status will be returned.

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
let name = "name_example"; // String | Name must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]/` `v2/service_instances/[INSTANCE_ID]/service_bindings/[BINDING_ID]` or `projects/[PROJECT_ID]/brokers/[BROKER_ID]/` `/instances/[INSTANCE_ID]/bindings/[BINDING_ID]`.
let opts = {
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'acceptsIncomplete': true, // Boolean | See CreateServiceInstanceRequest for details.
  'planId': "planId_example", // String | The plan id of the service instance.
  'serviceId': "serviceId_example" // String | Additional query parameter hints. The service id of the service instance.
};
apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsDelete(name, opts, (error, data, response) => {
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
 **name** | **String**| Name must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/&#x60; &#x60;v2/service_instances/[INSTANCE_ID]/service_bindings/[BINDING_ID]&#x60; or &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/&#x60; &#x60;/instances/[INSTANCE_ID]/bindings/[BINDING_ID]&#x60;. | 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **accessToken** | **String**| OAuth access token. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **acceptsIncomplete** | **Boolean**| See CreateServiceInstanceRequest for details. | [optional] 
 **planId** | **String**| The plan id of the service instance. | [optional] 
 **serviceId** | **String**| Additional query parameter hints. The service id of the service instance. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1beta1DeleteBindingResponse**](GoogleCloudServicebrokerV1beta1DeleteBindingResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet

> GoogleCloudServicebrokerV1beta1GetBindingResponse servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet(name, opts)



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
let name = "name_example"; // String | Name must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]/service_bindings`.
let opts = {
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'planId': "planId_example", // String | Plan id.
  'serviceId': "serviceId_example" // String | Service id.
};
apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| Name must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]/service_bindings&#x60;. | 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **accessToken** | **String**| OAuth access token. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **planId** | **String**| Plan id. | [optional] 
 **serviceId** | **String**| Service id. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1beta1GetBindingResponse**](GoogleCloudServicebrokerV1beta1GetBindingResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*


## servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation

> GoogleCloudServicebrokerV1beta1Operation servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation(name, opts)



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
let name = "name_example"; // String | Name must match `projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]/service_binding/[BINDING_ID]`.
let opts = {
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'callback': "callback_example", // String | JSONP
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'xgafv': "xgafv_example", // String | V1 error format.
  'alt': "'json'", // String | Data format for response.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'operation': "operation_example", // String | If `operation` was returned during mutation operation, this field must be populated with the provided value.
  'planId': "planId_example", // String | Plan id.
  'serviceId': "serviceId_example" // String | Service id.
};
apiInstance.servicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperation(name, opts, (error, data, response) => {
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
 **name** | **String**| Name must match &#x60;projects/[PROJECT_ID]/brokers/[BROKER_ID]/v2/service_instances/[INSTANCE_ID]/service_binding/[BINDING_ID]&#x60;. | 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **xgafv** | **String**| V1 error format. | [optional] 
 **alt** | **String**| Data format for response. | [optional] [default to &#39;json&#39;]
 **accessToken** | **String**| OAuth access token. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] [default to true]
 **operation** | **String**| If &#x60;operation&#x60; was returned during mutation operation, this field must be populated with the provided value. | [optional] 
 **planId** | **String**| Plan id. | [optional] 
 **serviceId** | **String**| Service id. | [optional] 

### Return type

[**GoogleCloudServicebrokerV1beta1Operation**](GoogleCloudServicebrokerV1beta1Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

