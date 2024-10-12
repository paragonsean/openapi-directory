# LoginApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV20LoginGet**](LoginApi.md#apiV20LoginGet) | **GET** /api/v2.0/login |  |


<a id="apiV20LoginGet"></a>
# **apiV20LoginGet**
> apiV20LoginGet(password, username)



Login endpoint, refresh your API token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LoginApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    LoginApi apiInstance = new LoginApi(defaultClient);
    String password = "password_example"; // String | EnteroBase Password
    String username = "username_example"; // String | EnteroBase username
    try {
      apiInstance.apiV20LoginGet(password, username);
    } catch (ApiException e) {
      System.err.println("Exception when calling LoginApi#apiV20LoginGet");
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
| **password** | **String**| EnteroBase Password | [optional] |
| **username** | **String**| EnteroBase username | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A login object |  -  |
| **403** | Unauthorised access for this specific resource or data |  -  |

