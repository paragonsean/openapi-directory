# BigQueryDataTransferApi.ProjectsApi

All URIs are relative to *https://bigquerydatatransfer.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bigquerydatatransferProjectsLocationsDataSourcesCheckValidCreds**](ProjectsApi.md#bigquerydatatransferProjectsLocationsDataSourcesCheckValidCreds) | **POST** /v1/{name}:checkValidCreds | 
[**bigquerydatatransferProjectsLocationsDataSourcesList**](ProjectsApi.md#bigquerydatatransferProjectsLocationsDataSourcesList) | **GET** /v1/{parent}/dataSources | 
[**bigquerydatatransferProjectsLocationsEnrollDataSources**](ProjectsApi.md#bigquerydatatransferProjectsLocationsEnrollDataSources) | **POST** /v1/{name}:enrollDataSources | 
[**bigquerydatatransferProjectsLocationsList**](ProjectsApi.md#bigquerydatatransferProjectsLocationsList) | **GET** /v1/{name}/locations | 
[**bigquerydatatransferProjectsLocationsUnenrollDataSources**](ProjectsApi.md#bigquerydatatransferProjectsLocationsUnenrollDataSources) | **POST** /v1/{name}:unenrollDataSources | 
[**bigquerydatatransferProjectsTransferConfigsCreate**](ProjectsApi.md#bigquerydatatransferProjectsTransferConfigsCreate) | **POST** /v1/{parent}/transferConfigs | 
[**bigquerydatatransferProjectsTransferConfigsList**](ProjectsApi.md#bigquerydatatransferProjectsTransferConfigsList) | **GET** /v1/{parent}/transferConfigs | 
[**bigquerydatatransferProjectsTransferConfigsPatch**](ProjectsApi.md#bigquerydatatransferProjectsTransferConfigsPatch) | **PATCH** /v1/{name} | 
[**bigquerydatatransferProjectsTransferConfigsRunsDelete**](ProjectsApi.md#bigquerydatatransferProjectsTransferConfigsRunsDelete) | **DELETE** /v1/{name} | 
[**bigquerydatatransferProjectsTransferConfigsRunsGet**](ProjectsApi.md#bigquerydatatransferProjectsTransferConfigsRunsGet) | **GET** /v1/{name} | 
[**bigquerydatatransferProjectsTransferConfigsRunsList**](ProjectsApi.md#bigquerydatatransferProjectsTransferConfigsRunsList) | **GET** /v1/{parent}/runs | 
[**bigquerydatatransferProjectsTransferConfigsRunsTransferLogsList**](ProjectsApi.md#bigquerydatatransferProjectsTransferConfigsRunsTransferLogsList) | **GET** /v1/{parent}/transferLogs | 
[**bigquerydatatransferProjectsTransferConfigsScheduleRuns**](ProjectsApi.md#bigquerydatatransferProjectsTransferConfigsScheduleRuns) | **POST** /v1/{parent}:scheduleRuns | 
[**bigquerydatatransferProjectsTransferConfigsStartManualRuns**](ProjectsApi.md#bigquerydatatransferProjectsTransferConfigsStartManualRuns) | **POST** /v1/{parent}:startManualRuns | 



## bigquerydatatransferProjectsLocationsDataSourcesCheckValidCreds

> CheckValidCredsResponse bigquerydatatransferProjectsLocationsDataSourcesCheckValidCreds(name, opts)



Returns true if valid credentials exist for the given data source and requesting user.

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
let name = "name_example"; // String | Required. The data source in the form: `projects/{project_id}/dataSources/{data_source_id}` or `projects/{project_id}/locations/{location_id}/dataSources/{data_source_id}`.
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
  'body': {key: null} // Object | 
};
apiInstance.bigquerydatatransferProjectsLocationsDataSourcesCheckValidCreds(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The data source in the form: &#x60;projects/{project_id}/dataSources/{data_source_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/dataSources/{data_source_id}&#x60;. | 
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
 **body** | **Object**|  | [optional] 

### Return type

[**CheckValidCredsResponse**](CheckValidCredsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bigquerydatatransferProjectsLocationsDataSourcesList

> ListDataSourcesResponse bigquerydatatransferProjectsLocationsDataSourcesList(parent, opts)



Lists supported data sources and returns their settings.

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The BigQuery project id for which data sources should be returned. Must be in the form: `projects/{project_id}` or `projects/{project_id}/locations/{location_id}`
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
  'pageSize': 56, // Number | Page size. The default page size is the maximum value of 1000 results.
  'pageToken': "pageToken_example" // String | Pagination token, which can be used to request a specific page of `ListDataSourcesRequest` list results. For multiple-page results, `ListDataSourcesResponse` outputs a `next_page` token, which can be used as the `page_token` value to request the next page of list results.
};
apiInstance.bigquerydatatransferProjectsLocationsDataSourcesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The BigQuery project id for which data sources should be returned. Must be in the form: &#x60;projects/{project_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}&#x60; | 
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
 **pageSize** | **Number**| Page size. The default page size is the maximum value of 1000 results. | [optional] 
 **pageToken** | **String**| Pagination token, which can be used to request a specific page of &#x60;ListDataSourcesRequest&#x60; list results. For multiple-page results, &#x60;ListDataSourcesResponse&#x60; outputs a &#x60;next_page&#x60; token, which can be used as the &#x60;page_token&#x60; value to request the next page of list results. | [optional] 

### Return type

[**ListDataSourcesResponse**](ListDataSourcesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bigquerydatatransferProjectsLocationsEnrollDataSources

> Object bigquerydatatransferProjectsLocationsEnrollDataSources(name, opts)



Enroll data sources in a user project. This allows users to create transfer configurations for these data sources. They will also appear in the ListDataSources RPC and as such, will appear in the [BigQuery UI](https://console.cloud.google.com/bigquery), and the documents can be found in the public guide for [BigQuery Web UI](https://cloud.google.com/bigquery/bigquery-web-ui) and [Data Transfer Service](https://cloud.google.com/bigquery/docs/working-with-transfers).

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
let name = "name_example"; // String | The name of the project resource in the form: `projects/{project_id}`
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
  'enrollDataSourcesRequest': new BigQueryDataTransferApi.EnrollDataSourcesRequest() // EnrollDataSourcesRequest | 
};
apiInstance.bigquerydatatransferProjectsLocationsEnrollDataSources(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the project resource in the form: &#x60;projects/{project_id}&#x60; | 
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
 **enrollDataSourcesRequest** | [**EnrollDataSourcesRequest**](EnrollDataSourcesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bigquerydatatransferProjectsLocationsList

> ListLocationsResponse bigquerydatatransferProjectsLocationsList(name, opts)



Lists information about the supported locations for this service.

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
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
apiInstance.bigquerydatatransferProjectsLocationsList(name, opts, (error, data, response) => {
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


## bigquerydatatransferProjectsLocationsUnenrollDataSources

> Object bigquerydatatransferProjectsLocationsUnenrollDataSources(name, opts)



Unenroll data sources in a user project. This allows users to remove transfer configurations for these data sources. They will no longer appear in the ListDataSources RPC and will also no longer appear in the [BigQuery UI](https://console.cloud.google.com/bigquery). Data transfers configurations of unenrolled data sources will not be scheduled.

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
let name = "name_example"; // String | The name of the project resource in the form: `projects/{project_id}`
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
  'unenrollDataSourcesRequest': new BigQueryDataTransferApi.UnenrollDataSourcesRequest() // UnenrollDataSourcesRequest | 
};
apiInstance.bigquerydatatransferProjectsLocationsUnenrollDataSources(name, opts, (error, data, response) => {
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
 **name** | **String**| The name of the project resource in the form: &#x60;projects/{project_id}&#x60; | 
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
 **unenrollDataSourcesRequest** | [**UnenrollDataSourcesRequest**](UnenrollDataSourcesRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bigquerydatatransferProjectsTransferConfigsCreate

> TransferConfig bigquerydatatransferProjectsTransferConfigsCreate(parent, opts)



Creates a new data transfer configuration.

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The BigQuery project id where the transfer configuration should be created. Must be in the format projects/{project_id}/locations/{location_id} or projects/{project_id}. If specified location and location of the destination bigquery dataset do not match - the request will fail.
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
  'authorizationCode': "authorizationCode_example", // String | Optional OAuth2 authorization code to use with this transfer configuration. This is required only if `transferConfig.dataSourceId` is 'youtube_channel' and new credentials are needed, as indicated by `CheckValidCreds`. In order to obtain authorization_code, make a request to the following URL: https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=authorization_code&client_id=client_id&scope=data_source_scopes * The client_id is the OAuth client_id of the a data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when `service_account_name` is used to create the transfer config.
  'serviceAccountName': "serviceAccountName_example", // String | Optional service account email. If this field is set, the transfer config will be created with this service account's credentials. It requires that the requesting user calling this API has permissions to act as this service account. Note that not all data sources support service account credentials when creating a transfer config. For the latest list of data sources, read about [using service accounts](https://cloud.google.com/bigquery-transfer/docs/use-service-accounts).
  'versionInfo': "versionInfo_example", // String | Optional version info. This is required only if `transferConfig.dataSourceId` is not 'youtube_channel' and new credentials are needed, as indicated by `CheckValidCreds`. In order to obtain version info, make a request to the following URL: https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=version_info&client_id=client_id&scope=data_source_scopes * The client_id is the OAuth client_id of the a data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when `service_account_name` is used to create the transfer config.
  'transferConfig': new BigQueryDataTransferApi.TransferConfig() // TransferConfig | 
};
apiInstance.bigquerydatatransferProjectsTransferConfigsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The BigQuery project id where the transfer configuration should be created. Must be in the format projects/{project_id}/locations/{location_id} or projects/{project_id}. If specified location and location of the destination bigquery dataset do not match - the request will fail. | 
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
 **authorizationCode** | **String**| Optional OAuth2 authorization code to use with this transfer configuration. This is required only if &#x60;transferConfig.dataSourceId&#x60; is &#39;youtube_channel&#39; and new credentials are needed, as indicated by &#x60;CheckValidCreds&#x60;. In order to obtain authorization_code, make a request to the following URL: https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?redirect_uri&#x3D;urn:ietf:wg:oauth:2.0:oob&amp;response_type&#x3D;authorization_code&amp;client_id&#x3D;client_id&amp;scope&#x3D;data_source_scopes * The client_id is the OAuth client_id of the a data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when &#x60;service_account_name&#x60; is used to create the transfer config. | [optional] 
 **serviceAccountName** | **String**| Optional service account email. If this field is set, the transfer config will be created with this service account&#39;s credentials. It requires that the requesting user calling this API has permissions to act as this service account. Note that not all data sources support service account credentials when creating a transfer config. For the latest list of data sources, read about [using service accounts](https://cloud.google.com/bigquery-transfer/docs/use-service-accounts). | [optional] 
 **versionInfo** | **String**| Optional version info. This is required only if &#x60;transferConfig.dataSourceId&#x60; is not &#39;youtube_channel&#39; and new credentials are needed, as indicated by &#x60;CheckValidCreds&#x60;. In order to obtain version info, make a request to the following URL: https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?redirect_uri&#x3D;urn:ietf:wg:oauth:2.0:oob&amp;response_type&#x3D;version_info&amp;client_id&#x3D;client_id&amp;scope&#x3D;data_source_scopes * The client_id is the OAuth client_id of the a data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when &#x60;service_account_name&#x60; is used to create the transfer config. | [optional] 
 **transferConfig** | [**TransferConfig**](TransferConfig.md)|  | [optional] 

### Return type

[**TransferConfig**](TransferConfig.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bigquerydatatransferProjectsTransferConfigsList

> ListTransferConfigsResponse bigquerydatatransferProjectsTransferConfigsList(parent, opts)



Returns information about all transfer configs owned by a project in the specified location.

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
let parent = "parent_example"; // String | Required. The BigQuery project id for which transfer configs should be returned: `projects/{project_id}` or `projects/{project_id}/locations/{location_id}`
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
  'dataSourceIds': ["null"], // [String] | When specified, only configurations of requested data sources are returned.
  'pageSize': 56, // Number | Page size. The default page size is the maximum value of 1000 results.
  'pageToken': "pageToken_example" // String | Pagination token, which can be used to request a specific page of `ListTransfersRequest` list results. For multiple-page results, `ListTransfersResponse` outputs a `next_page` token, which can be used as the `page_token` value to request the next page of list results.
};
apiInstance.bigquerydatatransferProjectsTransferConfigsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The BigQuery project id for which transfer configs should be returned: &#x60;projects/{project_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}&#x60; | 
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
 **dataSourceIds** | [**[String]**](String.md)| When specified, only configurations of requested data sources are returned. | [optional] 
 **pageSize** | **Number**| Page size. The default page size is the maximum value of 1000 results. | [optional] 
 **pageToken** | **String**| Pagination token, which can be used to request a specific page of &#x60;ListTransfersRequest&#x60; list results. For multiple-page results, &#x60;ListTransfersResponse&#x60; outputs a &#x60;next_page&#x60; token, which can be used as the &#x60;page_token&#x60; value to request the next page of list results. | [optional] 

### Return type

[**ListTransferConfigsResponse**](ListTransferConfigsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bigquerydatatransferProjectsTransferConfigsPatch

> TransferConfig bigquerydatatransferProjectsTransferConfigsPatch(name, opts)



Updates a data transfer configuration. All fields must be set, even if they are not updated.

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
let name = "name_example"; // String | The resource name of the transfer config. Transfer config names have the form either `projects/{project_id}/locations/{region}/transferConfigs/{config_id}` or `projects/{project_id}/transferConfigs/{config_id}`, where `config_id` is usually a UUID, even though it is not guaranteed or required. The name is ignored when creating a transfer config.
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
  'authorizationCode': "authorizationCode_example", // String | Optional OAuth2 authorization code to use with this transfer configuration. This is required only if `transferConfig.dataSourceId` is 'youtube_channel' and new credentials are needed, as indicated by `CheckValidCreds`. In order to obtain authorization_code, make a request to the following URL: https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=authorization_code&client_id=client_id&scope=data_source_scopes * The client_id is the OAuth client_id of the a data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when `service_account_name` is used to update the transfer config.
  'serviceAccountName': "serviceAccountName_example", // String | Optional service account email. If this field is set, the transfer config will be created with this service account's credentials. It requires that the requesting user calling this API has permissions to act as this service account. Note that not all data sources support service account credentials when creating a transfer config. For the latest list of data sources, read about [using service accounts](https://cloud.google.com/bigquery-transfer/docs/use-service-accounts).
  'updateMask': "updateMask_example", // String | Required. Required list of fields to be updated in this request.
  'versionInfo': "versionInfo_example", // String | Optional version info. This is required only if `transferConfig.dataSourceId` is not 'youtube_channel' and new credentials are needed, as indicated by `CheckValidCreds`. In order to obtain version info, make a request to the following URL: https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?redirect_uri=urn:ietf:wg:oauth:2.0:oob&response_type=version_info&client_id=client_id&scope=data_source_scopes * The client_id is the OAuth client_id of the a data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when `service_account_name` is used to update the transfer config.
  'transferConfig': new BigQueryDataTransferApi.TransferConfig() // TransferConfig | 
};
apiInstance.bigquerydatatransferProjectsTransferConfigsPatch(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource name of the transfer config. Transfer config names have the form either &#x60;projects/{project_id}/locations/{region}/transferConfigs/{config_id}&#x60; or &#x60;projects/{project_id}/transferConfigs/{config_id}&#x60;, where &#x60;config_id&#x60; is usually a UUID, even though it is not guaranteed or required. The name is ignored when creating a transfer config. | 
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
 **authorizationCode** | **String**| Optional OAuth2 authorization code to use with this transfer configuration. This is required only if &#x60;transferConfig.dataSourceId&#x60; is &#39;youtube_channel&#39; and new credentials are needed, as indicated by &#x60;CheckValidCreds&#x60;. In order to obtain authorization_code, make a request to the following URL: https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?redirect_uri&#x3D;urn:ietf:wg:oauth:2.0:oob&amp;response_type&#x3D;authorization_code&amp;client_id&#x3D;client_id&amp;scope&#x3D;data_source_scopes * The client_id is the OAuth client_id of the a data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when &#x60;service_account_name&#x60; is used to update the transfer config. | [optional] 
 **serviceAccountName** | **String**| Optional service account email. If this field is set, the transfer config will be created with this service account&#39;s credentials. It requires that the requesting user calling this API has permissions to act as this service account. Note that not all data sources support service account credentials when creating a transfer config. For the latest list of data sources, read about [using service accounts](https://cloud.google.com/bigquery-transfer/docs/use-service-accounts). | [optional] 
 **updateMask** | **String**| Required. Required list of fields to be updated in this request. | [optional] 
 **versionInfo** | **String**| Optional version info. This is required only if &#x60;transferConfig.dataSourceId&#x60; is not &#39;youtube_channel&#39; and new credentials are needed, as indicated by &#x60;CheckValidCreds&#x60;. In order to obtain version info, make a request to the following URL: https://www.gstatic.com/bigquerydatatransfer/oauthz/auth?redirect_uri&#x3D;urn:ietf:wg:oauth:2.0:oob&amp;response_type&#x3D;version_info&amp;client_id&#x3D;client_id&amp;scope&#x3D;data_source_scopes * The client_id is the OAuth client_id of the a data source as returned by ListDataSources method. * data_source_scopes are the scopes returned by ListDataSources method. Note that this should not be set when &#x60;service_account_name&#x60; is used to update the transfer config. | [optional] 
 **transferConfig** | [**TransferConfig**](TransferConfig.md)|  | [optional] 

### Return type

[**TransferConfig**](TransferConfig.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bigquerydatatransferProjectsTransferConfigsRunsDelete

> Object bigquerydatatransferProjectsTransferConfigsRunsDelete(name, opts)



Deletes the specified transfer run.

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
let name = "name_example"; // String | Required. The field will contain name of the resource requested, for example: `projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}` or `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}`
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
apiInstance.bigquerydatatransferProjectsTransferConfigsRunsDelete(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The field will contain name of the resource requested, for example: &#x60;projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}&#x60; | 
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


## bigquerydatatransferProjectsTransferConfigsRunsGet

> TransferRun bigquerydatatransferProjectsTransferConfigsRunsGet(name, opts)



Returns information about the particular transfer run.

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
let name = "name_example"; // String | Required. The field will contain name of the resource requested, for example: `projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}` or `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}`
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
apiInstance.bigquerydatatransferProjectsTransferConfigsRunsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The field will contain name of the resource requested, for example: &#x60;projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}&#x60; | 
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

[**TransferRun**](TransferRun.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bigquerydatatransferProjectsTransferConfigsRunsList

> ListTransferRunsResponse bigquerydatatransferProjectsTransferConfigsRunsList(parent, opts)



Returns information about running and completed transfer runs.

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
let parent = "parent_example"; // String | Required. Name of transfer configuration for which transfer runs should be retrieved. Format of transfer configuration resource name is: `projects/{project_id}/transferConfigs/{config_id}` or `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`.
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
  'pageSize': 56, // Number | Page size. The default page size is the maximum value of 1000 results.
  'pageToken': "pageToken_example", // String | Pagination token, which can be used to request a specific page of `ListTransferRunsRequest` list results. For multiple-page results, `ListTransferRunsResponse` outputs a `next_page` token, which can be used as the `page_token` value to request the next page of list results.
  'runAttempt': "runAttempt_example", // String | Indicates how run attempts are to be pulled.
  'states': ["null"] // [String] | When specified, only transfer runs with requested states are returned.
};
apiInstance.bigquerydatatransferProjectsTransferConfigsRunsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Name of transfer configuration for which transfer runs should be retrieved. Format of transfer configuration resource name is: &#x60;projects/{project_id}/transferConfigs/{config_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}&#x60;. | 
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
 **pageSize** | **Number**| Page size. The default page size is the maximum value of 1000 results. | [optional] 
 **pageToken** | **String**| Pagination token, which can be used to request a specific page of &#x60;ListTransferRunsRequest&#x60; list results. For multiple-page results, &#x60;ListTransferRunsResponse&#x60; outputs a &#x60;next_page&#x60; token, which can be used as the &#x60;page_token&#x60; value to request the next page of list results. | [optional] 
 **runAttempt** | **String**| Indicates how run attempts are to be pulled. | [optional] 
 **states** | [**[String]**](String.md)| When specified, only transfer runs with requested states are returned. | [optional] 

### Return type

[**ListTransferRunsResponse**](ListTransferRunsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bigquerydatatransferProjectsTransferConfigsRunsTransferLogsList

> ListTransferLogsResponse bigquerydatatransferProjectsTransferConfigsRunsTransferLogsList(parent, opts)



Returns log messages for the transfer run.

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
let parent = "parent_example"; // String | Required. Transfer run name in the form: `projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}` or `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}`
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
  'messageTypes': ["null"], // [String] | Message types to return. If not populated - INFO, WARNING and ERROR messages are returned.
  'pageSize': 56, // Number | Page size. The default page size is the maximum value of 1000 results.
  'pageToken': "pageToken_example" // String | Pagination token, which can be used to request a specific page of `ListTransferLogsRequest` list results. For multiple-page results, `ListTransferLogsResponse` outputs a `next_page` token, which can be used as the `page_token` value to request the next page of list results.
};
apiInstance.bigquerydatatransferProjectsTransferConfigsRunsTransferLogsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Transfer run name in the form: &#x60;projects/{project_id}/transferConfigs/{config_id}/runs/{run_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}/runs/{run_id}&#x60; | 
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
 **messageTypes** | [**[String]**](String.md)| Message types to return. If not populated - INFO, WARNING and ERROR messages are returned. | [optional] 
 **pageSize** | **Number**| Page size. The default page size is the maximum value of 1000 results. | [optional] 
 **pageToken** | **String**| Pagination token, which can be used to request a specific page of &#x60;ListTransferLogsRequest&#x60; list results. For multiple-page results, &#x60;ListTransferLogsResponse&#x60; outputs a &#x60;next_page&#x60; token, which can be used as the &#x60;page_token&#x60; value to request the next page of list results. | [optional] 

### Return type

[**ListTransferLogsResponse**](ListTransferLogsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## bigquerydatatransferProjectsTransferConfigsScheduleRuns

> ScheduleTransferRunsResponse bigquerydatatransferProjectsTransferConfigsScheduleRuns(parent, opts)



Creates transfer runs for a time range [start_time, end_time]. For each date - or whatever granularity the data source supports - in the range, one transfer run is created. Note that runs are created per UTC time in the time range. DEPRECATED: use StartManualTransferRuns instead.

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
let parent = "parent_example"; // String | Required. Transfer configuration name in the form: `projects/{project_id}/transferConfigs/{config_id}` or `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`.
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
  'scheduleTransferRunsRequest': new BigQueryDataTransferApi.ScheduleTransferRunsRequest() // ScheduleTransferRunsRequest | 
};
apiInstance.bigquerydatatransferProjectsTransferConfigsScheduleRuns(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Transfer configuration name in the form: &#x60;projects/{project_id}/transferConfigs/{config_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}&#x60;. | 
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
 **scheduleTransferRunsRequest** | [**ScheduleTransferRunsRequest**](ScheduleTransferRunsRequest.md)|  | [optional] 

### Return type

[**ScheduleTransferRunsResponse**](ScheduleTransferRunsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bigquerydatatransferProjectsTransferConfigsStartManualRuns

> StartManualTransferRunsResponse bigquerydatatransferProjectsTransferConfigsStartManualRuns(parent, opts)



Start manual transfer runs to be executed now with schedule_time equal to current time. The transfer runs can be created for a time range where the run_time is between start_time (inclusive) and end_time (exclusive), or for a specific run_time.

### Example

```javascript
import BigQueryDataTransferApi from 'big_query_data_transfer_api';
let defaultClient = BigQueryDataTransferApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryDataTransferApi.ProjectsApi();
let parent = "parent_example"; // String | Transfer configuration name in the form: `projects/{project_id}/transferConfigs/{config_id}` or `projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}`.
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
  'startManualTransferRunsRequest': new BigQueryDataTransferApi.StartManualTransferRunsRequest() // StartManualTransferRunsRequest | 
};
apiInstance.bigquerydatatransferProjectsTransferConfigsStartManualRuns(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Transfer configuration name in the form: &#x60;projects/{project_id}/transferConfigs/{config_id}&#x60; or &#x60;projects/{project_id}/locations/{location_id}/transferConfigs/{config_id}&#x60;. | 
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
 **startManualTransferRunsRequest** | [**StartManualTransferRunsRequest**](StartManualTransferRunsRequest.md)|  | [optional] 

### Return type

[**StartManualTransferRunsResponse**](StartManualTransferRunsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

