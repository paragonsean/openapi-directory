# OnDemandRegionsApi

All URIs are relative to *https://api.vimeo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVodRegion**](OnDemandRegionsApi.md#addVodRegion) | **PUT** /ondemand/pages/{ondemand_id}/regions/{country} | Add a specific region to an On Demand page |
| [**deleteVodRegion**](OnDemandRegionsApi.md#deleteVodRegion) | **DELETE** /ondemand/pages/{ondemand_id}/regions/{country} | Remove a specific region from an On Demand page |
| [**deleteVodRegions**](OnDemandRegionsApi.md#deleteVodRegions) | **DELETE** /ondemand/pages/{ondemand_id}/regions | Remove a list of regions from an On Demand page |
| [**getRegion**](OnDemandRegionsApi.md#getRegion) | **GET** /ondemand/regions/{country} | Get a specific On Demand region |
| [**getRegions**](OnDemandRegionsApi.md#getRegions) | **GET** /ondemand/regions | Get all the On Demand regions |
| [**getVodRegion**](OnDemandRegionsApi.md#getVodRegion) | **GET** /ondemand/pages/{ondemand_id}/regions/{country} | Get a specific region of an On Demand page |
| [**getVodRegions**](OnDemandRegionsApi.md#getVodRegions) | **GET** /ondemand/pages/{ondemand_id}/regions | Get all the regions of an On Demand page |
| [**setVodRegions**](OnDemandRegionsApi.md#setVodRegions) | **PUT** /ondemand/pages/{ondemand_id}/regions | Add a list of regions to an On Demand page |


<a id="addVodRegion"></a>
# **addVodRegion**
> OnDemandRegion addVodRegion(country, ondemandId)

Add a specific region to an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandRegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandRegionsApi apiInstance = new OnDemandRegionsApi(defaultClient);
    String country = "US"; // String | The country code.
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      OnDemandRegion result = apiInstance.addVodRegion(country, ondemandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandRegionsApi#addVodRegion");
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
| **country** | **String**| The country code. | |
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |

### Return type

[**OnDemandRegion**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.region+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The region was added. |  -  |
| **403** | You can&#39;t modify an On Demand page that you don&#39;t own. |  -  |
| **404** | No such On Demand page or region exists. |  -  |

<a id="deleteVodRegion"></a>
# **deleteVodRegion**
> deleteVodRegion(country, ondemandId)

Remove a specific region from an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandRegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandRegionsApi apiInstance = new OnDemandRegionsApi(defaultClient);
    String country = "US"; // String | The country code.
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      apiInstance.deleteVodRegion(country, ondemandId);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandRegionsApi#deleteVodRegion");
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
| **country** | **String**| The country code. | |
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |

### Return type

null (empty response body)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.region+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | The On Demand region was deleted. |  -  |
| **403** | You can&#39;t modify an On Demand page that you don&#39;t own. |  -  |
| **404** | No such On Demand page or region exists. |  -  |

<a id="deleteVodRegions"></a>
# **deleteVodRegions**
> List&lt;OnDemandRegion&gt; deleteVodRegions(ondemandId, deleteVodRegionsRequest)

Remove a list of regions from an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandRegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandRegionsApi apiInstance = new OnDemandRegionsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    DeleteVodRegionsRequest deleteVodRegionsRequest = new DeleteVodRegionsRequest(); // DeleteVodRegionsRequest | 
    try {
      List<OnDemandRegion> result = apiInstance.deleteVodRegions(ondemandId, deleteVodRegionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandRegionsApi#deleteVodRegions");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **deleteVodRegionsRequest** | [**DeleteVodRegionsRequest**](DeleteVodRegionsRequest.md)|  | [optional] |

### Return type

[**List&lt;OnDemandRegion&gt;**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.ondemand.region+json
 - **Accept**: application/vnd.vimeo.ondemand.region+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The On Demand regions were deleted. |  -  |
| **403** | You can&#39;t modify an On Demand page that you don&#39;t own. |  -  |
| **404** | No such On Demand page or region exists. |  -  |

<a id="getRegion"></a>
# **getRegion**
> OnDemandRegion getRegion(country)

Get a specific On Demand region

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandRegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandRegionsApi apiInstance = new OnDemandRegionsApi(defaultClient);
    String country = "US"; // String | The country code.
    try {
      OnDemandRegion result = apiInstance.getRegion(country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandRegionsApi#getRegion");
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
| **country** | **String**| The country code. | |

### Return type

[**OnDemandRegion**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.region+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The On Demand region was returned. |  -  |
| **404** | No such On Demand region exists. |  -  |

<a id="getRegions"></a>
# **getRegions**
> List&lt;OnDemandRegion&gt; getRegions()

Get all the On Demand regions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandRegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandRegionsApi apiInstance = new OnDemandRegionsApi(defaultClient);
    try {
      List<OnDemandRegion> result = apiInstance.getRegions();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandRegionsApi#getRegions");
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

[**List&lt;OnDemandRegion&gt;**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.region+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The On Demand regions were returned. |  -  |

<a id="getVodRegion"></a>
# **getVodRegion**
> OnDemandRegion getVodRegion(country, ondemandId)

Get a specific region of an On Demand page

Checks whether an On Demand page belongs to a region.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandRegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandRegionsApi apiInstance = new OnDemandRegionsApi(defaultClient);
    String country = "US"; // String | The country code.
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      OnDemandRegion result = apiInstance.getVodRegion(country, ondemandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandRegionsApi#getVodRegion");
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
| **country** | **String**| The country code. | |
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |

### Return type

[**OnDemandRegion**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.region+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The On Demand page&#39;s region was returned. |  -  |
| **404** | No such On Demand page or region exists. |  -  |

<a id="getVodRegions"></a>
# **getVodRegions**
> List&lt;OnDemandRegion&gt; getVodRegions(ondemandId)

Get all the regions of an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandRegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandRegionsApi apiInstance = new OnDemandRegionsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    try {
      List<OnDemandRegion> result = apiInstance.getVodRegions(ondemandId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandRegionsApi#getVodRegions");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |

### Return type

[**List&lt;OnDemandRegion&gt;**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.vimeo.ondemand.region+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The regions were returned. |  -  |
| **404** | No such On Demand page exists. |  -  |

<a id="setVodRegions"></a>
# **setVodRegions**
> OnDemandRegion setVodRegions(ondemandId, setVodRegionsRequest)

Add a list of regions to an On Demand page

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OnDemandRegionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vimeo.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    OnDemandRegionsApi apiInstance = new OnDemandRegionsApi(defaultClient);
    BigDecimal ondemandId = new BigDecimal("61326"); // BigDecimal | The ID of the On Demand.
    SetVodRegionsRequest setVodRegionsRequest = new SetVodRegionsRequest(); // SetVodRegionsRequest | 
    try {
      OnDemandRegion result = apiInstance.setVodRegions(ondemandId, setVodRegionsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OnDemandRegionsApi#setVodRegions");
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
| **ondemandId** | **BigDecimal**| The ID of the On Demand. | |
| **setVodRegionsRequest** | [**SetVodRegionsRequest**](SetVodRegionsRequest.md)|  | |

### Return type

[**OnDemandRegion**](OnDemandRegion.md)

### Authorization

[oauth2](../README.md#oauth2), [oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/vnd.vimeo.ondemand.region+json
 - **Accept**: application/vnd.vimeo.ondemand.region+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The list of regions was set. |  -  |
| **403** | You can&#39;t modify an On Demand page that you don&#39;t own. |  -  |
| **404** | No such On Demand page or region exists. |  -  |

