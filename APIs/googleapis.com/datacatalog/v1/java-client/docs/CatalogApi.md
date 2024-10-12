# CatalogApi

All URIs are relative to *https://datacatalog.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**datacatalogCatalogSearch**](CatalogApi.md#datacatalogCatalogSearch) | **POST** /v1/catalog:search |  |


<a id="datacatalogCatalogSearch"></a>
# **datacatalogCatalogSearch**
> GoogleCloudDatacatalogV1SearchCatalogResponse datacatalogCatalogSearch($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDatacatalogV1SearchCatalogRequest)



Searches Data Catalog for multiple resources like entries and tags that match a query. This is a [Custom Method] (https://cloud.google.com/apis/design/custom_methods) that doesn&#39;t return all information on a resource, only its ID and high level fields. To get more information, you can subsequently call specific get methods. Note: Data Catalog search queries don&#39;t guarantee full recall. Results that match your query might not be returned, even in subsequent result pages. Additionally, returned (and not returned) results can vary if you repeat search queries. For more information, see [Data Catalog search syntax] (https://cloud.google.com/data-catalog/docs/how-to/search-reference).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://datacatalog.googleapis.com");
    
    // Configure OAuth2 access token for authorization: Oauth2c
    OAuth Oauth2c = (OAuth) defaultClient.getAuthentication("Oauth2c");
    Oauth2c.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: Oauth2
    OAuth Oauth2 = (OAuth) defaultClient.getAuthentication("Oauth2");
    Oauth2.setAccessToken("YOUR ACCESS TOKEN");

    CatalogApi apiInstance = new CatalogApi(defaultClient);
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
    GoogleCloudDatacatalogV1SearchCatalogRequest googleCloudDatacatalogV1SearchCatalogRequest = new GoogleCloudDatacatalogV1SearchCatalogRequest(); // GoogleCloudDatacatalogV1SearchCatalogRequest | 
    try {
      GoogleCloudDatacatalogV1SearchCatalogResponse result = apiInstance.datacatalogCatalogSearch($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, googleCloudDatacatalogV1SearchCatalogRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogApi#datacatalogCatalogSearch");
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
| **googleCloudDatacatalogV1SearchCatalogRequest** | [**GoogleCloudDatacatalogV1SearchCatalogRequest**](GoogleCloudDatacatalogV1SearchCatalogRequest.md)|  | [optional] |

### Return type

[**GoogleCloudDatacatalogV1SearchCatalogResponse**](GoogleCloudDatacatalogV1SearchCatalogResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

