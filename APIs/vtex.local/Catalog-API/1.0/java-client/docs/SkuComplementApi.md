# SkuComplementApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSKUComplement**](SkuComplementApi.md#createSKUComplement) | **POST** /api/catalog/pvt/skucomplement | Create SKU Complement |
| [**deleteSKUComplementbySKUComplementID**](SkuComplementApi.md#deleteSKUComplementbySKUComplementID) | **DELETE** /api/catalog/pvt/skucomplement/{skuComplementId} | Delete SKU Complement by SKU Complement ID |
| [**getSKUComplementbySKUComplementID**](SkuComplementApi.md#getSKUComplementbySKUComplementID) | **GET** /api/catalog/pvt/skucomplement/{skuComplementId} | Get SKU Complement by SKU Complement ID |
| [**getSKUComplementbySKUID**](SkuComplementApi.md#getSKUComplementbySKUID) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/complement | Get SKU Complement by SKU ID |
| [**getSKUComplementsbyComplementTypeID**](SkuComplementApi.md#getSKUComplementsbyComplementTypeID) | **GET** /api/catalog/pvt/stockkeepingunit/{skuId}/complement/{complementTypeId} | Get SKU Complements by Complement Type ID |
| [**getSKUcomplementsbytype**](SkuComplementApi.md#getSKUcomplementsbytype) | **GET** /api/catalog_system/pvt/sku/complements/{parentSkuId}/{type} | Get SKU complements by type |


<a id="createSKUComplement"></a>
# **createSKUComplement**
> List&lt;SkuComplementInner&gt; createSKUComplement(contentType, accept, requestBody2)

Create SKU Complement

Creates a new SKU Complement on a Parent SKU.     ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 62,      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuComplementApi;

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

    SkuComplementApi apiInstance = new SkuComplementApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    RequestBody2 requestBody2 = new RequestBody2(); // RequestBody2 | 
    try {
      List<SkuComplementInner> result = apiInstance.createSKUComplement(contentType, accept, requestBody2);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuComplementApi#createSKUComplement");
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
| **requestBody2** | [**RequestBody2**](RequestBody2.md)|  | [optional] |

### Return type

[**List&lt;SkuComplementInner&gt;**](SkuComplementInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="deleteSKUComplementbySKUComplementID"></a>
# **deleteSKUComplementbySKUComplementID**
> deleteSKUComplementbySKUComplementID(contentType, accept, skuComplementId)

Delete SKU Complement by SKU Complement ID

Deletes a previously existing SKU Complement by SKU Complement ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuComplementApi;

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

    SkuComplementApi apiInstance = new SkuComplementApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuComplementId = 1; // Integer | SKU Complement’s unique numerical identifier.
    try {
      apiInstance.deleteSKUComplementbySKUComplementID(contentType, accept, skuComplementId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuComplementApi#deleteSKUComplementbySKUComplementID");
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
| **skuComplementId** | **Integer**| SKU Complement’s unique numerical identifier. | |

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

<a id="getSKUComplementbySKUComplementID"></a>
# **getSKUComplementbySKUComplementID**
> List&lt;SkuComplementInner&gt; getSKUComplementbySKUComplementID(contentType, accept, skuComplementId)

Get SKU Complement by SKU Complement ID

Retrieves an existing SKU Complement by its SKU Complement ID.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 62,      \&quot;SkuId\&quot;: 2,      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementTypeId\&quot;: 2  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuComplementApi;

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

    SkuComplementApi apiInstance = new SkuComplementApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuComplementId = 1; // Integer | SKU Complement’s unique numerical identifier.
    try {
      List<SkuComplementInner> result = apiInstance.getSKUComplementbySKUComplementID(contentType, accept, skuComplementId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuComplementApi#getSKUComplementbySKUComplementID");
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
| **skuComplementId** | **Integer**| SKU Complement’s unique numerical identifier. | |

### Return type

[**List&lt;SkuComplementInner&gt;**](SkuComplementInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getSKUComplementbySKUID"></a>
# **getSKUComplementbySKUID**
> List&lt;SkuComplementInner&gt; getSKUComplementbySKUID(contentType, accept, skuId)

Get SKU Complement by SKU ID

Retrieves an existing SKU Complement by its SKU ID.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 61,          \&quot;SkuId\&quot;: 7,          \&quot;ParentSkuId\&quot;: 1,          \&quot;ComplementTypeId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuComplementApi;

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

    SkuComplementApi apiInstance = new SkuComplementApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    try {
      List<SkuComplementInner> result = apiInstance.getSKUComplementbySKUID(contentType, accept, skuId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuComplementApi#getSKUComplementbySKUID");
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
| **skuId** | **Integer**| SKU’s unique numerical identifier. | |

### Return type

[**List&lt;SkuComplementInner&gt;**](SkuComplementInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getSKUComplementsbyComplementTypeID"></a>
# **getSKUComplementsbyComplementTypeID**
> List&lt;SkuComplementInner&gt; getSKUComplementsbyComplementTypeID(contentType, accept, skuId, complementTypeId)

Get SKU Complements by Complement Type ID

Retrieves all the existing SKU Complements with the same Complement Type ID of a specific SKU.     ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 61,          \&quot;SkuId\&quot;: 7,          \&quot;ParentSkuId\&quot;: 1,          \&quot;ComplementTypeId\&quot;: 1      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuComplementApi;

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

    SkuComplementApi apiInstance = new SkuComplementApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer skuId = 1; // Integer | ID of the SKU which will be inserted as a Complement in the Parent SKU.
    Integer complementTypeId = 1; // Integer | Complement Type ID. This represents the type of the complement. The possible values are: `1` for Accessory; `2` for Suggestion; `3` for Similar Product; `5` for Show Together.
    try {
      List<SkuComplementInner> result = apiInstance.getSKUComplementsbyComplementTypeID(contentType, accept, skuId, complementTypeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuComplementApi#getSKUComplementsbyComplementTypeID");
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
| **skuId** | **Integer**| ID of the SKU which will be inserted as a Complement in the Parent SKU. | |
| **complementTypeId** | **Integer**| Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together. | |

### Return type

[**List&lt;SkuComplementInner&gt;**](SkuComplementInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getSKUcomplementsbytype"></a>
# **getSKUcomplementsbytype**
> GetSKUcomplementsbytype200Response getSKUcomplementsbytype(contentType, accept, parentSkuId, type)

Get SKU complements by type

Retrieves all the existing SKU complements with the same complement type ID of a specific SKU.      ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;ParentSkuId\&quot;: 1,      \&quot;ComplementSkuIds\&quot;: [          7      ],      \&quot;Type\&quot;: \&quot;1\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuComplementApi;

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

    SkuComplementApi apiInstance = new SkuComplementApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer parentSkuId = 1; // Integer | ID of the Parent SKU, where the Complement is inserted.
    Integer type = 1; // Integer | Complement Type ID. This represents the type of the complement. The possible values are: `1` for Accessory; `2` for Suggestion; `3` for Similar Product; `5` for Show Together.
    try {
      GetSKUcomplementsbytype200Response result = apiInstance.getSKUcomplementsbytype(contentType, accept, parentSkuId, type);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuComplementApi#getSKUcomplementsbytype");
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
| **parentSkuId** | **Integer**| ID of the Parent SKU, where the Complement is inserted. | |
| **type** | **Integer**| Complement Type ID. This represents the type of the complement. The possible values are: &#x60;1&#x60; for Accessory; &#x60;2&#x60; for Suggestion; &#x60;3&#x60; for Similar Product; &#x60;5&#x60; for Show Together. | |

### Return type

[**GetSKUcomplementsbytype200Response**](GetSKUcomplementsbytype200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

