# UsersApi

All URIs are relative to *https://api.notion.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retrieveAUser**](UsersApi.md#retrieveAUser) | **GET** /v1/users/{id} | Retrieve a user |


<a id="retrieveAUser"></a>
# **retrieveAUser**
> RetrieveAUser200Response retrieveAUser(id, notionVersion)

Retrieve a user

Retrieve a user object using the ID specified in the request path.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.notion.com");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String id = "{{USER_ID}}"; // String | 
    String notionVersion = "{{NOTION_VERSION}}"; // String | 
    try {
      RetrieveAUser200Response result = apiInstance.retrieveAUser(id, notionVersion);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#retrieveAUser");
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
| **id** | **String**|  | |
| **notionVersion** | **String**|  | [optional] |

### Return type

[**RetrieveAUser200Response**](RetrieveAUser200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success - Retrieve a user |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Security-Policy -  <br>  * Date -  <br>  * ETag -  <br>  * Expect-CT -  <br>  * Referrer-Policy -  <br>  * Server -  <br>  * Set-Cookie -  <br>  * Strict-Transport-Security -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Content-Security-Policy -  <br>  * X-Content-Type-Options -  <br>  * X-DNS-Prefetch-Control -  <br>  * X-Download-Options -  <br>  * X-Frame-Options -  <br>  * X-WebKit-CSP -  <br>  * X-XSS-Protection -  <br>  |

