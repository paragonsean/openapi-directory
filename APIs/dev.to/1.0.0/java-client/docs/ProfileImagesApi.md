# ProfileImagesApi

All URIs are relative to *https://dev.to/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getProfileImage**](ProfileImagesApi.md#getProfileImage) | **GET** /api/profile_images/{username} | A Users or organizations profile image |


<a id="getProfileImage"></a>
# **getProfileImage**
> List&lt;ProfileImage&gt; getProfileImage(username)

A Users or organizations profile image

This endpoint allows the client to retrieve a user or organization profile image information by its         corresponding username.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProfileImagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dev.to/api");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    ProfileImagesApi apiInstance = new ProfileImagesApi(defaultClient);
    String username = "janedoe"; // String | The parameter is the username of the user or the username of the organization.
    try {
      List<ProfileImage> result = apiInstance.getProfileImage(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProfileImagesApi#getProfileImage");
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
| **username** | **String**| The parameter is the username of the user or the username of the organization. | |

### Return type

[**List&lt;ProfileImage&gt;**](ProfileImage.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An object containing profile image details |  -  |
| **404** | Resource Not Found |  -  |

