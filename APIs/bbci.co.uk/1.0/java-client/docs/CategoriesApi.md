# CategoriesApi

All URIs are relative to *https://ibl.api.bbci.co.uk/ibl/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCategories**](CategoriesApi.md#getCategories) | **GET** /categories | Get categories |
| [**getSubCategories**](CategoriesApi.md#getSubCategories) | **GET** /categories/{category} | Get sub-categories |


<a id="getCategories"></a>
# **getCategories**
> Object getCategories(lang)

Get categories

Get the list of all the categories in TV &amp; iPlayer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String lang = "en"; // String | The language for any applicable localised strings.
    try {
      Object result = apiInstance.getCategories(lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#getCategories");
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
| **lang** | **String**| The language for any applicable localised strings. | [enum: en, cy, ga, gd, pi] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

<a id="getSubCategories"></a>
# **getSubCategories**
> Object getSubCategories(category, lang)

Get sub-categories

Get sub-categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://ibl.api.bbci.co.uk/ibl/v1");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String category = "category_example"; // String | The category identifier to return results from.
    String lang = "en"; // String | The language for any applicable localised strings.
    try {
      Object result = apiInstance.getSubCategories(category, lang);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#getSubCategories");
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
| **category** | **String**| The category identifier to return results from. | |
| **lang** | **String**| The language for any applicable localised strings. | [enum: en, cy, ga, gd, pi] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Default response |  -  |

