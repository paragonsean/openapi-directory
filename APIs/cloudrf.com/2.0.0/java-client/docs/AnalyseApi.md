# AnalyseApi

All URIs are relative to *https://api.cloudrf.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**interference**](AnalyseApi.md#interference) | **GET** /interference | Find the best server for overlapping coverage |
| [**mesh**](AnalyseApi.md#mesh) | **GET** /mesh | Merge sites into a super layer. |
| [**network**](AnalyseApi.md#network) | **GET** /network | Find the best server for somewhere |


<a id="interference"></a>
# **interference**
> interference(network, name)

Find the best server for overlapping coverage

Merge and analyse sites within a network channel to determine the best server at a given location. Each site will be dynamically allocated a monochrome colour from a palette and the strongest signal promoted at a given location.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloudrf.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AnalyseApi apiInstance = new AnalyseApi(defaultClient);
    String network = "network_example"; // String | Network name eg. Overlapping broadcast stations
    String name = "name_example"; // String | Interference layer name eg. QRM_map
    try {
      apiInstance.interference(network, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyseApi#interference");
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
| **network** | **String**| Network name eg. Overlapping broadcast stations | |
| **name** | **String**| Interference layer name eg. QRM_map | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request OK |  -  |

<a id="mesh"></a>
# **mesh**
> mesh(network, name)

Merge sites into a super layer.

A merge of &#39;area&#39; calculations for a network to create a single super layer. Stronger signals are promoted over weaker ones. The same colour key must be used.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloudrf.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AnalyseApi apiInstance = new AnalyseApi(defaultClient);
    String network = "network_example"; // String | Network name eg. 100_BLUE_repeaters_nationwide
    String name = "name_example"; // String | Super layer name eg. National_map
    try {
      apiInstance.mesh(network, name);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyseApi#mesh");
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
| **network** | **String**| Network name eg. 100_BLUE_repeaters_nationwide | |
| **name** | **String**| Super layer name eg. National_map | |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request OK |  -  |

<a id="network"></a>
# **network**
> network(net, nam, lat, lon, alt, rxg)

Find the best server for somewhere

Query your network to find the best server(s) for a given receiver/customer location. A previously generated network is required.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AnalyseApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.cloudrf.com");
    
    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    AnalyseApi apiInstance = new AnalyseApi(defaultClient);
    String net = "net_example"; // String | Network name
    String nam = "nam_example"; // String | Super layer name
    Float lat = 3.4F; // Float | Latitude in decimal degrees
    Float lon = 3.4F; // Float | Longitude in decimal degrees
    Integer alt = 56; // Integer | Height above ground level in metres
    Float rxg = 3.4F; // Float | Receiver gain in dBi
    try {
      apiInstance.network(net, nam, lat, lon, alt, rxg);
    } catch (ApiException e) {
      System.err.println("Exception when calling AnalyseApi#network");
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
| **net** | **String**| Network name | |
| **nam** | **String**| Super layer name | |
| **lat** | **Float**| Latitude in decimal degrees | |
| **lon** | **Float**| Longitude in decimal degrees | |
| **alt** | **Integer**| Height above ground level in metres | |
| **rxg** | **Float**| Receiver gain in dBi | [optional] |

### Return type

null (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request OK |  -  |

