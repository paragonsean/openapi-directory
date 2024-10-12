# DefaultApi

All URIs are relative to *https://api.bigdatacloud.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**ipGeolocationWithConfidenceAreaAndHazardReportApi**](DefaultApi.md#ipGeolocationWithConfidenceAreaAndHazardReportApi) | **GET** /data/ip-geolocation-full | IP Geolocation with Confidence Area and Hazard Report API |
| [**ipGeolocationWithConfidenceAreaApi**](DefaultApi.md#ipGeolocationWithConfidenceAreaApi) | **GET** /data/ip-geolocation-with-confidence | IP Geolocation with Confidence Area API |


<a id="ipGeolocationWithConfidenceAreaAndHazardReportApi"></a>
# **ipGeolocationWithConfidenceAreaAndHazardReportApi**
> ipGeolocationWithConfidenceAreaAndHazardReportApi(ip, localityLanguage, key)

IP Geolocation with Confidence Area and Hazard Report API

This API returns additional security hazard report in addition to confidence area and locality information.

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
    defaultClient.setBasePath("https://api.bigdatacloud.net");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ip = "193.114.112.122"; // String | IPv4 IP address in a string or numeric format. If omitted, the caller’s IP address is assumed 
    String localityLanguage = "en"; // String | Preferred language for locality names in ISO 639-1 format, such as 'en' for English, 'es' for Spanish etc. Please note: 147 common world languages are supported, full list here, but not all languages are available for every location. If requested language is not available for a requested location it will default to English, if no English is available, the native, local names will be provided 
    String key = "{{API KEY}}"; // String | Your API key 
    try {
      apiInstance.ipGeolocationWithConfidenceAreaAndHazardReportApi(ip, localityLanguage, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipGeolocationWithConfidenceAreaAndHazardReportApi");
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
| **ip** | **String**| IPv4 IP address in a string or numeric format. If omitted, the caller’s IP address is assumed  | [optional] |
| **localityLanguage** | **String**| Preferred language for locality names in ISO 639-1 format, such as &#39;en&#39; for English, &#39;es&#39; for Spanish etc. Please note: 147 common world languages are supported, full list here, but not all languages are available for every location. If requested language is not available for a requested location it will default to English, if no English is available, the native, local names will be provided  | [optional] |
| **key** | **String**| Your API key  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ipGeolocationWithConfidenceAreaApi"></a>
# **ipGeolocationWithConfidenceAreaApi**
> ipGeolocationWithConfidenceAreaApi(ip, localityLanguage, key)

IP Geolocation with Confidence Area API

Returns list of geocoordinates which represents estimated geolocation confidence area.

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
    defaultClient.setBasePath("https://api.bigdatacloud.net");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ip = "193.114.112.122"; // String | IPv4 IP address in a string or numeric format. If omitted, the caller’s IP address is assumed 
    String localityLanguage = "en"; // String | Preferred language for locality names in ISO 639-1 format, such as 'en' for English, 'es' for Spanish etc. Please note: 147 common world languages are supported, full list here, but not all languages are available for every location. If requested language is not available for a requested location it will default to English, if no English is available, the native, local names will be provided 
    String key = "{{API KEY}}"; // String | Your API key 
    try {
      apiInstance.ipGeolocationWithConfidenceAreaApi(ip, localityLanguage, key);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#ipGeolocationWithConfidenceAreaApi");
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
| **ip** | **String**| IPv4 IP address in a string or numeric format. If omitted, the caller’s IP address is assumed  | [optional] |
| **localityLanguage** | **String**| Preferred language for locality names in ISO 639-1 format, such as &#39;en&#39; for English, &#39;es&#39; for Spanish etc. Please note: 147 common world languages are supported, full list here, but not all languages are available for every location. If requested language is not available for a requested location it will default to English, if no English is available, the native, local names will be provided  | [optional] |
| **key** | **String**| Your API key  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

