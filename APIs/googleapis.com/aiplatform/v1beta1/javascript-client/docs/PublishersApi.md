# VertexAiApi.PublishersApi

All URIs are relative to *https://aiplatform.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aiplatformPublishersModelsGet**](PublishersApi.md#aiplatformPublishersModelsGet) | **GET** /v1beta1/{name} | 
[**aiplatformPublishersModelsList**](PublishersApi.md#aiplatformPublishersModelsList) | **GET** /v1beta1/{parent}/models | 



## aiplatformPublishersModelsGet

> GoogleCloudAiplatformV1beta1PublisherModel aiplatformPublishersModelsGet(name, opts)



Gets a Model Garden publisher model.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.PublishersApi();
let name = "name_example"; // String | Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`
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
  'languageCode': "languageCode_example", // String | Optional. The IETF BCP-47 language code representing the language in which the publisher model's text information should be written in (see go/bcp47).
  'view': "view_example" // String | Optional. PublisherModel view specifying which fields to read.
};
apiInstance.aiplatformPublishersModelsGet(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The name of the PublisherModel resource. Format: &#x60;publishers/{publisher}/models/{publisher_model}&#x60; | 
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
 **languageCode** | **String**| Optional. The IETF BCP-47 language code representing the language in which the publisher model&#39;s text information should be written in (see go/bcp47). | [optional] 
 **view** | **String**| Optional. PublisherModel view specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1beta1PublisherModel**](GoogleCloudAiplatformV1beta1PublisherModel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## aiplatformPublishersModelsList

> GoogleCloudAiplatformV1beta1ListPublisherModelsResponse aiplatformPublishersModelsList(parent, opts)



Lists publisher models in Model Garden.

### Example

```javascript
import VertexAiApi from 'vertex_ai_api';
let defaultClient = VertexAiApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new VertexAiApi.PublishersApi();
let parent = "parent_example"; // String | Required. The name of the Publisher from which to list the PublisherModels. Format: `publishers/{publisher}`
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
  'filter': "filter_example", // String | Optional. The standard list filter.
  'languageCode': "languageCode_example", // String | Optional. The IETF BCP-47 language code representing the language in which the publisher models' text information should be written in (see go/bcp47). If not set, by default English (en).
  'orderBy': "orderBy_example", // String | Optional. A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending.
  'pageSize': 56, // Number | Optional. The standard list page size.
  'pageToken': "pageToken_example", // String | Optional. The standard list page token. Typically obtained via ListPublisherModelsResponse.next_page_token of the previous ModelGardenService.ListPublisherModels call.
  'view': "view_example" // String | Optional. PublisherModel view specifying which fields to read.
};
apiInstance.aiplatformPublishersModelsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. The name of the Publisher from which to list the PublisherModels. Format: &#x60;publishers/{publisher}&#x60; | 
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
 **filter** | **String**| Optional. The standard list filter. | [optional] 
 **languageCode** | **String**| Optional. The IETF BCP-47 language code representing the language in which the publisher models&#39; text information should be written in (see go/bcp47). If not set, by default English (en). | [optional] 
 **orderBy** | **String**| Optional. A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. | [optional] 
 **pageSize** | **Number**| Optional. The standard list page size. | [optional] 
 **pageToken** | **String**| Optional. The standard list page token. Typically obtained via ListPublisherModelsResponse.next_page_token of the previous ModelGardenService.ListPublisherModels call. | [optional] 
 **view** | **String**| Optional. PublisherModel view specifying which fields to read. | [optional] 

### Return type

[**GoogleCloudAiplatformV1beta1ListPublisherModelsResponse**](GoogleCloudAiplatformV1beta1ListPublisherModelsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

