# CategoriesApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**categoriesFlatGet**](CategoriesApi.md#categoriesFlatGet) | **GET** /categories/flat |  |
| [**categoriesGet**](CategoriesApi.md#categoriesGet) | **GET** /categories | List of supported product categories |
| [**categoriesProductTypeCategoryGet**](CategoriesApi.md#categoriesProductTypeCategoryGet) | **GET** /categories/{product_type}/{category} | Get subcategory details |
| [**categoriesTaxonomyGet**](CategoriesApi.md#categoriesTaxonomyGet) | **GET** /categories/taxonomy | Full taxonomy tree of categories including middle categories |
| [**categoriesUuidGet**](CategoriesApi.md#categoriesUuidGet) | **GET** /categories/{uuid} | Get category details |


<a id="categoriesFlatGet"></a>
# **categoriesFlatGet**
> categoriesFlatGet()



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
    defaultClient.setBasePath("https://api.reverb.com/api");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    try {
      apiInstance.categoriesFlatGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesFlatGet");
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

<a id="categoriesGet"></a>
# **categoriesGet**
> categoriesGet()

List of supported product categories

List of supported product categories

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
    defaultClient.setBasePath("https://api.reverb.com/api");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    try {
      apiInstance.categoriesGet();
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

<a id="categoriesProductTypeCategoryGet"></a>
# **categoriesProductTypeCategoryGet**
> categoriesProductTypeCategoryGet(productType, category)

Get subcategory details

Get subcategory details

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
    defaultClient.setBasePath("https://api.reverb.com/api");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String productType = "productType_example"; // String | 
    String category = "category_example"; // String | 
    try {
      apiInstance.categoriesProductTypeCategoryGet(productType, category);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesProductTypeCategoryGet");
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
| **productType** | **String**|  | |
| **category** | **String**|  | |

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

<a id="categoriesTaxonomyGet"></a>
# **categoriesTaxonomyGet**
> categoriesTaxonomyGet()

Full taxonomy tree of categories including middle categories

Full taxonomy tree of categories including middle categories

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
    defaultClient.setBasePath("https://api.reverb.com/api");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    try {
      apiInstance.categoriesTaxonomyGet();
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesTaxonomyGet");
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

<a id="categoriesUuidGet"></a>
# **categoriesUuidGet**
> categoriesUuidGet(uuid)

Get category details

Get category details

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
    defaultClient.setBasePath("https://api.reverb.com/api");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String uuid = "uuid_example"; // String | 
    try {
      apiInstance.categoriesUuidGet(uuid);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#categoriesUuidGet");
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
| **uuid** | **String**|  | |

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

