# BrandApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtBrandBrandIdDelete**](BrandApi.md#apiCatalogPvtBrandBrandIdDelete) | **DELETE** /api/catalog/pvt/brand/{brandId} | Delete Brand |
| [**apiCatalogPvtBrandBrandIdGet**](BrandApi.md#apiCatalogPvtBrandBrandIdGet) | **GET** /api/catalog/pvt/brand/{brandId} | Get Brand and context |
| [**apiCatalogPvtBrandBrandIdPut**](BrandApi.md#apiCatalogPvtBrandBrandIdPut) | **PUT** /api/catalog/pvt/brand/{brandId} | Update Brand |
| [**apiCatalogPvtBrandPost**](BrandApi.md#apiCatalogPvtBrandPost) | **POST** /api/catalog/pvt/brand | Create Brand |
| [**brand**](BrandApi.md#brand) | **GET** /api/catalog_system/pvt/brand/{brandId} | Get Brand |
| [**brandList**](BrandApi.md#brandList) | **GET** /api/catalog_system/pvt/brand/list | Get Brand List |
| [**brandListPerPage**](BrandApi.md#brandListPerPage) | **GET** /api/catalog_system/pvt/brand/pagedlist | Get Brand List Per Page |


<a id="apiCatalogPvtBrandBrandIdDelete"></a>
# **apiCatalogPvtBrandBrandIdDelete**
> apiCatalogPvtBrandBrandIdDelete(brandId, contentType, accept)

Delete Brand

Deletes an existing Brand.

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
    String brandId = "123"; // String | Brand’s unique numerical identifier.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      apiInstance.apiCatalogPvtBrandBrandIdDelete(brandId, contentType, accept);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandApi#apiCatalogPvtBrandBrandIdDelete");
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
| **brandId** | **String**| Brand’s unique numerical identifier. | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

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

<a id="apiCatalogPvtBrandBrandIdGet"></a>
# **apiCatalogPvtBrandBrandIdGet**
> BrandCreateUpdate apiCatalogPvtBrandBrandIdGet(contentType, accept, brandId)

Get Brand and context

Retrieves information about a specific Brand and its context.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;

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
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String brandId = "123"; // String | Brand ID.
    try {
      BrandCreateUpdate result = apiInstance.apiCatalogPvtBrandBrandIdGet(contentType, accept, brandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandApi#apiCatalogPvtBrandBrandIdGet");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **brandId** | **String**| Brand ID. | |

### Return type

[**BrandCreateUpdate**](BrandCreateUpdate.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtBrandBrandIdPut"></a>
# **apiCatalogPvtBrandBrandIdPut**
> BrandCreateUpdate apiCatalogPvtBrandBrandIdPut(brandId, contentType, accept, brandCreateUpdate)

Update Brand

Updates a previously existing Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;

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
    String brandId = "123"; // String | Brand’s unique numerical identifier.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    BrandCreateUpdate brandCreateUpdate = new BrandCreateUpdate(); // BrandCreateUpdate | 
    try {
      BrandCreateUpdate result = apiInstance.apiCatalogPvtBrandBrandIdPut(brandId, contentType, accept, brandCreateUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandApi#apiCatalogPvtBrandBrandIdPut");
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
| **brandId** | **String**| Brand’s unique numerical identifier. | |
| **contentType** | **String**| Type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **brandCreateUpdate** | [**BrandCreateUpdate**](BrandCreateUpdate.md)|  | [optional] |

### Return type

[**BrandCreateUpdate**](BrandCreateUpdate.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtBrandPost"></a>
# **apiCatalogPvtBrandPost**
> BrandCreateUpdate apiCatalogPvtBrandPost(contentType, accept, brandCreateUpdate)

Create Brand

Creates a new Brand.  ## Request and response body example    &#x60;&#x60;&#x60;json  {    \&quot;Id\&quot;: 2000013,    \&quot;Name\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Text\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Keywords\&quot;: \&quot;orma\&quot;,    \&quot;SiteTitle\&quot;: \&quot;Orma Carbon\&quot;,    \&quot;Active\&quot;: true,    \&quot;MenuHome\&quot;: true,    \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,    \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,    \&quot;Score\&quot;: null,    \&quot;LinkId\&quot;: \&quot;orma-carbon\&quot;  }  &#x60;&#x60;&#x60;

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
    BrandCreateUpdate brandCreateUpdate = new BrandCreateUpdate(); // BrandCreateUpdate | Request body.
    try {
      BrandCreateUpdate result = apiInstance.apiCatalogPvtBrandPost(contentType, accept, brandCreateUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandApi#apiCatalogPvtBrandPost");
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
| **brandCreateUpdate** | [**BrandCreateUpdate**](BrandCreateUpdate.md)| Request body. | [optional] |

### Return type

[**BrandCreateUpdate**](BrandCreateUpdate.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="brand"></a>
# **brand**
> BrandGet brand(contentType, accept, brandId)

Get Brand

Retrieves a specific Brand by its ID.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;id\&quot;: 7000000,    \&quot;name\&quot;: \&quot;Pedigree\&quot;,    \&quot;isActive\&quot;: true,    \&quot;title\&quot;: \&quot;Pedigree\&quot;,    \&quot;metaTagDescription\&quot;: \&quot;Pedigree\&quot;,    \&quot;imageUrl\&quot;: null  }  &#x60;&#x60;&#x60;

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
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String brandId = "123"; // String | Brand ID.
    try {
      BrandGet result = apiInstance.brand(contentType, accept, brandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandApi#brand");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **brandId** | **String**| Brand ID. | |

### Return type

[**BrandGet**](BrandGet.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="brandList"></a>
# **brandList**
> List&lt;BrandGet&gt; brandList(contentType, accept)

Get Brand List

Retrieves all Brands registered in the store&#39;s Catalog.   &gt;⚠️ This route&#39;s response is limited to 20k results. If you need to obtain more results, please use the [Get Brand List](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-brand-list) endpoint instead to get a paginated response.   ## Response body example    &#x60;&#x60;&#x60;json  [    {      \&quot;id\&quot;: 9280,      \&quot;name\&quot;: \&quot;Brand\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Brand\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Brand\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000000,      \&quot;name\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;Orma Carbon\&quot;,      \&quot;imageUrl\&quot;: null    },    {      \&quot;id\&quot;: 2000001,      \&quot;name\&quot;: \&quot;Pedigree\&quot;,      \&quot;isActive\&quot;: true,      \&quot;title\&quot;: \&quot;Pedigree\&quot;,      \&quot;metaTagDescription\&quot;: \&quot;\&quot;,      \&quot;imageUrl\&quot;: null    }  ]  &#x60;&#x60;&#x60;

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
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      List<BrandGet> result = apiInstance.brandList(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandApi#brandList");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

[**List&lt;BrandGet&gt;**](BrandGet.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="brandListPerPage"></a>
# **brandListPerPage**
> BrandListPerPage200Response brandListPerPage(contentType, accept, pageSize, page)

Get Brand List Per Page

Retrieves all Brands registered in the store&#39;s Catalog by page number.  ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;items\&quot;: [      {        \&quot;id\&quot;: 2000000,        \&quot;name\&quot;: \&quot;Farm\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Farm\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Farm\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000001,        \&quot;name\&quot;: \&quot;Adidas\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;\&quot;,        \&quot;imageUrl\&quot;: null      },      {        \&quot;id\&quot;: 2000002,        \&quot;name\&quot;: \&quot;Brastemp\&quot;,        \&quot;isActive\&quot;: true,        \&quot;title\&quot;: \&quot;Brastemp\&quot;,        \&quot;metaTagDescription\&quot;: \&quot;Brastemp\&quot;,        \&quot;imageUrl\&quot;: null      }    ],      \&quot;paging\&quot;: {        \&quot;page\&quot;: 1,          \&quot;perPage\&quot;: 3,            \&quot;total\&quot;: 6,              \&quot;pages\&quot;: 2      }  }  &#x60;&#x60;&#x60;

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
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer pageSize = 5; // Integer | Quantity of brands per page.
    Integer page = 1; // Integer | Page number of the brand list.
    try {
      BrandListPerPage200Response result = apiInstance.brandListPerPage(contentType, accept, pageSize, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BrandApi#brandListPerPage");
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
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **pageSize** | **Integer**| Quantity of brands per page. | |
| **page** | **Integer**| Page number of the brand list. | |

### Return type

[**BrandListPerPage200Response**](BrandListPerPage200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

