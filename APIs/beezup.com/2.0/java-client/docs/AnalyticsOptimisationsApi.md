# AnalyticsOptimisationsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**copyOptimisation**](AnalyticsOptimisationsApi.md#copyOptimisation) | **POST** /v2/user/analytics/{storeId}/optimisations/copy | Copy product optimisations between 2 channels |
| [**optimise**](AnalyticsOptimisationsApi.md#optimise) | **POST** /v2/user/analytics/{storeId}/optimisations/{actionName} | Optimise products by page |
| [**optimiseAll**](AnalyticsOptimisationsApi.md#optimiseAll) | **POST** /v2/user/analytics/{storeId}/optimisations/all/{actionName} | Optimise all products |
| [**optimiseByCategory**](AnalyticsOptimisationsApi.md#optimiseByCategory) | **POST** /v2/user/analytics/{storeId}/optimisations/bycategory/{catalogCategoryId}/{actionName} | Optimise products by category |
| [**optimiseByChannel**](AnalyticsOptimisationsApi.md#optimiseByChannel) | **POST** /v2/user/analytics/{storeId}/optimisations/bychannel/{channelId}/{actionName} | Optimise products by channel |
| [**optimiseByProduct**](AnalyticsOptimisationsApi.md#optimiseByProduct) | **POST** /v2/user/analytics/{storeId}/optimisations/byproduct/{productId}/{actionName} | Optimise product |


<a id="copyOptimisation"></a>
# **copyOptimisation**
> CopyOptimisationResponse copyOptimisation(storeId, copyOptimisationRequest)

Copy product optimisations between 2 channels

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsOptimisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsOptimisationsApi apiInstance = new AnalyticsOptimisationsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    CopyOptimisationRequest copyOptimisationRequest = new CopyOptimisationRequest(); // CopyOptimisationRequest | 
    try {
      CopyOptimisationResponse result = apiInstance.copyOptimisation(storeId, copyOptimisationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsOptimisationsApi#copyOptimisation");
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
| **storeId** | **String**| Your store identifier | |
| **copyOptimisationRequest** | [**CopyOptimisationRequest**](CopyOptimisationRequest.md)|  | |

### Return type

[**CopyOptimisationResponse**](CopyOptimisationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Products optimisatisation copied |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="optimise"></a>
# **optimise**
> optimise(storeId, actionName, optimiseRequest)

Optimise products by page

/!\\ WARNING /!\\ \\ Apply the operation on every product related to this request. \\ This operation is used at the bottom of the analytics page result. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsOptimisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsOptimisationsApi apiInstance = new AnalyticsOptimisationsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String actionName = "reenable"; // String | 
    OptimiseRequest optimiseRequest = new OptimiseRequest(); // OptimiseRequest | 
    try {
      apiInstance.optimise(storeId, actionName, optimiseRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsOptimisationsApi#optimise");
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
| **storeId** | **String**| Your store identifier | |
| **actionName** | **String**|  | [enum: reenable, disable] |
| **optimiseRequest** | [**OptimiseRequest**](OptimiseRequest.md)|  | |

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
| **204** | Products optimisatized |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="optimiseAll"></a>
# **optimiseAll**
> optimiseAll(storeId, actionName, optimiseAllRequest)

Optimise all products

/!\\ WARNING /!\\ \\ Apply the operation on every product related to this request. \\ This operation is used at the bottom of the analytics page result. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsOptimisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsOptimisationsApi apiInstance = new AnalyticsOptimisationsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String actionName = "reenable"; // String | 
    OptimiseAllRequest optimiseAllRequest = new OptimiseAllRequest(); // OptimiseAllRequest | 
    try {
      apiInstance.optimiseAll(storeId, actionName, optimiseAllRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsOptimisationsApi#optimiseAll");
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
| **storeId** | **String**| Your store identifier | |
| **actionName** | **String**|  | [enum: reenable, disable] |
| **optimiseAllRequest** | [**OptimiseAllRequest**](OptimiseAllRequest.md)|  | |

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
| **204** | Products optimisatized |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="optimiseByCategory"></a>
# **optimiseByCategory**
> optimiseByCategory(storeId, catalogCategoryId, actionName, requestBody)

Optimise products by category

/!\\ WARNING /!\\ \\ This operation will reenable or disable products&#39;s category for every channel indicated in the body. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsOptimisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsOptimisationsApi apiInstance = new AnalyticsOptimisationsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String catalogCategoryId = "catalogCategoryId_example"; // String | The category identifier concerned by this optimisation
    String actionName = "reenable"; // String | 
    Set<String> requestBody = Arrays.asList(); // Set<String> | The channel identifier list concerned by this optimisation
    try {
      apiInstance.optimiseByCategory(storeId, catalogCategoryId, actionName, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsOptimisationsApi#optimiseByCategory");
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
| **storeId** | **String**| Your store identifier | |
| **catalogCategoryId** | **String**| The category identifier concerned by this optimisation | |
| **actionName** | **String**|  | [enum: reenable, disable] |
| **requestBody** | [**Set&lt;String&gt;**](String.md)| The channel identifier list concerned by this optimisation | [optional] |

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
| **204** | Products optimisatized |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="optimiseByChannel"></a>
# **optimiseByChannel**
> optimiseByChannel(storeId, channelId, actionName)

Optimise products by channel

/!\\ WARNING /!\\ \\ Apply the operation on every product on this channel. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsOptimisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsOptimisationsApi apiInstance = new AnalyticsOptimisationsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String channelId = "channelId_example"; // String | The channel identifier concerned by this optimisation
    String actionName = "reenable"; // String | 
    try {
      apiInstance.optimiseByChannel(storeId, channelId, actionName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsOptimisationsApi#optimiseByChannel");
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
| **storeId** | **String**| Your store identifier | |
| **channelId** | **String**| The channel identifier concerned by this optimisation | |
| **actionName** | **String**|  | [enum: reenable, disable] |

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
| **204** | Products optimisatized |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="optimiseByProduct"></a>
# **optimiseByProduct**
> optimiseByProduct(storeId, productId, actionName, requestBody)

Optimise product

/!\\ WARNING /!\\ \\ This operation will reenable or disable this product for every channel indicated in the body. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyticsOptimisationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    AnalyticsOptimisationsApi apiInstance = new AnalyticsOptimisationsApi(defaultClient);
    String storeId = "storeId_example"; // String | Your store identifier
    String productId = "productId_example"; // String | The product identifier concerned by this optimisation
    String actionName = "reenable"; // String | 
    Set<String> requestBody = Arrays.asList(); // Set<String> | The channel identifier list concerned by this optimisation
    try {
      apiInstance.optimiseByProduct(storeId, productId, actionName, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyticsOptimisationsApi#optimiseByProduct");
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
| **storeId** | **String**| Your store identifier | |
| **productId** | **String**| The product identifier concerned by this optimisation | |
| **actionName** | **String**|  | [enum: reenable, disable] |
| **requestBody** | [**Set&lt;String&gt;**](String.md)| The channel identifier list concerned by this optimisation | [optional] |

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
| **204** | Product(s) optimisatized |  -  |
| **400** | Invalid request |  -  |
| **404** | Store or resource not found |  -  |
| **0** | Occurs when something goes wrong |  -  |

