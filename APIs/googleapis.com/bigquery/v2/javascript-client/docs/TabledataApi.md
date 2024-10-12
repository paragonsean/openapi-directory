# BigQueryApi.TabledataApi

All URIs are relative to *https://bigquery.googleapis.com/bigquery/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bigqueryTabledataInsertAll**](TabledataApi.md#bigqueryTabledataInsertAll) | **POST** /projects/{projectId}/datasets/{datasetId}/tables/{tableId}/insertAll | 
[**bigqueryTabledataList**](TabledataApi.md#bigqueryTabledataList) | **GET** /projects/{projectId}/datasets/{datasetId}/tables/{tableId}/data | 



## bigqueryTabledataInsertAll

> TableDataInsertAllResponse bigqueryTabledataInsertAll(projectId, datasetId, tableId, opts)



Streams data into BigQuery one record at a time without needing to run a load job.

### Example

```javascript
import BigQueryApi from 'big_query_api';
let defaultClient = BigQueryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryApi.TabledataApi();
let projectId = "projectId_example"; // String | Required. Project ID of the destination.
let datasetId = "datasetId_example"; // String | Required. Dataset ID of the destination.
let tableId = "tableId_example"; // String | Required. Table ID of the destination.
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
  'tableDataInsertAllRequest': new BigQueryApi.TableDataInsertAllRequest() // TableDataInsertAllRequest | 
};
apiInstance.bigqueryTabledataInsertAll(projectId, datasetId, tableId, opts, (error, data, response) => {
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
 **projectId** | **String**| Required. Project ID of the destination. | 
 **datasetId** | **String**| Required. Dataset ID of the destination. | 
 **tableId** | **String**| Required. Table ID of the destination. | 
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
 **tableDataInsertAllRequest** | [**TableDataInsertAllRequest**](TableDataInsertAllRequest.md)|  | [optional] 

### Return type

[**TableDataInsertAllResponse**](TableDataInsertAllResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bigqueryTabledataList

> TableDataList bigqueryTabledataList(projectId, datasetId, tableId, opts)



List the content of a table in rows.

### Example

```javascript
import BigQueryApi from 'big_query_api';
let defaultClient = BigQueryApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new BigQueryApi.TabledataApi();
let projectId = "projectId_example"; // String | Required. Project id of the table to list.
let datasetId = "datasetId_example"; // String | Required. Dataset id of the table to list.
let tableId = "tableId_example"; // String | Required. Table id of the table to list.
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
  'formatOptionsUseInt64Timestamp': true, // Boolean | Optional. Output timestamp as usec int64. Default is false.
  'maxResults': 56, // Number | Row limit of the table.
  'pageToken': "pageToken_example", // String | To retrieve the next page of table data, set this field to the string provided in the pageToken field of the response body from your previous call to tabledata.list.
  'selectedFields': "selectedFields_example", // String | Subset of fields to return, supports select into sub fields. Example: selected_fields = \"a,e.d.f\";
  'startIndex': "startIndex_example" // String | Start row index of the table.
};
apiInstance.bigqueryTabledataList(projectId, datasetId, tableId, opts, (error, data, response) => {
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
 **projectId** | **String**| Required. Project id of the table to list. | 
 **datasetId** | **String**| Required. Dataset id of the table to list. | 
 **tableId** | **String**| Required. Table id of the table to list. | 
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
 **formatOptionsUseInt64Timestamp** | **Boolean**| Optional. Output timestamp as usec int64. Default is false. | [optional] 
 **maxResults** | **Number**| Row limit of the table. | [optional] 
 **pageToken** | **String**| To retrieve the next page of table data, set this field to the string provided in the pageToken field of the response body from your previous call to tabledata.list. | [optional] 
 **selectedFields** | **String**| Subset of fields to return, supports select into sub fields. Example: selected_fields &#x3D; \&quot;a,e.d.f\&quot;; | [optional] 
 **startIndex** | **String**| Start row index of the table. | [optional] 

### Return type

[**TableDataList**](TableDataList.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

