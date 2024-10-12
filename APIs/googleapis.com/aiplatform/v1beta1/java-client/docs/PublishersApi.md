# PublishersApi

All URIs are relative to *https://aiplatform.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**aiplatformPublishersModelsGet**](PublishersApi.md#aiplatformPublishersModelsGet) | **GET** /v1beta1/{name} |  |
| [**aiplatformPublishersModelsList**](PublishersApi.md#aiplatformPublishersModelsList) | **GET** /v1beta1/{parent}/models |  |


<a id="aiplatformPublishersModelsGet"></a>
# **aiplatformPublishersModelsGet**
> GoogleCloudAiplatformV1beta1PublisherModel aiplatformPublishersModelsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, view)



Gets a Model Garden publisher model.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublishersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiplatform.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PublishersApi apiInstance = new PublishersApi(defaultClient);
    String name = "name_example"; // String | Required. The name of the PublisherModel resource. Format: `publishers/{publisher}/models/{publisher_model}`
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String languageCode = "languageCode_example"; // String | Optional. The IETF BCP-47 language code representing the language in which the publisher model's text information should be written in (see go/bcp47).
    String view = "PUBLISHER_MODEL_VIEW_UNSPECIFIED"; // String | Optional. PublisherModel view specifying which fields to read.
    try {
      GoogleCloudAiplatformV1beta1PublisherModel result = apiInstance.aiplatformPublishersModelsGet(name, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublishersApi#aiplatformPublishersModelsGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **name** | **String**| Required. The name of the PublisherModel resource. Format: &#x60;publishers/{publisher}/models/{publisher_model}&#x60; | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **languageCode** | **String**| Optional. The IETF BCP-47 language code representing the language in which the publisher model&#39;s text information should be written in (see go/bcp47). | [optional] |
| **view** | **String**| Optional. PublisherModel view specifying which fields to read. | [optional] [enum: PUBLISHER_MODEL_VIEW_UNSPECIFIED, PUBLISHER_MODEL_VIEW_BASIC, PUBLISHER_MODEL_VIEW_FULL, PUBLISHER_MODEL_VERSION_VIEW_BASIC] |

### Return type

[**GoogleCloudAiplatformV1beta1PublisherModel**](GoogleCloudAiplatformV1beta1PublisherModel.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="aiplatformPublishersModelsList"></a>
# **aiplatformPublishersModelsList**
> GoogleCloudAiplatformV1beta1ListPublisherModelsResponse aiplatformPublishersModelsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, languageCode, orderBy, pageSize, pageToken, view)



Lists publisher models in Model Garden.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PublishersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://aiplatform.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    PublishersApi apiInstance = new PublishersApi(defaultClient);
    String parent = "parent_example"; // String | Required. The name of the Publisher from which to list the PublisherModels. Format: `publishers/{publisher}`
    String $xgafv = "1"; // String | V1 error format.
    String accessToken = "accessToken_example"; // String | OAuth access token.
    String alt = "json"; // String | Data format for response.
    String paramCallback = "paramCallback_example"; // String | JSONP
    String fields = "fields_example"; // String | Selector specifying which fields to include in a partial response.
    String key = "key_example"; // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    String oauthToken = "oauthToken_example"; // String | OAuth 2.0 token for the current user.
    Boolean prettyPrint = true; // Boolean | Returns response with indentations and line breaks.
    String quotaUser = "quotaUser_example"; // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    String uploadProtocol = "uploadProtocol_example"; // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
    String uploadType = "uploadType_example"; // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
    String filter = "filter_example"; // String | Optional. The standard list filter.
    String languageCode = "languageCode_example"; // String | Optional. The IETF BCP-47 language code representing the language in which the publisher models' text information should be written in (see go/bcp47). If not set, by default English (en).
    String orderBy = "orderBy_example"; // String | Optional. A comma-separated list of fields to order by, sorted in ascending order. Use \"desc\" after a field name for descending.
    Integer pageSize = 56; // Integer | Optional. The standard list page size.
    String pageToken = "pageToken_example"; // String | Optional. The standard list page token. Typically obtained via ListPublisherModelsResponse.next_page_token of the previous ModelGardenService.ListPublisherModels call.
    String view = "PUBLISHER_MODEL_VIEW_UNSPECIFIED"; // String | Optional. PublisherModel view specifying which fields to read.
    try {
      GoogleCloudAiplatformV1beta1ListPublisherModelsResponse result = apiInstance.aiplatformPublishersModelsList(parent, $xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, languageCode, orderBy, pageSize, pageToken, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PublishersApi#aiplatformPublishersModelsList");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **parent** | **String**| Required. The name of the Publisher from which to list the PublisherModels. Format: &#x60;publishers/{publisher}&#x60; | |
| **$xgafv** | **String**| V1 error format. | [optional] [enum: 1, 2] |
| **accessToken** | **String**| OAuth access token. | [optional] |
| **alt** | **String**| Data format for response. | [optional] [enum: json, media, proto] |
| **paramCallback** | **String**| JSONP | [optional] |
| **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] |
| **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] |
| **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] |
| **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] |
| **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] |
| **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] |
| **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] |
| **filter** | **String**| Optional. The standard list filter. | [optional] |
| **languageCode** | **String**| Optional. The IETF BCP-47 language code representing the language in which the publisher models&#39; text information should be written in (see go/bcp47). If not set, by default English (en). | [optional] |
| **orderBy** | **String**| Optional. A comma-separated list of fields to order by, sorted in ascending order. Use \&quot;desc\&quot; after a field name for descending. | [optional] |
| **pageSize** | **Integer**| Optional. The standard list page size. | [optional] |
| **pageToken** | **String**| Optional. The standard list page token. Typically obtained via ListPublisherModelsResponse.next_page_token of the previous ModelGardenService.ListPublisherModels call. | [optional] |
| **view** | **String**| Optional. PublisherModel view specifying which fields to read. | [optional] [enum: PUBLISHER_MODEL_VIEW_UNSPECIFIED, PUBLISHER_MODEL_VIEW_BASIC, PUBLISHER_MODEL_VIEW_FULL, PUBLISHER_MODEL_VERSION_VIEW_BASIC] |

### Return type

[**GoogleCloudAiplatformV1beta1ListPublisherModelsResponse**](GoogleCloudAiplatformV1beta1ListPublisherModelsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

