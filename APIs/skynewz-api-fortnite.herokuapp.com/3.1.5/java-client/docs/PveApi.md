# PveApi

All URIs are relative to *https://skynewz-api-fortnite.herokuapp.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**pveInfoGet**](PveApi.md#pveInfoGet) | **GET** /pve/info | Get Fortnite PVE Info (storm, etc) |
| [**pveUserUsernameGet**](PveApi.md#pveUserUsernameGet) | **GET** /pve/user/{username} | Get PVE Stat by given username |


<a id="pveInfoGet"></a>
# **pveInfoGet**
> Object pveInfoGet()

Get Fortnite PVE Info (storm, etc)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://skynewz-api-fortnite.herokuapp.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    PveApi apiInstance = new PveApi(defaultClient);
    try {
      Object result = apiInstance.pveInfoGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PveApi#pveInfoGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All okay |  -  |
| **0** | Unexpected error |  -  |

<a id="pveUserUsernameGet"></a>
# **pveUserUsernameGet**
> Object pveUserUsernameGet(username)

Get PVE Stat by given username

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PveApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://skynewz-api-fortnite.herokuapp.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    PveApi apiInstance = new PveApi(defaultClient);
    String username = "username_example"; // String | Fortnite username
    try {
      Object result = apiInstance.pveUserUsernameGet(username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PveApi#pveUserUsernameGet");
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
| **username** | **String**| Fortnite username | |

### Return type

**Object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | All okay |  -  |
| **404** | User not found or not found on this plateform |  -  |
| **0** | Unexpected error |  -  |

