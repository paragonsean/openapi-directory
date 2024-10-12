# CategoriesApi

All URIs are relative to *https://dash.readme.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCategory**](CategoriesApi.md#getCategory) | **GET** /categories/{slug} | Get category |
| [**getCategoryDocs**](CategoriesApi.md#getCategoryDocs) | **GET** /categories/{slug}/docs | Get docs for category |


<a id="getCategory"></a>
# **getCategory**
> getCategory(slug, xReadmeVersion)

Get category

Returns the category with this slug

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String slug = "getting-started"; // String | Slug of category. Slugs must be all lowercase, and replace spaces with hyphens. For example, for the the category \"Getting Started\", enter the slug \"getting-started\"
    String xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    try {
      apiInstance.getCategory(slug, xReadmeVersion);
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
| **slug** | **String**| Slug of category. Slugs must be all lowercase, and replace spaces with hyphens. For example, for the the category \&quot;Getting Started\&quot;, enter the slug \&quot;getting-started\&quot; | |
| **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The category exists and has been returned |  -  |
| **404** | There is no category with that slug |  -  |

<a id="getCategoryDocs"></a>
# **getCategoryDocs**
> getCategoryDocs(slug, xReadmeVersion)

Get docs for category

Returns the docs and children docs within this category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://dash.readme.io/api/v1");
    
    // Configure HTTP basic authorization: apiKey
    HttpBasicAuth apiKey = (HttpBasicAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setUsername("YOUR USERNAME");
    apiKey.setPassword("YOUR PASSWORD");

    CategoriesApi apiInstance = new CategoriesApi(defaultClient);
    String slug = "getting-started"; // String | Slug of category. Slugs must be all lowercase, and replace spaces with hyphens. For example, for the the category \"Getting Started\", enter the slug \"getting-started\"
    String xReadmeVersion = "v3.0"; // String | Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions.
    try {
      apiInstance.getCategoryDocs(slug, xReadmeVersion);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoriesApi#getCategoryDocs");
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
| **slug** | **String**| Slug of category. Slugs must be all lowercase, and replace spaces with hyphens. For example, for the the category \&quot;Getting Started\&quot;, enter the slug \&quot;getting-started\&quot; | |
| **xReadmeVersion** | **String**| Version number of your docs project, for example, v3.0. To see all valid versions for your docs project call https://docs.readme.com/developers/reference/version#getversions. | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The category exists and all of the docs have been returned |  -  |
| **404** | There is no category with that slug |  -  |

