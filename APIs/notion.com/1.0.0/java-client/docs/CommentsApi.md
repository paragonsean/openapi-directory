# CommentsApi

All URIs are relative to *https://api.notion.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retrieveComments**](CommentsApi.md#retrieveComments) | **GET** /v1/comments | Retrieve comments |


<a id="retrieveComments"></a>
# **retrieveComments**
> RetrieveComments200Response retrieveComments(blockId, pageSize, notionVersion)

Retrieve comments

Retrieve a user object using the ID specified in the request path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.notion.com");

    CommentsApi apiInstance = new CommentsApi(defaultClient);
    String blockId = "{{BLOCK_ID}}"; // String | 
    String pageSize = "100"; // String | 
    String notionVersion = "{{NOTION_VERSION}}"; // String | 
    try {
      RetrieveComments200Response result = apiInstance.retrieveComments(blockId, pageSize, notionVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommentsApi#retrieveComments");
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
| **blockId** | **String**|  | [optional] |
| **pageSize** | **String**|  | [optional] |
| **notionVersion** | **String**|  | [optional] |

### Return type

[**RetrieveComments200Response**](RetrieveComments200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success - Retrieve a comment |  * Connection -  <br>  * Content-Length -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * ETag -  <br>  * Keep-Alive -  <br>  * Referrer-Policy -  <br>  * Strict-Transport-Security -  <br>  * Vary -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-Permitted-Cross-Domain-Policies -  <br>  * X-XSS-Protection -  <br>  |

