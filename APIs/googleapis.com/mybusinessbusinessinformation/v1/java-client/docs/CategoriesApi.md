# CategoriesApi

All URIs are relative to *https://mybusinessbusinessinformation.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**mybusinessbusinessinformationCategoriesBatchGet**](CategoriesApi.md#mybusinessbusinessinformationCategoriesBatchGet) | **GET** /v1/categories:batchGet |  |
| [**mybusinessbusinessinformationCategoriesList**](CategoriesApi.md#mybusinessbusinessinformationCategoriesList) | **GET** /v1/categories |  |


<a id="mybusinessbusinessinformationCategoriesBatchGet"></a>
# **mybusinessbusinessinformationCategoriesBatchGet**
> BatchGetCategoriesResponse mybusinessbusinessinformationCategoriesBatchGet($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, names, regionCode, view)



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
    defaultClient.setBasePath("https://mybusinessbusinessinformation.googleapis.com");

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
    String languageCode = "languageCode_example"; // String | Required. The BCP 47 code of language that the category names should be returned in.
    List<String> names = Arrays.asList(); // List<String> | Required. At least one name must be set. The GConcept ids the localized category names should be returned for. To return details for more than one category, repeat this parameter in the request.
    String regionCode = "regionCode_example"; // String | Optional. The ISO 3166-1 alpha-2 country code used to infer non-standard language.
    String view = "CATEGORY_VIEW_UNSPECIFIED"; // String | Required. Specifies which parts to the Category resource should be returned in the response.
    try {
      BatchGetCategoriesResponse result = apiInstance.mybusinessbusinessinformationCategoriesBatchGet($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, languageCode, names, regionCode, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#mybusinessbusinessinformationCategoriesBatchGet");
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
| **languageCode** | **String**| Required. The BCP 47 code of language that the category names should be returned in. | [optional] |
| **names** | [**List&lt;String&gt;**](String.md)| Required. At least one name must be set. The GConcept ids the localized category names should be returned for. To return details for more than one category, repeat this parameter in the request. | [optional] |
| **regionCode** | **String**| Optional. The ISO 3166-1 alpha-2 country code used to infer non-standard language. | [optional] |
| **view** | **String**| Required. Specifies which parts to the Category resource should be returned in the response. | [optional] [enum: CATEGORY_VIEW_UNSPECIFIED, BASIC, FULL] |

### Return type

[**BatchGetCategoriesResponse**](BatchGetCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="mybusinessbusinessinformationCategoriesList"></a>
# **mybusinessbusinessinformationCategoriesList**
> ListCategoriesResponse mybusinessbusinessinformationCategoriesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, languageCode, pageSize, pageToken, regionCode, view)



Returns a list of business categories. Search will match the category name but not the category ID. Search only matches the front of a category name (that is, &#39;food&#39; may return &#39;Food Court&#39; but not &#39;Fast Food Restaurant&#39;).

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
    defaultClient.setBasePath("https://mybusinessbusinessinformation.googleapis.com");

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
    String filter = "filter_example"; // String | Optional. Filter string from user. The only field that supported is `displayName`. Eg: `filter=displayName=foo`.
    String languageCode = "languageCode_example"; // String | Required. The BCP 47 code of language.
    Integer pageSize = 56; // Integer | Optional. How many categories to fetch per page. Default is 100, minimum is 1, and maximum page size is 100.
    String pageToken = "pageToken_example"; // String | Optional. If specified, the next page of categories will be fetched.
    String regionCode = "regionCode_example"; // String | Required. The ISO 3166-1 alpha-2 country code.
    String view = "CATEGORY_VIEW_UNSPECIFIED"; // String | Required. Specifies which parts to the Category resource should be returned in the response.
    try {
      ListCategoriesResponse result = apiInstance.mybusinessbusinessinformationCategoriesList($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, filter, languageCode, pageSize, pageToken, regionCode, view);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#mybusinessbusinessinformationCategoriesList");
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
| **filter** | **String**| Optional. Filter string from user. The only field that supported is &#x60;displayName&#x60;. Eg: &#x60;filter&#x3D;displayName&#x3D;foo&#x60;. | [optional] |
| **languageCode** | **String**| Required. The BCP 47 code of language. | [optional] |
| **pageSize** | **Integer**| Optional. How many categories to fetch per page. Default is 100, minimum is 1, and maximum page size is 100. | [optional] |
| **pageToken** | **String**| Optional. If specified, the next page of categories will be fetched. | [optional] |
| **regionCode** | **String**| Required. The ISO 3166-1 alpha-2 country code. | [optional] |
| **view** | **String**| Required. Specifies which parts to the Category resource should be returned in the response. | [optional] [enum: CATEGORY_VIEW_UNSPECIFIED, BASIC, FULL] |

### Return type

[**ListCategoriesResponse**](ListCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

