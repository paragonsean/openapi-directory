# StatsApi

All URIs are relative to *https://skynewz-api-fortnite.herokuapp.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**statsIdPlateformIdGet**](StatsApi.md#statsIdPlateformIdGet) | **GET** /stats/id/{plateform}/{id} | Get user&#39;s stats by user id |
| [**statsPlateformUsernameGet**](StatsApi.md#statsPlateformUsernameGet) | **GET** /stats/{plateform}/{username} | Get user&#39;s stats by username |


<a id="statsIdPlateformIdGet"></a>
# **statsIdPlateformIdGet**
> StatsIdPlateformIdGet200Response statsIdPlateformIdGet(plateform, id)

Get user&#39;s stats by user id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://skynewz-api-fortnite.herokuapp.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String plateform = "plateform_example"; // String | Playing plateform, can be xb1, ps4 or pc
    String id = "id_example"; // String | Player ID
    try {
      StatsIdPlateformIdGet200Response result = apiInstance.statsIdPlateformIdGet(plateform, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#statsIdPlateformIdGet");
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
| **id** | **String**| Player ID | |

### Return type

[**StatsIdPlateformIdGet200Response**](StatsIdPlateformIdGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | JSON Object of user stats |  -  |
| **400** | Please precise a good platform: ps4/xb1/pc |  -  |
| **404** | User not found or not found on this plateform |  -  |
| **0** | Unexpected error |  -  |

<a id="statsPlateformUsernameGet"></a>
# **statsPlateformUsernameGet**
> StatsIdPlateformIdGet200Response statsPlateformUsernameGet(plateform, username)

Get user&#39;s stats by username

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://skynewz-api-fortnite.herokuapp.com/api");
    
    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    StatsApi apiInstance = new StatsApi(defaultClient);
    String plateform = "plateform_example"; // String | Playing plateform, can be xb1, ps4 or pc
    String username = "username_example"; // String | Player username
    try {
      StatsIdPlateformIdGet200Response result = apiInstance.statsPlateformUsernameGet(plateform, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatsApi#statsPlateformUsernameGet");
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

[**StatsIdPlateformIdGet200Response**](StatsIdPlateformIdGet200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | JSON Object of user stats |  -  |
| **400** | Please precise a good platform: ps4/xb1/pc |  -  |
| **404** | User not found or not found on this plateform |  -  |
| **0** | Unexpected error |  -  |

