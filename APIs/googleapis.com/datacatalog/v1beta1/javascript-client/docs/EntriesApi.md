# GoogleCloudDataCatalogApi.EntriesApi

All URIs are relative to *https://datacatalog.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datacatalogEntriesLookup**](EntriesApi.md#datacatalogEntriesLookup) | **GET** /v1beta1/entries:lookup | 



## datacatalogEntriesLookup

> GoogleCloudDatacatalogV1beta1Entry datacatalogEntriesLookup(opts)



Get an entry by target resource name. This method allows clients to use the resource name from the source Google Cloud Platform service to get the Data Catalog Entry.

### Example

```javascript
import GoogleCloudDataCatalogApi from 'google_cloud_data_catalog_api';
let defaultClient = GoogleCloudDataCatalogApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new GoogleCloudDataCatalogApi.EntriesApi();
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
  'linkedResource': "linkedResource_example", // String | The full name of the Google Cloud Platform resource the Data Catalog entry represents. See: https://cloud.google.com/apis/design/resource_names#full_resource_name. Full names are case-sensitive. Examples: * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId * //pubsub.googleapis.com/projects/projectId/topics/topicId
  'sqlResource': "sqlResource_example" // String | The SQL name of the entry. SQL names are case-sensitive. Examples: * `pubsub.project_id.topic_id` * ``pubsub.project_id.`topic.id.with.dots` `` * `bigquery.table.project_id.dataset_id.table_id` * `bigquery.dataset.project_id.dataset_id` * `datacatalog.entry.project_id.location_id.entry_group_id.entry_id` `*_id`s should satisfy the standard SQL rules for identifiers. https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical.
};
apiInstance.datacatalogEntriesLookup(opts, (error, data, response) => {
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
 **linkedResource** | **String**| The full name of the Google Cloud Platform resource the Data Catalog entry represents. See: https://cloud.google.com/apis/design/resource_names#full_resource_name. Full names are case-sensitive. Examples: * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId * //pubsub.googleapis.com/projects/projectId/topics/topicId | [optional] 
 **sqlResource** | **String**| The SQL name of the entry. SQL names are case-sensitive. Examples: * &#x60;pubsub.project_id.topic_id&#x60; * &#x60;&#x60;pubsub.project_id.&#x60;topic.id.with.dots&#x60; &#x60;&#x60; * &#x60;bigquery.table.project_id.dataset_id.table_id&#x60; * &#x60;bigquery.dataset.project_id.dataset_id&#x60; * &#x60;datacatalog.entry.project_id.location_id.entry_group_id.entry_id&#x60; &#x60;*_id&#x60;s should satisfy the standard SQL rules for identifiers. https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical. | [optional] 

### Return type

[**GoogleCloudDatacatalogV1beta1Entry**](GoogleCloudDatacatalogV1beta1Entry.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

