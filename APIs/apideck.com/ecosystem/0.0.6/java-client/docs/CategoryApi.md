# CategoryApi

All URIs are relative to *https://api.apideck.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**categoriesAll**](CategoryApi.md#categoriesAll) | **GET** /ecosystems/{ecosystem_id}/categories | List categories |
| [**categoriesOne**](CategoryApi.md#categoriesOne) | **GET** /ecosystems/{ecosystem_id}/categories/{id} | Get category |
| [**categoryListingsAll**](CategoryApi.md#categoryListingsAll) | **GET** /ecosystems/{ecosystem_id}/categories/{id}/listings | List category listings |


<a id="categoriesAll"></a>
# **categoriesAll**
> GetCategoriesResponse categoriesAll(ecosystemId, cursor, limit)

List categories

List categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apideck.com");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String ecosystemId = "ecosystemId_example"; // String | 
    String cursor = "cursor_example"; // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    Integer limit = 50; // Integer | Number of records to return
    try {
      GetCategoriesResponse result = apiInstance.categoriesAll(ecosystemId, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoriesAll");
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
| **ecosystemId** | **String**|  | |
| **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] |
| **limit** | **Integer**| Number of records to return | [optional] [default to 50] |

### Return type

[**GetCategoriesResponse**](GetCategoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Categories |  -  |

<a id="categoriesOne"></a>
# **categoriesOne**
> GetCategoryResponse categoriesOne(ecosystemId, id)

Get category

Get category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apideck.com");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String ecosystemId = "ecosystemId_example"; // String | 
    String id = "id_example"; // String | ID of the record you are acting upon.
    try {
      GetCategoryResponse result = apiInstance.categoriesOne(ecosystemId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoriesOne");
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
| **ecosystemId** | **String**|  | |
| **id** | **String**| ID of the record you are acting upon. | |

### Return type

[**GetCategoryResponse**](GetCategoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Category |  -  |

<a id="categoryListingsAll"></a>
# **categoryListingsAll**
> GetListingsResponse categoryListingsAll(ecosystemId, id, cursor, limit)

List category listings

List category listings

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apideck.com");

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String ecosystemId = "ecosystemId_example"; // String | 
    String id = "id_example"; // String | ID of the record you are acting upon.
    String cursor = "cursor_example"; // String | Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    Integer limit = 50; // Integer | Number of records to return
    try {
      GetListingsResponse result = apiInstance.categoryListingsAll(ecosystemId, id, cursor, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoryListingsAll");
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
| **ecosystemId** | **String**|  | |
| **id** | **String**| ID of the record you are acting upon. | |
| **cursor** | **String**| Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response. | [optional] |
| **limit** | **Integer**| Number of records to return | [optional] [default to 50] |

### Return type

[**GetListingsResponse**](GetListingsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Listings |  -  |

