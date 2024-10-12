# SpinApi

All URIs are relative to *https://spinitron.com/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**spinsGet**](SpinApi.md#spinsGet) | **GET** /spins | Returns spins optionally filtered by {start} and/or {end} datetimes |
| [**spinsIdGet**](SpinApi.md#spinsIdGet) | **GET** /spins/{id} | Get a Spin by id |
| [**spinsPost**](SpinApi.md#spinsPost) | **POST** /spins | Log a Spin |


<a id="spinsGet"></a>
# **spinsGet**
> SpinsGet200Response spinsGet(start, end, playlistId, showId, count, page, fields, expand)

Returns spins optionally filtered by {start} and/or {end} datetimes

Get Spins optionally filtered by a datetime range. Only past Spins will be returned. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpinApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://spinitron.com/api");
    
    // Configure API key authorization: accessToken
    ApiKeyAuth accessToken = (ApiKeyAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //accessToken.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: httpBearer
    HttpBearerAuth httpBearer = (HttpBearerAuth) defaultClient.getAuthentication("httpBearer");
    httpBearer.setBearerToken("BEARER TOKEN");

    SpinApi apiInstance = new SpinApi(defaultClient);
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | The datetime starting from items must be returned. 
    OffsetDateTime end = OffsetDateTime.now(); // OffsetDateTime | The ending datetime. 
    Integer playlistId = 56; // Integer | Filter by playlist
    Integer showId = 56; // Integer | Filter by show
    Integer count = 20; // Integer | Amount of items to return
    Integer page = 56; // Integer | Offset, used together with count
    List<String> fields = Arrays.asList(); // List<String> | Allows to select only needed fields
    List<String> expand = Arrays.asList(); // List<String> | Allows to select extra fields
    try {
      SpinsGet200Response result = apiInstance.spinsGet(start, end, playlistId, showId, count, page, fields, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpinApi#spinsGet");
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
| **start** | **OffsetDateTime**| The datetime starting from items must be returned.  | [optional] |
| **end** | **OffsetDateTime**| The ending datetime.  | [optional] |
| **playlistId** | **Integer**| Filter by playlist | [optional] |
| **showId** | **Integer**| Filter by show | [optional] |
| **count** | **Integer**| Amount of items to return | [optional] [default to 20] |
| **page** | **Integer**| Offset, used together with count | [optional] |
| **fields** | [**List&lt;String&gt;**](String.md)| Allows to select only needed fields | [optional] |
| **expand** | [**List&lt;String&gt;**](String.md)| Allows to select extra fields | [optional] |

### Return type

[**SpinsGet200Response**](SpinsGet200Response.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The spins |  -  |

<a id="spinsIdGet"></a>
# **spinsIdGet**
> Spin spinsIdGet(id, fields, expand)

Get a Spin by id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpinApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://spinitron.com/api");
    
    // Configure API key authorization: accessToken
    ApiKeyAuth accessToken = (ApiKeyAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //accessToken.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: httpBearer
    HttpBearerAuth httpBearer = (HttpBearerAuth) defaultClient.getAuthentication("httpBearer");
    httpBearer.setBearerToken("BEARER TOKEN");

    SpinApi apiInstance = new SpinApi(defaultClient);
    Integer id = 56; // Integer | 
    List<String> fields = Arrays.asList(); // List<String> | Allows to select only needed fields
    List<String> expand = Arrays.asList(); // List<String> | Allows to select extra fields
    try {
      Spin result = apiInstance.spinsIdGet(id, fields, expand);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpinApi#spinsIdGet");
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
| **id** | **Integer**|  | |
| **fields** | [**List&lt;String&gt;**](String.md)| Allows to select only needed fields | [optional] |
| **expand** | [**List&lt;String&gt;**](String.md)| Allows to select extra fields | [optional] |

### Return type

[**Spin**](Spin.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The spin |  -  |
| **404** | Spin not found |  -  |

<a id="spinsPost"></a>
# **spinsPost**
> Spin spinsPost(artist, song, composer, duration, genre, isrc, label, live, release, start)

Log a Spin

An endpoint for automation systems to log spins into the spin table.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SpinApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://spinitron.com/api");
    
    // Configure API key authorization: accessToken
    ApiKeyAuth accessToken = (ApiKeyAuth) defaultClient.getAuthentication("accessToken");
    accessToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //accessToken.setApiKeyPrefix("Token");

    // Configure HTTP bearer authorization: httpBearer
    HttpBearerAuth httpBearer = (HttpBearerAuth) defaultClient.getAuthentication("httpBearer");
    httpBearer.setBearerToken("BEARER TOKEN");

    SpinApi apiInstance = new SpinApi(defaultClient);
    String artist = "artist_example"; // String | 
    String song = "song_example"; // String | 
    String composer = "composer_example"; // String | 
    Integer duration = 56; // Integer | 
    String genre = "genre_example"; // String | 
    String isrc = "isrc_example"; // String | 
    String label = "label_example"; // String | 
    Boolean live = true; // Boolean | Only when automation params are configured with the \\\"Pass through\\\" mode. Enables \\\"live assist\\\" mode. Default mode is \\\"full automation\\\". 
    String release = "release_example"; // String | 
    OffsetDateTime start = OffsetDateTime.now(); // OffsetDateTime | 
    try {
      Spin result = apiInstance.spinsPost(artist, song, composer, duration, genre, isrc, label, live, release, start);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SpinApi#spinsPost");
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
| **artist** | **String**|  | |
| **song** | **String**|  | |
| **composer** | **String**|  | [optional] |
| **duration** | **Integer**|  | [optional] |
| **genre** | **String**|  | [optional] |
| **isrc** | **String**|  | [optional] |
| **label** | **String**|  | [optional] |
| **live** | **Boolean**| Only when automation params are configured with the \\\&quot;Pass through\\\&quot; mode. Enables \\\&quot;live assist\\\&quot; mode. Default mode is \\\&quot;full automation\\\&quot;.  | [optional] |
| **release** | **String**|  | [optional] |
| **start** | **OffsetDateTime**|  | [optional] |

### Return type

[**Spin**](Spin.md)

### Authorization

[accessToken](../README.md#accessToken), [httpBearer](../README.md#httpBearer)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | The new created Spin. |  -  |
| **422** | Validation failed. |  -  |
| **0** | Failed to create the object for unknown reason. |  -  |

