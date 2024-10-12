# SessionManagementApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sessionsPost**](SessionManagementApi.md#sessionsPost) | **POST** /sessions/ | Update Order Configuration |


<a id="sessionsPost"></a>
# **sessionsPost**
> Object sessionsPost(contentType, accept, requestBody)

Update Order Configuration

Updates the Order Configuration. You should use this route every time you edit a configuration value

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SessionManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    SessionManagementApi apiInstance = new SessionManagementApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    RequestBody requestBody = new RequestBody(); // RequestBody | 
    try {
      Object result = apiInstance.sessionsPost(contentType, accept, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SessionManagementApi#sessionsPost");
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
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand | [default to application/json] |
| **requestBody** | [**RequestBody**](RequestBody.md)|  | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

