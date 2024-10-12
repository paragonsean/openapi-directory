# ArtistApi

All URIs are relative to *https://api.musixmatch.com/ws/1.1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**artistGetGet**](ArtistApi.md#artistGetGet) | **GET** /artist.get |  |
| [**artistRelatedGetGet**](ArtistApi.md#artistRelatedGetGet) | **GET** /artist.related.get |  |
| [**artistSearchGet**](ArtistApi.md#artistSearchGet) | **GET** /artist.search |  |
| [**chartArtistsGetGet**](ArtistApi.md#chartArtistsGetGet) | **GET** /chart.artists.get |  |


<a id="artistGetGet"></a>
# **artistGetGet**
> ArtistGetGet200Response artistGetGet(artistId, format, paramCallback)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    ArtistApi apiInstance = new ArtistApi(defaultClient);
    String artistId = "artistId_example"; // String |  The musiXmatch artist id
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    try {
      ArtistGetGet200Response result = apiInstance.artistGetGet(artistId, format, paramCallback);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtistApi#artistGetGet");
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
| **artistId** | **String**|  The musiXmatch artist id | |
| **format** | **String**| output format: json, jsonp, xml. | [optional] [default to json] |
| **paramCallback** | **String**| jsonp callback | [optional] |

### Return type

[**ArtistGetGet200Response**](ArtistGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

<a id="artistRelatedGetGet"></a>
# **artistRelatedGetGet**
> ArtistRelatedGetGet200Response artistRelatedGetGet(artistId, format, paramCallback, pageSize, page)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    ArtistApi apiInstance = new ArtistApi(defaultClient);
    String artistId = "artistId_example"; // String | The musiXmatch artist id
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    BigDecimal pageSize = new BigDecimal(78); // BigDecimal | Define the page size for paginated results.Range is 1 to 100.
    BigDecimal page = new BigDecimal(78); // BigDecimal | Define the page number for paginated results
    try {
      ArtistRelatedGetGet200Response result = apiInstance.artistRelatedGetGet(artistId, format, paramCallback, pageSize, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtistApi#artistRelatedGetGet");
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
| **artistId** | **String**| The musiXmatch artist id | |
| **format** | **String**| output format: json, jsonp, xml. | [optional] [default to json] |
| **paramCallback** | **String**| jsonp callback | [optional] |
| **pageSize** | **BigDecimal**| Define the page size for paginated results.Range is 1 to 100. | [optional] |
| **page** | **BigDecimal**| Define the page number for paginated results | [optional] |

### Return type

[**ArtistRelatedGetGet200Response**](ArtistRelatedGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

<a id="artistSearchGet"></a>
# **artistSearchGet**
> ArtistRelatedGetGet200Response artistSearchGet(format, paramCallback, qArtist, fArtistId, page, pageSize)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    ArtistApi apiInstance = new ArtistApi(defaultClient);
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    String qArtist = "qArtist_example"; // String | The song artist
    BigDecimal fArtistId = new BigDecimal(78); // BigDecimal | When set, filter by this artist id
    BigDecimal page = new BigDecimal(78); // BigDecimal | Define the page number for paginated results
    BigDecimal pageSize = new BigDecimal(78); // BigDecimal | Define the page size for paginated results.Range is 1 to 100.
    try {
      ArtistRelatedGetGet200Response result = apiInstance.artistSearchGet(format, paramCallback, qArtist, fArtistId, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtistApi#artistSearchGet");
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
| **format** | **String**| output format: json, jsonp, xml. | [optional] [default to json] |
| **paramCallback** | **String**| jsonp callback | [optional] |
| **qArtist** | **String**| The song artist | [optional] |
| **fArtistId** | **BigDecimal**| When set, filter by this artist id | [optional] |
| **page** | **BigDecimal**| Define the page number for paginated results | [optional] |
| **pageSize** | **BigDecimal**| Define the page size for paginated results.Range is 1 to 100. | [optional] |

### Return type

[**ArtistRelatedGetGet200Response**](ArtistRelatedGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

<a id="chartArtistsGetGet"></a>
# **chartArtistsGetGet**
> ChartArtistsGetGet200Response chartArtistsGetGet(format, paramCallback, page, pageSize, country)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ArtistApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.musixmatch.com/ws/1.1");
    
    // Configure API key authorization: key
    ApiKeyAuth key = (ApiKeyAuth) defaultClient.getAuthentication("key");
    key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //key.setApiKeyPrefix("Token");

    ArtistApi apiInstance = new ArtistApi(defaultClient);
    String format = "json"; // String | output format: json, jsonp, xml.
    String paramCallback = "paramCallback_example"; // String | jsonp callback
    BigDecimal page = new BigDecimal(78); // BigDecimal | Define the page number for paginated results
    BigDecimal pageSize = new BigDecimal(78); // BigDecimal | Define the page size for paginated results.Range is 1 to 100.
    String country = "us"; // String | A valid ISO 3166 country code
    try {
      ChartArtistsGetGet200Response result = apiInstance.chartArtistsGetGet(format, paramCallback, page, pageSize, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ArtistApi#chartArtistsGetGet");
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
| **format** | **String**| output format: json, jsonp, xml. | [optional] [default to json] |
| **paramCallback** | **String**| jsonp callback | [optional] |
| **page** | **BigDecimal**| Define the page number for paginated results | [optional] |
| **pageSize** | **BigDecimal**| Define the page size for paginated results.Range is 1 to 100. | [optional] |
| **country** | **String**| A valid ISO 3166 country code | [optional] [default to us] |

### Return type

[**ChartArtistsGetGet200Response**](ChartArtistsGetGet200Response.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The request was successful. |  -  |

