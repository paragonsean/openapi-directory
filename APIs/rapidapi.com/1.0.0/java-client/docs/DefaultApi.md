# DefaultApi

All URIs are relative to *https://moon-phase.p.rapidapi.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAdvancedMoonPhaseData**](DefaultApi.md#getAdvancedMoonPhaseData) | **GET** /advanced | Get Advanced Moon Phase Data |
| [**getBasicMoonPhaseData**](DefaultApi.md#getBasicMoonPhaseData) | **GET** /basic | Get Basic Moon Phase Data |
| [**getEmojiOfMoonPhase**](DefaultApi.md#getEmojiOfMoonPhase) | **GET** /emoji | Get Emoji of Moon Phase |
| [**getLunarCalendar**](DefaultApi.md#getLunarCalendar) | **GET** /calendar | Get Lunar Calendar |
| [**getPlainTextMoonPhaseData**](DefaultApi.md#getPlainTextMoonPhaseData) | **GET** /plain-text | Get Plain Text Moon Phase Data |


<a id="getAdvancedMoonPhaseData"></a>
# **getAdvancedMoonPhaseData**
> GetAdvancedMoonPhaseData200Response getAdvancedMoonPhaseData(filters, xRapidapiKey)

Get Advanced Moon Phase Data

Get Advanced Moon Phase Data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://moon-phase.p.rapidapi.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String filters = "moon.phase_name,moon.stage,moon_phases.full_moon.next"; // String | Filter data in the Advanced Moon API by specifying the desired fields using the `filters` parameter in the request. Include a comma-separated list of keys to retrieve customized data, allowing you to fetch specific moon phase information and related details.
    String xRapidapiKey = "{{Rapidapi-Key}}"; // String | 
    try {
      GetAdvancedMoonPhaseData200Response result = apiInstance.getAdvancedMoonPhaseData(filters, xRapidapiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getAdvancedMoonPhaseData");
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
| **filters** | **String**| Filter data in the Advanced Moon API by specifying the desired fields using the &#x60;filters&#x60; parameter in the request. Include a comma-separated list of keys to retrieve customized data, allowing you to fetch specific moon phase information and related details. | [optional] |
| **xRapidapiKey** | **String**|  | [optional] |

### Return type

[**GetAdvancedMoonPhaseData200Response**](GetAdvancedMoonPhaseData200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Advanced Moon Phase Data |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * alt-svc -  <br>  |

<a id="getBasicMoonPhaseData"></a>
# **getBasicMoonPhaseData**
> GetBasicMoonPhaseData200Response getBasicMoonPhaseData(xRapidapiKey)

Get Basic Moon Phase Data

Get Basic Moon Phase Data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://moon-phase.p.rapidapi.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xRapidapiKey = "{{Rapidapi-Key}}"; // String | 
    try {
      GetBasicMoonPhaseData200Response result = apiInstance.getBasicMoonPhaseData(xRapidapiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getBasicMoonPhaseData");
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
| **xRapidapiKey** | **String**|  | [optional] |

### Return type

[**GetBasicMoonPhaseData200Response**](GetBasicMoonPhaseData200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Basic Moon Phase Data |  * Access-Control-Allow-Origin -  <br>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Tk -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Cache -  <br>  * alt-svc -  <br>  |

<a id="getEmojiOfMoonPhase"></a>
# **getEmojiOfMoonPhase**
> getEmojiOfMoonPhase(xRapidapiKey)

Get Emoji of Moon Phase

Get Emoji of Moon Phase

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://moon-phase.p.rapidapi.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xRapidapiKey = "{{Rapidapi-Key}}"; // String | 
    try {
      apiInstance.getEmojiOfMoonPhase(xRapidapiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getEmojiOfMoonPhase");
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
| **xRapidapiKey** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Emoji of Moon Phase |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * alt-svc -  <br>  |

<a id="getLunarCalendar"></a>
# **getLunarCalendar**
> getLunarCalendar(filters, xRapidapiKey)

Get Lunar Calendar

Get Lunar Calendar

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://moon-phase.p.rapidapi.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String filters = "moon.phase_name,moon.stage,moon_phases.full_moon.next"; // String | Filter data in the Advanced Moon API by specifying the desired fields using the `filters` parameter in the request. Include a comma-separated list of keys to retrieve customized data, allowing you to fetch specific moon phase information and related details.
    String xRapidapiKey = "{{Rapidapi-Key}}"; // String | 
    try {
      apiInstance.getLunarCalendar(filters, xRapidapiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getLunarCalendar");
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
| **filters** | **String**| Filter data in the Advanced Moon API by specifying the desired fields using the &#x60;filters&#x60; parameter in the request. Include a comma-separated list of keys to retrieve customized data, allowing you to fetch specific moon phase information and related details. | [optional] |
| **xRapidapiKey** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Lunar Calendar |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Cache-Control -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * alt-svc -  <br>  |

<a id="getPlainTextMoonPhaseData"></a>
# **getPlainTextMoonPhaseData**
> getPlainTextMoonPhaseData(xRapidapiKey)

Get Plain Text Moon Phase Data

Get Plain Text Moon Phase Data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://moon-phase.p.rapidapi.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String xRapidapiKey = "{{Rapidapi-Key}}"; // String | 
    try {
      apiInstance.getPlainTextMoonPhaseData(xRapidapiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getPlainTextMoonPhaseData");
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
| **xRapidapiKey** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Get Plain Text Moon Phase Data |  * Access-Control-Allow-Origin -  <br>  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Date -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Tk -  <br>  * Transfer-Encoding -  <br>  * Vary -  <br>  * X-Cache -  <br>  * X-RapidAPI-Region -  <br>  * X-RapidAPI-Version -  <br>  * alt-svc -  <br>  |

