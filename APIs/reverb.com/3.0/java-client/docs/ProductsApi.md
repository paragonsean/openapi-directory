# ProductsApi

All URIs are relative to *https://api.reverb.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsReviewsIdGet**](ProductsApi.md#productsReviewsIdGet) | **GET** /products/reviews/{id} | View a review |
| [**productsReviewsIdPut**](ProductsApi.md#productsReviewsIdPut) | **PUT** /products/reviews/{id} | Update a review |
| [**productsSlugReviewsGet**](ProductsApi.md#productsSlugReviewsGet) | **GET** /products/{slug}/reviews | View reviews of a comparison shopping page |
| [**productsSlugReviewsPost**](ProductsApi.md#productsSlugReviewsPost) | **POST** /products/{slug}/reviews | Create a review for a product |


<a id="productsReviewsIdGet"></a>
# **productsReviewsIdGet**
> productsReviewsIdGet(id)

View a review

View a review

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.productsReviewsIdGet(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsReviewsIdGet");
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

<a id="productsReviewsIdPut"></a>
# **productsReviewsIdPut**
> productsReviewsIdPut(id, productsReviewsIdPutRequest)

Update a review

Update a review

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String id = "id_example"; // String | 
    ProductsReviewsIdPutRequest productsReviewsIdPutRequest = new ProductsReviewsIdPutRequest(); // ProductsReviewsIdPutRequest | the content of the request
    try {
      apiInstance.productsReviewsIdPut(id, productsReviewsIdPutRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsReviewsIdPut");
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
| **productsReviewsIdPutRequest** | [**ProductsReviewsIdPutRequest**](ProductsReviewsIdPutRequest.md)| the content of the request | [optional] |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

<a id="productsSlugReviewsGet"></a>
# **productsSlugReviewsGet**
> productsSlugReviewsGet(slug)

View reviews of a comparison shopping page

View reviews of a comparison shopping page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.productsSlugReviewsGet(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsSlugReviewsGet");
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

<a id="productsSlugReviewsPost"></a>
# **productsSlugReviewsPost**
> productsSlugReviewsPost(slug)

Create a review for a product

Create a review for a product

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.reverb.com/api");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    ProductsApi apiInstance = new ProductsApi(defaultClient);
    String slug = "slug_example"; // String | 
    try {
      apiInstance.productsSlugReviewsPost(slug);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsApi#productsSlugReviewsPost");
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

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **0** | Unexpected error |  -  |

