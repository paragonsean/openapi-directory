# SalesChannelMappingApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retrieveMapping**](SalesChannelMappingApi.md#retrieveMapping) | **GET** /seller-register/pvt/sellers/{sellerId}/sales-channel/mapping | Get Sales Channel Mapping Data |
| [**upsertMapping**](SalesChannelMappingApi.md#upsertMapping) | **PUT** /seller-register/pvt/sellers/{sellerId}/sales-channel/mapping | Upsert Sales Channel Mapping |


<a id="retrieveMapping"></a>
# **retrieveMapping**
> List&lt;Object&gt; retrieveMapping(contentType, accept, accountName, environment, an, sellerId)

Get Sales Channel Mapping Data

Retrieves information about the mapping between marketplace&#39;s sales channels and a specific seller.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesChannelMappingApi;

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

    SalesChannelMappingApi apiInstance = new SalesChannelMappingApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. Used as part of the URL
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String an = "apiexamples"; // String | Marketplace's account name, the same one inputted on the endpoint's path.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    try {
      List<Object> result = apiInstance.retrieveMapping(contentType, accept, accountName, environment, an, sellerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesChannelMappingApi#retrieveMapping");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. Used as part of the URL | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **an** | **String**| Marketplace&#39;s account name, the same one inputted on the endpoint&#39;s path. | [default to apiexamples] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to seller123] |

### Return type

**List&lt;Object&gt;**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="upsertMapping"></a>
# **upsertMapping**
> List&lt;Object&gt; upsertMapping(contentType, accept, accountName, environment, an, sellerId, upsertMappingRequest)

Upsert Sales Channel Mapping

This endpoint allows the marketplace to map its sales channels with a seller&#39;s [affiliate](https://help.vtex.com/en/tutorial/configuring-affiliates--tutorials_187). The seller can have multiple sales channels associated with the same marketplace, by creating different affiliates. The mapping enables the seller to segment catalog, prices, inventory, logistics, and payments in the marketplace.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SalesChannelMappingApi;

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

    SalesChannelMappingApi apiInstance = new SalesChannelMappingApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    String accountName = "apiexamples"; // String | Name of the VTEX account that belongs to the marketplace. Used as part of the URL.
    String environment = "vtexcommercestable"; // String | Environment to use. Used as part of the URL.
    String an = "apiexamples"; // String | Marketplace's account name, the same one inputted on the endpoint's path.
    String sellerId = "seller123"; // String | A string that identifies the seller in the marketplace. This ID must be created by the marketplace.
    List<UpsertMappingRequest> upsertMappingRequest = Arrays.asList(); // List<UpsertMappingRequest> | 
    try {
      List<Object> result = apiInstance.upsertMapping(contentType, accept, accountName, environment, an, sellerId, upsertMappingRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SalesChannelMappingApi#upsertMapping");
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
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **accountName** | **String**| Name of the VTEX account that belongs to the marketplace. Used as part of the URL. | [default to apiexamples] |
| **environment** | **String**| Environment to use. Used as part of the URL. | [default to vtexcommercestable] |
| **an** | **String**| Marketplace&#39;s account name, the same one inputted on the endpoint&#39;s path. | [default to apiexamples] |
| **sellerId** | **String**| A string that identifies the seller in the marketplace. This ID must be created by the marketplace. | [default to seller123] |
| **upsertMappingRequest** | [**List&lt;UpsertMappingRequest&gt;**](UpsertMappingRequest.md)|  | |

### Return type

**List&lt;Object&gt;**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

