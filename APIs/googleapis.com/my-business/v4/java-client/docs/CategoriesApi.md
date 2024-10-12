# CategoriesApi

All URIs are relative to *https://mybusiness.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mybusinessCategoriesBatchGet**](CategoriesApi.md#mybusinessCategoriesBatchGet) | **GET** /v4/categories:batchGet |  |
| [**mybusinessCategoriesList**](CategoriesApi.md#mybusinessCategoriesList) | **GET** /v4/categories |  |


<a id="mybusinessCategoriesBatchGet"></a>
# **mybusinessCategoriesBatchGet**
> BatchGetBusinessCategoriesResponse mybusinessCategoriesBatchGet($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, categoryIds, languageCode, regionCode, view)



Returns a list of business categories for the provided language and GConcept ids.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mybusiness.googleapis.com");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
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
    List<String> categoryIds = Arrays.asList(); // List<String> | Required. At least one name must be set. The GConcept ids the localized category names should be returned for.
    String languageCode = "languageCode_example"; // String | Required. The BCP 47 code of language that the category names should be returned in.
    String regionCode = "regionCode_example"; // String | Optional. The ISO 3166-1 alpha-2 country code used to infer non-standard language.
    String view = "CATEGORY_VIEW_UNSPECIFIED"; // String | Required. Specifies which parts to the Category resource should be returned in the response.
    try {
      BatchGetBusinessCategoriesResponse result = apiInstance.mybusinessCategoriesBatchGet($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, categoryIds, languageCode, regionCode, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#mybusinessCategoriesBatchGet");
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
| **categoryIds** | [**List&lt;String&gt;**](String.md)| Required. At least one name must be set. The GConcept ids the localized category names should be returned for. | [optional] |
| **languageCode** | **String**| Required. The BCP 47 code of language that the category names should be returned in. | [optional] |
| **regionCode** | **String**| Optional. The ISO 3166-1 alpha-2 country code used to infer non-standard language. | [optional] |
| **view** | **String**| Required. Specifies which parts to the Category resource should be returned in the response. | [optional] [enum: CATEGORY_VIEW_UNSPECIFIED, BASIC, FULL] |

### Return type

[**BatchGetBusinessCategoriesResponse**](BatchGetBusinessCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="mybusinessCategoriesList"></a>
# **mybusinessCategoriesList**
> ListBusinessCategoriesResponse mybusinessCategoriesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, pageSize, pageToken, regionCode, searchTerm, view)



Returns a list of business categories. Search will match the category name but not the category ID. *Note:* Search only matches the front of a category name (that is, &#39;food&#39; may return &#39;Food Court&#39; but not &#39;Fast Food Restaurant&#39;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://mybusiness.googleapis.com");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
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
    String languageCode = "languageCode_example"; // String | The BCP 47 code of language. If the language is not available, it will default to English.
    Integer pageSize = 56; // Integer | How many categories to fetch per page. Default is 100, minimum is 1, and maximum page size is 100.
    String pageToken = "pageToken_example"; // String | If specified, the next page of categories will be fetched.
    String regionCode = "regionCode_example"; // String | The ISO 3166-1 alpha-2 country code.
    String searchTerm = "searchTerm_example"; // String | Optional filter string from user.
    String view = "CATEGORY_VIEW_UNSPECIFIED"; // String | Optional. Specifies which parts to the Category resource should be returned in the response.
    try {
      ListBusinessCategoriesResponse result = apiInstance.mybusinessCategoriesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, pageSize, pageToken, regionCode, searchTerm, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#mybusinessCategoriesList");
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
| **languageCode** | **String**| The BCP 47 code of language. If the language is not available, it will default to English. | [optional] |
| **pageSize** | **Integer**| How many categories to fetch per page. Default is 100, minimum is 1, and maximum page size is 100. | [optional] |
| **pageToken** | **String**| If specified, the next page of categories will be fetched. | [optional] |
| **regionCode** | **String**| The ISO 3166-1 alpha-2 country code. | [optional] |
| **searchTerm** | **String**| Optional filter string from user. | [optional] |
| **view** | **String**| Optional. Specifies which parts to the Category resource should be returned in the response. | [optional] [enum: CATEGORY_VIEW_UNSPECIFIED, BASIC, FULL] |

### Return type

[**ListBusinessCategoriesResponse**](ListBusinessCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

