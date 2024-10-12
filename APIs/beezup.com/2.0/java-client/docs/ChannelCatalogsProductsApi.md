# ChannelCatalogsProductsApi

All URIs are relative to *https://api.beezup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exportChannelCatalogProductInfoList**](ChannelCatalogsProductsApi.md#exportChannelCatalogProductInfoList) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/products/export | Export channel catalog product information list |
| [**getChannelCatalogProductByChannelCatalog**](ChannelCatalogsProductsApi.md#getChannelCatalogProductByChannelCatalog) | **POST** /v2/user/channelCatalogs/products | Get channel catalog products related to these channel catalogs |
| [**getChannelCatalogProductInfo**](ChannelCatalogsProductsApi.md#getChannelCatalogProductInfo) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/products/{productId} | Get channel catalog product information |
| [**getChannelCatalogProductInfoList**](ChannelCatalogsProductsApi.md#getChannelCatalogProductInfoList) | **POST** /v2/user/channelCatalogs/{channelCatalogId}/products | Get channel catalog product information list |
| [**getChannelCatalogProductsCounters**](ChannelCatalogsProductsApi.md#getChannelCatalogProductsCounters) | **GET** /v2/user/channelCatalogs/{channelCatalogId}/products/counters | Get channel catalog products&#39; counters |


<a id="exportChannelCatalogProductInfoList"></a>
# **exportChannelCatalogProductInfoList**
> BeezUPCommonLink3 exportChannelCatalogProductInfoList(channelCatalogId, format, getChannelCatalogProductInfoListRequest)

Export channel catalog product information list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsProductsApi apiInstance = new ChannelCatalogsProductsApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    String format = "xlsx"; // String | The file type of the exportation
    GetChannelCatalogProductInfoListRequest getChannelCatalogProductInfoListRequest = new GetChannelCatalogProductInfoListRequest(); // GetChannelCatalogProductInfoListRequest | The channel catalog product list filter
    try {
      BeezUPCommonLink3 result = apiInstance.exportChannelCatalogProductInfoList(channelCatalogId, format, getChannelCatalogProductInfoListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsProductsApi#exportChannelCatalogProductInfoList");
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
| **format** | **String**| The file type of the exportation | [enum: xlsx, csv] |
| **getChannelCatalogProductInfoListRequest** | [**GetChannelCatalogProductInfoListRequest**](GetChannelCatalogProductInfoListRequest.md)| The channel catalog product list filter | |

### Return type

[**BeezUPCommonLink3**](BeezUPCommonLink3.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel catalog product information list exported |  * Location - The location of the generated invoice. Might take a few seconds to be available <br>  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getChannelCatalogProductByChannelCatalog"></a>
# **getChannelCatalogProductByChannelCatalog**
> ChannelCatalogProductByChannelCatalogResponse getChannelCatalogProductByChannelCatalog(channelCatalogProductByChannelCatalogRequest)

Get channel catalog products related to these channel catalogs

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsProductsApi apiInstance = new ChannelCatalogsProductsApi(defaultClient);
    ChannelCatalogProductByChannelCatalogRequest channelCatalogProductByChannelCatalogRequest = new ChannelCatalogProductByChannelCatalogRequest(); // ChannelCatalogProductByChannelCatalogRequest | 
    try {
      ChannelCatalogProductByChannelCatalogResponse result = apiInstance.getChannelCatalogProductByChannelCatalog(channelCatalogProductByChannelCatalogRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsProductsApi#getChannelCatalogProductByChannelCatalog");
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
| **channelCatalogProductByChannelCatalogRequest** | [**ChannelCatalogProductByChannelCatalogRequest**](ChannelCatalogProductByChannelCatalogRequest.md)|  | |

### Return type

[**ChannelCatalogProductByChannelCatalogResponse**](ChannelCatalogProductByChannelCatalogResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The channel catalog product by channel catalog |  -  |
| **404** | ProductId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getChannelCatalogProductInfo"></a>
# **getChannelCatalogProductInfo**
> ChannelCatalogProductInfo getChannelCatalogProductInfo(channelCatalogId, productId)

Get channel catalog product information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsProductsApi apiInstance = new ChannelCatalogsProductsApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    String productId = "578419df-1bbf-41a6-96fa-862e42182b67"; // String | The product identifier
    try {
      ChannelCatalogProductInfo result = apiInstance.getChannelCatalogProductInfo(channelCatalogId, productId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsProductsApi#getChannelCatalogProductInfo");
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
| **productId** | **String**| The product identifier | |

### Return type

[**ChannelCatalogProductInfo**](ChannelCatalogProductInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel catalog product information |  -  |
| **404** | ChannelCatalog or ProductId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getChannelCatalogProductInfoList"></a>
# **getChannelCatalogProductInfoList**
> ChannelCatalogProductInfoList getChannelCatalogProductInfoList(channelCatalogId, getChannelCatalogProductInfoListRequest)

Get channel catalog product information list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsProductsApi apiInstance = new ChannelCatalogsProductsApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    GetChannelCatalogProductInfoListRequest getChannelCatalogProductInfoListRequest = new GetChannelCatalogProductInfoListRequest(); // GetChannelCatalogProductInfoListRequest | The channel catalog product list filter
    try {
      ChannelCatalogProductInfoList result = apiInstance.getChannelCatalogProductInfoList(channelCatalogId, getChannelCatalogProductInfoListRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsProductsApi#getChannelCatalogProductInfoList");
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
| **getChannelCatalogProductInfoListRequest** | [**GetChannelCatalogProductInfoListRequest**](GetChannelCatalogProductInfoListRequest.md)| The channel catalog product list filter | |

### Return type

[**ChannelCatalogProductInfoList**](ChannelCatalogProductInfoList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel catalog product information |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

<a id="getChannelCatalogProductsCounters"></a>
# **getChannelCatalogProductsCounters**
> ChannelCatalogProductsCounters getChannelCatalogProductsCounters(channelCatalogId)

Get channel catalog products&#39; counters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChannelCatalogsProductsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.beezup.com");

    ChannelCatalogsProductsApi apiInstance = new ChannelCatalogsProductsApi(defaultClient);
    String channelCatalogId = "6d6b04de-406b-4539-8e7e-bf3e8da5dfb0"; // String | The channel catalog identifier
    try {
      ChannelCatalogProductsCounters result = apiInstance.getChannelCatalogProductsCounters(channelCatalogId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChannelCatalogsProductsApi#getChannelCatalogProductsCounters");
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

[**ChannelCatalogProductsCounters**](ChannelCatalogProductsCounters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Channel catalog products&#39; counters |  -  |
| **404** | ChannelCatalogId not found or not authorized |  -  |
| **0** | Occurs when something goes wrong |  -  |

