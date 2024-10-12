# SecurityApi

All URIs are relative to *https://skynewz-api-fortnite.herokuapp.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**oauthTokenPost**](SecurityApi.md#oauthTokenPost) | **POST** /oauth/token | Get a Bearer token |


<a id="oauthTokenPost"></a>
# **oauthTokenPost**
> OauthTokenPost200Response oauthTokenPost(email, password)

Get a Bearer token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SecurityApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://skynewz-api-fortnite.herokuapp.com/api");

    SecurityApi apiInstance = new SecurityApi(defaultClient);
    String email = "email_example"; // String | 
    String password = "password_example"; // String | 
    try {
      OauthTokenPost200Response result = apiInstance.oauthTokenPost(email, password);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SecurityApi#oauthTokenPost");
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
| **email** | **String**|  | |
| **password** | **String**|  | |

### Return type

[**OauthTokenPost200Response**](OauthTokenPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded, application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Your access token |  -  |
| **401** | Authentication failed |  -  |
| **404** | Authentication failed. User not found |  -  |

