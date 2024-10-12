# EntitiesApi

All URIs are relative to *https://kgsearch.googleapis.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**kgsearchEntitiesSearch**](EntitiesApi.md#kgsearchEntitiesSearch) | **GET** /v1/entities:search |  |


<a id="kgsearchEntitiesSearch"></a>
# **kgsearchEntitiesSearch**
> SearchResponse kgsearchEntitiesSearch($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, ids, indent, languages, limit, prefix, query, types)



Searches Knowledge Graph for entities that match the constraints. A list of matched entities will be returned in response, which will be in JSON-LD format and compatible with http://schema.org

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EntitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kgsearch.googleapis.com");

    EntitiesApi apiInstance = new EntitiesApi(defaultClient);
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
    List<String> ids = Arrays.asList(); // List<String> | The list of entity id to be used for search instead of query string. To specify multiple ids in the HTTP request, repeat the parameter in the URL as in ...?ids=A&ids=B
    Boolean indent = true; // Boolean | Enables indenting of json results.
    List<String> languages = Arrays.asList(); // List<String> | The list of language codes (defined in ISO 693) to run the query with, e.g. 'en'.
    Integer limit = 56; // Integer | Limits the number of entities to be returned.
    Boolean prefix = true; // Boolean | Enables prefix match against names and aliases of entities
    String query = "query_example"; // String | The literal query string for search.
    List<String> types = Arrays.asList(); // List<String> | Restricts returned entities with these types, e.g. Person (as defined in http://schema.org/Person). If multiple types are specified, returned entities will contain one or more of these types.
    try {
      SearchResponse result = apiInstance.kgsearchEntitiesSearch($xgafv, accessToken, alt, paramCallback, fields, key, oauthToken, prettyPrint, quotaUser, uploadProtocol, uploadType, ids, indent, languages, limit, prefix, query, types);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EntitiesApi#kgsearchEntitiesSearch");
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
| **ids** | [**List&lt;String&gt;**](String.md)| The list of entity id to be used for search instead of query string. To specify multiple ids in the HTTP request, repeat the parameter in the URL as in ...?ids&#x3D;A&amp;ids&#x3D;B | [optional] |
| **indent** | **Boolean**| Enables indenting of json results. | [optional] |
| **languages** | [**List&lt;String&gt;**](String.md)| The list of language codes (defined in ISO 693) to run the query with, e.g. &#39;en&#39;. | [optional] |
| **limit** | **Integer**| Limits the number of entities to be returned. | [optional] |
| **prefix** | **Boolean**| Enables prefix match against names and aliases of entities | [optional] |
| **query** | **String**| The literal query string for search. | [optional] |
| **types** | [**List&lt;String&gt;**](String.md)| Restricts returned entities with these types, e.g. Person (as defined in http://schema.org/Person). If multiple types are specified, returned entities will contain one or more of these types. | [optional] |

### Return type

[**SearchResponse**](SearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

