# PriceTablesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getallpricetablesandrules**](PriceTablesApi.md#getallpricetablesandrules) | **GET** /pricing/pipeline/catalog | Get all price tables and their rules |
| [**getrulesforapricetable**](PriceTablesApi.md#getrulesforapricetable) | **GET** /pricing/pipeline/catalog/{priceTableId} | Get rules for a price table |
| [**listpricetables**](PriceTablesApi.md#listpricetables) | **GET** /pricing/tables | List price tables |
| [**pricingPipelineCatalogPriceTableIdPut**](PriceTablesApi.md#pricingPipelineCatalogPriceTableIdPut) | **PUT** /pricing/pipeline/catalog/{priceTableId} | Update rules for a price table |


<a id="getallpricetablesandrules"></a>
# **getallpricetablesandrules**
> List&lt;Getallpricetablesandrules200ResponseInner&gt; getallpricetablesandrules(contentType, accept)

Get all price tables and their rules

This method will retrieve all price tables and their rules.    ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;tradePolicyId\&quot;: \&quot;2\&quot;,          \&quot;rules\&quot;: [              {                  \&quot;id\&quot;: 0,                  \&quot;context\&quot;: {                      \&quot;categories\&quot;: {},                      \&quot;brands\&quot;: {},                      \&quot;stockStatuses\&quot;: null,                      \&quot;internalCategories\&quot;: null,                      \&quot;markupRange\&quot;: null,                      \&quot;dateRange\&quot;: null                  },                  \&quot;percentualModifier\&quot;: 20              }          ]      },      {          \&quot;tradePolicyId\&quot;: \&quot;b2c\&quot;,          \&quot;rules\&quot;: [              {                  \&quot;id\&quot;: 0,                  \&quot;context\&quot;: {                      \&quot;categories\&quot;: {},                      \&quot;brands\&quot;: {                          \&quot;2000009\&quot;: \&quot;Whiskas\&quot;                      },                      \&quot;stockStatuses\&quot;: null,                      \&quot;internalCategories\&quot;: null,                      \&quot;markupRange\&quot;: null,                      \&quot;dateRange\&quot;: null                  },                  \&quot;percentualModifier\&quot;: 15              }          ]      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriceTablesApi;

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

    PriceTablesApi apiInstance = new PriceTablesApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      List<Getallpricetablesandrules200ResponseInner> result = apiInstance.getallpricetablesandrules(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriceTablesApi#getallpricetablesandrules");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |

### Return type

[**List&lt;Getallpricetablesandrules200ResponseInner&gt;**](Getallpricetablesandrules200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getrulesforapricetable"></a>
# **getrulesforapricetable**
> Getrulesforapricetable200Response getrulesforapricetable(contentType, accept, priceTableId)

Get rules for a price table

This method will retrieve the rules from a specific Price Table.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;tradePolicyId\&quot;: \&quot;b2c\&quot;,      \&quot;rules\&quot;: [{          \&quot;id\&quot;: 0,          \&quot;context\&quot;: {              \&quot;categories\&quot;: {},              \&quot;brands\&quot;: {                  \&quot;2000009\&quot;: \&quot;Whiskas\&quot;              },              \&quot;stockStatuses\&quot;: null,              \&quot;internalCategories\&quot;: null,              \&quot;markupRange\&quot;: null,              \&quot;dateRange\&quot;: null          },          \&quot;percentualModifier\&quot;: 15      }]  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriceTablesApi;

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

    PriceTablesApi apiInstance = new PriceTablesApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String priceTableId = "b2c"; // String | Price Table Name.
    try {
      Getrulesforapricetable200Response result = apiInstance.getrulesforapricetable(contentType, accept, priceTableId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriceTablesApi#getrulesforapricetable");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **priceTableId** | **String**| Price Table Name. | |

### Return type

[**Getrulesforapricetable200Response**](Getrulesforapricetable200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **429** | Too many requests |  -  |

<a id="listpricetables"></a>
# **listpricetables**
> List&lt;String&gt; listpricetables(contentType, accept)

List price tables

This method will list all price tables.    ## Response body example    &#x60;&#x60;&#x60;json  [      \&quot;1\&quot;,      \&quot;2\&quot;,      \&quot;3\&quot;,      \&quot;b2c\&quot;,      \&quot;b2b\&quot;,      \&quot;gold\&quot;  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriceTablesApi;

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

    PriceTablesApi apiInstance = new PriceTablesApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      List<String> result = apiInstance.listpricetables(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriceTablesApi#listpricetables");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |

### Return type

**List&lt;String&gt;**

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="pricingPipelineCatalogPriceTableIdPut"></a>
# **pricingPipelineCatalogPriceTableIdPut**
> pricingPipelineCatalogPriceTableIdPut(contentType, accept, priceTableId, pricingPipelineCatalogPriceTableIdPutRequest)

Update rules for a price table

This method will update the rules from a specific Price Table. It will delete all the rules from the requested Price Table and create new rules based on the content of the request.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;rules\&quot;: [            {                 \&quot;id\&quot;: 1,                 \&quot;context\&quot;: {                      \&quot;categories\&quot;: {                           \&quot;Category ID\&quot;: \&quot;1\&quot;,                           \&quot;Category Name\&quot;: \&quot;Alimentação\&quot;                      },                      \&quot;brands\&quot;: {                           \&quot;Brand ID\&quot;: \&quot;2000002\&quot;,                           \&quot;Brand Name\&quot;: \&quot;Whiskas\&quot;                      },                      \&quot;markupRange\&quot;: {                           \&quot;from\&quot;: 0,                           \&quot;to\&quot;: 200                      },                      \&quot;dateRange\&quot;: {                           \&quot;from\&quot;: \&quot;2022-01-23T19:00:00.000Z\&quot;,                           \&quot;to\&quot;: \&quot;2023-10-26T00:00:00.000Z\&quot;                      }                 },                 \&quot;percentualModifier\&quot;: 0            }      ]  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriceTablesApi;

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

    PriceTablesApi apiInstance = new PriceTablesApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String priceTableId = "priceTableId_example"; // String | Price Table Name.
    PricingPipelineCatalogPriceTableIdPutRequest pricingPipelineCatalogPriceTableIdPutRequest = new PricingPipelineCatalogPriceTableIdPutRequest(); // PricingPipelineCatalogPriceTableIdPutRequest | 
    try {
      apiInstance.pricingPipelineCatalogPriceTableIdPut(contentType, accept, priceTableId, pricingPipelineCatalogPriceTableIdPutRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriceTablesApi#pricingPipelineCatalogPriceTableIdPut");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **priceTableId** | **String**| Price Table Name. | |
| **pricingPipelineCatalogPriceTableIdPutRequest** | [**PricingPipelineCatalogPriceTableIdPutRequest**](PricingPipelineCatalogPriceTableIdPutRequest.md)|  | [optional] |

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
| **201** | Created |  -  |

