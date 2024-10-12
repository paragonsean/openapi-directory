# CreateUserApi

All URIs are relative to *http://okta.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUserInGroup**](CreateUserApi.md#createUserInGroup) | **POST** /api/v1/users | Create User in Group |


<a id="createUserInGroup"></a>
# **createUserInGroup**
> createUserInGroup(activate, createUserInGroupRequest)

Create User in Group

Create User in Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreateUserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://okta.local");

    CreateUserApi apiInstance = new CreateUserApi(defaultClient);
    String activate = "false"; // String | 
    CreateUserInGroupRequest createUserInGroupRequest = new CreateUserInGroupRequest(); // CreateUserInGroupRequest | 
    try {
      apiInstance.createUserInGroup(activate, createUserInGroupRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreateUserApi#createUserInGroup");
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
| **activate** | **String**|  | [optional] |
| **createUserInGroupRequest** | [**CreateUserInGroupRequest**](CreateUserInGroupRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

