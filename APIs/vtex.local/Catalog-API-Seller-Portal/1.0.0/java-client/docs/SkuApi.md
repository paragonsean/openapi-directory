# SkuApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listSKU**](SkuApi.md#listSKU) | **GET** /api/catalog-seller-portal/skus/ids | Get List of SKUs |
| [**searchSKU**](SkuApi.md#searchSKU) | **GET** /api/catalog-seller-portal/skus/_search | Search for SKU |


<a id="listSKU"></a>
# **listSKU**
> ListSKU200Response listSKU(contentType, accept, from, to)

Get List of SKUs

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about all SKUs.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;data\&quot;: [          \&quot;1\&quot;,          \&quot;10\&quot;,          \&quot;11\&quot;,          \&quot;12\&quot;,          \&quot;13\&quot;,          \&quot;14\&quot;,          \&quot;15\&quot;,          \&quot;16\&quot;,          \&quot;19\&quot;,          \&quot;2\&quot;,          \&quot;20\&quot;,          \&quot;21\&quot;,          \&quot;22\&quot;,          \&quot;23\&quot;,          \&quot;24\&quot;      ],      \&quot;_metadata\&quot;: {          \&quot;total\&quot;: 65,          \&quot;from\&quot;: 1,          \&quot;to\&quot;: 15      }  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuApi;

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

    SkuApi apiInstance = new SkuApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String from = "1"; // String | The first page of the interval of the product list.
    String to = "50"; // String | The last page of the interval of the product list.
    try {
      ListSKU200Response result = apiInstance.listSKU(contentType, accept, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuApi#listSKU");
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
| **from** | **String**| The first page of the interval of the product list. | [optional] |
| **to** | **String**| The last page of the interval of the product list. | [optional] |

### Return type

[**ListSKU200Response**](ListSKU200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="searchSKU"></a>
# **searchSKU**
> SearchSKU200Response searchSKU(contentType, accept, from, to, id, externalid)

Search for SKU

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about an SKU taking into consideration the defined search criteria. It is mandatory to use at least one query parameter.     ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;data\&quot;: [      {        \&quot;id\&quot;: \&quot;2\&quot;,        \&quot;productId\&quot;: \&quot;2\&quot;,        \&quot;externalId\&quot;: \&quot;1909621862\&quot;      }    ],    \&quot;_metadata\&quot;: {      \&quot;total\&quot;: 1,      \&quot;from\&quot;: 1,      \&quot;to\&quot;: 15    }  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SkuApi;

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

    SkuApi apiInstance = new SkuApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String from = "1"; // String | The first page of the interval of the product list.
    String to = "50"; // String | The last page of the interval of the product list.
    Integer id = 1; // Integer | SKU unique idenfier number.
    Integer externalid = 123456789; // Integer | SKU reference unique identifier number in the store.
    try {
      SearchSKU200Response result = apiInstance.searchSKU(contentType, accept, from, to, id, externalid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SkuApi#searchSKU");
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
| **from** | **String**| The first page of the interval of the product list. | [optional] |
| **to** | **String**| The last page of the interval of the product list. | [optional] |
| **id** | **Integer**| SKU unique idenfier number. | [optional] |
| **externalid** | **Integer**| SKU reference unique identifier number in the store. | [optional] |

### Return type

[**SearchSKU200Response**](SearchSKU200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

