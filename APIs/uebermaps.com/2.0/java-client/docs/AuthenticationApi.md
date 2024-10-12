# AuthenticationApi

All URIs are relative to *http://uebermaps.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**authenticationPost**](AuthenticationApi.md#authenticationPost) | **POST** /authentication | Sign in user |


<a id="authenticationPost"></a>
# **authenticationPost**
> UserFullProfile authenticationPost(user)

Sign in user

Sign in user. Wrap authentication parameters in [user].

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://uebermaps.com/api/v2");

    AuthenticationApi apiInstance = new AuthenticationApi(defaultClient);
    UserAuthentication user = new UserAuthentication(); // UserAuthentication | user authentication attributes
    try {
      UserFullProfile result = apiInstance.authenticationPost(user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationApi#authenticationPost");
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
| **user** | [**UserAuthentication**](UserAuthentication.md)| user authentication attributes | |

### Return type

[**UserFullProfile**](UserFullProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Contains user data including authentication token for subsequent requests |  -  |

