# LegacyCollectionApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiCatalogPvtCollectionCollectionIdDelete**](LegacyCollectionApi.md#apiCatalogPvtCollectionCollectionIdDelete) | **DELETE** /api/catalog/pvt/collection/{collectionId} | Delete Collection |
| [**apiCatalogPvtCollectionCollectionIdGet**](LegacyCollectionApi.md#apiCatalogPvtCollectionCollectionIdGet) | **GET** /api/catalog/pvt/collection/{collectionId} | Get Collection |
| [**apiCatalogPvtCollectionCollectionIdPut**](LegacyCollectionApi.md#apiCatalogPvtCollectionCollectionIdPut) | **PUT** /api/catalog/pvt/collection/{collectionId} | Update Collection |
| [**apiCatalogPvtCollectionPost**](LegacyCollectionApi.md#apiCatalogPvtCollectionPost) | **POST** /api/catalog/pvt/collection | Create Collection |


<a id="apiCatalogPvtCollectionCollectionIdDelete"></a>
# **apiCatalogPvtCollectionCollectionIdDelete**
> apiCatalogPvtCollectionCollectionIdDelete(contentType, accept, collectionId)

Delete Collection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Deletes a previously existing Collection.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacyCollectionApi;

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

    LegacyCollectionApi apiInstance = new LegacyCollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer collectionId = 151; // Integer | Collection’s unique numerical identifier.
    try {
      apiInstance.apiCatalogPvtCollectionCollectionIdDelete(contentType, accept, collectionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacyCollectionApi#apiCatalogPvtCollectionCollectionIdDelete");
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

<a id="apiCatalogPvtCollectionCollectionIdGet"></a>
# **apiCatalogPvtCollectionCollectionIdGet**
> ApiCatalogPvtCollectionPost200Response apiCatalogPvtCollectionCollectionIdGet(contentType, accept, collectionId)

Get Collection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Retrieves general information of a Collection.    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 159,      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Description\&quot;: null,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;,      \&quot;TotalProducts\&quot;: 0,      \&quot;Type\&quot;: \&quot;Manual\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacyCollectionApi;

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

    LegacyCollectionApi apiInstance = new LegacyCollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer collectionId = 151; // Integer | Collection’s unique numerical identifier.
    try {
      ApiCatalogPvtCollectionPost200Response result = apiInstance.apiCatalogPvtCollectionCollectionIdGet(contentType, accept, collectionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacyCollectionApi#apiCatalogPvtCollectionCollectionIdGet");
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

[**ApiCatalogPvtCollectionPost200Response**](ApiCatalogPvtCollectionPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtCollectionCollectionIdPut"></a>
# **apiCatalogPvtCollectionCollectionIdPut**
> ApiCatalogPvtCollectionPost200Response apiCatalogPvtCollectionCollectionIdPut(contentType, accept, collectionId, resquestBody1)

Update Collection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Updates a previously created Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 159,      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Description\&quot;: null,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;,      \&quot;TotalProducts\&quot;: 0,      \&quot;Type\&quot;: \&quot;Manual\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacyCollectionApi;

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

    LegacyCollectionApi apiInstance = new LegacyCollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer collectionId = 151; // Integer | Collection’s unique numerical identifier.
    ResquestBody1 resquestBody1 = new ResquestBody1(); // ResquestBody1 | 
    try {
      ApiCatalogPvtCollectionPost200Response result = apiInstance.apiCatalogPvtCollectionCollectionIdPut(contentType, accept, collectionId, resquestBody1);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacyCollectionApi#apiCatalogPvtCollectionCollectionIdPut");
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
| **resquestBody1** | [**ResquestBody1**](ResquestBody1.md)|  | [optional] |

### Return type

[**ApiCatalogPvtCollectionPost200Response**](ApiCatalogPvtCollectionPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="apiCatalogPvtCollectionPost"></a>
# **apiCatalogPvtCollectionPost**
> ApiCatalogPvtCollectionPost200Response apiCatalogPvtCollectionPost(contentType, accept, resquestBody)

Create Collection

 &gt;⚠️ There are two ways to configure collections, through Legacy CMS Portal or using the Beta Collection module. This endpoint is compatible with [collections configured through the Legacy CMS Portal](https://help.vtex.com/en/tutorial/adding-collections-cms--2YBy6P6X0NFRpkD2ZBxF6L).  Creates a new Collection.  ## Request body example    &#x60;&#x60;&#x60;json  {      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;  }  &#x60;&#x60;&#x60;    ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 159,      \&quot;Name\&quot;: \&quot;Winter\&quot;,      \&quot;Description\&quot;: null,      \&quot;Searchable\&quot;: false,      \&quot;Highlight\&quot;: false,      \&quot;DateFrom\&quot;: \&quot;2021-09-27T10:47:00\&quot;,      \&quot;DateTo\&quot;: \&quot;2027-09-27T10:47:00\&quot;,      \&quot;TotalProducts\&quot;: 0,      \&quot;Type\&quot;: \&quot;Manual\&quot;  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LegacyCollectionApi;

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

    LegacyCollectionApi apiInstance = new LegacyCollectionApi(defaultClient);
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    ResquestBody resquestBody = new ResquestBody(); // ResquestBody | 
    try {
      ApiCatalogPvtCollectionPost200Response result = apiInstance.apiCatalogPvtCollectionPost(contentType, accept, resquestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LegacyCollectionApi#apiCatalogPvtCollectionPost");
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
| **resquestBody** | [**ResquestBody**](ResquestBody.md)|  | [optional] |

### Return type

[**ApiCatalogPvtCollectionPost200Response**](ApiCatalogPvtCollectionPost200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

