# CategoriesApi

All URIs are relative to *https://rms.api.bbc.co.uk*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**categoriesGet**](CategoriesApi.md#categoriesGet) | **GET** /categories | List of categories |
| [**categoriesIdGet**](CategoriesApi.md#categoriesIdGet) | **GET** /categories/{id} | Category by ID |


<a id="categoriesGet"></a>
# **categoriesGet**
> CategoriesResponse categoriesGet(xAPIKey, kind)

List of categories

Retrieve Categories 

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
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String kind = "promoted"; // String | Filter by provided query. E.g. 'promoted' returns promoted categories
    try {
      CategoriesResponse result = apiInstance.categoriesGet(xAPIKey, kind);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesGet");
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
| **xAPIKey** | **String**| API_KEY | |
| **kind** | **String**| Filter by provided query. E.g. &#39;promoted&#39; returns promoted categories | [optional] [enum: promoted] |

### Return type

[**CategoriesResponse**](CategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

<a id="categoriesIdGet"></a>
# **categoriesIdGet**
> CategoriesResponse categoriesIdGet(xAPIKey, id)

Category by ID

Retrieve Categories by ID 

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
    defaultClient.setBasePath("https://rms.api.bbc.co.uk");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String xAPIKey = "xAPIKey_example"; // String | API_KEY
    String id = "id_example"; // String | Retrieve information about the category. E.g. 'sport-football-europeanchampionship'
    try {
      CategoriesResponse result = apiInstance.categoriesIdGet(xAPIKey, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesIdGet");
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
| **xAPIKey** | **String**| API_KEY | |
| **id** | **String**| Retrieve information about the category. E.g. &#39;sport-football-europeanchampionship&#39; | |

### Return type

[**CategoriesResponse**](CategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Unexpected error |  -  |

