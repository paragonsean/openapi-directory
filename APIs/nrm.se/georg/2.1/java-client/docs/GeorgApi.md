# GeorgApi

All URIs are relative to *http://localhost/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**autoComplete**](GeorgApi.md#autoComplete) | **GET** /autocomplete | Search |
| [**getReverseGeoCode**](GeorgApi.md#getReverseGeoCode) | **GET** /reverse | Get reverse geocoding |
| [**search**](GeorgApi.md#search) | **GET** /search | Get geocoding |
| [**searchCoordinates**](GeorgApi.md#searchCoordinates) | **GET** /coordinates | Search coordinates in different formate |
| [**uploadFile**](GeorgApi.md#uploadFile) | **POST** /upload | Batch upload |


<a id="autoComplete"></a>
# **autoComplete**
> String autoComplete(text, sources, layers, countryCode, size)

Search

Return search results in json

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeorgApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/api");

    GeorgApi apiInstance = new GeorgApi(defaultClient);
    String text = "text_example"; // String | 
    String sources = "sources_example"; // String | 
    String layers = "layers_example"; // String | 
    String countryCode = "countryCode_example"; // String | 
    Integer size = 56; // Integer | 
    try {
      String result = apiInstance.autoComplete(text, sources, layers, countryCode, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeorgApi#autoComplete");
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
| **text** | **String**|  | [optional] |
| **sources** | **String**|  | [optional] |
| **layers** | **String**|  | [optional] |
| **countryCode** | **String**|  | [optional] |
| **size** | **Integer**|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="getReverseGeoCode"></a>
# **getReverseGeoCode**
> String getReverseGeoCode(lat, lng)

Get reverse geocoding

Return search results in json

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeorgApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/api");

    GeorgApi apiInstance = new GeorgApi(defaultClient);
    Double lat = 3.4D; // Double | 
    Double lng = 3.4D; // Double | 
    try {
      String result = apiInstance.getReverseGeoCode(lat, lng);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeorgApi#getReverseGeoCode");
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
| **lat** | **Double**|  | [optional] |
| **lng** | **Double**|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="search"></a>
# **search**
> String search(text, sources, layers, countryCode, size)

Get geocoding

Return search results in json

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeorgApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/api");

    GeorgApi apiInstance = new GeorgApi(defaultClient);
    String text = "text_example"; // String | 
    String sources = "sources_example"; // String | 
    String layers = "layers_example"; // String | 
    String countryCode = "countryCode_example"; // String | 
    Integer size = 56; // Integer | 
    try {
      String result = apiInstance.search(text, sources, layers, countryCode, size);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeorgApi#search");
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
| **text** | **String**|  | [optional] |
| **sources** | **String**|  | [optional] |
| **layers** | **String**|  | [optional] |
| **countryCode** | **String**|  | [optional] |
| **size** | **Integer**|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="searchCoordinates"></a>
# **searchCoordinates**
> String searchCoordinates(coordinates)

Search coordinates in different formate

Return search results in json

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeorgApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/api");

    GeorgApi apiInstance = new GeorgApi(defaultClient);
    String coordinates = "coordinates_example"; // String | 
    try {
      String result = apiInstance.searchCoordinates(coordinates);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeorgApi#searchCoordinates");
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
| **coordinates** | **String**|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |

<a id="uploadFile"></a>
# **uploadFile**
> uploadFile(type, formData, formDataMap, parts, preamble)

Batch upload

Upload csv file with minimum two columns (Id, SourceLocality). Return search results in json

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GeorgApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost/api");

    GeorgApi apiInstance = new GeorgApi(defaultClient);
    String type = "type_example"; // String | 
    Map<String, InputPart> formData = new HashMap(); // Map<String, InputPart> | 
    Map<String, List<InputPart>> formDataMap = new HashMap(); // Map<String, List<InputPart>> | 
    List<InputPart> parts = Arrays.asList(); // List<InputPart> | 
    String preamble = "preamble_example"; // String | 
    try {
      apiInstance.uploadFile(type, formData, formDataMap, parts, preamble);
    } catch (ApiException e) {
      System.err.println("Exception when calling GeorgApi#uploadFile");
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
| **type** | **String**|  | [optional] |
| **formData** | [**Map&lt;String, InputPart&gt;**](Map.md)|  | [optional] |
| **formDataMap** | [**Map&lt;String, List&lt;InputPart&gt;&gt;**](Map.md)|  | [optional] |
| **parts** | [**List&lt;InputPart&gt;**](InputPart.md)|  | [optional] |
| **preamble** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | File uploaded |  -  |

