# RecordersApi

All URIs are relative to *http://api.cambase.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1RecordersCreate**](RecordersApi.md#apiV1RecordersCreate) | **POST** /api/v1/recorders.json | Creates a new Recorder |
| [**apiV1RecordersIdJsonPatch**](RecordersApi.md#apiV1RecordersIdJsonPatch) | **PATCH** /api/v1/recorders/{id}.json | Updates an existing Recorder |
| [**apiV1RecordersIdJsonPut**](RecordersApi.md#apiV1RecordersIdJsonPut) | **PUT** /api/v1/recorders/{id}.json | Updates an existing Recorder |
| [**apiV1RecordersIndex**](RecordersApi.md#apiV1RecordersIndex) | **GET** /api/v1/recorders.json | Fetches all Recorders |
| [**apiV1RecordersSearch**](RecordersApi.md#apiV1RecordersSearch) | **GET** /api/v1/recorders/search.json | Searches all Recorders |
| [**apiV1RecordersShow**](RecordersApi.md#apiV1RecordersShow) | **GET** /api/v1/recorders/{id}.json | Fetches a single Recorder |


<a id="apiV1RecordersCreate"></a>
# **apiV1RecordersCreate**
> apiV1RecordersCreate(vendorId, recorderModel, recorderName, recorderRecorderType, recorderResolution, recorderOnvif, recorderPsia, recorderPtz, recorderDiscontinued, recorderSupport3rdparty, recorderSdCard, recorderUpnp, recorderHotSwap, recorderHdmi, recorderDigitalIo, recorderAudioIn, recorderAudioOut, recorderInputChannels, recorderPlaybackChannels, recorderUsb, recorderSdhc, recorderMobileAccess, recorderAlarms, recorderRaidSupport, recorderStorage, recorderAdditionalInformation, recorderDefaultUsername, recorderDefaultPassword, recorderJpegUrl, recorderH264Url, recorderMjpegUrl, recorderOfficialUrl)

Creates a new Recorder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    RecordersApi apiInstance = new RecordersApi(defaultClient);
    String vendorId = "vendorId_example"; // String | Vendor ID
    String recorderModel = "recorderModel_example"; // String | Model
    String recorderName = "recorderName_example"; // String | Name
    String recorderRecorderType = "recorderRecorderType_example"; // String | Type
    String recorderResolution = "recorderResolution_example"; // String | Resolution
    String recorderOnvif = "recorderOnvif_example"; // String | ONVIF
    String recorderPsia = "recorderPsia_example"; // String | PSIA
    String recorderPtz = "recorderPtz_example"; // String | PTZ
    String recorderDiscontinued = "recorderDiscontinued_example"; // String | Discontinued
    String recorderSupport3rdparty = "recorderSupport3rdparty_example"; // String | 3rd pparty Camera Support
    String recorderSdCard = "recorderSdCard_example"; // String | SD Card
    String recorderUpnp = "recorderUpnp_example"; // String | UPnP
    String recorderHotSwap = "recorderHotSwap_example"; // String | Hot Swap
    String recorderHdmi = "recorderHdmi_example"; // String | HDMI Support
    String recorderDigitalIo = "recorderDigitalIo_example"; // String | Digital I/O
    String recorderAudioIn = "recorderAudioIn_example"; // String | Audio In
    String recorderAudioOut = "recorderAudioOut_example"; // String | Audio Out
    String recorderInputChannels = "recorderInputChannels_example"; // String | Input Channels
    String recorderPlaybackChannels = "recorderPlaybackChannels_example"; // String | Playback Channels
    String recorderUsb = "recorderUsb_example"; // String | USB Ports
    String recorderSdhc = "recorderSdhc_example"; // String | SD Card (GB)
    String recorderMobileAccess = "recorderMobileAccess_example"; // String | Mobile Access
    String recorderAlarms = "recorderAlarms_example"; // String | Alarms
    String recorderRaidSupport = "recorderRaidSupport_example"; // String | Raid Support
    String recorderStorage = "recorderStorage_example"; // String | Internal Storage
    String recorderAdditionalInformation = "recorderAdditionalInformation_example"; // String | Additional Information
    String recorderDefaultUsername = "recorderDefaultUsername_example"; // String | Default Username
    String recorderDefaultPassword = "recorderDefaultPassword_example"; // String | Default Password
    String recorderJpegUrl = "recorderJpegUrl_example"; // String | JPEG URL
    String recorderH264Url = "recorderH264Url_example"; // String | H264 URL
    String recorderMjpegUrl = "recorderMjpegUrl_example"; // String | MJPEG URL
    String recorderOfficialUrl = "recorderOfficialUrl_example"; // String | Official URL
    try {
      apiInstance.apiV1RecordersCreate(vendorId, recorderModel, recorderName, recorderRecorderType, recorderResolution, recorderOnvif, recorderPsia, recorderPtz, recorderDiscontinued, recorderSupport3rdparty, recorderSdCard, recorderUpnp, recorderHotSwap, recorderHdmi, recorderDigitalIo, recorderAudioIn, recorderAudioOut, recorderInputChannels, recorderPlaybackChannels, recorderUsb, recorderSdhc, recorderMobileAccess, recorderAlarms, recorderRaidSupport, recorderStorage, recorderAdditionalInformation, recorderDefaultUsername, recorderDefaultPassword, recorderJpegUrl, recorderH264Url, recorderMjpegUrl, recorderOfficialUrl);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordersApi#apiV1RecordersCreate");
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
| **vendorId** | **String**| Vendor ID | |
| **recorderModel** | **String**| Model | |
| **recorderName** | **String**| Name | |
| **recorderRecorderType** | **String**| Type | |
| **recorderResolution** | **String**| Resolution | [optional] |
| **recorderOnvif** | **String**| ONVIF | [optional] |
| **recorderPsia** | **String**| PSIA | [optional] |
| **recorderPtz** | **String**| PTZ | [optional] |
| **recorderDiscontinued** | **String**| Discontinued | [optional] |
| **recorderSupport3rdparty** | **String**| 3rd pparty Camera Support | [optional] |
| **recorderSdCard** | **String**| SD Card | [optional] |
| **recorderUpnp** | **String**| UPnP | [optional] |
| **recorderHotSwap** | **String**| Hot Swap | [optional] |
| **recorderHdmi** | **String**| HDMI Support | [optional] |
| **recorderDigitalIo** | **String**| Digital I/O | [optional] |
| **recorderAudioIn** | **String**| Audio In | [optional] |
| **recorderAudioOut** | **String**| Audio Out | [optional] |
| **recorderInputChannels** | **String**| Input Channels | [optional] |
| **recorderPlaybackChannels** | **String**| Playback Channels | [optional] |
| **recorderUsb** | **String**| USB Ports | [optional] |
| **recorderSdhc** | **String**| SD Card (GB) | [optional] |
| **recorderMobileAccess** | **String**| Mobile Access | [optional] |
| **recorderAlarms** | **String**| Alarms | [optional] |
| **recorderRaidSupport** | **String**| Raid Support | [optional] |
| **recorderStorage** | **String**| Internal Storage | [optional] |
| **recorderAdditionalInformation** | **String**| Additional Information | [optional] |
| **recorderDefaultUsername** | **String**| Default Username | [optional] |
| **recorderDefaultPassword** | **String**| Default Password | [optional] |
| **recorderJpegUrl** | **String**| JPEG URL | [optional] |
| **recorderH264Url** | **String**| H264 URL | [optional] |
| **recorderMjpegUrl** | **String**| MJPEG URL | [optional] |
| **recorderOfficialUrl** | **String**| Official URL | [optional] |

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
| **200** | No response was specified |  -  |
| **401** | Unauthorized |  -  |
| **406** | Not Acceptable |  -  |

<a id="apiV1RecordersIdJsonPatch"></a>
# **apiV1RecordersIdJsonPatch**
> apiV1RecordersIdJsonPatch(id, vendorId, recorderModel, recorderName, recorderRecorderType, recorderResolution, recorderOnvif, recorderPsia, recorderPtz, recorderDiscontinued, recorderSupport3rdparty, recorderSdCard, recorderUpnp, recorderHotSwap, recorderHdmi, recorderDigitalIo, recorderAudioIn, recorderAudioOut, recorderInputChannels, recorderPlaybackChannels, recorderUsb, recorderSdhc, recorderMobileAccess, recorderAlarms, recorderRaidSupport, recorderStorage, recorderAdditionalInformation, recorderDefaultUsername, recorderDefaultPassword, recorderJpegUrl, recorderH264Url, recorderMjpegUrl, recorderOfficialUrl)

Updates an existing Recorder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    RecordersApi apiInstance = new RecordersApi(defaultClient);
    String id = "id_example"; // String | Recorder ID
    String vendorId = "vendorId_example"; // String | Vendor ID
    String recorderModel = "recorderModel_example"; // String | Model
    String recorderName = "recorderName_example"; // String | Name
    String recorderRecorderType = "recorderRecorderType_example"; // String | Type
    String recorderResolution = "recorderResolution_example"; // String | Resolution
    String recorderOnvif = "recorderOnvif_example"; // String | ONVIF
    String recorderPsia = "recorderPsia_example"; // String | PSIA
    String recorderPtz = "recorderPtz_example"; // String | PTZ
    String recorderDiscontinued = "recorderDiscontinued_example"; // String | Discontinued
    String recorderSupport3rdparty = "recorderSupport3rdparty_example"; // String | 3rd pparty Camera Support
    String recorderSdCard = "recorderSdCard_example"; // String | SD Card
    String recorderUpnp = "recorderUpnp_example"; // String | UPnP
    String recorderHotSwap = "recorderHotSwap_example"; // String | Hot Swap
    String recorderHdmi = "recorderHdmi_example"; // String | HDMI Support
    String recorderDigitalIo = "recorderDigitalIo_example"; // String | Digital I/O
    String recorderAudioIn = "recorderAudioIn_example"; // String | Audio In
    String recorderAudioOut = "recorderAudioOut_example"; // String | Audio Out
    String recorderInputChannels = "recorderInputChannels_example"; // String | Input Channels
    String recorderPlaybackChannels = "recorderPlaybackChannels_example"; // String | Playback Channels
    String recorderUsb = "recorderUsb_example"; // String | USB Ports
    String recorderSdhc = "recorderSdhc_example"; // String | SD Card (GB)
    String recorderMobileAccess = "recorderMobileAccess_example"; // String | Mobile Access
    String recorderAlarms = "recorderAlarms_example"; // String | Alarms
    String recorderRaidSupport = "recorderRaidSupport_example"; // String | Raid Support
    String recorderStorage = "recorderStorage_example"; // String | Internal Storage
    String recorderAdditionalInformation = "recorderAdditionalInformation_example"; // String | Additional Information
    String recorderDefaultUsername = "recorderDefaultUsername_example"; // String | Default Username
    String recorderDefaultPassword = "recorderDefaultPassword_example"; // String | Default Password
    String recorderJpegUrl = "recorderJpegUrl_example"; // String | JPEG URL
    String recorderH264Url = "recorderH264Url_example"; // String | H264 URL
    String recorderMjpegUrl = "recorderMjpegUrl_example"; // String | MJPEG URL
    String recorderOfficialUrl = "recorderOfficialUrl_example"; // String | Official URL
    try {
      apiInstance.apiV1RecordersIdJsonPatch(id, vendorId, recorderModel, recorderName, recorderRecorderType, recorderResolution, recorderOnvif, recorderPsia, recorderPtz, recorderDiscontinued, recorderSupport3rdparty, recorderSdCard, recorderUpnp, recorderHotSwap, recorderHdmi, recorderDigitalIo, recorderAudioIn, recorderAudioOut, recorderInputChannels, recorderPlaybackChannels, recorderUsb, recorderSdhc, recorderMobileAccess, recorderAlarms, recorderRaidSupport, recorderStorage, recorderAdditionalInformation, recorderDefaultUsername, recorderDefaultPassword, recorderJpegUrl, recorderH264Url, recorderMjpegUrl, recorderOfficialUrl);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordersApi#apiV1RecordersIdJsonPatch");
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
| **id** | **String**| Recorder ID | |
| **vendorId** | **String**| Vendor ID | |
| **recorderModel** | **String**| Model | |
| **recorderName** | **String**| Name | |
| **recorderRecorderType** | **String**| Type | |
| **recorderResolution** | **String**| Resolution | [optional] |
| **recorderOnvif** | **String**| ONVIF | [optional] |
| **recorderPsia** | **String**| PSIA | [optional] |
| **recorderPtz** | **String**| PTZ | [optional] |
| **recorderDiscontinued** | **String**| Discontinued | [optional] |
| **recorderSupport3rdparty** | **String**| 3rd pparty Camera Support | [optional] |
| **recorderSdCard** | **String**| SD Card | [optional] |
| **recorderUpnp** | **String**| UPnP | [optional] |
| **recorderHotSwap** | **String**| Hot Swap | [optional] |
| **recorderHdmi** | **String**| HDMI Support | [optional] |
| **recorderDigitalIo** | **String**| Digital I/O | [optional] |
| **recorderAudioIn** | **String**| Audio In | [optional] |
| **recorderAudioOut** | **String**| Audio Out | [optional] |
| **recorderInputChannels** | **String**| Input Channels | [optional] |
| **recorderPlaybackChannels** | **String**| Playback Channels | [optional] |
| **recorderUsb** | **String**| USB Ports | [optional] |
| **recorderSdhc** | **String**| SD Card (GB) | [optional] |
| **recorderMobileAccess** | **String**| Mobile Access | [optional] |
| **recorderAlarms** | **String**| Alarms | [optional] |
| **recorderRaidSupport** | **String**| Raid Support | [optional] |
| **recorderStorage** | **String**| Internal Storage | [optional] |
| **recorderAdditionalInformation** | **String**| Additional Information | [optional] |
| **recorderDefaultUsername** | **String**| Default Username | [optional] |
| **recorderDefaultPassword** | **String**| Default Password | [optional] |
| **recorderJpegUrl** | **String**| JPEG URL | [optional] |
| **recorderH264Url** | **String**| H264 URL | [optional] |
| **recorderMjpegUrl** | **String**| MJPEG URL | [optional] |
| **recorderOfficialUrl** | **String**| Official URL | [optional] |

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
| **200** | No response was specified |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="apiV1RecordersIdJsonPut"></a>
# **apiV1RecordersIdJsonPut**
> apiV1RecordersIdJsonPut(id, vendorId, recorderModel, recorderName, recorderRecorderType, recorderResolution, recorderOnvif, recorderPsia, recorderPtz, recorderDiscontinued, recorderSupport3rdparty, recorderSdCard, recorderUpnp, recorderHotSwap, recorderHdmi, recorderDigitalIo, recorderAudioIn, recorderAudioOut, recorderInputChannels, recorderPlaybackChannels, recorderUsb, recorderSdhc, recorderMobileAccess, recorderAlarms, recorderRaidSupport, recorderStorage, recorderAdditionalInformation, recorderDefaultUsername, recorderDefaultPassword, recorderJpegUrl, recorderH264Url, recorderMjpegUrl, recorderOfficialUrl)

Updates an existing Recorder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    RecordersApi apiInstance = new RecordersApi(defaultClient);
    String id = "id_example"; // String | Recorder ID
    String vendorId = "vendorId_example"; // String | Vendor ID
    String recorderModel = "recorderModel_example"; // String | Model
    String recorderName = "recorderName_example"; // String | Name
    String recorderRecorderType = "recorderRecorderType_example"; // String | Type
    String recorderResolution = "recorderResolution_example"; // String | Resolution
    String recorderOnvif = "recorderOnvif_example"; // String | ONVIF
    String recorderPsia = "recorderPsia_example"; // String | PSIA
    String recorderPtz = "recorderPtz_example"; // String | PTZ
    String recorderDiscontinued = "recorderDiscontinued_example"; // String | Discontinued
    String recorderSupport3rdparty = "recorderSupport3rdparty_example"; // String | 3rd pparty Camera Support
    String recorderSdCard = "recorderSdCard_example"; // String | SD Card
    String recorderUpnp = "recorderUpnp_example"; // String | UPnP
    String recorderHotSwap = "recorderHotSwap_example"; // String | Hot Swap
    String recorderHdmi = "recorderHdmi_example"; // String | HDMI Support
    String recorderDigitalIo = "recorderDigitalIo_example"; // String | Digital I/O
    String recorderAudioIn = "recorderAudioIn_example"; // String | Audio In
    String recorderAudioOut = "recorderAudioOut_example"; // String | Audio Out
    String recorderInputChannels = "recorderInputChannels_example"; // String | Input Channels
    String recorderPlaybackChannels = "recorderPlaybackChannels_example"; // String | Playback Channels
    String recorderUsb = "recorderUsb_example"; // String | USB Ports
    String recorderSdhc = "recorderSdhc_example"; // String | SD Card (GB)
    String recorderMobileAccess = "recorderMobileAccess_example"; // String | Mobile Access
    String recorderAlarms = "recorderAlarms_example"; // String | Alarms
    String recorderRaidSupport = "recorderRaidSupport_example"; // String | Raid Support
    String recorderStorage = "recorderStorage_example"; // String | Internal Storage
    String recorderAdditionalInformation = "recorderAdditionalInformation_example"; // String | Additional Information
    String recorderDefaultUsername = "recorderDefaultUsername_example"; // String | Default Username
    String recorderDefaultPassword = "recorderDefaultPassword_example"; // String | Default Password
    String recorderJpegUrl = "recorderJpegUrl_example"; // String | JPEG URL
    String recorderH264Url = "recorderH264Url_example"; // String | H264 URL
    String recorderMjpegUrl = "recorderMjpegUrl_example"; // String | MJPEG URL
    String recorderOfficialUrl = "recorderOfficialUrl_example"; // String | Official URL
    try {
      apiInstance.apiV1RecordersIdJsonPut(id, vendorId, recorderModel, recorderName, recorderRecorderType, recorderResolution, recorderOnvif, recorderPsia, recorderPtz, recorderDiscontinued, recorderSupport3rdparty, recorderSdCard, recorderUpnp, recorderHotSwap, recorderHdmi, recorderDigitalIo, recorderAudioIn, recorderAudioOut, recorderInputChannels, recorderPlaybackChannels, recorderUsb, recorderSdhc, recorderMobileAccess, recorderAlarms, recorderRaidSupport, recorderStorage, recorderAdditionalInformation, recorderDefaultUsername, recorderDefaultPassword, recorderJpegUrl, recorderH264Url, recorderMjpegUrl, recorderOfficialUrl);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordersApi#apiV1RecordersIdJsonPut");
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
| **id** | **String**| Recorder ID | |
| **vendorId** | **String**| Vendor ID | |
| **recorderModel** | **String**| Model | |
| **recorderName** | **String**| Name | |
| **recorderRecorderType** | **String**| Type | |
| **recorderResolution** | **String**| Resolution | [optional] |
| **recorderOnvif** | **String**| ONVIF | [optional] |
| **recorderPsia** | **String**| PSIA | [optional] |
| **recorderPtz** | **String**| PTZ | [optional] |
| **recorderDiscontinued** | **String**| Discontinued | [optional] |
| **recorderSupport3rdparty** | **String**| 3rd pparty Camera Support | [optional] |
| **recorderSdCard** | **String**| SD Card | [optional] |
| **recorderUpnp** | **String**| UPnP | [optional] |
| **recorderHotSwap** | **String**| Hot Swap | [optional] |
| **recorderHdmi** | **String**| HDMI Support | [optional] |
| **recorderDigitalIo** | **String**| Digital I/O | [optional] |
| **recorderAudioIn** | **String**| Audio In | [optional] |
| **recorderAudioOut** | **String**| Audio Out | [optional] |
| **recorderInputChannels** | **String**| Input Channels | [optional] |
| **recorderPlaybackChannels** | **String**| Playback Channels | [optional] |
| **recorderUsb** | **String**| USB Ports | [optional] |
| **recorderSdhc** | **String**| SD Card (GB) | [optional] |
| **recorderMobileAccess** | **String**| Mobile Access | [optional] |
| **recorderAlarms** | **String**| Alarms | [optional] |
| **recorderRaidSupport** | **String**| Raid Support | [optional] |
| **recorderStorage** | **String**| Internal Storage | [optional] |
| **recorderAdditionalInformation** | **String**| Additional Information | [optional] |
| **recorderDefaultUsername** | **String**| Default Username | [optional] |
| **recorderDefaultPassword** | **String**| Default Password | [optional] |
| **recorderJpegUrl** | **String**| JPEG URL | [optional] |
| **recorderH264Url** | **String**| H264 URL | [optional] |
| **recorderMjpegUrl** | **String**| MJPEG URL | [optional] |
| **recorderOfficialUrl** | **String**| Official URL | [optional] |

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
| **200** | No response was specified |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

<a id="apiV1RecordersIndex"></a>
# **apiV1RecordersIndex**
> apiV1RecordersIndex(page, order)

Fetches all Recorders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    RecordersApi apiInstance = new RecordersApi(defaultClient);
    Integer page = 56; // Integer | Page number
    String order = "order_example"; // String | Sort order
    try {
      apiInstance.apiV1RecordersIndex(page, order);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordersApi#apiV1RecordersIndex");
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
| **page** | **Integer**| Page number | [optional] |
| **order** | **String**| Sort order | [optional] |

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
| **200** | No response was specified |  -  |
| **401** | Unauthorized |  -  |
| **406** | The request you made is not acceptable |  -  |
| **416** | Requested Range Not Satisfiable |  -  |

<a id="apiV1RecordersSearch"></a>
# **apiV1RecordersSearch**
> apiV1RecordersSearch(page, qModelCont, qVendorNameCont, qSdhcEq, qTypeEq, qResolutionEq, qInputChannelsEq, qPlaybackChannelsEq, qOnvifTrue, qPsiaTrue, qPtzTrue, qSdCardTrue, qUpnpTrue, qAudioInTrue, qAudioOutTrue, qHdmiTrue, qHotSwapTrue, qSupport3rdpartyTrue, qDigitalIoTrue)

Searches all Recorders

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    RecordersApi apiInstance = new RecordersApi(defaultClient);
    Integer page = 56; // Integer | Page number
    String qModelCont = "qModelCont_example"; // String | Model
    String qVendorNameCont = "qVendorNameCont_example"; // String | Vendor
    String qSdhcEq = "qSdhcEq_example"; // String | SD Card (GB)
    String qTypeEq = "qTypeEq_example"; // String | Type
    String qResolutionEq = "qResolutionEq_example"; // String | Resolution
    String qInputChannelsEq = "qInputChannelsEq_example"; // String | Input Channels
    String qPlaybackChannelsEq = "qPlaybackChannelsEq_example"; // String | Playback Channels
    String qOnvifTrue = "qOnvifTrue_example"; // String | ONVIF
    String qPsiaTrue = "qPsiaTrue_example"; // String | PSIA
    String qPtzTrue = "qPtzTrue_example"; // String | PTZ
    String qSdCardTrue = "qSdCardTrue_example"; // String | SD Card
    String qUpnpTrue = "qUpnpTrue_example"; // String | UPnP
    String qAudioInTrue = "qAudioInTrue_example"; // String | Audio In
    String qAudioOutTrue = "qAudioOutTrue_example"; // String | Audio Out
    String qHdmiTrue = "qHdmiTrue_example"; // String | HDMI Support
    String qHotSwapTrue = "qHotSwapTrue_example"; // String | Hot Swap
    String qSupport3rdpartyTrue = "qSupport3rdpartyTrue_example"; // String | 3rd pparty Camera Support
    String qDigitalIoTrue = "qDigitalIoTrue_example"; // String | Digital I/O
    try {
      apiInstance.apiV1RecordersSearch(page, qModelCont, qVendorNameCont, qSdhcEq, qTypeEq, qResolutionEq, qInputChannelsEq, qPlaybackChannelsEq, qOnvifTrue, qPsiaTrue, qPtzTrue, qSdCardTrue, qUpnpTrue, qAudioInTrue, qAudioOutTrue, qHdmiTrue, qHotSwapTrue, qSupport3rdpartyTrue, qDigitalIoTrue);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordersApi#apiV1RecordersSearch");
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
| **page** | **Integer**| Page number | [optional] |
| **qModelCont** | **String**| Model | [optional] |
| **qVendorNameCont** | **String**| Vendor | [optional] |
| **qSdhcEq** | **String**| SD Card (GB) | [optional] |
| **qTypeEq** | **String**| Type | [optional] |
| **qResolutionEq** | **String**| Resolution | [optional] |
| **qInputChannelsEq** | **String**| Input Channels | [optional] |
| **qPlaybackChannelsEq** | **String**| Playback Channels | [optional] |
| **qOnvifTrue** | **String**| ONVIF | [optional] |
| **qPsiaTrue** | **String**| PSIA | [optional] |
| **qPtzTrue** | **String**| PTZ | [optional] |
| **qSdCardTrue** | **String**| SD Card | [optional] |
| **qUpnpTrue** | **String**| UPnP | [optional] |
| **qAudioInTrue** | **String**| Audio In | [optional] |
| **qAudioOutTrue** | **String**| Audio Out | [optional] |
| **qHdmiTrue** | **String**| HDMI Support | [optional] |
| **qHotSwapTrue** | **String**| Hot Swap | [optional] |
| **qSupport3rdpartyTrue** | **String**| 3rd pparty Camera Support | [optional] |
| **qDigitalIoTrue** | **String**| Digital I/O | [optional] |

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
| **200** | No response was specified |  -  |
| **401** | Unauthorized |  -  |
| **406** | The request you made is not acceptable |  -  |
| **416** | Requested Range Not Satisfiable |  -  |

<a id="apiV1RecordersShow"></a>
# **apiV1RecordersShow**
> apiV1RecordersShow(id)

Fetches a single Recorder

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RecordersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    RecordersApi apiInstance = new RecordersApi(defaultClient);
    Integer id = 56; // Integer | Recorder ID
    try {
      apiInstance.apiV1RecordersShow(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling RecordersApi#apiV1RecordersShow");
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
| **id** | **Integer**| Recorder ID | |

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
| **200** | No response was specified |  -  |
| **401** | Unauthorized |  -  |
| **404** | Not Found |  -  |
| **406** | Not Acceptable |  -  |

