# TaxonomyServicesApi

All URIs are relative to *https://viatorapi.viator.com/service*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**taxonomyAttractions**](TaxonomyServicesApi.md#taxonomyAttractions) | **POST** /taxonomy/attractions | /taxonomy/attractions |
| [**taxonomyCategories**](TaxonomyServicesApi.md#taxonomyCategories) | **GET** /taxonomy/categories | /taxonomy/categories |
| [**taxonomyDestinations**](TaxonomyServicesApi.md#taxonomyDestinations) | **GET** /taxonomy/destinations | /taxonomy/destinations |


<a id="taxonomyAttractions"></a>
# **taxonomyAttractions**
> TaxonomyAttractions200Response taxonomyAttractions(acceptLanguage, taxonomyAttractionsRequest)

/taxonomy/attractions

Get attractions - Retrieves a list of attractions (things like the Eiffel Tower or Empire State Building) and their associated unique numeric identifiers - The attraction&#39;s identifier (&#x60;seoId&#x60;) can be used as a means of searching for available products; for example, in the [/search/products](#operation/searchProducts) service. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxonomyServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    TaxonomyServicesApi apiInstance = new TaxonomyServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    TaxonomyAttractionsRequest taxonomyAttractionsRequest = new TaxonomyAttractionsRequest(); // TaxonomyAttractionsRequest | 
    try {
      TaxonomyAttractions200Response result = apiInstance.taxonomyAttractions(acceptLanguage, taxonomyAttractionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxonomyServicesApi#taxonomyAttractions");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **taxonomyAttractionsRequest** | [**TaxonomyAttractionsRequest**](TaxonomyAttractionsRequest.md)|  | [optional] |

### Return type

[**TaxonomyAttractions200Response**](TaxonomyAttractions200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="taxonomyCategories"></a>
# **taxonomyCategories**
> TaxonomyCategories200Response taxonomyCategories(acceptLanguage, destId)

/taxonomy/categories

Get all product categories - Retrieves a list of product categories for a destination that can be used as a means of filtering when searching for products using the [/search/products](/#operation/searchProducts) service - This service can be used to get a list of all categories and subcategories for a destination by including its &#x60;destId&#x60;, or you can omit the &#x60;destId&#x60; to get a list of all categories and subcategories - **Note:** If no &#x60;destId&#x60; is passed, &#x60;productCount&#x60; and &#x60;thumbnailURL&#x60; will be &#x60;null&#x60; as they are destination-specific fields 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxonomyServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    TaxonomyServicesApi apiInstance = new TaxonomyServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    Integer destId = 684; // Integer | **unique numeric identifier** of the destination to enquire about (optional) - `destinationId` is returned by [/taxonomy/destinations](#operation/taxonomyDestinations) 
    try {
      TaxonomyCategories200Response result = apiInstance.taxonomyCategories(acceptLanguage, destId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxonomyServicesApi#taxonomyCategories");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |
| **destId** | **Integer**| **unique numeric identifier** of the destination to enquire about (optional) - &#x60;destinationId&#x60; is returned by [/taxonomy/destinations](#operation/taxonomyDestinations)  | [optional] |

### Return type

[**TaxonomyCategories200Response**](TaxonomyCategories200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="taxonomyDestinations"></a>
# **taxonomyDestinations**
> TaxonomyDestinations200Response taxonomyDestinations(acceptLanguage)

/taxonomy/destinations

Get details of all destinations supported by this API - Retrieves all the country taxonomy/city nodes as a flat list - Returns a complete list of Viator destinations, including destination names and parent identifiers - Used to provide navigation through drill down lists or combo boxes 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TaxonomyServicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://viatorapi.viator.com/service");
    
    // Configure API key authorization: Legacy-API-key
    ApiKeyAuth Legacy-API-key = (ApiKeyAuth) defaultClient.getAuthentication("Legacy-API-key");
    Legacy-API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Legacy-API-key.setApiKeyPrefix("Token");

    // Configure API key authorization: API-key
    ApiKeyAuth API-key = (ApiKeyAuth) defaultClient.getAuthentication("API-key");
    API-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //API-key.setApiKeyPrefix("Token");

    TaxonomyServicesApi apiInstance = new TaxonomyServicesApi(defaultClient);
    String acceptLanguage = "en-US"; // String | Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes) 
    try {
      TaxonomyDestinations200Response result = apiInstance.taxonomyDestinations(acceptLanguage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TaxonomyServicesApi#taxonomyDestinations");
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
| **acceptLanguage** | **String**| Specifies the language into which the natural-language fields in the response from this service will be translated (see [Accept-Language header](#section/Appendices/Accept-Language-header) for available langage codes)  | |

### Return type

[**TaxonomyDestinations200Response**](TaxonomyDestinations200Response.md)

### Authorization

[Legacy-API-key](../README.md#Legacy-API-key), [API-key](../README.md#API-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

