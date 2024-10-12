# RequestApiKeyApi

All URIs are relative to *http://api.climatekuul.com:8000/footprint*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**requestApiKey**](RequestApiKeyApi.md#requestApiKey) | **POST** /requestApiKey | requestApiKey |


<a id="requestApiKey"></a>
# **requestApiKey**
> requestApiKey(apiKeyL1, apiKeyL2, email, password, userFirstName, userLastName)

requestApiKey

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RequestApiKeyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    RequestApiKeyApi apiInstance = new RequestApiKeyApi(defaultClient);
    String apiKeyL1 = "apiKeyL1_example"; // String | Api Key for client
    String apiKeyL2 = "apiKeyL2_example"; // String | Integration Partner Api Key
    String email = "email_example"; // String | User email
    Integer password = 56; // Integer | User password
    String userFirstName = "userFirstName_example"; // String | User first name
    String userLastName = "userLastName_example"; // String | User last name
    try {
      apiInstance.requestApiKey(apiKeyL1, apiKeyL2, email, password, userFirstName, userLastName);
    } catch (ApiException e) {
      System.err.println("Exception when calling RequestApiKeyApi#requestApiKey");
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
| **apiKeyL1** | **String**| Api Key for client | |
| **apiKeyL2** | **String**| Integration Partner Api Key | |
| **email** | **String**| User email | |
| **password** | **Integer**| User password | |
| **userFirstName** | **String**| User first name | |
| **userLastName** | **String**| User last name | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

