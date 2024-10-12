# ThemesCustomColorsApi

All URIs are relative to *https://api.presalytics.io/ooxml-automation*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**themesCustomcolorsGetId**](ThemesCustomColorsApi.md#themesCustomcolorsGetId) | **GET** /Themes/CustomColors/{id} | CustomColors: Get by Id |


<a id="themesCustomcolorsGetId"></a>
# **themesCustomcolorsGetId**
> ThemeCustomColors themesCustomcolorsGetId(id)

CustomColors: Get by Id

Get by Id: Use this method to retrieve a CustomColors object by its primary key (id)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ThemesCustomColorsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.presalytics.io/ooxml-automation");

    ThemesCustomColorsApi apiInstance = new ThemesCustomColorsApi(defaultClient);
    UUID id = UUID.randomUUID(); // UUID | 
    try {
      ThemeCustomColors result = apiInstance.themesCustomcolorsGetId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ThemesCustomColorsApi#themesCustomcolorsGetId");
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

[**ThemeCustomColors**](ThemeCustomColors.md)

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

