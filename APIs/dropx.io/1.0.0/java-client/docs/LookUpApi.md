# LookUpApi

All URIs are relative to *http://dropx.io/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**productsLinkSearchGet**](LookUpApi.md#productsLinkSearchGet) | **GET** /products/link-search | Search for similar products by providing a link to any e-commerce product. |
| [**productsLinkSearchV2Get**](LookUpApi.md#productsLinkSearchV2Get) | **GET** /products/link-search-v2 | Search for similar products by providing a link to any e-commerce product. |
| [**productsSearchGet**](LookUpApi.md#productsSearchGet) | **GET** /products/search | Search for any product using title |
| [**productsSearchV2Get**](LookUpApi.md#productsSearchV2Get) | **GET** /products/search-v2 | Search for any product using title |
| [**productsTitleSearchGet**](LookUpApi.md#productsTitleSearchGet) | **GET** /products/title-search | Search for any product using title |


<a id="productsLinkSearchGet"></a>
# **productsLinkSearchGet**
> productsLinkSearchGet(url, providers)

Search for similar products by providing a link to any e-commerce product.

Returns list of e-commerce product that are close to the one provided -- one from each provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookUpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://dropx.io/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LookUpApi apiInstance = new LookUpApi(defaultClient);
    String url = "url_example"; // String | URL must be a url encoded value
    String providers = "providers_example"; // String | A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a ',' seperated values to filter response by required e-commerce providers
    try {
      apiInstance.productsLinkSearchGet(url, providers);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookUpApi#productsLinkSearchGet");
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
| **url** | **String**| URL must be a url encoded value | |
| **providers** | **String**| A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a &#39;,&#39; seperated values to filter response by required e-commerce providers | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of search details |  -  |
| **401** | Invalid authentication |  -  |
| **452** | Requested url parameter value is not a valid url |  -  |
| **453** | Requested ip is not white listed app token assigned ip list |  -  |
| **454** | App does not have any IP |  -  |
| **455** | User requested with invalid app token |  -  |
| **456** | User reached maximum allow limit according to his plan |  -  |
| **458** | Requested search does not have any response |  -  |
| **459** | Requested search products api required parameter \&quot;term\&quot; is missing |  -  |
| **460** | Requested similar search products api required parameter \&quot;url\&quot; is missing |  -  |
| **461** | Requested search product api required \&quot;term\&quot; parameter does not have valid value or empty value passed |  -  |
| **462** | Requested similar search product api required \&quot;url\&quot; parameter does not have valid url or empty value passed |  -  |
| **463** | Error in processing search request in elastic search |  -  |
| **490** | some unexpected error raised in processing user request |  -  |
| **500** | internal server error |  -  |

<a id="productsLinkSearchV2Get"></a>
# **productsLinkSearchV2Get**
> productsLinkSearchV2Get(url, providers)

Search for similar products by providing a link to any e-commerce product.

Returns list of e-commerce product that are close to the one provided -- one from each provider

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookUpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://dropx.io/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LookUpApi apiInstance = new LookUpApi(defaultClient);
    String url = "url_example"; // String | URL must be a url encoded value
    String providers = "providers_example"; // String | A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a ',' seperated values to filter response by required e-commerce providers
    try {
      apiInstance.productsLinkSearchV2Get(url, providers);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookUpApi#productsLinkSearchV2Get");
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
| **url** | **String**| URL must be a url encoded value | |
| **providers** | **String**| A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a &#39;,&#39; seperated values to filter response by required e-commerce providers | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of search details |  -  |
| **401** | Invalid authentication |  -  |
| **452** | Requested url parameter value is not a valid url |  -  |
| **453** | Requested ip is not white listed app token assigned ip list |  -  |
| **454** | App does not have any IP |  -  |
| **455** | User requested with invalid app token |  -  |
| **456** | User reached maximum allow limit according to his plan |  -  |
| **458** | Requested search does not have any response |  -  |
| **459** | Requested search products api required parameter \&quot;term\&quot; is missing |  -  |
| **460** | Requested similar search products api required parameter \&quot;url\&quot; is missing |  -  |
| **461** | Requested search product api required \&quot;term\&quot; parameter does not have valid value or empty value passed |  -  |
| **462** | Requested similar search product api required \&quot;url\&quot; parameter does not have valid url or empty value passed |  -  |
| **463** | Error in processing search request in elastic search |  -  |
| **490** | some unexpected error raised in processing user request |  -  |
| **500** | internal server error |  -  |

<a id="productsSearchGet"></a>
# **productsSearchGet**
> productsSearchGet(term, providers)

Search for any product using title

Returns one unique result from every provider that dropx.io tracks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookUpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://dropx.io/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LookUpApi apiInstance = new LookUpApi(defaultClient);
    String term = "term_example"; // String | search terms giving any title of products that are sold online
    String providers = "providers_example"; // String | A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a ',' seperated values to filter response by required e-commerce providers
    try {
      apiInstance.productsSearchGet(term, providers);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookUpApi#productsSearchGet");
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
| **term** | **String**| search terms giving any title of products that are sold online | |
| **providers** | **String**| A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a &#39;,&#39; seperated values to filter response by required e-commerce providers | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of search details |  -  |
| **401** | Invalid authentication |  -  |
| **452** | Requested url parameter value is not a valid url |  -  |
| **453** | Requested ip is not white listed app token assigned ip list |  -  |
| **454** | App does not have any IP |  -  |
| **455** | User requested with invalid app token |  -  |
| **456** | User reached maximum allow limit according to his plan |  -  |
| **458** | Requested search does not have any response |  -  |
| **459** | Requested search products api required parameter \&quot;term\&quot; is missing |  -  |
| **460** | Requested similar search products api required parameter \&quot;url\&quot; is missing |  -  |
| **461** | Requested search product api required \&quot;term\&quot; parameter does not have valid value or empty value passed |  -  |
| **462** | Requested similar search product api required \&quot;url\&quot; parameter does not have valid url or empty value passed |  -  |
| **463** | Error in processing search request in elastic search |  -  |
| **490** | some unexpected error raised in processing user request |  -  |
| **500** | internal server error |  -  |

<a id="productsSearchV2Get"></a>
# **productsSearchV2Get**
> productsSearchV2Get(term, providers)

Search for any product using title

Returns one unique result from every provider that dropx.io tracks

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookUpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://dropx.io/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LookUpApi apiInstance = new LookUpApi(defaultClient);
    String term = "term_example"; // String | search terms giving any title of products that are sold online
    String providers = "providers_example"; // String | A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a ',' seperated values to filter response by required e-commerce providers
    try {
      apiInstance.productsSearchV2Get(term, providers);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookUpApi#productsSearchV2Get");
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
| **term** | **String**| search terms giving any title of products that are sold online | |
| **providers** | **String**| A valid e commerce website link(eg. www.flipkart.com or http://www.amazon.in) by a &#39;,&#39; seperated values to filter response by required e-commerce providers | [optional] |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of search details |  -  |
| **401** | Invalid authentication |  -  |
| **452** | Requested url parameter value is not a valid url |  -  |
| **453** | Requested ip is not white listed app token assigned ip list |  -  |
| **454** | App does not have any IP |  -  |
| **455** | User requested with invalid app token |  -  |
| **456** | User reached maximum allow limit according to his plan |  -  |
| **458** | Requested search does not have any response |  -  |
| **459** | Requested search products api required parameter \&quot;term\&quot; is missing |  -  |
| **460** | Requested similar search products api required parameter \&quot;url\&quot; is missing |  -  |
| **461** | Requested search product api required \&quot;term\&quot; parameter does not have valid value or empty value passed |  -  |
| **462** | Requested similar search product api required \&quot;url\&quot; parameter does not have valid url or empty value passed |  -  |
| **463** | Error in processing search request in elastic search |  -  |
| **490** | some unexpected error raised in processing user request |  -  |
| **500** | internal server error |  -  |

<a id="productsTitleSearchGet"></a>
# **productsTitleSearchGet**
> productsTitleSearchGet(term)

Search for any product using title

Returns list of product ids

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LookUpApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://dropx.io/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    LookUpApi apiInstance = new LookUpApi(defaultClient);
    String term = "term_example"; // String | search terms giving any title of products that are sold online
    try {
      apiInstance.productsTitleSearchGet(term);
    } catch (ApiException e) {
      System.err.println("Exception when calling LookUpApi#productsTitleSearchGet");
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
| **term** | **String**| search terms giving any title of products that are sold online | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of product details |  -  |
| **401** | Invalid authentication |  -  |
| **456** | We are sorry, You have reached your limit |  -  |
| **458** | Oops...! we don\\&#39;t have enough data to serve your request |  -  |
| **459** | Oops...! Missing reqired \&quot;term\&quot; parameter to serve your request |  -  |
| **461** | Oops...! Required \&quot;term\&quot; parameter should not be empty |  -  |
| **464** | Error in finding default plan |  -  |
| **490** | Unexpected error occurred while processing your request |  -  |
| **500** | internal server error |  -  |

