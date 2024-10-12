# CrossSellingApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productSearchAccessories**](CrossSellingApi.md#productSearchAccessories) | **GET** /api/catalog_system/pub/products/crossselling/accessories/{productId} | Get Product Search of Accessories |
| [**productSearchShowTogether**](CrossSellingApi.md#productSearchShowTogether) | **GET** /api/catalog_system/pub/products/crossselling/showtogether/{productId} | Get Product Search of Show Together |
| [**productSearchSimilars**](CrossSellingApi.md#productSearchSimilars) | **GET** /api/catalog_system/pub/products/crossselling/similars/{productId} | Get Product Search of Similars |
| [**productSearchSuggestions**](CrossSellingApi.md#productSearchSuggestions) | **GET** /api/catalog_system/pub/products/crossselling/suggestions/{productId} | Get Product Search of Suggestions |
| [**productSearchWhoBoughtAlsoBought**](CrossSellingApi.md#productSearchWhoBoughtAlsoBought) | **GET** /api/catalog_system/pub/products/crossselling/whoboughtalsobought/{productId} | Get Product Search of Who Bought Also Bought |
| [**productSearchWhoSawAlsoBought**](CrossSellingApi.md#productSearchWhoSawAlsoBought) | **GET** /api/catalog_system/pub/products/crossselling/whosawalsobought/{productId} | Get Product Search of Who Saw Also Bought |
| [**productSearchWhoSawAlsoSaw**](CrossSellingApi.md#productSearchWhoSawAlsoSaw) | **GET** /api/catalog_system/pub/products/crossselling/whosawalsosaw/{productId} | Get Product Search of Who Saw Also Saw |


<a id="productSearchAccessories"></a>
# **productSearchAccessories**
> productSearchAccessories(accept, contentType, productId)

Get Product Search of Accessories

Retrieves general information about the product&#39;s accessories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrossSellingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CrossSellingApi apiInstance = new CrossSellingApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    Integer productId = 1; // Integer | Product's unique identifier
    try {
      apiInstance.productSearchAccessories(accept, contentType, productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrossSellingApi#productSearchAccessories");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Describes the type of the content being sent. | |
| **productId** | **Integer**| Product&#39;s unique identifier | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productSearchShowTogether"></a>
# **productSearchShowTogether**
> productSearchShowTogether(accept, contentType, productId)

Get Product Search of Show Together

Retrieves general information about the products that are show together with the product in question.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrossSellingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CrossSellingApi apiInstance = new CrossSellingApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    Integer productId = 1; // Integer | Product's unique identifier
    try {
      apiInstance.productSearchShowTogether(accept, contentType, productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrossSellingApi#productSearchShowTogether");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Describes the type of the content being sent. | |
| **productId** | **Integer**| Product&#39;s unique identifier | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productSearchSimilars"></a>
# **productSearchSimilars**
> productSearchSimilars(accept, contentType, productId)

Get Product Search of Similars

Retrieves general information about related product searches.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrossSellingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CrossSellingApi apiInstance = new CrossSellingApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    Integer productId = 1; // Integer | Product's unique identifier
    try {
      apiInstance.productSearchSimilars(accept, contentType, productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrossSellingApi#productSearchSimilars");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Describes the type of the content being sent. | |
| **productId** | **Integer**| Product&#39;s unique identifier | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productSearchSuggestions"></a>
# **productSearchSuggestions**
> productSearchSuggestions(accept, contentType, productId)

Get Product Search of Suggestions

Retrieves general information about other product suggestions related to the product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrossSellingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CrossSellingApi apiInstance = new CrossSellingApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    Integer productId = 1; // Integer | Product's unique identifier
    try {
      apiInstance.productSearchSuggestions(accept, contentType, productId);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrossSellingApi#productSearchSuggestions");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Describes the type of the content being sent. | |
| **productId** | **Integer**| Product&#39;s unique identifier | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productSearchWhoBoughtAlsoBought"></a>
# **productSearchWhoBoughtAlsoBought**
> List&lt;ProductSearchWhoBoughtAlsoBought200ResponseInner&gt; productSearchWhoBoughtAlsoBought(accept, contentType, productId)

Get Product Search of Who Bought Also Bought

Retrieves general information about other related products that the user also bought.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrossSellingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CrossSellingApi apiInstance = new CrossSellingApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String productId = "1"; // String | Product unique identifier.
    try {
      List<ProductSearchWhoBoughtAlsoBought200ResponseInner> result = apiInstance.productSearchWhoBoughtAlsoBought(accept, contentType, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrossSellingApi#productSearchWhoBoughtAlsoBought");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Describes the type of the content being sent. | |
| **productId** | **String**| Product unique identifier. | |

### Return type

[**List&lt;ProductSearchWhoBoughtAlsoBought200ResponseInner&gt;**](ProductSearchWhoBoughtAlsoBought200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productSearchWhoSawAlsoBought"></a>
# **productSearchWhoSawAlsoBought**
> List&lt;ProductSearchWhoBoughtAlsoBought200ResponseInner&gt; productSearchWhoSawAlsoBought(accept, contentType, productId)

Get Product Search of Who Saw Also Bought

Retrieves general information about other related products that the users saw and also bought.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrossSellingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CrossSellingApi apiInstance = new CrossSellingApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String productId = "1"; // String | Product unique identifier.
    try {
      List<ProductSearchWhoBoughtAlsoBought200ResponseInner> result = apiInstance.productSearchWhoSawAlsoBought(accept, contentType, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrossSellingApi#productSearchWhoSawAlsoBought");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Describes the type of the content being sent. | |
| **productId** | **String**| Product unique identifier. | |

### Return type

[**List&lt;ProductSearchWhoBoughtAlsoBought200ResponseInner&gt;**](ProductSearchWhoBoughtAlsoBought200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="productSearchWhoSawAlsoSaw"></a>
# **productSearchWhoSawAlsoSaw**
> List&lt;ProductSearchWhoBoughtAlsoBought200ResponseInner&gt; productSearchWhoSawAlsoSaw(accept, contentType, productId)

Get Product Search of Who Saw Also Saw

Retrieves general information about other related products that the users also saw.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CrossSellingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    CrossSellingApi apiInstance = new CrossSellingApi(defaultClient);
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    Integer productId = 1; // Integer | Product unique identifier.
    try {
      List<ProductSearchWhoBoughtAlsoBought200ResponseInner> result = apiInstance.productSearchWhoSawAlsoSaw(accept, contentType, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CrossSellingApi#productSearchWhoSawAlsoSaw");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | |
| **contentType** | **String**| Describes the type of the content being sent. | |
| **productId** | **Integer**| Product unique identifier. | |

### Return type

[**List&lt;ProductSearchWhoBoughtAlsoBought200ResponseInner&gt;**](ProductSearchWhoBoughtAlsoBought200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

