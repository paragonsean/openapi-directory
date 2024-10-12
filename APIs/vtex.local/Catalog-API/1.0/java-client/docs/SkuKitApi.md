# SkuKitApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtStockkeepingunitkitDelete**](SkuKitApi.md#apiCatalogPvtStockkeepingunitkitDelete) | **DELETE** /api/catalog/pvt/stockkeepingunitkit | Delete SKU Kit by SKU ID or Parent SKU ID |
| [**apiCatalogPvtStockkeepingunitkitGet**](SkuKitApi.md#apiCatalogPvtStockkeepingunitkitGet) | **GET** /api/catalog/pvt/stockkeepingunitkit | Get SKU Kit by SKU ID or Parent SKU ID |
| [**apiCatalogPvtStockkeepingunitkitKitIdDelete**](SkuKitApi.md#apiCatalogPvtStockkeepingunitkitKitIdDelete) | **DELETE** /api/catalog/pvt/stockkeepingunitkit/{kitId} | Delete SKU Kit by KitId |
| [**apiCatalogPvtStockkeepingunitkitKitIdGet**](SkuKitApi.md#apiCatalogPvtStockkeepingunitkitKitIdGet) | **GET** /api/catalog/pvt/stockkeepingunitkit/{kitId} | Get SKU Kit |
| [**apiCatalogPvtStockkeepingunitkitPost**](SkuKitApi.md#apiCatalogPvtStockkeepingunitkitPost) | **POST** /api/catalog/pvt/stockkeepingunitkit | Create SKU Kit |


<a id="apiCatalogPvtStockkeepingunitkitDelete"></a>
# **apiCatalogPvtStockkeepingunitkitDelete**
> apiCatalogPvtStockkeepingunitkitDelete(contentType, accept, skuId, parentSkuId)

Delete SKU Kit by SKU ID or Parent SKU ID

Deletes all Kit’s components based on the Parent SKU ID or deletes a specific Kit’s component based on the SKU ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuKitApi;

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

    SkuKitApi apiInstance = new SkuKitApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    Integer parentSkuId = 1; // Integer | Parent SKU’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtStockkeepingunitkitDelete(contentType, accept, skuId, parentSkuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuKitApi#apiCatalogPvtStockkeepingunitkitDelete");
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
| **skuId** | **Integer**| SKU’s unique numerical identifier. | [optional] |
| **parentSkuId** | **Integer**| Parent SKU’s unique numerical identifier. | [optional] |

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

<a id="apiCatalogPvtStockkeepingunitkitGet"></a>
# **apiCatalogPvtStockkeepingunitkitGet**
> SkuKit apiCatalogPvtStockkeepingunitkitGet(contentType, accept, skuId, parentSkuId)

Get SKU Kit by SKU ID or Parent SKU ID

Retrieves general information about the components of an SKU Kit by SKU ID or Parent SKU ID.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 7,      \&quot;StockKeepingUnitParent\&quot;: 7,      \&quot;StockKeepingUnitId\&quot;: 1,      \&quot;Quantity\&quot;: 1,      \&quot;UnitPrice\&quot;: 50.0000  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuKitApi;

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

    SkuKitApi apiInstance = new SkuKitApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    Integer parentSkuId = 1; // Integer | Parent SKU’s unique numerical identifier.
    try {
      SkuKit result = apiInstance.apiCatalogPvtStockkeepingunitkitGet(contentType, accept, skuId, parentSkuId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuKitApi#apiCatalogPvtStockkeepingunitkitGet");
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
| **skuId** | **Integer**| SKU’s unique numerical identifier. | [optional] |
| **parentSkuId** | **Integer**| Parent SKU’s unique numerical identifier. | [optional] |

### Return type

[**SkuKit**](SkuKit.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtStockkeepingunitkitKitIdDelete"></a>
# **apiCatalogPvtStockkeepingunitkitKitIdDelete**
> apiCatalogPvtStockkeepingunitkitKitIdDelete(contentType, accept, kitId)

Delete SKU Kit by KitId

Deletes a specific Kit’s component based on its Kit ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuKitApi;

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

    SkuKitApi apiInstance = new SkuKitApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer kitId = 1; // Integer | Kit’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtStockkeepingunitkitKitIdDelete(contentType, accept, kitId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuKitApi#apiCatalogPvtStockkeepingunitkitKitIdDelete");
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
| **kitId** | **Integer**| Kit’s unique numerical identifier. | |

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

<a id="apiCatalogPvtStockkeepingunitkitKitIdGet"></a>
# **apiCatalogPvtStockkeepingunitkitKitIdGet**
> SkuKit apiCatalogPvtStockkeepingunitkitKitIdGet(contentType, accept, kitId)

Get SKU Kit

Retrieves general information about a component of a Kit.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuKitApi;

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

    SkuKitApi apiInstance = new SkuKitApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer kitId = 1; // Integer | Kit’s unique numerical identifier
    try {
      SkuKit result = apiInstance.apiCatalogPvtStockkeepingunitkitKitIdGet(contentType, accept, kitId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuKitApi#apiCatalogPvtStockkeepingunitkitKitIdGet");
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
| **kitId** | **Integer**| Kit’s unique numerical identifier | |

### Return type

[**SkuKit**](SkuKit.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtStockkeepingunitkitPost"></a>
# **apiCatalogPvtStockkeepingunitkitPost**
> SkuKit apiCatalogPvtStockkeepingunitkitPost(contentType, accept, requestBody9)

Create SKU Kit

Adds a component to a specific Kit.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;StockKeepingUnitParent\&quot;: 7,      \&quot;StockKeepingUnitId\&quot;: 1,      \&quot;Quantity\&quot;: 1,      \&quot;UnitPrice\&quot;: 50.0000  }  &#x60;&#x60;&#x60;   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 7,      \&quot;StockKeepingUnitParent\&quot;: 7,      \&quot;StockKeepingUnitId\&quot;: 1,      \&quot;Quantity\&quot;: 1,      \&quot;UnitPrice\&quot;: 50.0000  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuKitApi;

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

    SkuKitApi apiInstance = new SkuKitApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    RequestBody9 requestBody9 = new RequestBody9(); // RequestBody9 | 
    try {
      SkuKit result = apiInstance.apiCatalogPvtStockkeepingunitkitPost(contentType, accept, requestBody9);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuKitApi#apiCatalogPvtStockkeepingunitkitPost");
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
| **requestBody9** | [**RequestBody9**](RequestBody9.md)|  | [optional] |

### Return type

[**SkuKit**](SkuKit.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

