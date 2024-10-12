# LegacySubcollectionApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtCollectionCollectionIdPositionPost**](LegacySubcollectionApi.md#apiCatalogPvtCollectionCollectionIdPositionPost) | **POST** /api/catalog/pvt/collection/{collectionId}/position | Reposition SKU on the Subcollection |
| [**apiCatalogPvtCollectionCollectionIdSubcollectionGet**](LegacySubcollectionApi.md#apiCatalogPvtCollectionCollectionIdSubcollectionGet) | **GET** /api/catalog/pvt/collection/{collectionId}/subcollection | Get Subcollection by Collection ID |
| [**apiCatalogPvtSubcollectionPost**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionPost) | **POST** /api/catalog/pvt/subcollection | Create Subcollection |
| [**apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId}/brand/{brandId} | Delete Brand from Subcollection |
| [**apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId}/brand/{categoryId} | Delete Category from Subcollection |
| [**apiCatalogPvtSubcollectionSubCollectionIdBrandPost**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdBrandPost) | **POST** /api/catalog/pvt/subcollection/{subCollectionId}/brand | Associate Brand to Subcollection |
| [**apiCatalogPvtSubcollectionSubCollectionIdCategoryPost**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdCategoryPost) | **POST** /api/catalog/pvt/subcollection/{subCollectionId}/category | Associate Category to Subcollection |
| [**apiCatalogPvtSubcollectionSubCollectionIdDelete**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId} | Delete Subcollection |
| [**apiCatalogPvtSubcollectionSubCollectionIdGet**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdGet) | **GET** /api/catalog/pvt/subcollection/{subCollectionId} | Get Subcollection |
| [**apiCatalogPvtSubcollectionSubCollectionIdPut**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdPut) | **PUT** /api/catalog/pvt/subcollection/{subCollectionId} | Update Subcollection |
| [**apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost) | **POST** /api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit | Add SKU to Subcollection |
| [**apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete**](LegacySubcollectionApi.md#apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete) | **DELETE** /api/catalog/pvt/subcollection/{subCollectionId}/stockkeepingunit/{skuId} | Delete SKU from Subcollection |


<a id="apiCatalogPvtCollectionCollectionIdPositionPost"></a>
# **apiCatalogPvtCollectionCollectionIdPositionPost**
> apiCatalogPvtCollectionCollectionIdPositionPost(contentType, accept, collectionId, apiCatalogPvtCollectionCollectionIdPositionPostRequest)

Reposition SKU on the Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Edits the position of an SKU that already exists in the Subcollection,  which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {       \&quot;skuId\&quot;: 1,       \&quot;position\&quot;: 1,       \&quot;subCollectionId\&quot;: 17  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacySubcollectionApi;

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

    LegacySubcollectionApi apiInstance = new LegacySubcollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer collectionId = 151; // Integer | Collection’s unique numerical identifier.
    ApiCatalogPvtCollectionCollectionIdPositionPostRequest apiCatalogPvtCollectionCollectionIdPositionPostRequest = new ApiCatalogPvtCollectionCollectionIdPositionPostRequest(); // ApiCatalogPvtCollectionCollectionIdPositionPostRequest | 
    try {
      apiInstance.apiCatalogPvtCollectionCollectionIdPositionPost(contentType, accept, collectionId, apiCatalogPvtCollectionCollectionIdPositionPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacySubcollectionApi#apiCatalogPvtCollectionCollectionIdPositionPost");
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
| **collectionId** | **Integer**| Collection’s unique numerical identifier. | |
| **apiCatalogPvtCollectionCollectionIdPositionPostRequest** | [**ApiCatalogPvtCollectionCollectionIdPositionPostRequest**](ApiCatalogPvtCollectionCollectionIdPositionPostRequest.md)|  | [optional] |

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
| **200** | OK |  -  |

<a id="apiCatalogPvtCollectionCollectionIdSubcollectionGet"></a>
# **apiCatalogPvtCollectionCollectionIdSubcollectionGet**
> List&lt;ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner&gt; apiCatalogPvtCollectionCollectionIdSubcollectionGet(contentType, accept, collectionId)

Get Subcollection by Collection ID

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves all Subcollections given a Collection ID. A Subcollection is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 12,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Subcollection\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: true      },      {          \&quot;Id\&quot;: 13,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;Test\&quot;,          \&quot;Type\&quot;: \&quot;Exclusive\&quot;,          \&quot;PreSale\&quot;: true,          \&quot;Release\&quot;: false      },      {          \&quot;Id\&quot;: 14,          \&quot;CollectionId\&quot;: 149,          \&quot;Name\&quot;: \&quot;asdfghj\&quot;,          \&quot;Type\&quot;: \&quot;Inclusive\&quot;,          \&quot;PreSale\&quot;: false,          \&quot;Release\&quot;: false      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacySubcollectionApi;

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

    LegacySubcollectionApi apiInstance = new LegacySubcollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer collectionId = 151; // Integer | Collection’s unique numerical identifier.
    try {
      List<ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner> result = apiInstance.apiCatalogPvtCollectionCollectionIdSubcollectionGet(contentType, accept, collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacySubcollectionApi#apiCatalogPvtCollectionCollectionIdSubcollectionGet");
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
| **collectionId** | **Integer**| Collection’s unique numerical identifier. | |

### Return type

[**List&lt;ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner&gt;**](ApiCatalogPvtCollectionCollectionIdSubcollectionGet200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSubcollectionPost"></a>
# **apiCatalogPvtSubcollectionPost**
> ApiCatalogPvtSubcollectionPost200Response apiCatalogPvtSubcollectionPost(contentType, accept, apiCatalogPvtSubcollectionPostRequest)

Create Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Creates a new Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection. A Subcollection can be either “Exclusive” (all the products contained in it will not be used) or “Inclusive” (all the products contained in it will be used).  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacySubcollectionApi;

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

    LegacySubcollectionApi apiInstance = new LegacySubcollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    ApiCatalogPvtSubcollectionPostRequest apiCatalogPvtSubcollectionPostRequest = new ApiCatalogPvtSubcollectionPostRequest(); // ApiCatalogPvtSubcollectionPostRequest | 
    try {
      ApiCatalogPvtSubcollectionPost200Response result = apiInstance.apiCatalogPvtSubcollectionPost(contentType, accept, apiCatalogPvtSubcollectionPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacySubcollectionApi#apiCatalogPvtSubcollectionPost");
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
| **apiCatalogPvtSubcollectionPostRequest** | [**ApiCatalogPvtSubcollectionPostRequest**](ApiCatalogPvtSubcollectionPostRequest.md)|  | [optional] |

### Return type

[**ApiCatalogPvtSubcollectionPost200Response**](ApiCatalogPvtSubcollectionPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete"></a>
# **apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete**
> apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete(contentType, accept, subCollectionId, brandId)

Delete Brand from Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Brand from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacySubcollectionApi;

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

    LegacySubcollectionApi apiInstance = new LegacySubcollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer subCollectionId = 1; // Integer | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    Integer brandId = 1; // Integer | Brand’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete(contentType, accept, subCollectionId, brandId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacySubcollectionApi#apiCatalogPvtSubcollectionSubCollectionIdBrandBrandIdDelete");
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
| **subCollectionId** | **Integer**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | |
| **brandId** | **Integer**| Brand’s unique numerical identifier. | |

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

<a id="apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete"></a>
# **apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete**
> apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete(contentType, accept, subCollectionId, categoryId)

Delete Category from Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a Category from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacySubcollectionApi;

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

    LegacySubcollectionApi apiInstance = new LegacySubcollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer subCollectionId = 1; // Integer | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    Integer categoryId = 1; // Integer | Category’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete(contentType, accept, subCollectionId, categoryId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacySubcollectionApi#apiCatalogPvtSubcollectionSubCollectionIdBrandCategoryIdDelete");
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
| **subCollectionId** | **Integer**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | |
| **categoryId** | **Integer**| Category’s unique numerical identifier. | |

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

<a id="apiCatalogPvtSubcollectionSubCollectionIdBrandPost"></a>
# **apiCatalogPvtSubcollectionSubCollectionIdBrandPost**
> ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response apiCatalogPvtSubcollectionSubCollectionIdBrandPost(contentType, accept, subCollectionId, requestBody10)

Associate Brand to Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Brand to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;BrandId\&quot;: 2000000  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacySubcollectionApi;

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

    LegacySubcollectionApi apiInstance = new LegacySubcollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer subCollectionId = 1; // Integer | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    RequestBody10 requestBody10 = new RequestBody10(); // RequestBody10 | 
    try {
      ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response result = apiInstance.apiCatalogPvtSubcollectionSubCollectionIdBrandPost(contentType, accept, subCollectionId, requestBody10);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacySubcollectionApi#apiCatalogPvtSubcollectionSubCollectionIdBrandPost");
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
| **subCollectionId** | **Integer**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | |
| **requestBody10** | [**RequestBody10**](RequestBody10.md)|  | [optional] |

### Return type

[**ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response**](ApiCatalogPvtSubcollectionSubCollectionIdBrandPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSubcollectionSubCollectionIdCategoryPost"></a>
# **apiCatalogPvtSubcollectionSubCollectionIdCategoryPost**
> ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response apiCatalogPvtSubcollectionSubCollectionIdCategoryPost(contentType, accept, subCollectionId, requestBody11)

Associate Category to Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single Category to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;CategoryId\&quot;: 1  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacySubcollectionApi;

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

    LegacySubcollectionApi apiInstance = new LegacySubcollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer subCollectionId = 1; // Integer | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    RequestBody11 requestBody11 = new RequestBody11(); // RequestBody11 | 
    try {
      ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response result = apiInstance.apiCatalogPvtSubcollectionSubCollectionIdCategoryPost(contentType, accept, subCollectionId, requestBody11);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacySubcollectionApi#apiCatalogPvtSubcollectionSubCollectionIdCategoryPost");
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
| **subCollectionId** | **Integer**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | |
| **requestBody11** | [**RequestBody11**](RequestBody11.md)|  | [optional] |

### Return type

[**ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response**](ApiCatalogPvtSubcollectionSubCollectionIdCategoryPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSubcollectionSubCollectionIdDelete"></a>
# **apiCatalogPvtSubcollectionSubCollectionIdDelete**
> apiCatalogPvtSubcollectionSubCollectionIdDelete(contentType, accept, subCollectionId)

Delete Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacySubcollectionApi;

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

    LegacySubcollectionApi apiInstance = new LegacySubcollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer subCollectionId = 1; // Integer | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    try {
      apiInstance.apiCatalogPvtSubcollectionSubCollectionIdDelete(contentType, accept, subCollectionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacySubcollectionApi#apiCatalogPvtSubcollectionSubCollectionIdDelete");
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
| **subCollectionId** | **Integer**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | |

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

<a id="apiCatalogPvtSubcollectionSubCollectionIdGet"></a>
# **apiCatalogPvtSubcollectionSubCollectionIdGet**
> ApiCatalogPvtSubcollectionPost200Response apiCatalogPvtSubcollectionSubCollectionIdGet(contentType, accept, subCollectionId)

Get Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves information about a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 13,      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacySubcollectionApi;

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

    LegacySubcollectionApi apiInstance = new LegacySubcollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer subCollectionId = 17; // Integer | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    try {
      ApiCatalogPvtSubcollectionPost200Response result = apiInstance.apiCatalogPvtSubcollectionSubCollectionIdGet(contentType, accept, subCollectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacySubcollectionApi#apiCatalogPvtSubcollectionSubCollectionIdGet");
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
| **subCollectionId** | **Integer**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | |

### Return type

[**ApiCatalogPvtSubcollectionPost200Response**](ApiCatalogPvtSubcollectionPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSubcollectionSubCollectionIdPut"></a>
# **apiCatalogPvtSubcollectionSubCollectionIdPut**
> ApiCatalogPvtSubcollectionPost200Response apiCatalogPvtSubcollectionSubCollectionIdPut(contentType, accept, subCollectionId, apiCatalogPvtSubcollectionSubCollectionIdPutRequest)

Update Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Updates a previously created Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.    ## Request or response body example    &#x60;&#x60;&#x60;json  {      \&quot;CollectionId\&quot;: 149,      \&quot;Name\&quot;: \&quot;Test\&quot;,      \&quot;Type\&quot;: \&quot;Exclusive\&quot;,      \&quot;PreSale\&quot;: true,      \&quot;Release\&quot;: false  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacySubcollectionApi;

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

    LegacySubcollectionApi apiInstance = new LegacySubcollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer subCollectionId = 17; // Integer | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    ApiCatalogPvtSubcollectionSubCollectionIdPutRequest apiCatalogPvtSubcollectionSubCollectionIdPutRequest = new ApiCatalogPvtSubcollectionSubCollectionIdPutRequest(); // ApiCatalogPvtSubcollectionSubCollectionIdPutRequest | 
    try {
      ApiCatalogPvtSubcollectionPost200Response result = apiInstance.apiCatalogPvtSubcollectionSubCollectionIdPut(contentType, accept, subCollectionId, apiCatalogPvtSubcollectionSubCollectionIdPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacySubcollectionApi#apiCatalogPvtSubcollectionSubCollectionIdPut");
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
| **subCollectionId** | **Integer**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | |
| **apiCatalogPvtSubcollectionSubCollectionIdPutRequest** | [**ApiCatalogPvtSubcollectionSubCollectionIdPutRequest**](ApiCatalogPvtSubcollectionSubCollectionIdPutRequest.md)|  | [optional] |

### Return type

[**ApiCatalogPvtSubcollectionPost200Response**](ApiCatalogPvtSubcollectionPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost"></a>
# **apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost**
> ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost(contentType, accept, subCollectionId, requestBody12)

Add SKU to Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Associates a single SKU to a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;SubCollectionId\&quot;: 17,      \&quot;SkuId\&quot;: 1  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacySubcollectionApi;

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

    LegacySubcollectionApi apiInstance = new LegacySubcollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer subCollectionId = 1; // Integer | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    RequestBody12 requestBody12 = new RequestBody12(); // RequestBody12 | 
    try {
      ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response result = apiInstance.apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost(contentType, accept, subCollectionId, requestBody12);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacySubcollectionApi#apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost");
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
| **subCollectionId** | **Integer**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | |
| **requestBody12** | [**RequestBody12**](RequestBody12.md)|  | [optional] |

### Return type

[**ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response**](ApiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete"></a>
# **apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete**
> apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete(contentType, accept, subCollectionId, skuId)

Delete SKU from Subcollection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes an SKU from a Subcollection, which is a [Group](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L#group-types) within a  Collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacySubcollectionApi;

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

    LegacySubcollectionApi apiInstance = new LegacySubcollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer subCollectionId = 1; // Integer | Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid).
    Integer skuId = 1; // Integer | SKU’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete(contentType, accept, subCollectionId, skuId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacySubcollectionApi#apiCatalogPvtSubcollectionSubCollectionIdStockkeepingunitSkuIdDelete");
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
| **subCollectionId** | **Integer**| Subcollection’s unique numerical identifier, which can be obtained by placing a request to [Get Subcollection by Collection ID](https://developers.vtex.com/vtex-rest-api/reference/catalog-api-get-subcollection-collectionid). | |
| **skuId** | **Integer**| SKU’s unique numerical identifier. | |

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

