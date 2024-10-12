# CategoryApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createCategory**](CategoryApi.md#createCategory) | **POST** /api/catalog-seller-portal/category-tree/categories | Create Category |
| [**getCategoryTree**](CategoryApi.md#getCategoryTree) | **GET** /api/catalog-seller-portal/category-tree | Get Category Tree |
| [**getbyid**](CategoryApi.md#getbyid) | **GET** /api/catalog-seller-portal/category-tree/categories/{categoryId} | Get Category by ID |
| [**updateCategoryTree**](CategoryApi.md#updateCategoryTree) | **PUT** /api/catalog-seller-portal/category-tree | Update Category Tree |


<a id="createCategory"></a>
# **createCategory**
> RootsInner createCategory(contentType, accept, createCategoryRequest)

Create Category

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Creates a new category.    ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;parentId\&quot;: \&quot;567\&quot;,    \&quot;Name\&quot;: \&quot;Beauty\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;value\&quot;: {      \&quot;id\&quot;: \&quot;1\&quot;,      \&quot;name\&quot;: \&quot;Beauty\&quot;,      \&quot;isActive\&quot;: false    },    \&quot;children\&quot;: [      {        \&quot;value\&quot;: {          \&quot;id\&quot;: \&quot;2\&quot;,          \&quot;name\&quot;: \&quot;Perfumes\&quot;,          \&quot;isActive\&quot;: false        }      }    ]  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

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

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    CreateCategoryRequest createCategoryRequest = new CreateCategoryRequest(); // CreateCategoryRequest | 
    try {
      RootsInner result = apiInstance.createCategory(contentType, accept, createCategoryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#createCategory");
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
| **createCategoryRequest** | [**CreateCategoryRequest**](CreateCategoryRequest.md)|  | |

### Return type

[**RootsInner**](RootsInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getCategoryTree"></a>
# **getCategoryTree**
> GetCategoryTree200Response getCategoryTree(contentType, accept, depth)

Get Category Tree

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about the category tree from the store.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;roots\&quot;: [          {              \&quot;value\&quot;: {                  \&quot;id\&quot;: \&quot;2\&quot;,                  \&quot;name\&quot;: \&quot;Departamento Artesanato\&quot;,                  \&quot;isActive\&quot;: true              },              \&quot;children\&quot;: [                  {                      \&quot;value\&quot;: {                          \&quot;id\&quot;: \&quot;3\&quot;,                          \&quot;name\&quot;: \&quot;Artesanato de Barro\&quot;,                          \&quot;isActive\&quot;: false                      },                      \&quot;children\&quot;: [                          {                              \&quot;value\&quot;: {                                  \&quot;id\&quot;: \&quot;4\&quot;,                                  \&quot;name\&quot;: \&quot;Artesanato de Barro Vermelho\&quot;,                                  \&quot;isActive\&quot;: false                              },                              \&quot;children\&quot;: []                          }                      ]                  }              ]          },          {              \&quot;value\&quot;: {                  \&quot;id\&quot;: \&quot;5\&quot;,                  \&quot;name\&quot;: \&quot;Perfumes\&quot;,                  \&quot;isActive\&quot;: false              },              \&quot;children\&quot;: [                  {                      \&quot;value\&quot;: {                          \&quot;id\&quot;: \&quot;6\&quot;,                          \&quot;name\&quot;: \&quot;Perfume Feminino\&quot;,                          \&quot;isActive\&quot;: false                      },                      \&quot;children\&quot;: []                  },                  {                      \&quot;value\&quot;: {                          \&quot;id\&quot;: \&quot;7\&quot;,                          \&quot;name\&quot;: \&quot;Perfume Masculino\&quot;,                          \&quot;isActive\&quot;: false,                          \&quot;displayOnMenu\&quot;: false,                          \&quot;score\&quot;: 0,                          \&quot;filterByBrand\&quot;: false,                          \&quot;isClickable\&quot;: false                      },                      \&quot;children\&quot;: []                  }              ]          }      ],      \&quot;createdAt\&quot;: \&quot;2021-08-16T20:57:13.070813Z\&quot;,      \&quot;updatedAt\&quot;: \&quot;2022-07-07T14:24:56.416337Z\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

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

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer depth = 1; // Integer | Category tree level.
    try {
      GetCategoryTree200Response result = apiInstance.getCategoryTree(contentType, accept, depth);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#getCategoryTree");
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
| **depth** | **Integer**| Category tree level. | [optional] |

### Return type

[**GetCategoryTree200Response**](GetCategoryTree200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getbyid"></a>
# **getbyid**
> Getbyid200Response getbyid(contentType, accept, categoryId)

Get Category by ID

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Retrieves general information about a category by its ID.     ## Response body example    &#x60;&#x60;&#x60;json  {    \&quot;value\&quot;: {      \&quot;id\&quot;: \&quot;1\&quot;,      \&quot;name\&quot;: \&quot;sandboxintegracao\&quot;,      \&quot;isActive\&quot;: false    },    \&quot;children\&quot;: [      {        \&quot;value\&quot;: {          \&quot;id\&quot;: \&quot;2\&quot;,          \&quot;name\&quot;: \&quot;Perfumes\&quot;,          \&quot;isActive\&quot;: false        }      }    ]  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

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

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String categoryId = "1"; // String | Category unique identifier number.
    try {
      Getbyid200Response result = apiInstance.getbyid(contentType, accept, categoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#getbyid");
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
| **categoryId** | **String**| Category unique identifier number. | |

### Return type

[**Getbyid200Response**](Getbyid200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateCategoryTree"></a>
# **updateCategoryTree**
> updateCategoryTree(contentType, accept, updateCategoryTreeRequest)

Update Category Tree

 &gt;📘 This API is part of the [Seller Portal Catalog](https://help.vtex.com/en/tutorial/how-the-seller-portal-catalog-works--7pMB6YOt6YQDQQbzFB4Pxp). This functionality is in the Beta stage and can be discontinued at any moment at VTEX&#39;s discretion. VTEX will not be responsible for any instabilities caused by its use or discontinuity. If you have any questions, please contact [our Support Center](https://support.vtex.com/hc/en-us/requests).      Updates the existing categories in the category tree.    ## Request body example    &#x60;&#x60;&#x60;json  {    \&quot;roots\&quot;: [      {        \&quot;value\&quot;: {          \&quot;id\&quot;: \&quot;2\&quot;,          \&quot;name\&quot;: \&quot;Departamento Artesanato\&quot;,          \&quot;isActive\&quot;: true        },        \&quot;children\&quot;: [          {            \&quot;value\&quot;: {              \&quot;id\&quot;: \&quot;3\&quot;,              \&quot;name\&quot;: \&quot;Artesanato de Barro\&quot;,              \&quot;isActive\&quot;: false            },            \&quot;children\&quot;: [              {                \&quot;value\&quot;: {                  \&quot;id\&quot;: \&quot;4\&quot;,                  \&quot;name\&quot;: \&quot;Artesanato de Barro Vermelho\&quot;,                  \&quot;isActive\&quot;: false                },                \&quot;children\&quot;: []              }            ]          }        ]      },      {        \&quot;value\&quot;: {          \&quot;id\&quot;: \&quot;5\&quot;,          \&quot;name\&quot;: \&quot;Perfumes\&quot;,          \&quot;isActive\&quot;: false        },        \&quot;children\&quot;: [          {            \&quot;value\&quot;: {              \&quot;id\&quot;: \&quot;6\&quot;,              \&quot;name\&quot;: \&quot;Perfume Feminino\&quot;,              \&quot;isActive\&quot;: false            },            \&quot;children\&quot;: []          },          {            \&quot;value\&quot;: {              \&quot;id\&quot;: \&quot;7\&quot;,              \&quot;name\&quot;: \&quot;Perfume Masculino\&quot;,              \&quot;isActive\&quot;: false,              \&quot;displayOnMenu\&quot;: false,              \&quot;score\&quot;: 0,              \&quot;filterByBrand\&quot;: false,              \&quot;isClickable\&quot;: false            },            \&quot;children\&quot;: []          }        ]      }    ]  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CategoryApi;

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

    CategoryApi apiInstance = new CategoryApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    UpdateCategoryTreeRequest updateCategoryTreeRequest = new UpdateCategoryTreeRequest(); // UpdateCategoryTreeRequest | OK
    try {
      apiInstance.updateCategoryTree(contentType, accept, updateCategoryTreeRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#updateCategoryTree");
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
| **updateCategoryTreeRequest** | [**UpdateCategoryTreeRequest**](UpdateCategoryTreeRequest.md)| OK | |

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

