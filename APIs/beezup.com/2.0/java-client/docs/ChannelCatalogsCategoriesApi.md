# ChannelCatalogsCategoriesApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configureChannelCatalogCategory**](ChannelCatalogsCategoriesApi.md#configureChannelCatalogCategory) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/categories/configure | Configure channel catalog category |
| [**disableChannelCatalogCategoryMapping**](ChannelCatalogsCategoriesApi.md#disableChannelCatalogCategoryMapping) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/categories/disableMapping | Disable a channel catalog category mapping |
| [**getChannelCatalogCategories**](ChannelCatalogsCategoriesApi.md#getChannelCatalogCategories) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/categories | Get channel catalog categories |
| [**reenableChannelCatalogCategoryMapping**](ChannelCatalogsCategoriesApi.md#reenableChannelCatalogCategoryMapping) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/categories/reenableMapping | Reenable a channel catalog category mapping |


<a id="configureChannelCatalogCategory"></a>
# **configureChannelCatalogCategory**
> configureChannelCatalogCategory(channelCatalogId, configureCategoryRequest)

Configure channel catalog category

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsCategoriesApi apiInstance = new ChannelCatalogsCategoriesApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    ConfigureCategoryRequest configureCategoryRequest = new ConfigureCategoryRequest(); // ConfigureCategoryRequest | 
    try {
      apiInstance.configureChannelCatalogCategory(channelCatalogId, configureCategoryRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsCategoriesApi#configureChannelCatalogCategory");
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
| **channelCatalogId** | **String**| The channel catalog identifier | |
| **configureCategoryRequest** | [**ConfigureCategoryRequest**](ConfigureCategoryRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Channel catalog category configured |  -  |
| **400** | BadRequest. See Error Response for more details |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="disableChannelCatalogCategoryMapping"></a>
# **disableChannelCatalogCategoryMapping**
> disableChannelCatalogCategoryMapping(channelCatalogId)

Disable a channel catalog category mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsCategoriesApi apiInstance = new ChannelCatalogsCategoriesApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    try {
      apiInstance.disableChannelCatalogCategoryMapping(channelCatalogId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsCategoriesApi#disableChannelCatalogCategoryMapping");
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
| **channelCatalogId** | **String**| The channel catalog identifier | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Channel catalog category mapping disabled |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getChannelCatalogCategories"></a>
# **getChannelCatalogCategories**
> ChannelCatalogCategoryConfigurationList getChannelCatalogCategories(channelCatalogId)

Get channel catalog categories

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsCategoriesApi apiInstance = new ChannelCatalogsCategoriesApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    try {
      ChannelCatalogCategoryConfigurationList result = apiInstance.getChannelCatalogCategories(channelCatalogId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsCategoriesApi#getChannelCatalogCategories");
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
| **channelCatalogId** | **String**| The channel catalog identifier | |

### Return type

[**ChannelCatalogCategoryConfigurationList**](ChannelCatalogCategoryConfigurationList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel catalog category mappings |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="reenableChannelCatalogCategoryMapping"></a>
# **reenableChannelCatalogCategoryMapping**
> reenableChannelCatalogCategoryMapping(channelCatalogId)

Reenable a channel catalog category mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsCategoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsCategoriesApi apiInstance = new ChannelCatalogsCategoriesApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    try {
      apiInstance.reenableChannelCatalogCategoryMapping(channelCatalogId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsCategoriesApi#reenableChannelCatalogCategoryMapping");
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
| **channelCatalogId** | **String**| The channel catalog identifier | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Channel catalog category mapping reenabled |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

