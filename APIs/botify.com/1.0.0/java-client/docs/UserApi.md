# UserApi

All URIs are relative to *https://api.botify.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getUserProjects**](UserApi.md#getUserProjects) | **GET** /projects/{username} | List all active projects for the user |


<a id="getUserProjects"></a>
# **getUserProjects**
> GetUserProjects200Response getUserProjects(username, page, size)

List all active projects for the user

List all active projects for the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.botify.com/v1");
    
    // Configure API key authorization: DjangoRestToken
    ApiKeyAuth DjangoRestToken = (ApiKeyAuth) defaultClient.getAuthentication("DjangoRestToken");
    DjangoRestToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //DjangoRestToken.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String username = "username_example"; // String | User's identifier
    Integer page = 56; // Integer | Page Number
    Integer size = 56; // Integer | Page Size
    try {
      GetUserProjects200Response result = apiInstance.getUserProjects(username, page, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#getUserProjects");
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
| **username** | **String**| User&#39;s identifier | |
| **page** | **Integer**| Page Number | [optional] |
| **size** | **Integer**| Page Size | [optional] |

### Return type

[**GetUserProjects200Response**](GetUserProjects200Response.md)

### Authorization

[DjangoRestToken](../README.md#DjangoRestToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **0** | error payload |  -  |

