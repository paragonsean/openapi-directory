# MarkerApi

All URIs are relative to *https://api.redirection.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deleteMarkerItem**](MarkerApi.md#deleteMarkerItem) | **DELETE** /markers/{id} | Removes the Marker resource. |
| [**getMarkerItem**](MarkerApi.md#getMarkerItem) | **GET** /markers/{id} | Retrieves a Marker resource. |
| [**postMarkerCollection**](MarkerApi.md#postMarkerCollection) | **POST** /markers | Creates a Marker resource. |
| [**putMarkerItem**](MarkerApi.md#putMarkerItem) | **PUT** /markers/{id} | Replaces the Marker resource. |


<a id="deleteMarkerItem"></a>
# **deleteMarkerItem**
> deleteMarkerItem(id)

Removes the Marker resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarkerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    MarkerApi apiInstance = new MarkerApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteMarkerItem(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarkerApi#deleteMarkerItem");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Marker resource deleted |  -  |
| **404** | Resource not found |  -  |

<a id="getMarkerItem"></a>
# **getMarkerItem**
> Marker getMarkerItem(id)

Retrieves a Marker resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarkerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    MarkerApi apiInstance = new MarkerApi(defaultClient);
    String id = "id_example"; // String | 
    try {
      Marker result = apiInstance.getMarkerItem(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarkerApi#getMarkerItem");
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
| **id** | **String**|  | |

### Return type

[**Marker**](Marker.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Marker resource response |  -  |
| **404** | Resource not found |  -  |

<a id="postMarkerCollection"></a>
# **postMarkerCollection**
> Marker postMarkerCollection(marker)

Creates a Marker resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarkerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    MarkerApi apiInstance = new MarkerApi(defaultClient);
    MarkerWrite marker = new MarkerWrite(); // MarkerWrite | The new Marker resource
    try {
      Marker result = apiInstance.postMarkerCollection(marker);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarkerApi#postMarkerCollection");
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
| **marker** | [**MarkerWrite**](MarkerWrite.md)| The new Marker resource | [optional] |

### Return type

[**Marker**](Marker.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Marker resource created |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

<a id="putMarkerItem"></a>
# **putMarkerItem**
> Marker putMarkerItem(id, marker)

Replaces the Marker resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MarkerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.redirection.io");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    MarkerApi apiInstance = new MarkerApi(defaultClient);
    String id = "id_example"; // String | 
    Marker marker = new Marker(); // Marker | The updated Marker resource
    try {
      Marker result = apiInstance.putMarkerItem(id, marker);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MarkerApi#putMarkerItem");
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
| **id** | **String**|  | |
| **marker** | [**Marker**](Marker.md)| The updated Marker resource | [optional] |

### Return type

[**Marker**](Marker.md)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, text/html, text/csv
 - **Accept**: application/ld+json, application/json, text/html, text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Marker resource updated |  -  |
| **400** | Invalid input |  -  |
| **404** | Resource not found |  -  |

