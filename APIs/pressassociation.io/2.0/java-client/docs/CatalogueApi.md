# CatalogueApi

All URIs are relative to *https://tv.api.pressassociation.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCatalogue**](CatalogueApi.md#getCatalogue) | **GET** /catalogue/{catalogueId} | Catalogue Detail |
| [**getCatalogueAsset**](CatalogueApi.md#getCatalogueAsset) | **GET** /catalogue/{catalogueId}/asset | Catalogue Asset Collection |
| [**getCatalogueAssetDetail**](CatalogueApi.md#getCatalogueAssetDetail) | **GET** /catalogue/{catalogueId}/asset/{assetId} | Catalogue Asset Detail |
| [**listCatalogues**](CatalogueApi.md#listCatalogues) | **GET** /catalogue | Catalogue Collection |


<a id="getCatalogue"></a>
# **getCatalogue**
> Object getCatalogue(catalogueId)

Catalogue Detail

Return the content of the selected catalogue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    CatalogueApi apiInstance = new CatalogueApi(defaultClient);
    String catalogueId = "catalogueId_example"; // String | The identifier for the selected catalogue.
    try {
      Object result = apiInstance.getCatalogue(catalogueId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogueApi#getCatalogue");
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
| **catalogueId** | **String**| The identifier for the selected catalogue. | |

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getCatalogueAsset"></a>
# **getCatalogueAsset**
> Object getCatalogueAsset(catalogueId, title, start, end, updatedAfter, limit, aliases)

Catalogue Asset Collection

Return the content of the selected catalogue.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    CatalogueApi apiInstance = new CatalogueApi(defaultClient);
    String catalogueId = "catalogueId_example"; // String | The identifier for the selected catalogue.
    String title = "title_example"; // String | The query string for a title search
    String start = "2015-05-05T00:00:00"; // String | The Start Date for the catalogue date range.
    String end = "2015-05-06T00:00:00"; // String | The End Date for the catalogue date range.
    String updatedAfter = "2015-05-06T00:00:00"; // String | Retrieve items only that have been updated after this point.
    BigDecimal limit = new BigDecimal("500"); // BigDecimal | Restrict number of returned items Min = 1, Max = 500.
    Boolean aliases = true; // Boolean | Flag to display Legacy and Provider Ids.
    try {
      Object result = apiInstance.getCatalogueAsset(catalogueId, title, start, end, updatedAfter, limit, aliases);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogueApi#getCatalogueAsset");
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
| **catalogueId** | **String**| The identifier for the selected catalogue. | |
| **title** | **String**| The query string for a title search | [optional] |
| **start** | **String**| The Start Date for the catalogue date range. | [optional] [default to 2015-05-05T00:00:00] |
| **end** | **String**| The End Date for the catalogue date range. | [optional] [default to 2015-05-06T00:00:00] |
| **updatedAfter** | **String**| Retrieve items only that have been updated after this point. | [optional] [default to 2015-05-06T00:00:00] |
| **limit** | **BigDecimal**| Restrict number of returned items Min &#x3D; 1, Max &#x3D; 500. | [optional] [default to 500] |
| **aliases** | **Boolean**| Flag to display Legacy and Provider Ids. | [optional] [default to true] |

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="getCatalogueAssetDetail"></a>
# **getCatalogueAssetDetail**
> Object getCatalogueAssetDetail(catalogueId, assetId)

Catalogue Asset Detail

Return the content of the selected catalogue asset.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    CatalogueApi apiInstance = new CatalogueApi(defaultClient);
    String catalogueId = "catalogueId_example"; // String | The identifier for the selected catalogue.
    String assetId = "assetId_example"; // String | The identifier for the selected catalogue asset.
    try {
      Object result = apiInstance.getCatalogueAssetDetail(catalogueId, assetId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogueApi#getCatalogueAssetDetail");
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
| **catalogueId** | **String**| The identifier for the selected catalogue. | |
| **assetId** | **String**| The identifier for the selected catalogue asset. | |

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="listCatalogues"></a>
# **listCatalogues**
> Object listCatalogues()

Catalogue Collection

Return a collection of Catalogues.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CatalogueApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://tv.api.pressassociation.io/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    CatalogueApi apiInstance = new CatalogueApi(defaultClient);
    try {
      Object result = apiInstance.listCatalogues();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CatalogueApi#listCatalogues");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

**Object**

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

