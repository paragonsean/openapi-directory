# CustomMusicApi

All URIs are relative to *https://api.shutterstock.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createAudioRenders**](CustomMusicApi.md#createAudioRenders) | **POST** /v2/ai/audio/renders | Create rendered audio |
| [**fetchRenders**](CustomMusicApi.md#fetchRenders) | **GET** /v2/ai/audio/renders | Get details about audio renders |
| [**listCustomDescriptors**](CustomMusicApi.md#listCustomDescriptors) | **GET** /v2/ai/audio/descriptors | List computer audio descriptors |
| [**listCustomInstruments**](CustomMusicApi.md#listCustomInstruments) | **GET** /v2/ai/audio/instruments | List computer audio instruments |


<a id="createAudioRenders"></a>
# **createAudioRenders**
> AudioRendersListResults createAudioRenders(createAudioRendersRequest)

Create rendered audio

This endpoint creates rendered audio from timeline data. It returns a render ID that you can use to download the finished audio when it is ready. The render ID is valid for up to 48 hours.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomMusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    CustomMusicApi apiInstance = new CustomMusicApi(defaultClient);
    CreateAudioRendersRequest createAudioRendersRequest = new CreateAudioRendersRequest(); // CreateAudioRendersRequest | Parameters for the audio, including the timeline and information about the output file
    try {
      AudioRendersListResults result = apiInstance.createAudioRenders(createAudioRendersRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomMusicApi#createAudioRenders");
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
| **createAudioRendersRequest** | [**CreateAudioRendersRequest**](CreateAudioRendersRequest.md)| Parameters for the audio, including the timeline and information about the output file | |

### Return type

[**AudioRendersListResults**](AudioRendersListResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

<a id="fetchRenders"></a>
# **fetchRenders**
> AudioRendersListResults fetchRenders(id)

Get details about audio renders

This endpoint shows the status of one or more audio renders, including download links for completed audio.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomMusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    CustomMusicApi apiInstance = new CustomMusicApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | One or more render IDs
    try {
      AudioRendersListResults result = apiInstance.fetchRenders(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomMusicApi#fetchRenders");
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
| **id** | [**List&lt;String&gt;**](String.md)| One or more render IDs | |

### Return type

[**AudioRendersListResults**](AudioRendersListResults.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="listCustomDescriptors"></a>
# **listCustomDescriptors**
> DescriptorsListResult listCustomDescriptors(renderSpeedOver, bandId, bandName, page, perPage, id, instrumentName, instrumentId, tempo, tempoTo, tempoFrom, name, tag)

List computer audio descriptors

This endpoint lists the descriptors that you can use in the audio regions in an audio render.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomMusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    CustomMusicApi apiInstance = new CustomMusicApi(defaultClient);
    BigDecimal renderSpeedOver = new BigDecimal("5"); // BigDecimal | Show descriptors with an average render speed that is greater than or equal to the specified value
    String bandId = "Corporate Folk Bonfire Band 1"; // String | Show descriptors that contain the specified band (case-sentsitive)
    String bandName = "Documentary Underscore Heartfelt Band 1"; // String | Show descriptors with the specified band name (case-sensitive)
    Integer page = 1; // Integer | Page number
    Integer perPage = 20; // Integer | Number of results per page
    List<String> id = Arrays.asList(); // List<String> | Show descriptors with the specified IDs (case-sensitive)
    String instrumentName = "Precision Bass - Full"; // String | Show descriptors with the specified instrument name (case-sensitive)
    String instrumentId = "direct_fluorescent_synth_lead"; // String | Show descriptors with the specified instrument ID (case-sensitive)
    BigDecimal tempo = new BigDecimal("90"); // BigDecimal | Show descriptors whose tempo range includes the specified tempo in beats per minute
    BigDecimal tempoTo = new BigDecimal("120"); // BigDecimal | Show descriptors with a tempo that is less than or equal to the specified number
    BigDecimal tempoFrom = new BigDecimal("60"); // BigDecimal | Show descriptors that have a tempo range that includes the specified tempo in beats per minute
    String name = "Corporate Pop Inspirational High Energy"; // String | Show descriptors with the specified name (case-sensitive)
    String tag = "Cinematic"; // String | Show descriptors with the specified tag, such as Cinematic or Roomy (case-sensitive)
    try {
      DescriptorsListResult result = apiInstance.listCustomDescriptors(renderSpeedOver, bandId, bandName, page, perPage, id, instrumentName, instrumentId, tempo, tempoTo, tempoFrom, name, tag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomMusicApi#listCustomDescriptors");
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
| **renderSpeedOver** | **BigDecimal**| Show descriptors with an average render speed that is greater than or equal to the specified value | [optional] |
| **bandId** | **String**| Show descriptors that contain the specified band (case-sentsitive) | [optional] |
| **bandName** | **String**| Show descriptors with the specified band name (case-sensitive) | [optional] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **id** | [**List&lt;String&gt;**](String.md)| Show descriptors with the specified IDs (case-sensitive) | [optional] |
| **instrumentName** | **String**| Show descriptors with the specified instrument name (case-sensitive) | [optional] |
| **instrumentId** | **String**| Show descriptors with the specified instrument ID (case-sensitive) | [optional] |
| **tempo** | **BigDecimal**| Show descriptors whose tempo range includes the specified tempo in beats per minute | [optional] |
| **tempoTo** | **BigDecimal**| Show descriptors with a tempo that is less than or equal to the specified number | [optional] |
| **tempoFrom** | **BigDecimal**| Show descriptors that have a tempo range that includes the specified tempo in beats per minute | [optional] |
| **name** | **String**| Show descriptors with the specified name (case-sensitive) | [optional] |
| **tag** | **String**| Show descriptors with the specified tag, such as Cinematic or Roomy (case-sensitive) | [optional] |

### Return type

[**DescriptorsListResult**](DescriptorsListResult.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="listCustomInstruments"></a>
# **listCustomInstruments**
> InstrumentsListResult listCustomInstruments(id, perPage, page, name, tag)

List computer audio instruments

This endpoint lists the instruments that you can include in computer audio. If you specify more than one search parameter, the API uses an AND condition.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CustomMusicApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.shutterstock.com");
    
    // Configure OAuth2 access token for authorization: customer_accessCode
    OAuth customer_accessCode = (OAuth) defaultClient.getAuthentication("customer_accessCode");
    customer_accessCode.setAccessToken("YOUR ACCESS TOKEN");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    CustomMusicApi apiInstance = new CustomMusicApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Show instruments with the specified ID
    Integer perPage = 20; // Integer | Number of results per page
    Integer page = 1; // Integer | Page number
    String name = "Precision Bass - Full"; // String | Show instruments with the specified name (case-sensitive)
    String tag = "Percussion"; // String | Show instruments with the specified tag, such as Percussion or Strings (case-sensitive)
    try {
      InstrumentsListResult result = apiInstance.listCustomInstruments(id, perPage, page, name, tag);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CustomMusicApi#listCustomInstruments");
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
| **id** | [**List&lt;String&gt;**](String.md)| Show instruments with the specified ID | [optional] |
| **perPage** | **Integer**| Number of results per page | [optional] [default to 20] |
| **page** | **Integer**| Page number | [optional] [default to 1] |
| **name** | **String**| Show instruments with the specified name (case-sensitive) | [optional] |
| **tag** | **String**| Show instruments with the specified tag, such as Percussion or Strings (case-sensitive) | [optional] |

### Return type

[**InstrumentsListResult**](InstrumentsListResult.md)

### Authorization

[customer_accessCode](../README.md#customer_accessCode), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |

