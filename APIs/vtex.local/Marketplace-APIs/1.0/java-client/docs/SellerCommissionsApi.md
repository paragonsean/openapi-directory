# SellerCommissionsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bulkUpsertSellerCommissions**](SellerCommissionsApi.md#bulkUpsertSellerCommissions) | **PUT** /seller-register/pvt/sellers/{sellerId}/commissions/categories | Upsert Seller Commissions in Bulk |
| [**listSellerCommissions**](SellerCommissionsApi.md#listSellerCommissions) | **GET** /seller-register/pvt/sellers/{sellerId}/commissions | List Seller Commissions by seller ID |
| [**removeSellerCommissions**](SellerCommissionsApi.md#removeSellerCommissions) | **DELETE** /seller-register/pvt/sellers/{sellerId}/commissions/{categoryId} | Remove Seller Commissions by Category ID |
| [**retrieveSellerCommissions**](SellerCommissionsApi.md#retrieveSellerCommissions) | **GET** /seller-register/pvt/sellers/{sellerId}/commissions/{categoryId} | Get Seller Commissions by Category ID |
| [**upsertSellerCommissions**](SellerCommissionsApi.md#upsertSellerCommissions) | **PUT** /seller-register/pvt/sellers/{sellerId}/commissions/{categoryId} | Upsert Seller Commissions by Category ID |


<a id="bulkUpsertSellerCommissions"></a>
# **bulkUpsertSellerCommissions**
> bulkUpsertSellerCommissions(accountName, environment, accept, contentType, sellerId, bulkUpsertSellerCommissionsRequest)

Upsert Seller Commissions in Bulk

This endpoint is used by marketplace operators to define comissions for multiple categories.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SellerCommissionsApi;

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

    SellerCommissionsApi apiInstance = new SellerCommissionsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    List<BulkUpsertSellerCommissionsRequest> bulkUpsertSellerCommissionsRequest = Arrays.asList(); // List<BulkUpsertSellerCommissionsRequest> | 
    try {
      apiInstance.bulkUpsertSellerCommissions(accountName, environment, accept, contentType, sellerId, bulkUpsertSellerCommissionsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerCommissionsApi#bulkUpsertSellerCommissions");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to seller123] |
| **bulkUpsertSellerCommissionsRequest** | [**List&lt;BulkUpsertSellerCommissionsRequest&gt;**](BulkUpsertSellerCommissionsRequest.md)|  | |

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

<a id="listSellerCommissions"></a>
# **listSellerCommissions**
> listSellerCommissions(accountName, environment, sellerId, accept, contentType)

List Seller Commissions by seller ID

This endpoint retrieves all comissions configured for a specific seller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SellerCommissionsApi;

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

    SellerCommissionsApi apiInstance = new SellerCommissionsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    try {
      apiInstance.listSellerCommissions(accountName, environment, sellerId, accept, contentType);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerCommissionsApi#listSellerCommissions");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to seller123] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |

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

<a id="removeSellerCommissions"></a>
# **removeSellerCommissions**
> removeSellerCommissions(accountName, environment, accept, contentType, sellerId, categoryId)

Remove Seller Commissions by Category ID

This endpoint removes a seller comission on the selected category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SellerCommissionsApi;

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

    SellerCommissionsApi apiInstance = new SellerCommissionsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    String categoryId = "6"; // String | ID of the category in which the comission was applied
    try {
      apiInstance.removeSellerCommissions(accountName, environment, accept, contentType, sellerId, categoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerCommissionsApi#removeSellerCommissions");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to seller123] |
| **categoryId** | **String**| ID of the category in which the comission was applied | [default to 6] |

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

<a id="retrieveSellerCommissions"></a>
# **retrieveSellerCommissions**
> retrieveSellerCommissions(accountName, environment, accept, contentType, sellerId, categoryId)

Get Seller Commissions by Category ID

This endpoint retrieves seller comissions applied to the selected category.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SellerCommissionsApi;

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

    SellerCommissionsApi apiInstance = new SellerCommissionsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    String categoryId = "6"; // String | ID of the category in which the comission was applied
    try {
      apiInstance.retrieveSellerCommissions(accountName, environment, accept, contentType, sellerId, categoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerCommissionsApi#retrieveSellerCommissions");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to seller123] |
| **categoryId** | **String**| ID of the category in which the comission was applied | [default to 6] |

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

<a id="upsertSellerCommissions"></a>
# **upsertSellerCommissions**
> upsertSellerCommissions(accountName, environment, sellerId, categoryId, accept, contentType, upsertSellerCommissionsRequest)

Upsert Seller Commissions by Category ID

This endpoint is used by marketplace operators to define comissions for a single category, by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SellerCommissionsApi;

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

    SellerCommissionsApi apiInstance = new SellerCommissionsApi(defaultClient);
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    String categoryId = "6"; // String | ID of the category in which the comission will be applied.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    UpsertSellerCommissionsRequest upsertSellerCommissionsRequest = new UpsertSellerCommissionsRequest(); // UpsertSellerCommissionsRequest | 
    try {
      apiInstance.upsertSellerCommissions(accountName, environment, sellerId, categoryId, accept, contentType, upsertSellerCommissionsRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SellerCommissionsApi#upsertSellerCommissions");
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
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. All data extracted, and changes added will be posted into this account. | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to seller123] |
| **categoryId** | **String**| ID of the category in which the comission will be applied. | [default to 6] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **upsertSellerCommissionsRequest** | [**UpsertSellerCommissionsRequest**](UpsertSellerCommissionsRequest.md)|  | |

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

