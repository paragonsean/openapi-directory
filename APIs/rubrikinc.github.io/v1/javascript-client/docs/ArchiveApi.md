# RubrikRestApi.ArchiveApi

All URIs are relative to */api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**disableArchivalLocation**](ArchiveApi.md#disableArchivalLocation) | **POST** /archive/location/{id}/owner/disable | Disable location for archival and modification operations
[**enableArchivalLocation**](ArchiveApi.md#enableArchivalLocation) | **POST** /archive/location/{id}/owner/enable | Enable archival location for archival and modification operations
[**getAwsAccountId**](ArchiveApi.md#getAwsAccountId) | **GET** /archive/aws/s3/{id}/account_id | Get the AWS account ID of an AWS S3 archival location
[**refreshArchivalLocationDataSources**](ArchiveApi.md#refreshArchivalLocationDataSources) | **POST** /archive/location/{location_id}/reader/refresh/data_sources | Refresh archive information for a list of data sources



## disableArchivalLocation

> disableArchivalLocation(id)

Disable location for archival and modification operations

Disables archiving and any changes to the data for the specified archival location. This operation disables snapshot upload, snapshot expiration, consolidation, and garbage collection operations on the archival location. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ArchiveApi();
let id = "id_example"; // String | ID assigned to an archival location object.
apiInstance.disableArchivalLocation(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to an archival location object. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## enableArchivalLocation

> enableArchivalLocation(id)

Enable archival location for archival and modification operations

Enable archiving and other operations that were previously disabled on the specified archival location. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ArchiveApi();
let id = "id_example"; // String | ID assigned to an archival location object.
apiInstance.enableArchivalLocation(id, (error, data, response) => {
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
 **id** | **String**| ID assigned to an archival location object. | 

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## getAwsAccountId

> StringResponse getAwsAccountId(id)

Get the AWS account ID of an AWS S3 archival location

Get the AWS account ID of an AWS S3 archival location.

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ArchiveApi();
let id = "id_example"; // String | ID of an AWS archival location that uses the S3 protocol.
apiInstance.getAwsAccountId(id, (error, data, response) => {
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
 **id** | **String**| ID of an AWS archival location that uses the S3 protocol. | 

### Return type

[**StringResponse**](StringResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## refreshArchivalLocationDataSources

> AsyncRequestStatus refreshArchivalLocationDataSources(locationId, readerRefreshDataSourcesRequest)

Refresh archive information for a list of data sources

Update the current Rubrik CDM cluster with information about the changes made to a list of data sources in an archival location by the Rubrik CDM cluster that owns the archival location. 

### Example

```javascript
import RubrikRestApi from 'rubrik_rest_api';
let defaultClient = RubrikRestApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: Bearer
let Bearer = defaultClient.authentications['Bearer'];
Bearer.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Bearer.apiKeyPrefix = 'Token';

let apiInstance = new RubrikRestApi.ArchiveApi();
let locationId = "locationId_example"; // String | ID assigned to an archival location object.
let readerRefreshDataSourcesRequest = new RubrikRestApi.ReaderRefreshDataSourcesRequest(); // ReaderRefreshDataSourcesRequest | A set of local and archival IDs for data sources to refresh. For a data source, either a local or archival data source ID should be specified. The operation will fail if `none` is specified. 
apiInstance.refreshArchivalLocationDataSources(locationId, readerRefreshDataSourcesRequest, (error, data, response) => {
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
 **locationId** | **String**| ID assigned to an archival location object. | 
 **readerRefreshDataSourcesRequest** | [**ReaderRefreshDataSourcesRequest**](ReaderRefreshDataSourcesRequest.md)| A set of local and archival IDs for data sources to refresh. For a data source, either a local or archival data source ID should be specified. The operation will fail if &#x60;none&#x60; is specified.  | 

### Return type

[**AsyncRequestStatus**](AsyncRequestStatus.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

