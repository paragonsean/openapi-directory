# CategoryApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtCategoryCategoryIdGet**](CategoryApi.md#apiCatalogPvtCategoryCategoryIdGet) | **GET** /api/catalog/pvt/category/{categoryId} | Get Category by ID |
| [**apiCatalogPvtCategoryCategoryIdPut**](CategoryApi.md#apiCatalogPvtCategoryCategoryIdPut) | **PUT** /api/catalog/pvt/category/{categoryId} | Update Category |
| [**apiCatalogPvtCategoryPost**](CategoryApi.md#apiCatalogPvtCategoryPost) | **POST** /api/catalog/pvt/category | Create Category |
| [**categoryTree**](CategoryApi.md#categoryTree) | **GET** /api/catalog_system/pub/category/tree/{categoryLevels} | Get Category Tree |


<a id="apiCatalogPvtCategoryCategoryIdGet"></a>
# **apiCatalogPvtCategoryCategoryIdGet**
> Category apiCatalogPvtCategoryCategoryIdGet(contentType, accept, categoryId)

Get Category by ID

Retrieves general information about a Category.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 3367,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;

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
    Integer categoryId = 9289; // Integer | Category’s unique numerical identifier.
    try {
      Category result = apiInstance.apiCatalogPvtCategoryCategoryIdGet(contentType, accept, categoryId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#apiCatalogPvtCategoryCategoryIdGet");
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
| **categoryId** | **Integer**| Category’s unique numerical identifier. | |

### Return type

[**Category**](Category.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtCategoryCategoryIdPut"></a>
# **apiCatalogPvtCategoryCategoryIdPut**
> Category apiCatalogPvtCategoryCategoryIdPut(contentType, accept, categoryId, apiCatalogPvtCategoryCategoryIdPutRequest)

Update Category

Updates a previously existing Category.    ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;

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
    Integer categoryId = 9289; // Integer | Category’s unique numerical identifier.
    ApiCatalogPvtCategoryCategoryIdPutRequest apiCatalogPvtCategoryCategoryIdPutRequest = new ApiCatalogPvtCategoryCategoryIdPutRequest(); // ApiCatalogPvtCategoryCategoryIdPutRequest | 
    try {
      Category result = apiInstance.apiCatalogPvtCategoryCategoryIdPut(contentType, accept, categoryId, apiCatalogPvtCategoryCategoryIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#apiCatalogPvtCategoryCategoryIdPut");
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
| **categoryId** | **Integer**| Category’s unique numerical identifier. | |
| **apiCatalogPvtCategoryCategoryIdPutRequest** | [**ApiCatalogPvtCategoryCategoryIdPutRequest**](ApiCatalogPvtCategoryCategoryIdPutRequest.md)|  | [optional] |

### Return type

[**Category**](Category.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtCategoryPost"></a>
# **apiCatalogPvtCategoryPost**
> Category apiCatalogPvtCategoryPost(contentType, accept, createCategoryRequest)

Create Category

Creates a new Category.    If there is a need to create a new category with a specific custom ID, specify the &#x60;Id&#x60; (integer) in the request. Otherwise, VTEX will generate the ID automatically.    ## Request body example (automatically generated ID)    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Request body example (custom ID)    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: null,      \&quot;AdWordsRemarketingCode\&quot;: null,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;SPECIFICATION\&quot;,      \&quot;Score\&quot;: null  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Home Appliances\&quot;,      \&quot;FatherCategoryId\&quot;: null,      \&quot;Title\&quot;: \&quot;Home Appliances\&quot;,      \&quot;Description\&quot;: \&quot;Discover our range of home appliances. Find smart vacuums, kitchen and laundry appliances to suit your needs. Order online now.\&quot;,      \&quot;Keywords\&quot;: \&quot;Kitchen, Laundry, Appliances\&quot;,      \&quot;IsActive\&quot;: true,      \&quot;LomadeeCampaignCode\&quot;: \&quot;\&quot;,      \&quot;AdWordsRemarketingCode\&quot;: \&quot;\&quot;,      \&quot;ShowInStoreFront\&quot;: true,      \&quot;ShowBrandFilter\&quot;: true,      \&quot;ActiveStoreFrontLink\&quot;: true,      \&quot;GlobalCategoryId\&quot;: 604,      \&quot;StockKeepingUnitSelectionMode\&quot;: \&quot;LIST\&quot;,      \&quot;Score\&quot;: null,      \&quot;LinkId\&quot;: \&quot;Alimentacao\&quot;,      \&quot;HasChildren\&quot;: true  }  &#x60;&#x60;&#x60;

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
      Category result = apiInstance.apiCatalogPvtCategoryPost(contentType, accept, createCategoryRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#apiCatalogPvtCategoryPost");
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
| **createCategoryRequest** | [**CreateCategoryRequest**](CreateCategoryRequest.md)|  | [optional] |

### Return type

[**Category**](Category.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="categoryTree"></a>
# **categoryTree**
> List&lt;GetCategoryTree&gt; categoryTree(contentType, accept, categoryLevels)

Get Category Tree

Retrieves the Category Tree of your store. Get all the category levels registered in the Catalog or define the level up to which you want to get.    &gt; 📘 Onboarding guide   &gt;  &gt; Check the new [Catalog onboarding guide](https://developers.vtex.com/vtex-rest-api/docs/catalog-overview). We created this guide to improve the onboarding experience for developers at VTEX. It assembles all documentation on our Developer Portal about Catalog and is organized by focusing on the developer&#39;s journey.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;id\&quot;: 1,          \&quot;name\&quot;: \&quot;Alimentação\&quot;,          \&quot;hasChildren\&quot;: true,          \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao\&quot;,          \&quot;children\&quot;: [              {                  \&quot;id\&quot;: 6,                  \&quot;name\&quot;: \&quot;Bebedouro\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/bebedouro\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Bebedouro para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 7,                  \&quot;name\&quot;: \&quot;Comedouro\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/comedouro\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Comedouro para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 8,                  \&quot;name\&quot;: \&quot;Biscoitos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/biscoitos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Biscoitos para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 9,                  \&quot;name\&quot;: \&quot;Petiscos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/petiscos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Petiscos para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 10,                  \&quot;name\&quot;: \&quot;Ração Seca\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/racao-seca\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ração Seca para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 11,                  \&quot;name\&quot;: \&quot;Ração Úmida\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/alimentacao/racao-umida\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ração Úmida para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              }          ],          \&quot;Title\&quot;: \&quot;Alimentação para Gatos\&quot;,          \&quot;MetaTagDescription\&quot;: \&quot;\&quot;      },      {          \&quot;id\&quot;: 2,          \&quot;name\&quot;: \&quot;Brinquedos\&quot;,          \&quot;hasChildren\&quot;: true,          \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos\&quot;,          \&quot;children\&quot;: [              {                  \&quot;id\&quot;: 12,                  \&quot;name\&quot;: \&quot;Bolinhas\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/bolinhas\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Bolinhas para Gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 13,                  \&quot;name\&quot;: \&quot;Ratinhos\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/ratinhos\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Ratinhos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;\&quot;              },              {                  \&quot;id\&quot;: 19,                  \&quot;name\&quot;: \&quot;Arranhador para gato\&quot;,                  \&quot;hasChildren\&quot;: false,                  \&quot;url\&quot;: \&quot;https://lojadobreno.vtexcommercestable.com.br/brinquedos/arranhador-para-gato\&quot;,                  \&quot;children\&quot;: [],                  \&quot;Title\&quot;: \&quot;Brinquedo Arranhador para gatos\&quot;,                  \&quot;MetaTagDescription\&quot;: \&quot;Arranhador gatos é indispensável no lar com felinos. Ideais para afiar as unhas e garantir a diversão\&quot;              }          ],          \&quot;Title\&quot;: \&quot;Brinquedos para Gatos\&quot;,          \&quot;MetaTagDescription\&quot;: \&quot;\&quot;      }  ]  &#x60;&#x60;&#x60;

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
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String categoryLevels = "1"; // String | Value of the category level you need to retrieve.
    try {
      List<GetCategoryTree> result = apiInstance.categoryTree(contentType, accept, categoryLevels);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CategoryApi#categoryTree");
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
| **categoryLevels** | **String**| Value of the category level you need to retrieve. | |

### Return type

[**List&lt;GetCategoryTree&gt;**](GetCategoryTree.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

