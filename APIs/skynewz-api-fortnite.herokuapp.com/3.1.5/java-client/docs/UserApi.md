# UserApi

All URIs are relative to *https://skynewz-api-fortnite.herokuapp.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userPlateformUsernameGet**](UserApi.md#userPlateformUsernameGet) | **GET** /user/{plateform}/{username} | Get a user by username |


<a id="userPlateformUsernameGet"></a>
# **userPlateformUsernameGet**
> UserPlateformUsernameGet200Response userPlateformUsernameGet(plateform, username)

Get a user by username

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
    defaultClient.setBasePath("https://skynewz-api-fortnite.herokuapp.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    UserApi apiInstance = new UserApi(defaultClient);
    String plateform = "plateform_example"; // String | Playing plateform, can be xb1, ps4 or pc
    String username = "username_example"; // String | Player username
    try {
      UserPlateformUsernameGet200Response result = apiInstance.userPlateformUsernameGet(plateform, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userPlateformUsernameGet");
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
| **plateform** | **String**| Playing plateform, can be xb1, ps4 or pc | |
| **username** | **String**| Player username | |

### Return type

[**UserPlateformUsernameGet200Response**](UserPlateformUsernameGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | JSON Object of user |  -  |
| **404** | User not found or not found on this plateform |  -  |
| **0** | Unexpected error |  -  |

