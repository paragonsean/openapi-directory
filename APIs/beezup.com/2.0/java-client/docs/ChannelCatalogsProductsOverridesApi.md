# ChannelCatalogsProductsOverridesApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**configureChannelCatalogProductValueOverrideCopy**](ChannelCatalogsProductsOverridesApi.md#configureChannelCatalogProductValueOverrideCopy) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/products/{productId}/overrides/copy | Copy channel catalog product value override |
| [**deleteChannelCatalogProductValueOverride**](ChannelCatalogsProductsOverridesApi.md#deleteChannelCatalogProductValueOverride) | **DELETE** /v2/user/channelCatalogs/{channelCatalogId}/products/{productId}/overrides/{channelColumnId} | Delete a specific channel catalog product value override |
| [**getChannelCatalogProductValueOverrideCopy**](ChannelCatalogsProductsOverridesApi.md#getChannelCatalogProductValueOverrideCopy) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/products/{productId}/overrides/copy | Get channel catalog product value override compatibilities status |
| [**overrideChannelCatalogProductValues**](ChannelCatalogsProductsOverridesApi.md#overrideChannelCatalogProductValues) | **PUT** /v2/user/channelCatalogs/{channelCatalogId}/products/{productId}/overrides | Override channel catalog product values |


<a id="configureChannelCatalogProductValueOverrideCopy"></a>
# **configureChannelCatalogProductValueOverrideCopy**
> configureChannelCatalogProductValueOverrideCopy(channelCatalogId, productId)

Copy channel catalog product value override

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsProductsOverridesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsProductsOverridesApi apiInstance = new ChannelCatalogsProductsOverridesApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    String productId = "578419df-1bbf-41a6-96fa-862e42182b67"; // String | The product identifier
    try {
      apiInstance.configureChannelCatalogProductValueOverrideCopy(channelCatalogId, productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsProductsOverridesApi#configureChannelCatalogProductValueOverrideCopy");
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
| **productId** | **String**| The product identifier | |

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
| **204** | Channel catalog product value override deleted |  -  |
| **404** | ChannelCatalogId or ProductId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="deleteChannelCatalogProductValueOverride"></a>
# **deleteChannelCatalogProductValueOverride**
> deleteChannelCatalogProductValueOverride(channelCatalogId, productId, channelColumnId)

Delete a specific channel catalog product value override

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsProductsOverridesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsProductsOverridesApi apiInstance = new ChannelCatalogsProductsOverridesApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    String productId = "578419df-1bbf-41a6-96fa-862e42182b67"; // String | The product identifier
    String channelColumnId = "8a76f06a-fefc-4c0d-bcfe-b210f1482977"; // String | The channel column identifier
    try {
      apiInstance.deleteChannelCatalogProductValueOverride(channelCatalogId, productId, channelColumnId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsProductsOverridesApi#deleteChannelCatalogProductValueOverride");
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
| **productId** | **String**| The product identifier | |
| **channelColumnId** | **String**| The channel column identifier | |

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
| **204** | Channel catalog product value override deleted |  -  |
| **404** | ChannelCatalogId or ProductId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getChannelCatalogProductValueOverrideCopy"></a>
# **getChannelCatalogProductValueOverrideCopy**
> getChannelCatalogProductValueOverrideCopy(channelCatalogId, productId)

Get channel catalog product value override compatibilities status

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsProductsOverridesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsProductsOverridesApi apiInstance = new ChannelCatalogsProductsOverridesApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    String productId = "578419df-1bbf-41a6-96fa-862e42182b67"; // String | The product identifier
    try {
      apiInstance.getChannelCatalogProductValueOverrideCopy(channelCatalogId, productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsProductsOverridesApi#getChannelCatalogProductValueOverrideCopy");
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
| **productId** | **String**| The product identifier | |

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
| **204** | placeholder. will be completed soon. |  -  |
| **404** | ChannelCatalog or ProductId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="overrideChannelCatalogProductValues"></a>
# **overrideChannelCatalogProductValues**
> overrideChannelCatalogProductValues(channelCatalogId, productId, requestBody)

Override channel catalog product values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsProductsOverridesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsProductsOverridesApi apiInstance = new ChannelCatalogsProductsOverridesApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    String productId = "578419df-1bbf-41a6-96fa-862e42182b67"; // String | The product identifier
    Map<String, String> requestBody = new HashMap(); // Map<String, String> | 
    try {
      apiInstance.overrideChannelCatalogProductValues(channelCatalogId, productId, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsProductsOverridesApi#overrideChannelCatalogProductValues");
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
| **productId** | **String**| The product identifier | |
| **requestBody** | [**Map&lt;String, String&gt;**](String.md)|  | |

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
| **204** | Channel catalog product overriden |  -  |
| **400** | BadRequest. See Error Response for more details |  -  |
| **404** | ChannelCatalogId or ProductId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

