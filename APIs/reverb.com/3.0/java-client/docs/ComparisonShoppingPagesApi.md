# ComparisonShoppingPagesApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**comparisonShoppingPagesFindGet**](ComparisonShoppingPagesApi.md#comparisonShoppingPagesFindGet) | **GET** /comparison_shopping_pages/find | Show comparison shopping page |
| [**comparisonShoppingPagesGet**](ComparisonShoppingPagesApi.md#comparisonShoppingPagesGet) | **GET** /comparison_shopping_pages | Returns a set of comparison shopping pages based on the current params |
| [**comparisonShoppingPagesIdGet**](ComparisonShoppingPagesApi.md#comparisonShoppingPagesIdGet) | **GET** /comparison_shopping_pages/{id} |  |
| [**comparisonShoppingPagesIdListingsGet**](ComparisonShoppingPagesApi.md#comparisonShoppingPagesIdListingsGet) | **GET** /comparison_shopping_pages/{id}/listings | Return new or used listings for a comparison shopping page |
| [**comparisonShoppingPagesIdReviewsGet**](ComparisonShoppingPagesApi.md#comparisonShoppingPagesIdReviewsGet) | **GET** /comparison_shopping_pages/{id}/reviews | View reviews of a comparison shopping page |


<a id="comparisonShoppingPagesFindGet"></a>
# **comparisonShoppingPagesFindGet**
> comparisonShoppingPagesFindGet(id, slug)

Show comparison shopping page

Show comparison shopping page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComparisonShoppingPagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ComparisonShoppingPagesApi apiInstance = new ComparisonShoppingPagesApi(defaultClient);
    String id = "id_example"; // String | ID of the comparison shopping page
    String slug = "slug_example"; // String | Slug of the comparison shopping page
    try {
      apiInstance.comparisonShoppingPagesFindGet(id, slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComparisonShoppingPagesApi#comparisonShoppingPagesFindGet");
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
| **id** | **String**| ID of the comparison shopping page | [optional] |
| **slug** | **String**| Slug of the comparison shopping page | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="comparisonShoppingPagesGet"></a>
# **comparisonShoppingPagesGet**
> comparisonShoppingPagesGet()

Returns a set of comparison shopping pages based on the current params

Returns a set of comparison shopping pages based on the current params

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComparisonShoppingPagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ComparisonShoppingPagesApi apiInstance = new ComparisonShoppingPagesApi(defaultClient);
    try {
      apiInstance.comparisonShoppingPagesGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling ComparisonShoppingPagesApi#comparisonShoppingPagesGet");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="comparisonShoppingPagesIdGet"></a>
# **comparisonShoppingPagesIdGet**
> comparisonShoppingPagesIdGet(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComparisonShoppingPagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ComparisonShoppingPagesApi apiInstance = new ComparisonShoppingPagesApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.comparisonShoppingPagesIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComparisonShoppingPagesApi#comparisonShoppingPagesIdGet");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="comparisonShoppingPagesIdListingsGet"></a>
# **comparisonShoppingPagesIdListingsGet**
> comparisonShoppingPagesIdListingsGet(id, condition, page, perPage, offset)

Return new or used listings for a comparison shopping page

Return new or used listings for a comparison shopping page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComparisonShoppingPagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ComparisonShoppingPagesApi apiInstance = new ComparisonShoppingPagesApi(defaultClient);
    String id = "id_example"; // String | 
    String condition = "condition_example"; // String | Condition of the listing
    Integer page = 1; // Integer | 
    Integer perPage = 24; // Integer | 
    Integer offset = 56; // Integer | 
    try {
      apiInstance.comparisonShoppingPagesIdListingsGet(id, condition, page, perPage, offset);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComparisonShoppingPagesApi#comparisonShoppingPagesIdListingsGet");
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
| **id** | **String**|  | |
| **condition** | **String**| Condition of the listing | |
| **page** | **Integer**|  | [optional] [default to 1] |
| **perPage** | **Integer**|  | [optional] [default to 24] |
| **offset** | **Integer**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="comparisonShoppingPagesIdReviewsGet"></a>
# **comparisonShoppingPagesIdReviewsGet**
> comparisonShoppingPagesIdReviewsGet(id)

View reviews of a comparison shopping page

View reviews of a comparison shopping page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ComparisonShoppingPagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ComparisonShoppingPagesApi apiInstance = new ComparisonShoppingPagesApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.comparisonShoppingPagesIdReviewsGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ComparisonShoppingPagesApi#comparisonShoppingPagesIdReviewsGet");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

