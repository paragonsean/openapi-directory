# SpecificationApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtSpecificationPost**](SpecificationApi.md#apiCatalogPvtSpecificationPost) | **POST** /api/catalog/pvt/specification | Create Specification |
| [**apiCatalogPvtSpecificationSpecificationIdGet**](SpecificationApi.md#apiCatalogPvtSpecificationSpecificationIdGet) | **GET** /api/catalog/pvt/specification/{specificationId} | Get Specification |
| [**apiCatalogPvtSpecificationSpecificationIdPut**](SpecificationApi.md#apiCatalogPvtSpecificationSpecificationIdPut) | **PUT** /api/catalog/pvt/specification/{specificationId} | Update Specification |


<a id="apiCatalogPvtSpecificationPost"></a>
# **apiCatalogPvtSpecificationPost**
> ApiCatalogPvtSpecificationPost200Response apiCatalogPvtSpecificationPost(contentType, accept, apiCatalogPvtSpecificationPostRequest)

Create Specification

Creates a new Product or SKU Specification.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Cotton\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 88,      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsWizard\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Cotton\&quot;  }  &#x60;&#x60;&#x60;  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecificationApi;

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

    SpecificationApi apiInstance = new SpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    ApiCatalogPvtSpecificationPostRequest apiCatalogPvtSpecificationPostRequest = new ApiCatalogPvtSpecificationPostRequest(); // ApiCatalogPvtSpecificationPostRequest | 
    try {
      ApiCatalogPvtSpecificationPost200Response result = apiInstance.apiCatalogPvtSpecificationPost(contentType, accept, apiCatalogPvtSpecificationPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecificationApi#apiCatalogPvtSpecificationPost");
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
| **apiCatalogPvtSpecificationPostRequest** | [**ApiCatalogPvtSpecificationPostRequest**](ApiCatalogPvtSpecificationPostRequest.md)|  | [optional] |

### Return type

[**ApiCatalogPvtSpecificationPost200Response**](ApiCatalogPvtSpecificationPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSpecificationSpecificationIdGet"></a>
# **apiCatalogPvtSpecificationSpecificationIdGet**
> RequestBody6 apiCatalogPvtSpecificationSpecificationIdGet(contentType, accept, specificationId)

Get Specification

Retrieves information of a Product or SKU Specification.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 88,      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsWizard\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Cotton\&quot;  }  &#x60;&#x60;&#x60;  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecificationApi;

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

    SpecificationApi apiInstance = new SpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer specificationId = 1; // Integer | Specification’s unique numerical identifier.
    try {
      RequestBody6 result = apiInstance.apiCatalogPvtSpecificationSpecificationIdGet(contentType, accept, specificationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecificationApi#apiCatalogPvtSpecificationSpecificationIdGet");
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
| **specificationId** | **Integer**| Specification’s unique numerical identifier. | |

### Return type

[**RequestBody6**](RequestBody6.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSpecificationSpecificationIdPut"></a>
# **apiCatalogPvtSpecificationSpecificationIdPut**
> ApiCatalogPvtSpecificationPost200Response apiCatalogPvtSpecificationSpecificationIdPut(contentType, accept, specificationId, requestBody7)

Update Specification

Updates a Product or SKU Specification.   ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Leather\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 88,      \&quot;FieldTypeId\&quot;: 1,      \&quot;CategoryId\&quot;: 4,      \&quot;FieldGroupId\&quot;: 20,      \&quot;Name\&quot;: \&quot;Material\&quot;,      \&quot;Description\&quot;: \&quot;Composition of the product.\&quot;,      \&quot;Position\&quot;: 1,      \&quot;IsFilter\&quot;: true,      \&quot;IsRequired\&quot;: true,      \&quot;IsOnProductDetails\&quot;: false,      \&quot;IsStockKeepingUnit\&quot;: false,      \&quot;IsWizard\&quot;: false,      \&quot;IsActive\&quot;: true,      \&quot;IsTopMenuLinkActive\&quot;: false,      \&quot;IsSideMenuLinkActive\&quot;: true,      \&quot;DefaultValue\&quot;: \&quot;Leather\&quot;  }  &#x60;&#x60;&#x60;  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpecificationApi;

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

    SpecificationApi apiInstance = new SpecificationApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer specificationId = 88; // Integer | Specification’s unique numerical identifier.
    RequestBody7 requestBody7 = new RequestBody7(); // RequestBody7 | 
    try {
      ApiCatalogPvtSpecificationPost200Response result = apiInstance.apiCatalogPvtSpecificationSpecificationIdPut(contentType, accept, specificationId, requestBody7);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpecificationApi#apiCatalogPvtSpecificationSpecificationIdPut");
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
| **specificationId** | **Integer**| Specification’s unique numerical identifier. | |
| **requestBody7** | [**RequestBody7**](RequestBody7.md)|  | [optional] |

### Return type

[**ApiCatalogPvtSpecificationPost200Response**](ApiCatalogPvtSpecificationPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

