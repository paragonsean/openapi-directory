# LifestyleAssetsApi

All URIs are relative to *https://demo.uat.naviplancentral.com/factfinder*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**lifestyleAssetsDeleteById**](LifestyleAssetsApi.md#lifestyleAssetsDeleteById) | **DELETE** /api/LifestyleAssets/{id} |  |
| [**lifestyleAssetsGetById**](LifestyleAssetsApi.md#lifestyleAssetsGetById) | **GET** /api/LifestyleAssets/{id} |  |
| [**lifestyleAssetsGetLifestyleAssetsByFactFinderIdByFactfinderid**](LifestyleAssetsApi.md#lifestyleAssetsGetLifestyleAssetsByFactFinderIdByFactfinderid) | **GET** /api/LifestyleAssets |  |
| [**lifestyleAssetsPostByModel**](LifestyleAssetsApi.md#lifestyleAssetsPostByModel) | **POST** /api/LifestyleAssets |  |
| [**lifestyleAssetsPutByIdModel**](LifestyleAssetsApi.md#lifestyleAssetsPutByIdModel) | **PUT** /api/LifestyleAssets/{id} |  |


<a id="lifestyleAssetsDeleteById"></a>
# **lifestyleAssetsDeleteById**
> lifestyleAssetsDeleteById(id)



Description: The operation removes a Lifestyle Asset tied to a Fact Finder.&lt;br /&gt;                Purpose: Allows for removal of a Lifestyle Asset from a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifestyleAssetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifestyleAssetsApi apiInstance = new LifestyleAssetsApi(defaultClient);
    Integer id = 56; // Integer | The Lifestyle Asset ID used to identify which Lifestyle Asset to remove
    try {
      apiInstance.lifestyleAssetsDeleteById(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifestyleAssetsApi#lifestyleAssetsDeleteById");
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
| **id** | **Integer**| The Lifestyle Asset ID used to identify which Lifestyle Asset to remove | |

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
| **401** | Unauthorized for Lifestyle Asset data access. |  -  |
| **403** | Request is restricted for access to Lifestyle Asset. |  -  |
| **404** | Lifestyle Asset not found. |  -  |

<a id="lifestyleAssetsGetById"></a>
# **lifestyleAssetsGetById**
> LifestyleAssetWithIdModel lifestyleAssetsGetById(id)



Description: This operation retrieves a single Lifestyle Asset for the specified Lifestyle Asset ID.&lt;br /&gt;                Purpose: Provides access to the Lifestyle Asset including description and market value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifestyleAssetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifestyleAssetsApi apiInstance = new LifestyleAssetsApi(defaultClient);
    Integer id = 56; // Integer | The ID of the Lifestyle Asset used to retreive the Lifestyle Asset
    try {
      LifestyleAssetWithIdModel result = apiInstance.lifestyleAssetsGetById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifestyleAssetsApi#lifestyleAssetsGetById");
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
| **id** | **Integer**| The ID of the Lifestyle Asset used to retreive the Lifestyle Asset | |

### Return type

[**LifestyleAssetWithIdModel**](LifestyleAssetWithIdModel.md)

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
| **401** | Unauthorized for Lifestyle Asset data access. |  -  |
| **403** | Request is restricted for access to Lifestyle Asset. |  -  |
| **404** | Lifestyle Asset not found. |  -  |

<a id="lifestyleAssetsGetLifestyleAssetsByFactFinderIdByFactfinderid"></a>
# **lifestyleAssetsGetLifestyleAssetsByFactFinderIdByFactfinderid**
> LifestyleAssetsModel lifestyleAssetsGetLifestyleAssetsByFactFinderIdByFactfinderid(factFinderId)



Description: This operation retrieves all Lifestyle Assets for the specified Fact Finder ID.&lt;br /&gt;                Purpose: Provides access to the Lifestyle Assets including description and market value.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifestyleAssetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifestyleAssetsApi apiInstance = new LifestyleAssetsApi(defaultClient);
    Integer factFinderId = 56; // Integer | The ID of the Fact Finder used to retrieve Lifestyle Assets
    try {
      LifestyleAssetsModel result = apiInstance.lifestyleAssetsGetLifestyleAssetsByFactFinderIdByFactfinderid(factFinderId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifestyleAssetsApi#lifestyleAssetsGetLifestyleAssetsByFactFinderIdByFactfinderid");
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
| **factFinderId** | **Integer**| The ID of the Fact Finder used to retrieve Lifestyle Assets | |

### Return type

[**LifestyleAssetsModel**](LifestyleAssetsModel.md)

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
| **401** | Unauthorized for Lifestyle Asset data access. |  -  |
| **403** | Request is restricted for access to Lifestyle Asset. |  -  |
| **404** | Lifestyle Asset not found. |  -  |

<a id="lifestyleAssetsPostByModel"></a>
# **lifestyleAssetsPostByModel**
> LifestyleAssetWithIdModel lifestyleAssetsPostByModel(model)



Description: The operation creates a Lifestyle Asset.&lt;br /&gt;                Purpose: Allows for creation of Lifestyle Assets on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifestyleAssetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifestyleAssetsApi apiInstance = new LifestyleAssetsApi(defaultClient);
    LifestyleAssetModel model = new LifestyleAssetModel(); // LifestyleAssetModel | The Lifestyle Asset to be added to the Fact Finder
    try {
      LifestyleAssetWithIdModel result = apiInstance.lifestyleAssetsPostByModel(model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifestyleAssetsApi#lifestyleAssetsPostByModel");
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
| **model** | [**LifestyleAssetModel**](LifestyleAssetModel.md)| The Lifestyle Asset to be added to the Fact Finder | |

### Return type

[**LifestyleAssetWithIdModel**](LifestyleAssetWithIdModel.md)

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
| **401** | Unauthorized for Lifestyle Asset data access. |  -  |
| **403** | Request is restricted for access to Lifestyle Asset. |  -  |
| **404** | Lifestyle Asset not found. |  -  |

<a id="lifestyleAssetsPutByIdModel"></a>
# **lifestyleAssetsPutByIdModel**
> LifestyleAssetWithIdModel lifestyleAssetsPutByIdModel(id, model)



Description: The operation updates a Lifestyle Asset.&lt;br /&gt;                Purpose: Allows for complete replacement of a Lifestyle Asset on a Fact Finder.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LifestyleAssetsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/factfinder");

    LifestyleAssetsApi apiInstance = new LifestyleAssetsApi(defaultClient);
    Integer id = 56; // Integer | The existing Lifestyle Asset ID used to identify which Lifestyle Asset to update
    LifestyleAssetModel model = new LifestyleAssetModel(); // LifestyleAssetModel | The Lifestyle Asset to be updated on a Fact Finder
    try {
      LifestyleAssetWithIdModel result = apiInstance.lifestyleAssetsPutByIdModel(id, model);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LifestyleAssetsApi#lifestyleAssetsPutByIdModel");
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
| **id** | **Integer**| The existing Lifestyle Asset ID used to identify which Lifestyle Asset to update | |
| **model** | [**LifestyleAssetModel**](LifestyleAssetModel.md)| The Lifestyle Asset to be updated on a Fact Finder | |

### Return type

[**LifestyleAssetWithIdModel**](LifestyleAssetWithIdModel.md)

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
| **401** | Unauthorized for Lifestyle Asset data access. |  -  |
| **403** | Request is restricted for access to Lifestyle Asset. |  -  |
| **404** | Lifestyle Asset not found. |  -  |

