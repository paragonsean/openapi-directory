# GymApi

All URIs are relative to *https://tl-api.azurewebsites.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**gymGet**](GymApi.md#gymGet) | **GET** /api/Gym/{gymID} | Get gym details This will return all properties related to gym entity              |


<a id="gymGet"></a>
# **gymGet**
> DefaultResponseDTOOfGymDTO gymGet(gymID)

Get gym details This will return all properties related to gym entity             

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GymApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tl-api.azurewebsites.net");
    
    // Configure OAuth2 access token for authorization: bearer
    OAuth bearer = (OAuth) defaultClient.getAuthentication("bearer");
    bearer.setAccessToken("YOUR ACCESS TOKEN");

    GymApi apiInstance = new GymApi(defaultClient);
    Integer gymID = 56; // Integer | indentity number (primary key) for gym object
    try {
      DefaultResponseDTOOfGymDTO result = apiInstance.gymGet(gymID);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GymApi#gymGet");
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
| **gymID** | **Integer**| indentity number (primary key) for gym object | |

### Return type

[**DefaultResponseDTOOfGymDTO**](DefaultResponseDTOOfGymDTO.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | API Response with Gym entity |  -  |
| **404** |  |  -  |

