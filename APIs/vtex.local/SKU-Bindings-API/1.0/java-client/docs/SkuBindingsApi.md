# SkuBindingsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**activateSKUBinding**](SkuBindingsApi.md#activateSKUBinding) | **POST** /sku-binding/pvt/skuseller/activate/{sellerId}/{skuSellerId} | Activate SKU Binding |
| [**bindtoanothersku**](SkuBindingsApi.md#bindtoanothersku) | **PUT** /sku-binding/pvt/skuseller/{sellerId}/{sellerSkuId} | Bind a seller&#39;s SKU to another SKU |
| [**changeNotification**](SkuBindingsApi.md#changeNotification) | **POST** /sku-binding/pvt/skuseller/changenotification/{skuId} | Change Notification with SKU ID |
| [**deactivateSKUBinding**](SkuBindingsApi.md#deactivateSKUBinding) | **POST** /sku-binding/pvt/skuseller/inactivate/{sellerId}/{skuSellerId} | Deactivate SKU Binding |
| [**deleteSKUsellerassociation**](SkuBindingsApi.md#deleteSKUsellerassociation) | **POST** /sku-binding/pvt/skuseller/remove/{sellerId}/{sellerSkuId} | Remove a seller&#39;s SKU Binding |
| [**getSKUseller**](SkuBindingsApi.md#getSKUseller) | **GET** /sku-binding/pvt/skuseller/{sellerId}/{sellerSkuId} | Get details of a seller&#39;s SKU |
| [**getallbySellerId**](SkuBindingsApi.md#getallbySellerId) | **GET** /sku-binding/pvt/skuseller/list/bysellerId/{sellerId} | Get all SKU Bindings by Seller ID |
| [**getbySkuId**](SkuBindingsApi.md#getbySkuId) | **GET** /catalog/pvt/skusellers/{skuId} | Get SKU Bindings by SKU ID |
| [**getpagedadmin**](SkuBindingsApi.md#getpagedadmin) | **GET** /sku-binding/pvt/skuseller/admin | Get SKU Bindings information |
| [**getpagedbySellerId**](SkuBindingsApi.md#getpagedbySellerId) | **GET** /sku-binding/pvt/skuseller/paged/sellerid/{sellerId} | Get paged SKU Bindings by Seller ID |
| [**insertSKUBinding**](SkuBindingsApi.md#insertSKUBinding) | **POST** /sku-binding/pvt/skuseller/insertion | Insert SKU Binding |
| [**skuBindingPvtSkusellerChangenotificationSellerIdSellerSkuIdPost**](SkuBindingsApi.md#skuBindingPvtSkusellerChangenotificationSellerIdSellerSkuIdPost) | **POST** /sku-binding/pvt/skuseller/changenotification/{sellerId}/{sellerSkuId} | Change Notification with Seller ID and Seller SKU ID |


<a id="activateSKUBinding"></a>
# **activateSKUBinding**
> activateSKUBinding(contentType, accept, sellerId, skuSellerId)

Activate SKU Binding

Changes the status of an SKU Binding to active, setting &#x60;isActive&#x60; to &#x60;true&#x60;.     &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/activate/{sellerId}/{skuSellerId}&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuBindingsApi;

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

    SkuBindingsApi apiInstance = new SkuBindingsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String sellerId = "vtxkfj7352"; // String | ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    String skuSellerId = "71"; // String | SKU ID in the seller's store.
    try {
      apiInstance.activateSKUBinding(contentType, accept, sellerId, skuSellerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuBindingsApi#activateSKUBinding");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **sellerId** | **String**| ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID. | |
| **skuSellerId** | **String**| SKU ID in the seller&#39;s store. | |

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

<a id="bindtoanothersku"></a>
# **bindtoanothersku**
> bindtoanothersku(contentType, accept, sellerId, sellerSkuId, bindtoanotherskuRequest)

Bind a seller&#39;s SKU to another SKU

Associates a seller&#39;s SKU to another marketplace SKU.     &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/{sellerId}/{sellerSkuId}&#x60;.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;StockKeepingUnitId\&quot;: 1  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuBindingsApi;

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

    SkuBindingsApi apiInstance = new SkuBindingsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String sellerId = "101"; // String | ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    String sellerSkuId = "1"; // String | SKU ID in the seller's store.
    BindtoanotherskuRequest bindtoanotherskuRequest = new BindtoanotherskuRequest(); // BindtoanotherskuRequest | Request body
    try {
      apiInstance.bindtoanothersku(contentType, accept, sellerId, sellerSkuId, bindtoanotherskuRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuBindingsApi#bindtoanothersku");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **sellerId** | **String**| ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID. | |
| **sellerSkuId** | **String**| SKU ID in the seller&#39;s store. | |
| **bindtoanotherskuRequest** | [**BindtoanotherskuRequest**](BindtoanotherskuRequest.md)| Request body | [optional] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="changeNotification"></a>
# **changeNotification**
> changeNotification(contentType, accept, skuId)

Change Notification with SKU ID

The seller is responsible for suggesting new SKUs to be sold in the VTEX marketplace and also for informing the marketplace about changes in their SKUs that already exist in the marketplace. Both actions start with a catalog notification, which is made by this request.  With this notification, the seller is telling the marketplace that something has changed about a specific SKU, like price or inventory, or that this is a new SKU that the seller would like to offer to the marketplace.  The body of the request should be empty.     &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/changenotification/{skuId}&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuBindingsApi;

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

    SkuBindingsApi apiInstance = new SkuBindingsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String skuId = "10"; // String | A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use to look for the SKU whose change the seller wants to inform. If the marketplace finds this ID, it responds with status code `200`. Otherwise, it responds with status code `404`.
    try {
      apiInstance.changeNotification(contentType, accept, skuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuBindingsApi#changeNotification");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **skuId** | **String**| A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use to look for the SKU whose change the seller wants to inform. If the marketplace finds this ID, it responds with status code &#x60;200&#x60;. Otherwise, it responds with status code &#x60;404&#x60;. | |

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
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **429** | Too many requests |  -  |

<a id="deactivateSKUBinding"></a>
# **deactivateSKUBinding**
> deactivateSKUBinding(contentType, accept, sellerId, skuSellerId)

Deactivate SKU Binding

Changes the status of an SKU Binding to inactive, setting &#x60;isActive&#x60; to &#x60;false&#x60;.      &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/inactivate/{sellerId}/{skuSellerId}&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuBindingsApi;

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

    SkuBindingsApi apiInstance = new SkuBindingsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String sellerId = "vtxkfj7352"; // String | ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    String skuSellerId = "71"; // String | SKU ID in the seller's store.
    try {
      apiInstance.deactivateSKUBinding(contentType, accept, sellerId, skuSellerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuBindingsApi#deactivateSKUBinding");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **sellerId** | **String**| ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID. | |
| **skuSellerId** | **String**| SKU ID in the seller&#39;s store. | |

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

<a id="deleteSKUsellerassociation"></a>
# **deleteSKUsellerassociation**
> deleteSKUsellerassociation(contentType, accept, sellerId, sellerSkuId)

Remove a seller&#39;s SKU Binding

Remove a seller&#39;s SKU binding, given the Seller ID and the SKU ID in the seller&#39;s store.      &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/remove/{sellerId}/{sellerSkuId}&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuBindingsApi;

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

    SkuBindingsApi apiInstance = new SkuBindingsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String sellerId = "vtxkfj7352"; // String | ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    String sellerSkuId = "71"; // String | SKU ID in the seller's store.
    try {
      apiInstance.deleteSKUsellerassociation(contentType, accept, sellerId, sellerSkuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuBindingsApi#deleteSKUsellerassociation");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **sellerId** | **String**| ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID. | |
| **sellerSkuId** | **String**| SKU ID in the seller&#39;s store. | |

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

<a id="getSKUseller"></a>
# **getSKUseller**
> GetSKUseller200Response getSKUseller(contentType, accept, sellerId, sellerSkuId)

Get details of a seller&#39;s SKU

Retrieves the details of a seller&#39;s SKU given a seller ID and the SKU ID in the seller&#39;s store.      &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/{sellerId}/{sellerSkuId}&#x60;.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;IsPersisted\&quot;: true,      \&quot;IsRemoved\&quot;: false,      \&quot;SkuSellerId\&quot;: 102,      \&quot;UpdateDate\&quot;: \&quot;2021-04-12T20:06:59.413Z\&quot;,      \&quot;RequestedUpdateDate\&quot;: null,      \&quot;SellerStockKeepingUnitId\&quot;: \&quot;71\&quot;,      \&quot;SellerId\&quot;: \&quot;vtxkfj7352\&quot;,      \&quot;StockKeepingUnitId\&quot;: 1,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuBindingsApi;

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

    SkuBindingsApi apiInstance = new SkuBindingsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String sellerId = "101"; // String | ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    String sellerSkuId = "1"; // String | SKU ID in the seller's store.
    try {
      GetSKUseller200Response result = apiInstance.getSKUseller(contentType, accept, sellerId, sellerSkuId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuBindingsApi#getSKUseller");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **sellerId** | **String**| ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID. | |
| **sellerSkuId** | **String**| SKU ID in the seller&#39;s store. | |

### Return type

[**GetSKUseller200Response**](GetSKUseller200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getallbySellerId"></a>
# **getallbySellerId**
> List&lt;GetallbySellerId200ResponseInner&gt; getallbySellerId(contentType, accept, sellerId)

Get all SKU Bindings by Seller ID

Retrieves a list of SKU Bindings given a specific Seller ID.      &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/list/bysellerId/{sellerId}&#x60;.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;SellerStockKeepingUnitId\&quot;: \&quot;24\&quot;,          \&quot;FreightCommissionPercentage\&quot;: null,          \&quot;ProductCommissionPercentage\&quot;: null,          \&quot;SellerId\&quot;: \&quot;vtxkfj7352\&quot;,          \&quot;StockKeepingUnitId\&quot;: 121,          \&quot;IsActive\&quot;: true      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuBindingsApi;

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

    SkuBindingsApi apiInstance = new SkuBindingsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String sellerId = "vtxkfj7352"; // String | ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    try {
      List<GetallbySellerId200ResponseInner> result = apiInstance.getallbySellerId(contentType, accept, sellerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuBindingsApi#getallbySellerId");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **sellerId** | **String**| ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID. | |

### Return type

[**List&lt;GetallbySellerId200ResponseInner&gt;**](GetallbySellerId200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getbySkuId"></a>
# **getbySkuId**
> List&lt;GetbySkuId200ResponseInner&gt; getbySkuId(contentType, accept, skuId)

Get SKU Bindings by SKU ID

Retrieves SKU Bindings details by SKU ID.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 48,          \&quot;SellerId\&quot;: \&quot;cosmetics1\&quot;,          \&quot;StockKeepingUnitId\&quot;: 1,          \&quot;SellerSkuId\&quot;: \&quot;42\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;LastUpdateDate\&quot;: \&quot;2020-10-21T19:13:00.657\&quot;,          \&quot;SalesPolicy\&quot;: 0      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuBindingsApi;

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

    SkuBindingsApi apiInstance = new SkuBindingsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String skuId = "1"; // String | SKU's unique identifier in the marketplace.
    try {
      List<GetbySkuId200ResponseInner> result = apiInstance.getbySkuId(contentType, accept, skuId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuBindingsApi#getbySkuId");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **skuId** | **String**| SKU&#39;s unique identifier in the marketplace. | |

### Return type

[**List&lt;GetbySkuId200ResponseInner&gt;**](GetbySkuId200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getpagedadmin"></a>
# **getpagedadmin**
> Getpagedadmin200Response getpagedadmin(contentType, accept, sellerId, skuId, sellerSkuId, isActive, size)

Get SKU Bindings information

Retrieves SKU Bindings administrative information using optional query params &#x60;sellerId&#x60;, &#x60;skuId&#x60;, &#x60;sellerSkuId&#x60; and &#x60;IsActive&#x60; to filter results and &#x60;size&#x60; to restrict the amount of results.      &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/admin&#x60;.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;IsPersisted\&quot;: true,          \&quot;IsRemoved\&quot;: false,          \&quot;SkuSellerId\&quot;: 1,          \&quot;UpdateDate\&quot;: \&quot;2019-12-04T01:56:00.673Z\&quot;,          \&quot;RequestedUpdateDate\&quot;: null,          \&quot;SellerStockKeepingUnitId\&quot;: \&quot;12\&quot;,          \&quot;SellerId\&quot;: \&quot;cosmetics1\&quot;,          \&quot;StockKeepingUnitId\&quot;: 25,          \&quot;IsActive\&quot;: true      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuBindingsApi;

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

    SkuBindingsApi apiInstance = new SkuBindingsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String sellerId = "vtxkfj7352"; // String | ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    String skuId = "1"; // String | SKU's unique identifier in the marketplace.
    String sellerSkuId = "71"; // String | SKU ID in the seller's store.
    Boolean isActive = true; // Boolean | Defines if the SKU binding is active.
    String size = "1"; // String | Amount of results.
    try {
      Getpagedadmin200Response result = apiInstance.getpagedadmin(contentType, accept, sellerId, skuId, sellerSkuId, isActive, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuBindingsApi#getpagedadmin");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **sellerId** | **String**| ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID. | [optional] |
| **skuId** | **String**| SKU&#39;s unique identifier in the marketplace. | [optional] |
| **sellerSkuId** | **String**| SKU ID in the seller&#39;s store. | [optional] |
| **isActive** | **Boolean**| Defines if the SKU binding is active. | [optional] |
| **size** | **String**| Amount of results. | [optional] |

### Return type

[**Getpagedadmin200Response**](Getpagedadmin200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getpagedbySellerId"></a>
# **getpagedbySellerId**
> List&lt;GetallbySellerId200ResponseInner&gt; getpagedbySellerId(page, size, contentType, accept, sellerId)

Get paged SKU Bindings by Seller ID

Retrieves a paged list of SKU Bindings given a specific Seller ID.      &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/paged/sellerid/{sellerId}&#x60;.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;SellerId\&quot;: \&quot;vtxkfj7352\&quot;,          \&quot;StockKeepingUnitId\&quot;: 121,          \&quot;SellerStockKeepingUnitId\&quot;: \&quot;24\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;FreightCommissionPercentage\&quot;: null,          \&quot;ProductCommissionPercentage\&quot;: null      },      {          \&quot;SellerId\&quot;: \&quot;vtxkfj7352\&quot;,          \&quot;StockKeepingUnitId\&quot;: 14,          \&quot;SellerStockKeepingUnitId\&quot;: \&quot;60\&quot;,          \&quot;IsActive\&quot;: true,          \&quot;FreightCommissionPercentage\&quot;: null,          \&quot;ProductCommissionPercentage\&quot;: null      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuBindingsApi;

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

    SkuBindingsApi apiInstance = new SkuBindingsApi(defaultClient);
    String page = "1"; // String | Page number.
    String size = "2"; // String | Amount of results per page.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String sellerId = "vtxkfj7352"; // String | ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    try {
      List<GetallbySellerId200ResponseInner> result = apiInstance.getpagedbySellerId(page, size, contentType, accept, sellerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuBindingsApi#getpagedbySellerId");
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
| **page** | **String**| Page number. | |
| **size** | **String**| Amount of results per page. | |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **sellerId** | **String**| ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID. | |

### Return type

[**List&lt;GetallbySellerId200ResponseInner&gt;**](GetallbySellerId200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="insertSKUBinding"></a>
# **insertSKUBinding**
> insertSKUBinding(contentType, accept, insertSKUBindingRequest)

Insert SKU Binding

Creates an SKU Binding, associating a seller&#39;s SKU with a marketplace&#39;s SKU.     &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/insertion&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuBindingsApi;

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

    SkuBindingsApi apiInstance = new SkuBindingsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    InsertSKUBindingRequest insertSKUBindingRequest = new InsertSKUBindingRequest(); // InsertSKUBindingRequest | Request body
    try {
      apiInstance.insertSKUBinding(contentType, accept, insertSKUBindingRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuBindingsApi#insertSKUBinding");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **insertSKUBindingRequest** | [**InsertSKUBindingRequest**](InsertSKUBindingRequest.md)| Request body | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **409** | Conflict |  -  |

<a id="skuBindingPvtSkusellerChangenotificationSellerIdSellerSkuIdPost"></a>
# **skuBindingPvtSkusellerChangenotificationSellerIdSellerSkuIdPost**
> skuBindingPvtSkusellerChangenotificationSellerIdSellerSkuIdPost(contentType, accept, sellerId, sellerSkuId)

Change Notification with Seller ID and Seller SKU ID

The seller is responsible for suggesting new SKUs to be sold in the VTEX marketplace and also for informing the marketplace about changes in their SKUs that already exist in the marketplace. Both actions start with a catalog notification, which is made by this request.  With this notification, the seller is telling the marketplace that something has changed about a specific SKU, like price or inventory, or that this is a new SKU that the seller would like to offer to the marketplace.  There are two information expected by the marketplace in this request: the &#x60;sellerId&#x60;, which identifies the seller, and the &#x60;sellerSkuId&#x60;, which identifies the binding of the seller with the SKU.  Both information are passed through the request URL. The body of the request should be empty.   &gt; ℹ This path is an updated version of &#x60;/api/catalog_system/pvt/skuseller/changenotification/{sellerId}/{sellerSkuId}&#x60;.    ## Example    Let&#39;s say your seller has the ID &#x60;123&#x60; in the marketplace and you want to inform the marketplace that has been a change in the SKU with ID &#x60;700&#x60;.    In this case, you would have to replace the &#x60;sellerId&#x60; parameter with the value &#x60;123&#x60; and the &#x60;skuId&#x60; parameter with the value &#x60;700&#x60;. The URL of the request would be the following.    &#x60;&#x60;&#x60;  https://{{accountName}}.vtexcommercestable.com.br/api/sku-binding/pvt/skuseller/changenotification/123/700  &#x60;&#x60;&#x60;    ## Response codes    The following response codes are possible for this request.  * 200: the SKU whose ID was informed in the URL already exists in the marketplace and was found. The marketplace can now proceed with a fulfillment simulation in order to get updated information about this SKU&#39;s inventory and price.  * 403: Failure in the authentication.  * 404: the SKU was not found in the marketplace. The body of the response, in this case, should follow this format: \&quot;Seller StockKeepingUnit &#x60;{{skuId}}&#x60; not found for this seller id &#x60;{{sellerId}}&#x60;. This means that the seller can now proceed with sending an offer to the marketplace in order to suggest that this SKU is sold there.  * 429: Failure due to too many requests.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuBindingsApi;

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

    SkuBindingsApi apiInstance = new SkuBindingsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String sellerId = "101"; // String | ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    String sellerSkuId = "1"; // String | ID of the binding of the seller with the SKU.
    try {
      apiInstance.skuBindingPvtSkusellerChangenotificationSellerIdSellerSkuIdPost(contentType, accept, sellerId, sellerSkuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuBindingsApi#skuBindingPvtSkusellerChangenotificationSellerIdSellerSkuIdPost");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **sellerId** | **String**| ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID. | |
| **sellerSkuId** | **String**| ID of the binding of the seller with the SKU. | |

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
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **429** | Too many requests |  -  |

