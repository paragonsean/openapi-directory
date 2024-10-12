# ChannelCatalogsGlobalApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addChannelCatalog**](ChannelCatalogsGlobalApi.md#addChannelCatalog) | **POST** /v2/user/channelCatalogs/ | Add a new channel catalog |
| [**deleteChannelCatalog**](ChannelCatalogsGlobalApi.md#deleteChannelCatalog) | **DELETE** /v2/user/channelCatalogs/{channelCatalogId} | Delete the channel catalog |
| [**getChannelCatalog**](ChannelCatalogsGlobalApi.md#getChannelCatalog) | **GET** /v2/user/channelCatalogs/{channelCatalogId} | Get the channel catalog information |
| [**getChannelCatalogFilterOperators**](ChannelCatalogsGlobalApi.md#getChannelCatalogFilterOperators) | **GET** /v2/user/channelCatalogs/filterOperators | Get channel catalog filter operators |
| [**getChannelCatalogs**](ChannelCatalogsGlobalApi.md#getChannelCatalogs) | **GET** /v2/user/channelCatalogs/ | List all your current channel catalogs |


<a id="addChannelCatalog"></a>
# **addChannelCatalog**
> LinksGetChannelCatalogLink addChannelCatalog(addChannelCatalogRequest)

Add a new channel catalog

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsGlobalApi apiInstance = new ChannelCatalogsGlobalApi(defaultClient);
    AddChannelCatalogRequest addChannelCatalogRequest = new AddChannelCatalogRequest(); // AddChannelCatalogRequest | 
    try {
      LinksGetChannelCatalogLink result = apiInstance.addChannelCatalog(addChannelCatalogRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsGlobalApi#addChannelCatalog");
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
| **addChannelCatalogRequest** | [**AddChannelCatalogRequest**](AddChannelCatalogRequest.md)|  | |

### Return type

[**LinksGetChannelCatalogLink**](LinksGetChannelCatalogLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | When the channel has been successfully added for this store |  * Location - The location of the generated invoice. Might take a few seconds to be available <br>  * Retry-After - The duration in second to wait before polling this resource <br>  |
| **404** | StoreId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="deleteChannelCatalog"></a>
# **deleteChannelCatalog**
> deleteChannelCatalog(channelCatalogId)

Delete the channel catalog

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsGlobalApi apiInstance = new ChannelCatalogsGlobalApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    try {
      apiInstance.deleteChannelCatalog(channelCatalogId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsGlobalApi#deleteChannelCatalog");
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
| **channelCatalogId** | **String**| The channel catalog identifier | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Channel catalog deleted |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getChannelCatalog"></a>
# **getChannelCatalog**
> ChannelCatalog getChannelCatalog(channelCatalogId)

Get the channel catalog information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsGlobalApi apiInstance = new ChannelCatalogsGlobalApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    try {
      ChannelCatalog result = apiInstance.getChannelCatalog(channelCatalogId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsGlobalApi#getChannelCatalog");
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
| **channelCatalogId** | **String**| The channel catalog identifier | |

### Return type

[**ChannelCatalog**](ChannelCatalog.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel catalog |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getChannelCatalogFilterOperators"></a>
# **getChannelCatalogFilterOperators**
> List&lt;FilterOperator&gt; getChannelCatalogFilterOperators()

Get channel catalog filter operators

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsGlobalApi apiInstance = new ChannelCatalogsGlobalApi(defaultClient);
    try {
      List<FilterOperator> result = apiInstance.getChannelCatalogFilterOperators();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsGlobalApi#getChannelCatalogFilterOperators");
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

[**List&lt;FilterOperator&gt;**](FilterOperator.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel catalog  filter operator list |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getChannelCatalogs"></a>
# **getChannelCatalogs**
> ChannelCatalogList getChannelCatalogs(storeId)

List all your current channel catalogs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsGlobalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsGlobalApi apiInstance = new ChannelCatalogsGlobalApi(defaultClient);
    String storeId = "04730364-9826-4ff3-92e4-51fccd02bf10"; // String | The store identifier
    try {
      ChannelCatalogList result = apiInstance.getChannelCatalogs(storeId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsGlobalApi#getChannelCatalogs");
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
| **storeId** | **String**| The store identifier | [optional] |

### Return type

[**ChannelCatalogList**](ChannelCatalogList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Occurs when something goes wrong |  -  |

