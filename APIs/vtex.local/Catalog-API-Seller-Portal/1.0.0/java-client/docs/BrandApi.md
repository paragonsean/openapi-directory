# BrandApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBrand**](BrandApi.md#getBrand) | **GET** /api/catalog-seller-portal/brands/{brandId} | Get Brand by ID |
| [**listBrand**](BrandApi.md#listBrand) | **GET** /api/catalog-seller-portal/brands | Get List of Brands |
| [**postBrand**](BrandApi.md#postBrand) | **POST** /api/catalog-seller-portal/brands | Create Brand |
| [**putBrand**](BrandApi.md#putBrand) | **PUT** /api/catalog-seller-portal/brands/{brandId} | Update Brand |


<a id="getBrand"></a>
# **getBrand**
> GetBrand200Response getBrand(contentType, accept, brandId)

Get Brand by ID

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about a brand by its ID.    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;id\&quot;: \&quot;863\&quot;,    \&quot;name\&quot;: \&quot;Zwilling\&quot;,    \&quot;isActive\&quot;: false,    \&quot;createdAt\&quot;: \&quot;2021-01-18T14:41:45.696488+00:00\&quot;,    \&quot;updatedAt\&quot;: \&quot;2021-01-18T14:41:45.696488+00:00\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrandApi;

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

    BrandApi apiInstance = new BrandApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String brandId = "863"; // String | Brand unique identifier number.
    try {
      GetBrand200Response result = apiInstance.getBrand(contentType, accept, brandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandApi#getBrand");
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
| **brandId** | **String**| Brand unique identifier number. | |

### Return type

[**GetBrand200Response**](GetBrand200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listBrand"></a>
# **listBrand**
> ListBrand200Response listBrand(contentType, accept, q, from, to, orderBy, name)

Get List of Brands

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about all brands of the store. It is mandatory to use at least one query parameter.     ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;data\&quot;: [          {              \&quot;id\&quot;: \&quot;7\&quot;,              \&quot;name\&quot;: \&quot;All For Paws\&quot;,              \&quot;isActive\&quot;: true,              \&quot;createdAt\&quot;: \&quot;2022-01-17T19:43:14.18678Z\&quot;,              \&quot;updatedAt\&quot;: \&quot;2022-01-17T19:43:14.18678Z\&quot;          },          {              \&quot;id\&quot;: \&quot;1\&quot;,              \&quot;name\&quot;: \&quot;AOC\&quot;,              \&quot;isActive\&quot;: true,              \&quot;createdAt\&quot;: \&quot;2021-08-16T21:13:40.55189Z\&quot;,              \&quot;updatedAt\&quot;: \&quot;2021-08-16T21:13:40.55189Z\&quot;          }      ],      \&quot;_metadata\&quot;: {          \&quot;total\&quot;: 18,          \&quot;from\&quot;: 1,          \&quot;to\&quot;: 2,          \&quot;orderBy\&quot;: \&quot;name,asc\&quot;      }  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrandApi;

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

    BrandApi apiInstance = new BrandApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String q = "tshirt"; // String | Search word.
    String from = "1"; // String | The first page of the interval of the brand list.
    String to = "50"; // String | The last page of the interval of the brand list.
    String orderBy = "status,asc;name,asc"; // String | The order that the list is displayed. You can select `name`, or `updated_at` to select the order criteria. Then you can add `,` , `asc` or `desc` to define the brands order.
    String name = "Zwilling"; // String | Brand name.
    try {
      ListBrand200Response result = apiInstance.listBrand(contentType, accept, q, from, to, orderBy, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandApi#listBrand");
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
| **q** | **String**| Search word. | [optional] |
| **from** | **String**| The first page of the interval of the brand list. | [optional] |
| **to** | **String**| The last page of the interval of the brand list. | [optional] |
| **orderBy** | **String**| The order that the list is displayed. You can select &#x60;name&#x60;, or &#x60;updated_at&#x60; to select the order criteria. Then you can add &#x60;,&#x60; , &#x60;asc&#x60; or &#x60;desc&#x60; to define the brands order. | [optional] |
| **name** | **String**| Brand name. | [optional] |

### Return type

[**ListBrand200Response**](ListBrand200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="postBrand"></a>
# **postBrand**
> PostBrand200Response postBrand(contentType, accept, postBrandRequest)

Create Brand

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Creates a new brand.    ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;name\&quot;: \&quot;Zwilling\&quot;,    \&quot;isActive\&quot;: true  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;id\&quot;: \&quot;20\&quot;,    \&quot;name\&quot;: \&quot;Zwilling\&quot;,    \&quot;isActive\&quot;: true,    \&quot;createdAt\&quot;: \&quot;2021-05-17T15:20:36.077253+00:00\&quot;,    \&quot;updatedAt\&quot;: \&quot;2021-01-18T14:41:45.696488+00:00\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrandApi;

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

    BrandApi apiInstance = new BrandApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    PostBrandRequest postBrandRequest = new PostBrandRequest(); // PostBrandRequest | 
    try {
      PostBrand200Response result = apiInstance.postBrand(contentType, accept, postBrandRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandApi#postBrand");
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
| **postBrandRequest** | [**PostBrandRequest**](PostBrandRequest.md)|  | [optional] |

### Return type

[**PostBrand200Response**](PostBrand200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="putBrand"></a>
# **putBrand**
> putBrand(contentType, accept, brandId, putBrandRequest)

Update Brand

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Updates an existing brand.     ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;id\&quot;: \&quot;20\&quot;,    \&quot;name\&quot;: \&quot;Zwilling\&quot;,    \&quot;isActive\&quot;: true  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BrandApi;

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

    BrandApi apiInstance = new BrandApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String brandId = "20"; // String | Brand unique identifier number.
    PutBrandRequest putBrandRequest = new PutBrandRequest(); // PutBrandRequest | 
    try {
      apiInstance.putBrand(contentType, accept, brandId, putBrandRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandApi#putBrand");
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
| **brandId** | **String**| Brand unique identifier number. | |
| **putBrandRequest** | [**PutBrandRequest**](PutBrandRequest.md)|  | [optional] |

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
| **204** | No Content |  -  |

