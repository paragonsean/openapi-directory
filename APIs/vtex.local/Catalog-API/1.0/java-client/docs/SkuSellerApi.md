# SkuSellerApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogSystemPvtSkusellerChangenotificationSellerIdSellerSkuIdPost**](SkuSellerApi.md#apiCatalogSystemPvtSkusellerChangenotificationSellerIdSellerSkuIdPost) | **POST** /api/catalog_system/pvt/skuseller/changenotification/{sellerId}/{sellerSkuId} | Change Notification with Seller ID and Seller SKU ID |
| [**changeNotification**](SkuSellerApi.md#changeNotification) | **POST** /api/catalog_system/pvt/skuseller/changenotification/{skuId} | Change Notification with SKU ID |
| [**deleteSKUsellerassociation**](SkuSellerApi.md#deleteSKUsellerassociation) | **POST** /api/catalog_system/pvt/skuseller/remove/{sellerId}/{sellerSkuId} | Remove a seller&#39;s SKU binding |
| [**getSKUseller**](SkuSellerApi.md#getSKUseller) | **GET** /api/catalog_system/pvt/skuseller/{sellerId}/{sellerSkuId} | Get details of a seller&#39;s SKU |


<a id="apiCatalogSystemPvtSkusellerChangenotificationSellerIdSellerSkuIdPost"></a>
# **apiCatalogSystemPvtSkusellerChangenotificationSellerIdSellerSkuIdPost**
> apiCatalogSystemPvtSkusellerChangenotificationSellerIdSellerSkuIdPost(contentType, accept, sellerId, sellerSkuId)

Change Notification with Seller ID and Seller SKU ID

 &gt; ⚠️ Check out the updated version of the SKU Seller endpoints in our [SKU Bindings API documentation](https://developers.vtex.com/vtex-rest-api/reference/getbyskuid). If you are doing this integration for the first time, we recommend that you follow the updated documentation.  The seller is responsible for suggesting new SKUs to be sold in the VTEX marketplace and also for informing the marketplace about changes in their SKUs that already exist in the marketplace. Both actions start with a catalog notification, which is made by this request.  With this notification, the seller is telling the marketplace that something has changed about a specific SKU, like price or inventory, or that this is a new SKU that the seller would like to offer to the marketplace.  There are two information expected by the marketplace in this request: the &#x60;sellerId&#x60;, which identifies the seller, and the &#x60;sellerSkuId&#x60;, which identifies the binding of the seller with the SKU.  Both information are passed through the request URL. The body of the request should be empty.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuSellerApi;

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

    SkuSellerApi apiInstance = new SkuSellerApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String sellerId = "101"; // String | ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    String sellerSkuId = "1"; // String | ID of the binding of the seller with the SKU.
    try {
      apiInstance.apiCatalogSystemPvtSkusellerChangenotificationSellerIdSellerSkuIdPost(contentType, accept, sellerId, sellerSkuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuSellerApi#apiCatalogSystemPvtSkusellerChangenotificationSellerIdSellerSkuIdPost");
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
| **204** | No Content |  -  |

<a id="changeNotification"></a>
# **changeNotification**
> changeNotification(contentType, accept, skuId)

Change Notification with SKU ID

 &gt; ⚠️ Check out the updated version of the SKU Seller endpoints in our [SKU Bindings API documentation](https://developers.vtex.com/vtex-rest-api/reference/getbyskuid). If you are doing this integration for the first time, we recommend that you follow the updated documentation.  The seller is responsible for suggesting new SKUs to be sold in the VTEX marketplace and also for informing the marketplace about changes in their SKUs that already exist in the marketplace. Both actions start with a catalog notification, which is made by this request.  With this notification, the seller is telling the marketplace that something has changed about a specific SKU, like price or inventory, or that this is a new SKU that the seller would like to offer to the marketplace.  The body of the request should be empty.  ## Example    Let&#39;s say your seller has the ID &#x60;123&#x60; in the marketplace and you want to inform the marketplace that has been a change in the SKU with ID &#x60;700&#x60;.    In this case, you would have to replace the &#x60;sellerId&#x60; parameter with the value &#x60;123&#x60; and the &#x60;skuId&#x60; parameter with the value &#x60;700&#x60;. The URL of the request would be the following.    &#x60;&#x60;&#x60;  https://{{accountName}}.vtexcommercestable.com.br/api/catalog_system/pvt/skuseller/changenotification/123/700  &#x60;&#x60;&#x60;    ## Response codes    The following response codes are possible for this request.    * 404: the SKU was not found in the marketplace. The body of the response, in this case, should follow this format: \&quot;Seller StockKeepingUnit &#x60;{{skuId}}&#x60; not found for this seller id &#x60;{{sellerId}}&#x60;\&quot;. This means that the seller can now proceed with sending an offer to the marketplace in order to suggest that this SKU is sold there.  * 200: the SKU whose ID was informed in the URL already exists in the marketplace and was found. The marketplace can now proceed with a fulfillment simulation in order to get updated information about this SKU&#39;s inventory and price.  * 429 - Failure due to too many requests.  * 403 - Failure in the authentication.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuSellerApi;

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

    SkuSellerApi apiInstance = new SkuSellerApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String skuId = "10"; // String | A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use to look for the SKU whose change the seller wants to inform. If the marketplace finds this ID, it responds with status code 200. Otherwise, it responds with status code 404.
    try {
      apiInstance.changeNotification(contentType, accept, skuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuSellerApi#changeNotification");
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
| **skuId** | **String**| A string that identifies the SKU in the marketplace. This is the ID that the marketplace will use to look for the SKU whose change the seller wants to inform. If the marketplace finds this ID, it responds with status code 200. Otherwise, it responds with status code 404. | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **403** | Forbidden |  -  |
| **404** | Not found |  -  |
| **429** | Too many requests |  -  |

<a id="deleteSKUsellerassociation"></a>
# **deleteSKUsellerassociation**
> deleteSKUsellerassociation(contentType, accept, sellerId, sellerSkuId)

Remove a seller&#39;s SKU binding

 &gt; ⚠️ Check out the updated version of the SKU Seller endpoints in our [SKU Bindings API documentation](https://developers.vtex.com/vtex-rest-api/reference/getbyskuid). If you are doing this integration for the first time, we recommend that you follow the updated documentation.  Remove a seller&#39;s SKU binding, given the seller ID and the SKU ID in the seller&#39;s store.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuSellerApi;

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

    SkuSellerApi apiInstance = new SkuSellerApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String sellerId = "101"; // String | ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    String sellerSkuId = "1"; // String | SKU ID in the seller's store.
    try {
      apiInstance.deleteSKUsellerassociation(contentType, accept, sellerId, sellerSkuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuSellerApi#deleteSKUsellerassociation");
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

 &gt; ⚠️ Check out the updated version of the SKU Seller endpoints in our [SKU Bindings API documentation](https://developers.vtex.com/vtex-rest-api/reference/getbyskuid). If you are doing this integration for the first time, we recommend that you follow the updated documentation.  Retrieves the details of a seller&#39;s SKU given a seller ID and the SKU ID in the seller&#39;s store.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;IsPersisted\&quot;: true,      \&quot;IsRemoved\&quot;: false,      \&quot;SkuSellerId\&quot;: 799,      \&quot;SellerId\&quot;: \&quot;myseller\&quot;,      \&quot;StockKeepingUnitId\&quot;: 50,      \&quot;SellerStockKeepingUnitId\&quot;: \&quot;502\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;UpdateDate\&quot;: \&quot;2018-10-11T04:52:42.1\&quot;,      \&quot;RequestedUpdateDate\&quot;: null  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuSellerApi;

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

    SkuSellerApi apiInstance = new SkuSellerApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String sellerId = "101"; // String | ID that identifies the seller in the marketplace. It can be the same as the seller name or a unique number. Check the **Sellers management** section in the Admin to get the correct ID.
    String sellerSkuId = "1"; // String | SKU ID in the seller's store.
    try {
      GetSKUseller200Response result = apiInstance.getSKUseller(contentType, accept, sellerId, sellerSkuId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuSellerApi#getSKUseller");
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

