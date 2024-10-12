# ServiceDirectoryApi.ProjectsApi

All URIs are relative to *https://servicedirectory.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**servicedirectoryProjectsLocationsList**](ProjectsApi.md#servicedirectoryProjectsLocationsList) | **GET** /v1beta1/{name}/locations | 
[**servicedirectoryProjectsLocationsNamespacesCreate**](ProjectsApi.md#servicedirectoryProjectsLocationsNamespacesCreate) | **POST** /v1beta1/{parent}/namespaces | 
[**servicedirectoryProjectsLocationsNamespacesList**](ProjectsApi.md#servicedirectoryProjectsLocationsNamespacesList) | **GET** /v1beta1/{parent}/namespaces | 
[**servicedirectoryProjectsLocationsNamespacesServicesCreate**](ProjectsApi.md#servicedirectoryProjectsLocationsNamespacesServicesCreate) | **POST** /v1beta1/{parent}/services | 
[**servicedirectoryProjectsLocationsNamespacesServicesEndpointsCreate**](ProjectsApi.md#servicedirectoryProjectsLocationsNamespacesServicesEndpointsCreate) | **POST** /v1beta1/{parent}/endpoints | 
[**servicedirectoryProjectsLocationsNamespacesServicesEndpointsDelete**](ProjectsApi.md#servicedirectoryProjectsLocationsNamespacesServicesEndpointsDelete) | **DELETE** /v1beta1/{name} | 
[**servicedirectoryProjectsLocationsNamespacesServicesEndpointsGet**](ProjectsApi.md#servicedirectoryProjectsLocationsNamespacesServicesEndpointsGet) | **GET** /v1beta1/{name} | 
[**servicedirectoryProjectsLocationsNamespacesServicesEndpointsList**](ProjectsApi.md#servicedirectoryProjectsLocationsNamespacesServicesEndpointsList) | **GET** /v1beta1/{parent}/endpoints | 
[**servicedirectoryProjectsLocationsNamespacesServicesEndpointsPatch**](ProjectsApi.md#servicedirectoryProjectsLocationsNamespacesServicesEndpointsPatch) | **PATCH** /v1beta1/{name} | 
[**servicedirectoryProjectsLocationsNamespacesServicesList**](ProjectsApi.md#servicedirectoryProjectsLocationsNamespacesServicesList) | **GET** /v1beta1/{parent}/services | 
[**servicedirectoryProjectsLocationsNamespacesServicesResolve**](ProjectsApi.md#servicedirectoryProjectsLocationsNamespacesServicesResolve) | **POST** /v1beta1/{name}:resolve | 
[**servicedirectoryProjectsLocationsNamespacesWorkloadsGetIamPolicy**](ProjectsApi.md#servicedirectoryProjectsLocationsNamespacesWorkloadsGetIamPolicy) | **POST** /v1beta1/{resource}:getIamPolicy | 
[**servicedirectoryProjectsLocationsNamespacesWorkloadsSetIamPolicy**](ProjectsApi.md#servicedirectoryProjectsLocationsNamespacesWorkloadsSetIamPolicy) | **POST** /v1beta1/{resource}:setIamPolicy | 
[**servicedirectoryProjectsLocationsNamespacesWorkloadsTestIamPermissions**](ProjectsApi.md#servicedirectoryProjectsLocationsNamespacesWorkloadsTestIamPermissions) | **POST** /v1beta1/{resource}:testIamPermissions | 



## servicedirectoryProjectsLocationsList

> ListLocationsResponse servicedirectoryProjectsLocationsList(name, opts)



Lists information about the supported locations for this service.

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let name = "name_example"; // String | The resource that owns the locations collection, if applicable.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | A filter to narrow down results to a preferred subset. The filtering language accepts strings like `\"displayName=tokyo\"`, and is documented in more detail in [AIP-160](https://google.aip.dev/160).
  'pageSize': 56, // Number | The maximum number of results to return. If not set, the service selects a default.
  'pageToken': "pageToken_example" // String | A page token received from the `next_page_token` field in the response. Send that page token to receive the subsequent page.
};
apiInstance.servicedirectoryProjectsLocationsList(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource that owns the locations collection, if applicable. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| A filter to narrow down results to a preferred subset. The filtering language accepts strings like &#x60;\&quot;displayName&#x3D;tokyo\&quot;&#x60;, and is documented in more detail in [AIP-160](https://google.aip.dev/160). | [optional] 
 **pageSize** | **Number**| The maximum number of results to return. If not set, the service selects a default. | [optional] 
 **pageToken** | **String**| A page token received from the &#x60;next_page_token&#x60; field in the response. Send that page token to receive the subsequent page. | [optional] 

### Return type

[**ListLocationsResponse**](ListLocationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicedirectoryProjectsLocationsNamespacesCreate

> Namespace servicedirectoryProjectsLocationsNamespacesCreate(parent, opts)



Creates a namespace, and returns the new namespace.

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the project and location the namespace will be created in.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'namespaceId': "namespaceId_example", // String | Required. The Resource ID must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
  'namespace': new ServiceDirectoryApi.Namespace() // Namespace | 
};
apiInstance.servicedirectoryProjectsLocationsNamespacesCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the project and location the namespace will be created in. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **namespaceId** | **String**| Required. The Resource ID must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression &#x60;[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?&#x60; which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. | [optional] 
 **namespace** | [**Namespace**](Namespace.md)|  | [optional] 

### Return type

[**Namespace**](Namespace.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicedirectoryProjectsLocationsNamespacesList

> ListNamespacesResponse servicedirectoryProjectsLocationsNamespacesList(parent, opts)



Lists all namespaces.

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the project and location whose namespaces you'd like to list.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Optional. The filter to list results by. General `filter` string syntax: ` ()` * `` can be `name`, `labels.` for map field, or `attributes.` for attributes field * `` can be `<`, `>`, `<=`, `>=`, `!=`, `=`, `:`. Of which `:` means `HAS`, and is roughly the same as `=` * `` must be the same data type as field * `` can be `AND`, `OR`, `NOT` Examples of valid filters: * `labels.owner` returns namespaces that have a label with the key `owner`, this is the same as `labels:owner` * `labels.owner=sd` returns namespaces that have key/value `owner=sd` * `name>projects/my-project/locations/us-east1/namespaces/namespace-c` returns namespaces that have name that is alphabetically later than the string, so \"namespace-e\" is returned but \"namespace-a\" is not * `labels.owner!=sd AND labels.foo=bar` returns namespaces that have `owner` in label key but value is not `sd` AND have key/value `foo=bar` * `doesnotexist.foo=bar` returns an empty list. Note that namespace doesn't have a field called \"doesnotexist\". Since the filter does not match any namespaces, it returns no results * `attributes.managed_registration=true` returns namespaces that are managed by a GCP product or service For more information about filtering, see [API Filtering](https://aip.dev/160).
  'orderBy': "orderBy_example", // String | Optional. The order to list results by. General `order_by` string syntax: ` () (,)` * `` allows value: `name` * `` ascending or descending order by ``. If this is left blank, `asc` is used Note that an empty `order_by` string results in default order, which is order by `name` in ascending order.
  'pageSize': 56, // Number | Optional. The maximum number of items to return.
  'pageToken': "pageToken_example" // String | Optional. The next_page_token value returned from a previous List request, if any.
};
apiInstance.servicedirectoryProjectsLocationsNamespacesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the project and location whose namespaces you&#39;d like to list. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Optional. The filter to list results by. General &#x60;filter&#x60; string syntax: &#x60; ()&#x60; * &#x60;&#x60; can be &#x60;name&#x60;, &#x60;labels.&#x60; for map field, or &#x60;attributes.&#x60; for attributes field * &#x60;&#x60; can be &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&#x3D;&#x60;, &#x60;:&#x60;. Of which &#x60;:&#x60; means &#x60;HAS&#x60;, and is roughly the same as &#x60;&#x3D;&#x60; * &#x60;&#x60; must be the same data type as field * &#x60;&#x60; can be &#x60;AND&#x60;, &#x60;OR&#x60;, &#x60;NOT&#x60; Examples of valid filters: * &#x60;labels.owner&#x60; returns namespaces that have a label with the key &#x60;owner&#x60;, this is the same as &#x60;labels:owner&#x60; * &#x60;labels.owner&#x3D;sd&#x60; returns namespaces that have key/value &#x60;owner&#x3D;sd&#x60; * &#x60;name&gt;projects/my-project/locations/us-east1/namespaces/namespace-c&#x60; returns namespaces that have name that is alphabetically later than the string, so \&quot;namespace-e\&quot; is returned but \&quot;namespace-a\&quot; is not * &#x60;labels.owner!&#x3D;sd AND labels.foo&#x3D;bar&#x60; returns namespaces that have &#x60;owner&#x60; in label key but value is not &#x60;sd&#x60; AND have key/value &#x60;foo&#x3D;bar&#x60; * &#x60;doesnotexist.foo&#x3D;bar&#x60; returns an empty list. Note that namespace doesn&#39;t have a field called \&quot;doesnotexist\&quot;. Since the filter does not match any namespaces, it returns no results * &#x60;attributes.managed_registration&#x3D;true&#x60; returns namespaces that are managed by a GCP product or service For more information about filtering, see [API Filtering](https://aip.dev/160). | [optional] 
 **orderBy** | **String**| Optional. The order to list results by. General &#x60;order_by&#x60; string syntax: &#x60; () (,)&#x60; * &#x60;&#x60; allows value: &#x60;name&#x60; * &#x60;&#x60; ascending or descending order by &#x60;&#x60;. If this is left blank, &#x60;asc&#x60; is used Note that an empty &#x60;order_by&#x60; string results in default order, which is order by &#x60;name&#x60; in ascending order. | [optional] 
 **pageSize** | **Number**| Optional. The maximum number of items to return. | [optional] 
 **pageToken** | **String**| Optional. The next_page_token value returned from a previous List request, if any. | [optional] 

### Return type

[**ListNamespacesResponse**](ListNamespacesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicedirectoryProjectsLocationsNamespacesServicesCreate

> Service servicedirectoryProjectsLocationsNamespacesServicesCreate(parent, opts)



Creates a service, and returns the new service.

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the namespace this service will belong to.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'serviceId': "serviceId_example", // String | Required. The Resource ID must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
  'service': new ServiceDirectoryApi.Service() // Service | 
};
apiInstance.servicedirectoryProjectsLocationsNamespacesServicesCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the namespace this service will belong to. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **serviceId** | **String**| Required. The Resource ID must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression &#x60;[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?&#x60; which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. | [optional] 
 **service** | [**Service**](Service.md)|  | [optional] 

### Return type

[**Service**](Service.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicedirectoryProjectsLocationsNamespacesServicesEndpointsCreate

> Endpoint servicedirectoryProjectsLocationsNamespacesServicesEndpointsCreate(parent, opts)



Creates an endpoint, and returns the new endpoint.

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the service that this endpoint provides.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'endpointId': "endpointId_example", // String | Required. The Resource ID must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
  'endpoint': new ServiceDirectoryApi.Endpoint() // Endpoint | 
};
apiInstance.servicedirectoryProjectsLocationsNamespacesServicesEndpointsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the service that this endpoint provides. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **endpointId** | **String**| Required. The Resource ID must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression &#x60;[a-z](?:[-a-z0-9]{0,61}[a-z0-9])?&#x60; which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. | [optional] 
 **endpoint** | [**Endpoint**](Endpoint.md)|  | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicedirectoryProjectsLocationsNamespacesServicesEndpointsDelete

> Object servicedirectoryProjectsLocationsNamespacesServicesEndpointsDelete(name, opts)



Deletes an endpoint.

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the endpoint to delete.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.servicedirectoryProjectsLocationsNamespacesServicesEndpointsDelete(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The name of the endpoint to delete. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicedirectoryProjectsLocationsNamespacesServicesEndpointsGet

> Endpoint servicedirectoryProjectsLocationsNamespacesServicesEndpointsGet(name, opts)



Gets an endpoint.

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the endpoint to get.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.servicedirectoryProjectsLocationsNamespacesServicesEndpointsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The name of the endpoint to get. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicedirectoryProjectsLocationsNamespacesServicesEndpointsList

> ListEndpointsResponse servicedirectoryProjectsLocationsNamespacesServicesEndpointsList(parent, opts)



Lists all endpoints.

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the service whose endpoints you'd like to list.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Optional. The filter to list results by. General `filter` string syntax: ` ()` * `` can be `name`, `address`, `port`, `metadata.` for map field, or `attributes.` for attributes field * `` can be `<`, `>`, `<=`, `>=`, `!=`, `=`, `:`. Of which `:` means `HAS`, and is roughly the same as `=` * `` must be the same data type as field * `` can be `AND`, `OR`, `NOT` Examples of valid filters: * `metadata.owner` returns endpoints that have a metadata with the key `owner`, this is the same as `metadata:owner` * `metadata.protocol=gRPC` returns endpoints that have key/value `protocol=gRPC` * `address=192.108.1.105` returns endpoints that have this address * `port>8080` returns endpoints that have port number larger than 8080 * `name>projects/my-project/locations/us-east1/namespaces/my-namespace/services/my-service/endpoints/endpoint-c` returns endpoints that have name that is alphabetically later than the string, so \"endpoint-e\" is returned but \"endpoint-a\" is not * `metadata.owner!=sd AND metadata.foo=bar` returns endpoints that have `owner` in metadata key but value is not `sd` AND have key/value `foo=bar` * `doesnotexist.foo=bar` returns an empty list. Note that endpoint doesn't have a field called \"doesnotexist\". Since the filter does not match any endpoints, it returns no results * `attributes.kubernetes_resource_type=KUBERNETES_RESOURCE_TYPE_CLUSTER_ IP` returns endpoints with the corresponding kubernetes_resource_type For more information about filtering, see [API Filtering](https://aip.dev/160).
  'orderBy': "orderBy_example", // String | Optional. The order to list results by. General `order_by` string syntax: ` () (,)` * `` allows values: `name`, `address`, `port` * `` ascending or descending order by ``. If this is left blank, `asc` is used Note that an empty `order_by` string results in default order, which is order by `name` in ascending order.
  'pageSize': 56, // Number | Optional. The maximum number of items to return.
  'pageToken': "pageToken_example" // String | Optional. The next_page_token value returned from a previous List request, if any.
};
apiInstance.servicedirectoryProjectsLocationsNamespacesServicesEndpointsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the service whose endpoints you&#39;d like to list. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Optional. The filter to list results by. General &#x60;filter&#x60; string syntax: &#x60; ()&#x60; * &#x60;&#x60; can be &#x60;name&#x60;, &#x60;address&#x60;, &#x60;port&#x60;, &#x60;metadata.&#x60; for map field, or &#x60;attributes.&#x60; for attributes field * &#x60;&#x60; can be &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&#x3D;&#x60;, &#x60;:&#x60;. Of which &#x60;:&#x60; means &#x60;HAS&#x60;, and is roughly the same as &#x60;&#x3D;&#x60; * &#x60;&#x60; must be the same data type as field * &#x60;&#x60; can be &#x60;AND&#x60;, &#x60;OR&#x60;, &#x60;NOT&#x60; Examples of valid filters: * &#x60;metadata.owner&#x60; returns endpoints that have a metadata with the key &#x60;owner&#x60;, this is the same as &#x60;metadata:owner&#x60; * &#x60;metadata.protocol&#x3D;gRPC&#x60; returns endpoints that have key/value &#x60;protocol&#x3D;gRPC&#x60; * &#x60;address&#x3D;192.108.1.105&#x60; returns endpoints that have this address * &#x60;port&gt;8080&#x60; returns endpoints that have port number larger than 8080 * &#x60;name&gt;projects/my-project/locations/us-east1/namespaces/my-namespace/services/my-service/endpoints/endpoint-c&#x60; returns endpoints that have name that is alphabetically later than the string, so \&quot;endpoint-e\&quot; is returned but \&quot;endpoint-a\&quot; is not * &#x60;metadata.owner!&#x3D;sd AND metadata.foo&#x3D;bar&#x60; returns endpoints that have &#x60;owner&#x60; in metadata key but value is not &#x60;sd&#x60; AND have key/value &#x60;foo&#x3D;bar&#x60; * &#x60;doesnotexist.foo&#x3D;bar&#x60; returns an empty list. Note that endpoint doesn&#39;t have a field called \&quot;doesnotexist\&quot;. Since the filter does not match any endpoints, it returns no results * &#x60;attributes.kubernetes_resource_type&#x3D;KUBERNETES_RESOURCE_TYPE_CLUSTER_ IP&#x60; returns endpoints with the corresponding kubernetes_resource_type For more information about filtering, see [API Filtering](https://aip.dev/160). | [optional] 
 **orderBy** | **String**| Optional. The order to list results by. General &#x60;order_by&#x60; string syntax: &#x60; () (,)&#x60; * &#x60;&#x60; allows values: &#x60;name&#x60;, &#x60;address&#x60;, &#x60;port&#x60; * &#x60;&#x60; ascending or descending order by &#x60;&#x60;. If this is left blank, &#x60;asc&#x60; is used Note that an empty &#x60;order_by&#x60; string results in default order, which is order by &#x60;name&#x60; in ascending order. | [optional] 
 **pageSize** | **Number**| Optional. The maximum number of items to return. | [optional] 
 **pageToken** | **String**| Optional. The next_page_token value returned from a previous List request, if any. | [optional] 

### Return type

[**ListEndpointsResponse**](ListEndpointsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicedirectoryProjectsLocationsNamespacesServicesEndpointsPatch

> Endpoint servicedirectoryProjectsLocationsNamespacesServicesEndpointsPatch(name, opts)



Updates an endpoint.

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let name = "name_example"; // String | Immutable. The resource name for the endpoint in the format `projects/_*_/locations/_*_/namespaces/_*_/services/_*_/endpoints/_*`.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'updateMask': "updateMask_example", // String | Required. List of fields to be updated in this request.
  'endpoint': new ServiceDirectoryApi.Endpoint() // Endpoint | 
};
apiInstance.servicedirectoryProjectsLocationsNamespacesServicesEndpointsPatch(name, opts, (error, data, response) => {
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
 **name** | **String**| Immutable. The resource name for the endpoint in the format &#x60;projects/_*_/locations/_*_/namespaces/_*_/services/_*_/endpoints/_*&#x60;. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **updateMask** | **String**| Required. List of fields to be updated in this request. | [optional] 
 **endpoint** | [**Endpoint**](Endpoint.md)|  | [optional] 

### Return type

[**Endpoint**](Endpoint.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicedirectoryProjectsLocationsNamespacesServicesList

> ListServicesResponse servicedirectoryProjectsLocationsNamespacesServicesList(parent, opts)



Lists all services belonging to a namespace.

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The resource name of the namespace whose services you'd like to list.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | Optional. The filter to list results by. General `filter` string syntax: ` ()` * `` can be `name` or `metadata.` for map field * `` can be `<`, `>`, `<=`, `>=`, `!=`, `=`, `:`. Of which `:` means `HAS`, and is roughly the same as `=` * `` must be the same data type as field * `` can be `AND`, `OR`, `NOT` Examples of valid filters: * `metadata.owner` returns services that have a metadata with the key `owner`, this is the same as `metadata:owner` * `metadata.protocol=gRPC` returns services that have key/value `protocol=gRPC` * `name>projects/my-project/locations/us-east1/namespaces/my-namespace/services/service-c` returns services that have name that is alphabetically later than the string, so \"service-e\" is returned but \"service-a\" is not * `metadata.owner!=sd AND metadata.foo=bar` returns services that have `owner` in metadata key but value is not `sd` AND have key/value `foo=bar` * `doesnotexist.foo=bar` returns an empty list. Note that service doesn't have a field called \"doesnotexist\". Since the filter does not match any services, it returns no results * `attributes.managed_registration=true` returns services that are managed by a GCP product or service For more information about filtering, see [API Filtering](https://aip.dev/160).
  'orderBy': "orderBy_example", // String | Optional. The order to list results by. General `order_by` string syntax: ` () (,)` * `` allows value: `name` * `` ascending or descending order by ``. If this is left blank, `asc` is used Note that an empty `order_by` string results in default order, which is order by `name` in ascending order.
  'pageSize': 56, // Number | Optional. The maximum number of items to return.
  'pageToken': "pageToken_example" // String | Optional. The next_page_token value returned from a previous List request, if any.
};
apiInstance.servicedirectoryProjectsLocationsNamespacesServicesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The resource name of the namespace whose services you&#39;d like to list. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| Optional. The filter to list results by. General &#x60;filter&#x60; string syntax: &#x60; ()&#x60; * &#x60;&#x60; can be &#x60;name&#x60; or &#x60;metadata.&#x60; for map field * &#x60;&#x60; can be &#x60;&lt;&#x60;, &#x60;&gt;&#x60;, &#x60;&lt;&#x3D;&#x60;, &#x60;&gt;&#x3D;&#x60;, &#x60;!&#x3D;&#x60;, &#x60;&#x3D;&#x60;, &#x60;:&#x60;. Of which &#x60;:&#x60; means &#x60;HAS&#x60;, and is roughly the same as &#x60;&#x3D;&#x60; * &#x60;&#x60; must be the same data type as field * &#x60;&#x60; can be &#x60;AND&#x60;, &#x60;OR&#x60;, &#x60;NOT&#x60; Examples of valid filters: * &#x60;metadata.owner&#x60; returns services that have a metadata with the key &#x60;owner&#x60;, this is the same as &#x60;metadata:owner&#x60; * &#x60;metadata.protocol&#x3D;gRPC&#x60; returns services that have key/value &#x60;protocol&#x3D;gRPC&#x60; * &#x60;name&gt;projects/my-project/locations/us-east1/namespaces/my-namespace/services/service-c&#x60; returns services that have name that is alphabetically later than the string, so \&quot;service-e\&quot; is returned but \&quot;service-a\&quot; is not * &#x60;metadata.owner!&#x3D;sd AND metadata.foo&#x3D;bar&#x60; returns services that have &#x60;owner&#x60; in metadata key but value is not &#x60;sd&#x60; AND have key/value &#x60;foo&#x3D;bar&#x60; * &#x60;doesnotexist.foo&#x3D;bar&#x60; returns an empty list. Note that service doesn&#39;t have a field called \&quot;doesnotexist\&quot;. Since the filter does not match any services, it returns no results * &#x60;attributes.managed_registration&#x3D;true&#x60; returns services that are managed by a GCP product or service For more information about filtering, see [API Filtering](https://aip.dev/160). | [optional] 
 **orderBy** | **String**| Optional. The order to list results by. General &#x60;order_by&#x60; string syntax: &#x60; () (,)&#x60; * &#x60;&#x60; allows value: &#x60;name&#x60; * &#x60;&#x60; ascending or descending order by &#x60;&#x60;. If this is left blank, &#x60;asc&#x60; is used Note that an empty &#x60;order_by&#x60; string results in default order, which is order by &#x60;name&#x60; in ascending order. | [optional] 
 **pageSize** | **Number**| Optional. The maximum number of items to return. | [optional] 
 **pageToken** | **String**| Optional. The next_page_token value returned from a previous List request, if any. | [optional] 

### Return type

[**ListServicesResponse**](ListServicesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicedirectoryProjectsLocationsNamespacesServicesResolve

> ResolveServiceResponse servicedirectoryProjectsLocationsNamespacesServicesResolve(name, opts)



Returns a service and its associated endpoints. Resolving a service is not considered an active developer method.

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let name = "name_example"; // String | Required. The name of the service to resolve.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'resolveServiceRequest': new ServiceDirectoryApi.ResolveServiceRequest() // ResolveServiceRequest | 
};
apiInstance.servicedirectoryProjectsLocationsNamespacesServicesResolve(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The name of the service to resolve. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **resolveServiceRequest** | [**ResolveServiceRequest**](ResolveServiceRequest.md)|  | [optional] 

### Return type

[**ResolveServiceResponse**](ResolveServiceResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicedirectoryProjectsLocationsNamespacesWorkloadsGetIamPolicy

> Policy servicedirectoryProjectsLocationsNamespacesWorkloadsGetIamPolicy(resource, opts)



Gets the IAM Policy for a resource

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let resource = "resource_example"; // String | REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'getIamPolicyRequest': new ServiceDirectoryApi.GetIamPolicyRequest() // GetIamPolicyRequest | 
};
apiInstance.servicedirectoryProjectsLocationsNamespacesWorkloadsGetIamPolicy(resource, opts, (error, data, response) => {
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
 **resource** | **String**| REQUIRED: The resource for which the policy is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **getIamPolicyRequest** | [**GetIamPolicyRequest**](GetIamPolicyRequest.md)|  | [optional] 

### Return type

[**Policy**](Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicedirectoryProjectsLocationsNamespacesWorkloadsSetIamPolicy

> Policy servicedirectoryProjectsLocationsNamespacesWorkloadsSetIamPolicy(resource, opts)



Sets the IAM Policy for a resource

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let resource = "resource_example"; // String | REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'setIamPolicyRequest': new ServiceDirectoryApi.SetIamPolicyRequest() // SetIamPolicyRequest | 
};
apiInstance.servicedirectoryProjectsLocationsNamespacesWorkloadsSetIamPolicy(resource, opts, (error, data, response) => {
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
 **resource** | **String**| REQUIRED: The resource for which the policy is being specified. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **setIamPolicyRequest** | [**SetIamPolicyRequest**](SetIamPolicyRequest.md)|  | [optional] 

### Return type

[**Policy**](Policy.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## servicedirectoryProjectsLocationsNamespacesWorkloadsTestIamPermissions

> TestIamPermissionsResponse servicedirectoryProjectsLocationsNamespacesWorkloadsTestIamPermissions(resource, opts)



Tests IAM permissions for a resource (namespace, service or service workload only).

### Example

```javascript
import ServiceDirectoryApi from 'service_directory_api';
let defaultClient = ServiceDirectoryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new ServiceDirectoryApi.ProjectsApi();
let resource = "resource_example"; // String | REQUIRED: The resource for which the policy detail is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'testIamPermissionsRequest': new ServiceDirectoryApi.TestIamPermissionsRequest() // TestIamPermissionsRequest | 
};
apiInstance.servicedirectoryProjectsLocationsNamespacesWorkloadsTestIamPermissions(resource, opts, (error, data, response) => {
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
 **resource** | **String**| REQUIRED: The resource for which the policy detail is being requested. See [Resource names](https://cloud.google.com/apis/design/resource_names) for the appropriate value for this field. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **testIamPermissionsRequest** | [**TestIamPermissionsRequest**](TestIamPermissionsRequest.md)|  | [optional] 

### Return type

[**TestIamPermissionsResponse**](TestIamPermissionsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

