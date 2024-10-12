# SupplierApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtSupplierPost**](SupplierApi.md#apiCatalogPvtSupplierPost) | **POST** /api/catalog/pvt/supplier | Create Supplier |
| [**apiCatalogPvtSupplierSupplierIdDelete**](SupplierApi.md#apiCatalogPvtSupplierSupplierIdDelete) | **DELETE** /api/catalog/pvt/supplier/{supplierId} | Delete Supplier |
| [**apiCatalogPvtSupplierSupplierIdPut**](SupplierApi.md#apiCatalogPvtSupplierSupplierIdPut) | **PUT** /api/catalog/pvt/supplier/{supplierId} | Update Supplier |


<a id="apiCatalogPvtSupplierPost"></a>
# **apiCatalogPvtSupplierPost**
> SupplierResponse apiCatalogPvtSupplierPost(contentType, accept, supplierRequest)

Create Supplier

Creates a new Supplier.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Supplier\&quot;,      \&quot;CorporateName\&quot;: \&quot;TopStore\&quot;,      \&quot;StateInscription\&quot;: \&quot;\&quot;,      \&quot;Cnpj\&quot;: \&quot;33304981001272\&quot;,      \&quot;Phone\&quot;: \&quot;3333333333\&quot;,      \&quot;CellPhone\&quot;: \&quot;4444444444\&quot;,      \&quot;CorportePhone\&quot;: \&quot;5555555555\&quot;,      \&quot;Email\&quot;: \&quot;email@email.com\&quot;,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Supplier\&quot;,      \&quot;CorporateName\&quot;: \&quot;TopStore\&quot;,      \&quot;StateInscription\&quot;: \&quot;\&quot;,      \&quot;Cnpj\&quot;: \&quot;33304981001272\&quot;,      \&quot;Phone\&quot;: \&quot;3333333333\&quot;,      \&quot;CellPhone\&quot;: \&quot;4444444444\&quot;,      \&quot;CorportePhone\&quot;: \&quot;5555555555\&quot;,      \&quot;Email\&quot;: \&quot;email@email.com\&quot;,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupplierApi;

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

    SupplierApi apiInstance = new SupplierApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    SupplierRequest supplierRequest = new SupplierRequest(); // SupplierRequest | 
    try {
      SupplierResponse result = apiInstance.apiCatalogPvtSupplierPost(contentType, accept, supplierRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupplierApi#apiCatalogPvtSupplierPost");
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
| **supplierRequest** | [**SupplierRequest**](SupplierRequest.md)|  | [optional] |

### Return type

[**SupplierResponse**](SupplierResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSupplierSupplierIdDelete"></a>
# **apiCatalogPvtSupplierSupplierIdDelete**
> apiCatalogPvtSupplierSupplierIdDelete(contentType, accept, supplierId)

Delete Supplier

Deletes an existing Supplier.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupplierApi;

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

    SupplierApi apiInstance = new SupplierApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer supplierId = 1; // Integer | Supplier's unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtSupplierSupplierIdDelete(contentType, accept, supplierId);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupplierApi#apiCatalogPvtSupplierSupplierIdDelete");
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
| **supplierId** | **Integer**| Supplier&#39;s unique numerical identifier. | |

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

<a id="apiCatalogPvtSupplierSupplierIdPut"></a>
# **apiCatalogPvtSupplierSupplierIdPut**
> SupplierResponse apiCatalogPvtSupplierSupplierIdPut(contentType, accept, supplierId, supplierRequest)

Update Supplier

Updates general information of an existing Supplier.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Supplier\&quot;,      \&quot;CorporateName\&quot;: \&quot;TopStore\&quot;,      \&quot;StateInscription\&quot;: \&quot;\&quot;,      \&quot;Cnpj\&quot;: \&quot;33304981001272\&quot;,      \&quot;Phone\&quot;: \&quot;3333333333\&quot;,      \&quot;CellPhone\&quot;: \&quot;4444444444\&quot;,      \&quot;CorportePhone\&quot;: \&quot;5555555555\&quot;,      \&quot;Email\&quot;: \&quot;email@email.com\&quot;,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Supplier\&quot;,      \&quot;CorporateName\&quot;: \&quot;TopStore\&quot;,      \&quot;StateInscription\&quot;: \&quot;\&quot;,      \&quot;Cnpj\&quot;: \&quot;33304981001272\&quot;,      \&quot;Phone\&quot;: \&quot;3333333333\&quot;,      \&quot;CellPhone\&quot;: \&quot;4444444444\&quot;,      \&quot;CorportePhone\&quot;: \&quot;5555555555\&quot;,      \&quot;Email\&quot;: \&quot;email@email.com\&quot;,      \&quot;IsActive\&quot;: true  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SupplierApi;

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

    SupplierApi apiInstance = new SupplierApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer supplierId = 1; // Integer | Supplier's unique numerical identifier.
    SupplierRequest supplierRequest = new SupplierRequest(); // SupplierRequest | 
    try {
      SupplierResponse result = apiInstance.apiCatalogPvtSupplierSupplierIdPut(contentType, accept, supplierId, supplierRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SupplierApi#apiCatalogPvtSupplierSupplierIdPut");
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
| **supplierId** | **Integer**| Supplier&#39;s unique numerical identifier. | |
| **supplierRequest** | [**SupplierRequest**](SupplierRequest.md)|  | [optional] |

### Return type

[**SupplierResponse**](SupplierResponse.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

