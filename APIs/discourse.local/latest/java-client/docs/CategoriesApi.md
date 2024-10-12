# CategoriesApi

All URIs are relative to *http://discourse.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCategory**](CategoriesApi.md#createCategory) | **POST** /categories.json | Creates a category |
| [**getCategory**](CategoriesApi.md#getCategory) | **GET** /c/{id}/show.json | Show category |
| [**getSite_0**](CategoriesApi.md#getSite_0) | **GET** /site.json | Get site info |
| [**listCategories**](CategoriesApi.md#listCategories) | **GET** /categories.json | Retrieves a list of categories |
| [**listCategoryTopics**](CategoriesApi.md#listCategoryTopics) | **GET** /c/{slug}/{id}.json | List topics |
| [**updateCategory**](CategoriesApi.md#updateCategory) | **PUT** /categories/{id}.json | Updates a category |


<a id="createCategory"></a>
# **createCategory**
> GetCategory200Response createCategory(createCategoryRequest)

Creates a category

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
    defaultClient.setBasePath("http://discourse.local");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    CreateCategoryRequest createCategoryRequest = new CreateCategoryRequest(); // CreateCategoryRequest | 
    try {
      GetCategory200Response result = apiInstance.createCategory(createCategoryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#createCategory");
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
| **createCategoryRequest** | [**CreateCategoryRequest**](CreateCategoryRequest.md)|  | [optional] |

### Return type

[**GetCategory200Response**](GetCategory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="getCategory"></a>
# **getCategory**
> GetCategory200Response getCategory(id)

Show category

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
    defaultClient.setBasePath("http://discourse.local");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    Integer id = 56; // Integer | 
    try {
      GetCategory200Response result = apiInstance.getCategory(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#getCategory");
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
| **id** | **Integer**|  | |

### Return type

[**GetCategory200Response**](GetCategory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | response |  -  |

<a id="getSite_0"></a>
# **getSite_0**
> GetSite200Response getSite_0()

Get site info

Can be used to fetch all categories and subcategories

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
    defaultClient.setBasePath("http://discourse.local");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    try {
      GetSite200Response result = apiInstance.getSite_0();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#getSite_0");
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

[**GetSite200Response**](GetSite200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="listCategories"></a>
# **listCategories**
> ListCategories200Response listCategories(includeSubcategories)

Retrieves a list of categories

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
    defaultClient.setBasePath("http://discourse.local");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    Boolean includeSubcategories = true; // Boolean | 
    try {
      ListCategories200Response result = apiInstance.listCategories(includeSubcategories);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#listCategories");
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
| **includeSubcategories** | **Boolean**|  | [optional] [enum: true] |

### Return type

[**ListCategories200Response**](ListCategories200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="listCategoryTopics"></a>
# **listCategoryTopics**
> ListCategoryTopics200Response listCategoryTopics(slug, id)

List topics

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
    defaultClient.setBasePath("http://discourse.local");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String slug = "slug_example"; // String | 
    Integer id = 56; // Integer | 
    try {
      ListCategoryTopics200Response result = apiInstance.listCategoryTopics(slug, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#listCategoryTopics");
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
| **slug** | **String**|  | |
| **id** | **Integer**|  | |

### Return type

[**ListCategoryTopics200Response**](ListCategoryTopics200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

<a id="updateCategory"></a>
# **updateCategory**
> UpdateCategory200Response updateCategory(id, createCategoryRequest)

Updates a category

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
    defaultClient.setBasePath("http://discourse.local");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    Integer id = 56; // Integer | 
    CreateCategoryRequest createCategoryRequest = new CreateCategoryRequest(); // CreateCategoryRequest | 
    try {
      UpdateCategory200Response result = apiInstance.updateCategory(id, createCategoryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#updateCategory");
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
| **id** | **Integer**|  | |
| **createCategoryRequest** | [**CreateCategoryRequest**](CreateCategoryRequest.md)|  | [optional] |

### Return type

[**UpdateCategory200Response**](UpdateCategory200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | success response |  -  |

