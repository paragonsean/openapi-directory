# ThemesLineMapApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**themesLinemapGetId**](ThemesLineMapApi.md#themesLinemapGetId) | **GET** /Themes/LineMap/{id} | LineMap: Get by Id |


<a id="themesLinemapGetId"></a>
# **themesLinemapGetId**
> ThemeLineMap themesLinemapGetId(id)

LineMap: Get by Id

Get by Id: Use this method to retrieve a LineMap object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThemesLineMapApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ThemesLineMapApi apiInstance = new ThemesLineMapApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      ThemeLineMap result = apiInstance.themesLinemapGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThemesLineMapApi#themesLinemapGetId");
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
| **id** | **UUID**|  | |

### Return type

[**ThemeLineMap**](ThemeLineMap.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

