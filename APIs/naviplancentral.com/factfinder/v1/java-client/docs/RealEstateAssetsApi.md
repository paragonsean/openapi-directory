# RealEstateAssetsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realEstateAssetsDeleteById**](RealEstateAssetsApi.md#realEstateAssetsDeleteById) | **DELETE** /api/RealEstateAssets/{id} |  |
| [**realEstateAssetsGetById**](RealEstateAssetsApi.md#realEstateAssetsGetById) | **GET** /api/RealEstateAssets/{id} |  |
| [**realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid**](RealEstateAssetsApi.md#realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid) | **GET** /api/RealEstateAssets |  |
| [**realEstateAssetsPostByModel**](RealEstateAssetsApi.md#realEstateAssetsPostByModel) | **POST** /api/RealEstateAssets |  |
| [**realEstateAssetsPutByIdModel**](RealEstateAssetsApi.md#realEstateAssetsPutByIdModel) | **PUT** /api/RealEstateAssets/{id} |  |


<a id="realEstateAssetsDeleteById"></a>
# **realEstateAssetsDeleteById**
> realEstateAssetsDeleteById(id)



Description: The operation removes a Real Estate Asset tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Real Estate Asset from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealEstateAssetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RealEstateAssetsApi apiInstance = new RealEstateAssetsApi(defaultClient);
    Integer id = 56; // Integer | The Real Estate Asset ID used to identify which Real Estate Asset to remove
    try {
      apiInstance.realEstateAssetsDeleteById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealEstateAssetsApi#realEstateAssetsDeleteById");
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
| **id** | **Integer**| The Real Estate Asset ID used to identify which Real Estate Asset to remove | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Deleted |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Real Estate Asset data access. |  -  |
| **403** | Request is restricted for access to Real Estate Asset. |  -  |
| **404** | Real Estate Asset not found. |  -  |

<a id="realEstateAssetsGetById"></a>
# **realEstateAssetsGetById**
> RealEstateAssetWithIdModel realEstateAssetsGetById(id)



Description: This operation retrieves a single Real Estate Asset for the specified Real Estate Asset ID.&lt;br /&gt;                Purpose: Provides access to the Real Estate Asset including description and market value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealEstateAssetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RealEstateAssetsApi apiInstance = new RealEstateAssetsApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Real Estate Asset used to retreive the Real Estate Asset
    try {
      RealEstateAssetWithIdModel result = apiInstance.realEstateAssetsGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealEstateAssetsApi#realEstateAssetsGetById");
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
| **id** | **Integer**| The ID of the Real Estate Asset used to retreive the Real Estate Asset | |

### Return type

[**RealEstateAssetWithIdModel**](RealEstateAssetWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Real Estate Asset data access. |  -  |
| **403** | Request is restricted for access to Real Estate Asset. |  -  |
| **404** | Real Estate Asset not found. |  -  |

<a id="realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid"></a>
# **realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid**
> RealEstateAssetsModel realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Real Estate Assets for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Real Estate Assets including description and market value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealEstateAssetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RealEstateAssetsApi apiInstance = new RealEstateAssetsApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Real Estate Assets
    try {
      RealEstateAssetsModel result = apiInstance.realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealEstateAssetsApi#realEstateAssetsGetRealEstateAssetsByFactFinderIdByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Real Estate Assets | |

### Return type

[**RealEstateAssetsModel**](RealEstateAssetsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Real Estate Asset data access. |  -  |
| **403** | Request is restricted for access to Real Estate Asset. |  -  |
| **404** | Real Estate Asset not found. |  -  |

<a id="realEstateAssetsPostByModel"></a>
# **realEstateAssetsPostByModel**
> RealEstateAssetWithIdModel realEstateAssetsPostByModel(model)



Description: The operation creates a Real Estate Asset.&lt;br /&gt;                Purpose: Allows for creation of Real Estate Assets on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealEstateAssetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RealEstateAssetsApi apiInstance = new RealEstateAssetsApi(defaultClient);
    RealEstateAssetModel model = new RealEstateAssetModel(); // RealEstateAssetModel | The Real Estate Asset to be added to the Fact Finder
    try {
      RealEstateAssetWithIdModel result = apiInstance.realEstateAssetsPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealEstateAssetsApi#realEstateAssetsPostByModel");
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
| **model** | [**RealEstateAssetModel**](RealEstateAssetModel.md)| The Real Estate Asset to be added to the Fact Finder | |

### Return type

[**RealEstateAssetWithIdModel**](RealEstateAssetWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Real Estate Asset data access. |  -  |
| **403** | Request is restricted for access to Real Estate Asset. |  -  |
| **404** | Real Estate Asset not found. |  -  |

<a id="realEstateAssetsPutByIdModel"></a>
# **realEstateAssetsPutByIdModel**
> RealEstateAssetWithIdModel realEstateAssetsPutByIdModel(id, model)



Description: The operation updates a Real Estate Asset.&lt;br /&gt;                Purpose: Allows for complete replacement of a Real Estate Asset on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealEstateAssetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    RealEstateAssetsApi apiInstance = new RealEstateAssetsApi(defaultClient);
    Integer id = 56; // Integer | The existing Real Estate Asset ID used to identify which Real Estate Asset to update
    RealEstateAssetModel model = new RealEstateAssetModel(); // RealEstateAssetModel | The Real Estate Asset to be updated on a Fact Finder
    try {
      RealEstateAssetWithIdModel result = apiInstance.realEstateAssetsPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealEstateAssetsApi#realEstateAssetsPutByIdModel");
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
| **id** | **Integer**| The existing Real Estate Asset ID used to identify which Real Estate Asset to update | |
| **model** | [**RealEstateAssetModel**](RealEstateAssetModel.md)| The Real Estate Asset to be updated on a Fact Finder | |

### Return type

[**RealEstateAssetWithIdModel**](RealEstateAssetWithIdModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | The request is invalid. |  -  |
| **401** | Unauthorized for Real Estate Asset data access. |  -  |
| **403** | Request is restricted for access to Real Estate Asset. |  -  |
| **404** | Real Estate Asset not found. |  -  |

