# UserPagingPoliciesApi

All URIs are relative to *https://api.victorops.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPublicV1UserUserPoliciesGet**](UserPagingPoliciesApi.md#apiPublicV1UserUserPoliciesGet) | **GET** /api-public/v1/user/{user}/policies | Get a list of paging policies for a user |


<a id="apiPublicV1UserUserPoliciesGet"></a>
# **apiPublicV1UserUserPoliciesGet**
> Policies apiPublicV1UserUserPoliciesGet(xVOApiId, xVOApiKey, user)

Get a list of paging policies for a user

Get paging policies for a user  This API may be called a maximum of 60 times per minute. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserPagingPoliciesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.victorops.com");

    UserPagingPoliciesApi apiInstance = new UserPagingPoliciesApi(defaultClient);
    String xVOApiId = "xVOApiId_example"; // String | Your API ID
    String xVOApiKey = "xVOApiKey_example"; // String | Your API Key
    String user = "user_example"; // String | The VictorOps user ID
    try {
      Policies result = apiInstance.apiPublicV1UserUserPoliciesGet(xVOApiId, xVOApiKey, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserPagingPoliciesApi#apiPublicV1UserUserPoliciesGet");
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
| **xVOApiId** | **String**| Your API ID | |
| **xVOApiKey** | **String**| Your API Key | |
| **user** | **String**| The VictorOps user ID | |

### Return type

[**Policies**](Policies.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All configured paging policies for a user |  -  |
| **400** | Problem with the request arguments.  The response payload may include an error message. |  -  |
| **401** | Authentication parameters missing |  -  |
| **403** | Authentication failed or rate-limit reached |  -  |
| **404** | User not found |  -  |
| **500** | Internal Server Error |  -  |

