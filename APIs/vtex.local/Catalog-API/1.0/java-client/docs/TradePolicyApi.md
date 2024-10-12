# TradePolicyApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtProductProductIdSalespolicyGet**](TradePolicyApi.md#apiCatalogPvtProductProductIdSalespolicyGet) | **GET** /api/catalog/pvt/product/{productId}/salespolicy | Get Trade Policies by Product ID |
| [**apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete**](TradePolicyApi.md#apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete) | **DELETE** /api/catalog/pvt/product/{productId}/salespolicy/{tradepolicyId} | Remove Product from Trade Policy |
| [**apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost**](TradePolicyApi.md#apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost) | **POST** /api/catalog/pvt/product/{productId}/salespolicy/{tradepolicyId} | Associate Product with Trade Policy |
| [**apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet**](TradePolicyApi.md#apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet) | **GET** /api/catalog_system/pvt/sku/stockkeepingunitidsbysaleschannel | List all SKUs of a Trade Policy |


<a id="apiCatalogPvtProductProductIdSalespolicyGet"></a>
# **apiCatalogPvtProductProductIdSalespolicyGet**
> List&lt;ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner&gt; apiCatalogPvtProductProductIdSalespolicyGet(contentType, accept, productId)

Get Trade Policies by Product ID

Retrieves a list of Trade Policies associated to a Product based on the Product&#39;s ID.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 1      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 2      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 3      },      {          \&quot;ProductId\&quot;: 1,          \&quot;StoreId\&quot;: 4      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TradePolicyApi;

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

    TradePolicyApi apiInstance = new TradePolicyApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    try {
      List<ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner> result = apiInstance.apiCatalogPvtProductProductIdSalespolicyGet(contentType, accept, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TradePolicyApi#apiCatalogPvtProductProductIdSalespolicyGet");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique numerical identifier. | |

### Return type

[**List&lt;ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner&gt;**](ApiCatalogPvtProductProductIdSalespolicyGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete"></a>
# **apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete**
> apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete(contentType, accept, productId, tradepolicyId)

Remove Product from Trade Policy

Disassociates a Trade Policy of a Product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TradePolicyApi;

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

    TradePolicyApi apiInstance = new TradePolicyApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    Integer tradepolicyId = 1; // Integer | Trade Policy’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete(contentType, accept, productId, tradepolicyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TradePolicyApi#apiCatalogPvtProductProductIdSalespolicyTradepolicyIdDelete");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique numerical identifier. | |
| **tradepolicyId** | **Integer**| Trade Policy’s unique numerical identifier. | |

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

<a id="apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost"></a>
# **apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost**
> apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost(contentType, accept, productId, tradepolicyId)

Associate Product with Trade Policy

Associates an existing Trade Policy with a Product.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TradePolicyApi;

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

    TradePolicyApi apiInstance = new TradePolicyApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer productId = 1; // Integer | Product’s unique numerical identifier.
    Integer tradepolicyId = 1; // Integer | Trade Policy’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost(contentType, accept, productId, tradepolicyId);
    } catch (ApiException e) {
      System.err.println("Exception when calling TradePolicyApi#apiCatalogPvtProductProductIdSalespolicyTradepolicyIdPost");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **productId** | **Integer**| Product’s unique numerical identifier. | |
| **tradepolicyId** | **Integer**| Trade Policy’s unique numerical identifier. | |

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

<a id="apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet"></a>
# **apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet**
> List&lt;Integer&gt; apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet(contentType, accept, sc, page, pageSize, onlyAssigned)

List all SKUs of a Trade Policy

Retrieves a list of SKU IDs of a Trade Policy.   ## Response body example    &#x60;&#x60;&#x60;json  [      405380,      405381,      405382,      405383,      405384,      405385,      405386,      405387,      405388,      405389,      405390,      405391,      405392,      405393,      405394,      405395,      405396,      405397,      405398,      405399,      405400,      405556  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TradePolicyApi;

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

    TradePolicyApi apiInstance = new TradePolicyApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer sc = 1; // Integer | Trade Policy’s unique numerical identifier.
    Integer page = 1; // Integer | Page number.
    Integer pageSize = 1; // Integer | Number of items in the page.
    Boolean onlyAssigned = true; // Boolean | If set as `false`, it allows the user to decide if the SKUs that are not assigned to a specific trade policy should be also returned.
    try {
      List<Integer> result = apiInstance.apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet(contentType, accept, sc, page, pageSize, onlyAssigned);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TradePolicyApi#apiCatalogSystemPvtSkuStockkeepingunitidsbysaleschannelGet");
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
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **sc** | **Integer**| Trade Policy’s unique numerical identifier. | |
| **page** | **Integer**| Page number. | [optional] |
| **pageSize** | **Integer**| Number of items in the page. | [optional] |
| **onlyAssigned** | **Boolean**| If set as &#x60;false&#x60;, it allows the user to decide if the SKUs that are not assigned to a specific trade policy should be also returned. | [optional] |

### Return type

**List&lt;Integer&gt;**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

