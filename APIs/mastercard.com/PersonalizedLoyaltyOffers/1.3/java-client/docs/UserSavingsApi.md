# UserSavingsApi

All URIs are relative to *https://api.mastercard.com/plo/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersavingsGet**](UserSavingsApi.md#usersavingsGet) | **GET** /usersavings | Returns Savings for the User |


<a id="usersavingsGet"></a>
# **usersavingsGet**
> UserSavingsResponse usersavingsGet(fid, userToken)

Returns Savings for the User

This resource returns the accumulated and potential savings for a Personalized Offers user. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserSavingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/plo/v1");

    UserSavingsApi apiInstance = new UserSavingsApi(defaultClient);
    String fid = "999999"; // String | Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation.
    String userToken = "userToken_example"; // String | Session identifier as returned by the UserToken resource.
    try {
      UserSavingsResponse result = apiInstance.usersavingsGet(fid, userToken);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserSavingsApi#usersavingsGet");
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
| **fid** | **String**| Financial Institution Identifier. Code that specifies the platform and configuration instance, provided by Mastercard during implementation. | |
| **userToken** | **String**| Session identifier as returned by the UserToken resource. | |

### Return type

[**UserSavingsResponse**](UserSavingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | This resource returns the accumulated and potential savings for a Personalized Offers user. |  -  |
| **0** | Unexpected error |  -  |

