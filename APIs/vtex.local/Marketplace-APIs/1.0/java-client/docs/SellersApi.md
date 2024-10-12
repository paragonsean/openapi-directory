# SellersApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getListSellers**](SellersApi.md#getListSellers) | **GET** /seller-register/pvt/sellers | List Sellers |
| [**getRetrieveSeller**](SellersApi.md#getRetrieveSeller) | **GET** /seller-register/pvt/sellers/{sellerId} | Get Seller data by ID |
| [**updateSeller**](SellersApi.md#updateSeller) | **PATCH** /seller-register/pvt/sellers/{sellerId} | Update Seller by Seller ID |
| [**upsertSellerRequest**](SellersApi.md#upsertSellerRequest) | **POST** /seller-register/pvt/sellers | Configure Seller Account |


<a id="getListSellers"></a>
# **getListSellers**
> getListSellers(accountName, environment, accept, contentType, from, to, keyword, integration, group, isActive, isBetterScope, isVtex, sc, sellerType, sort)

List Sellers

This endpoint lists all Sellers. This call&#39;s results can be filtered by [trade policies](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data) through the &#x60;sc&#x60; query param.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SellersApi;

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

    SellersApi apiInstance = new SellersApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Type of the content being sent.
    BigDecimal from = new BigDecimal("0"); // BigDecimal | The start number of pagination, being `0` the default value.
    BigDecimal to = new BigDecimal("100"); // BigDecimal | The end number of pagination, being `100` the default value.
    String keyword = "keyword"; // String | Search sellers by a keyword in `sellerId` or `sellerName`.
    String integration = "vtex-seller"; // String | Filters sellers by the name of who made the integration, if VTEX or an external hub. The possible values for VTEX integrations are: `vtex-sellerportal`, `vtex-seller` and `vtex-franchise`.
    String group = "Group"; // String | Groups are defined by keywords that group sellers into categories defined by the marketplace.
    Boolean isActive = false; // Boolean | Enables to filter sellers that are active (`true`) or unactive (`false`) in the marketplace.
    Boolean isBetterScope = false; // Boolean | The flag `isBetterScope` is used by the VTEX Checkout to simulate shopping carts, products, and shipping only in sellers with the field set as `true`, avoiding performance issues. When used as a query param, `isBetterScope` filters sellers that have the flag set as `true` or `false`.
    Boolean isVtex = false; // Boolean | When set as `true`, the list returned will be of sellers who have a VTEX store configured. When set as `false`, the list will be of sellers who do not have a VTEX store configured.
    String sc = "1"; // String | Filters sellers available for the marketplace's sales channel (or [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) indicated in this field.
    Integer sellerType = 1; // Integer | Filters sellers by their type, which can be regular seller (`1`) or whitelabel seller (`2`).
    String sort = "id:asc"; // String | Narrow the search filtering by the fields: `id`, `name` or `pendingoffers`. The list retrieved can be organized in an ascending (`asc`) or descending (`desc`) order. The standardized format is `{field}:{order}`, and the default value is `id:asc`.
    try {
      apiInstance.getListSellers(accountName, environment, accept, contentType, from, to, keyword, integration, group, isActive, isBetterScope, isVtex, sc, sellerType, sort);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellersApi#getListSellers");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **from** | **BigDecimal**| The start number of pagination, being &#x60;0&#x60; the default value. | [optional] [default to 0] |
| **to** | **BigDecimal**| The end number of pagination, being &#x60;100&#x60; the default value. | [optional] [default to 100] |
| **keyword** | **String**| Search sellers by a keyword in &#x60;sellerId&#x60; or &#x60;sellerName&#x60;. | [optional] [default to keyword] |
| **integration** | **String**| Filters sellers by the name of who made the integration, if VTEX or an external hub. The possible values for VTEX integrations are: &#x60;vtex-sellerportal&#x60;, &#x60;vtex-seller&#x60; and &#x60;vtex-franchise&#x60;. | [optional] [default to vtex-seller] |
| **group** | **String**| Groups are defined by keywords that group sellers into categories defined by the marketplace. | [optional] [default to Group] |
| **isActive** | **Boolean**| Enables to filter sellers that are active (&#x60;true&#x60;) or unactive (&#x60;false&#x60;) in the marketplace. | [optional] [default to false] |
| **isBetterScope** | **Boolean**| The flag &#x60;isBetterScope&#x60; is used by the VTEX Checkout to simulate shopping carts, products, and shipping only in sellers with the field set as &#x60;true&#x60;, avoiding performance issues. When used as a query param, &#x60;isBetterScope&#x60; filters sellers that have the flag set as &#x60;true&#x60; or &#x60;false&#x60;. | [optional] [default to false] |
| **isVtex** | **Boolean**| When set as &#x60;true&#x60;, the list returned will be of sellers who have a VTEX store configured. When set as &#x60;false&#x60;, the list will be of sellers who do not have a VTEX store configured. | [optional] [default to false] |
| **sc** | **String**| Filters sellers available for the marketplace&#39;s sales channel (or [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) indicated in this field. | [optional] [default to 1] |
| **sellerType** | **Integer**| Filters sellers by their type, which can be regular seller (&#x60;1&#x60;) or whitelabel seller (&#x60;2&#x60;). | [optional] [default to 1] |
| **sort** | **String**| Narrow the search filtering by the fields: &#x60;id&#x60;, &#x60;name&#x60; or &#x60;pendingoffers&#x60;. The list retrieved can be organized in an ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;) order. The standardized format is &#x60;{field}:{order}&#x60;, and the default value is &#x60;id:asc&#x60;. | [optional] [default to id:asc] |

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

<a id="getRetrieveSeller"></a>
# **getRetrieveSeller**
> getRetrieveSeller(accountName, environment, sellerId, accept, contentType, sc)

Get Seller data by ID

Marketplace operator may call this endpoint to retrieve information about a specific seller by filtering by ID. It is also possible to filter results by sales channel (or [trade policy](https://help.vtex.com/en/tutorial/como-funciona-uma-politica-comercial--6Xef8PZiFm40kg2STrMkMV#master-data)) through the &#x60;sc&#x60; query param.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SellersApi;

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

    SellersApi apiInstance = new SellersApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Type of the content being sent.
    String sc = "1"; // String | Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) associated to the seller account created.
    try {
      apiInstance.getRetrieveSeller(accountName, environment, sellerId, accept, contentType, sc);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellersApi#getRetrieveSeller");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace | [default to seller123] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **sc** | **String**| Sales channel (or [trade policy](https://help.vtex.com/en/tutorial/how-trade-policies-work--6Xef8PZiFm40kg2STrMkMV)) associated to the seller account created. | [optional] [default to 1] |

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

<a id="updateSeller"></a>
# **updateSeller**
> updateSeller(accountName, environment, accept, contentType, sellerId, requestBodyInner)

Update Seller by Seller ID

This endpoint allows marketplace operators to update the information of sellers connected to their account. You can replace a path&#39;s value with another value in order to update that single information. There is no need to fill all the body params available, only the one you wish to update.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SellersApi;

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

    SellersApi apiInstance = new SellersApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Type of the content being sent.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace
    List<RequestBodyInner> requestBodyInner = Arrays.asList(); // List<RequestBodyInner> | array of objects
    try {
      apiInstance.updateSeller(accountName, environment, accept, contentType, sellerId, requestBodyInner);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellersApi#updateSeller");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace | [default to seller123] |
| **requestBodyInner** | [**List&lt;RequestBodyInner&gt;**](RequestBodyInner.md)| array of objects | [optional] |

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

<a id="upsertSellerRequest"></a>
# **upsertSellerRequest**
> upsertSellerRequest(accountName, environment, accept, contentType, upsertSellerRequest)

Configure Seller Account

This endpoint is used by marketplace operators to configure the accounts of sellers that have already accepted the invitation to join their marketplaces.   For marketplaces to [add sellers](https://help.vtex.com/en/tutorial/adding-a-seller--tutorials_392) without the [Seller Invite](https://help.vtex.com/en/tutorial/marketplace-invited-sellers--6rb2FkcslmDueJ689Ulb9A) feature, call this endpoint directly.   This call includes all the information a seller needs to activate their account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SellersApi;

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

    SellersApi apiInstance = new SellersApi(defaultClient);
    String accountName = "apiexamples"; // String | Marketplace's account name, the same one inputted on the endpoint's path.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Type of the content being sent.
    UpsertSellerRequest upsertSellerRequest = new UpsertSellerRequest(); // UpsertSellerRequest | 
    try {
      apiInstance.upsertSellerRequest(accountName, environment, accept, contentType, upsertSellerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellersApi#upsertSellerRequest");
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
| **accountName** | **String**| Marketplace&#39;s account name, the same one inputted on the endpoint&#39;s path. | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **upsertSellerRequest** | [**UpsertSellerRequest**](UpsertSellerRequest.md)|  | |

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

