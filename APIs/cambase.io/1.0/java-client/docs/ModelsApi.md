# ModelsApi

All URIs are relative to *http://api.cambase.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1ModelsCreate**](ModelsApi.md#apiV1ModelsCreate) | **POST** /api/v1/models.json | Creates a new Model |
| [**apiV1ModelsIdJsonPatch**](ModelsApi.md#apiV1ModelsIdJsonPatch) | **PATCH** /api/v1/models/{id}.json | Updates an existing Model |
| [**apiV1ModelsIdJsonPut**](ModelsApi.md#apiV1ModelsIdJsonPut) | **PUT** /api/v1/models/{id}.json | Updates an existing Model |
| [**apiV1ModelsIndex**](ModelsApi.md#apiV1ModelsIndex) | **GET** /api/v1/models.json | Fetches all Models |
| [**apiV1ModelsSearch**](ModelsApi.md#apiV1ModelsSearch) | **GET** /api/v1/models/search.json | Searches all Models |
| [**apiV1ModelsShow**](ModelsApi.md#apiV1ModelsShow) | **GET** /api/v1/models/{id}.json | Fetches a single Model |


<a id="apiV1ModelsCreate"></a>
# **apiV1ModelsCreate**
> apiV1ModelsCreate(vendorId, modelModel, modelShape, modelResolution, modelOnvif, modelPsia, modelPtz, modelInfrared, modelVarifocal, modelSdCard, modelUpnp, modelAudioIn, modelAudioOut, modelDefaultUsername, modelDefaultPassword, modelJpegUrl, modelH264Url, modelMjpegUrl)

Creates a new Model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    ModelsApi apiInstance = new ModelsApi(defaultClient);
    String vendorId = "vendorId_example"; // String | Vendor ID
    String modelModel = "modelModel_example"; // String | Model
    String modelShape = "modelShape_example"; // String | Shape
    String modelResolution = "modelResolution_example"; // String | Resolution
    String modelOnvif = "modelOnvif_example"; // String | ONVIF
    String modelPsia = "modelPsia_example"; // String | PSIA
    String modelPtz = "modelPtz_example"; // String | PTZ
    String modelInfrared = "modelInfrared_example"; // String | Infrared
    String modelVarifocal = "modelVarifocal_example"; // String | Varifocal
    String modelSdCard = "modelSdCard_example"; // String | SD Card
    String modelUpnp = "modelUpnp_example"; // String | UPnP
    String modelAudioIn = "modelAudioIn_example"; // String | UPnP
    String modelAudioOut = "modelAudioOut_example"; // String | UPnP
    String modelDefaultUsername = "modelDefaultUsername_example"; // String | Default Username
    String modelDefaultPassword = "modelDefaultPassword_example"; // String | Default Password
    String modelJpegUrl = "modelJpegUrl_example"; // String | JPEG URL
    String modelH264Url = "modelH264Url_example"; // String | H264 URL
    String modelMjpegUrl = "modelMjpegUrl_example"; // String | MJPEG URL
    try {
      apiInstance.apiV1ModelsCreate(vendorId, modelModel, modelShape, modelResolution, modelOnvif, modelPsia, modelPtz, modelInfrared, modelVarifocal, modelSdCard, modelUpnp, modelAudioIn, modelAudioOut, modelDefaultUsername, modelDefaultPassword, modelJpegUrl, modelH264Url, modelMjpegUrl);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelsApi#apiV1ModelsCreate");
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
| **modelModel** | **String**| Model | |
| **modelShape** | **String**| Shape | [optional] |
| **modelResolution** | **String**| Resolution | [optional] |
| **modelOnvif** | **String**| ONVIF | [optional] |
| **modelPsia** | **String**| PSIA | [optional] |
| **modelPtz** | **String**| PTZ | [optional] |
| **modelInfrared** | **String**| Infrared | [optional] |
| **modelVarifocal** | **String**| Varifocal | [optional] |
| **modelSdCard** | **String**| SD Card | [optional] |
| **modelUpnp** | **String**| UPnP | [optional] |
| **modelAudioIn** | **String**| UPnP | [optional] |
| **modelAudioOut** | **String**| UPnP | [optional] |
| **modelDefaultUsername** | **String**| Default Username | [optional] |
| **modelDefaultPassword** | **String**| Default Password | [optional] |
| **modelJpegUrl** | **String**| JPEG URL | [optional] |
| **modelH264Url** | **String**| H264 URL | [optional] |
| **modelMjpegUrl** | **String**| MJPEG URL | [optional] |

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

<a id="apiV1ModelsIdJsonPatch"></a>
# **apiV1ModelsIdJsonPatch**
> apiV1ModelsIdJsonPatch(id, vendorId, modelModel, modelShape, modelResolution, modelOnvif, modelPsia, modelPtz, modelInfrared, modelVarifocal, modelSdCard, modelUpnp, modelAudioIn, modelAudioOut, modelDefaultUsername, modelDefaultPassword, modelJpegUrl, modelH264Url, modelMjpegUrl)

Updates an existing Model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    ModelsApi apiInstance = new ModelsApi(defaultClient);
    String id = "id_example"; // String | Model ID
    String vendorId = "vendorId_example"; // String | Vendor ID
    String modelModel = "modelModel_example"; // String | Model
    String modelShape = "modelShape_example"; // String | Shape
    String modelResolution = "modelResolution_example"; // String | Resolution
    String modelOnvif = "modelOnvif_example"; // String | ONVIF
    String modelPsia = "modelPsia_example"; // String | PSIA
    String modelPtz = "modelPtz_example"; // String | PTZ
    String modelInfrared = "modelInfrared_example"; // String | Infrared
    String modelVarifocal = "modelVarifocal_example"; // String | Varifocal
    String modelSdCard = "modelSdCard_example"; // String | SD Card
    String modelUpnp = "modelUpnp_example"; // String | UPnP
    String modelAudioIn = "modelAudioIn_example"; // String | Audio In
    String modelAudioOut = "modelAudioOut_example"; // String | Audio Out
    String modelDefaultUsername = "modelDefaultUsername_example"; // String | Default Username
    String modelDefaultPassword = "modelDefaultPassword_example"; // String | Default Password
    String modelJpegUrl = "modelJpegUrl_example"; // String | JPEG URL
    String modelH264Url = "modelH264Url_example"; // String | H264 URL
    String modelMjpegUrl = "modelMjpegUrl_example"; // String | MJPEG URL
    try {
      apiInstance.apiV1ModelsIdJsonPatch(id, vendorId, modelModel, modelShape, modelResolution, modelOnvif, modelPsia, modelPtz, modelInfrared, modelVarifocal, modelSdCard, modelUpnp, modelAudioIn, modelAudioOut, modelDefaultUsername, modelDefaultPassword, modelJpegUrl, modelH264Url, modelMjpegUrl);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelsApi#apiV1ModelsIdJsonPatch");
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
| **id** | **String**| Model ID | |
| **vendorId** | **String**| Vendor ID | |
| **modelModel** | **String**| Model | [optional] |
| **modelShape** | **String**| Shape | [optional] |
| **modelResolution** | **String**| Resolution | [optional] |
| **modelOnvif** | **String**| ONVIF | [optional] |
| **modelPsia** | **String**| PSIA | [optional] |
| **modelPtz** | **String**| PTZ | [optional] |
| **modelInfrared** | **String**| Infrared | [optional] |
| **modelVarifocal** | **String**| Varifocal | [optional] |
| **modelSdCard** | **String**| SD Card | [optional] |
| **modelUpnp** | **String**| UPnP | [optional] |
| **modelAudioIn** | **String**| Audio In | [optional] |
| **modelAudioOut** | **String**| Audio Out | [optional] |
| **modelDefaultUsername** | **String**| Default Username | [optional] |
| **modelDefaultPassword** | **String**| Default Password | [optional] |
| **modelJpegUrl** | **String**| JPEG URL | [optional] |
| **modelH264Url** | **String**| H264 URL | [optional] |
| **modelMjpegUrl** | **String**| MJPEG URL | [optional] |

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

<a id="apiV1ModelsIdJsonPut"></a>
# **apiV1ModelsIdJsonPut**
> apiV1ModelsIdJsonPut(id, vendorId, modelModel, modelShape, modelResolution, modelOnvif, modelPsia, modelPtz, modelInfrared, modelVarifocal, modelSdCard, modelUpnp, modelAudioIn, modelAudioOut, modelDefaultUsername, modelDefaultPassword, modelJpegUrl, modelH264Url, modelMjpegUrl)

Updates an existing Model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    ModelsApi apiInstance = new ModelsApi(defaultClient);
    String id = "id_example"; // String | Model ID
    String vendorId = "vendorId_example"; // String | Vendor ID
    String modelModel = "modelModel_example"; // String | Model
    String modelShape = "modelShape_example"; // String | Shape
    String modelResolution = "modelResolution_example"; // String | Resolution
    String modelOnvif = "modelOnvif_example"; // String | ONVIF
    String modelPsia = "modelPsia_example"; // String | PSIA
    String modelPtz = "modelPtz_example"; // String | PTZ
    String modelInfrared = "modelInfrared_example"; // String | Infrared
    String modelVarifocal = "modelVarifocal_example"; // String | Varifocal
    String modelSdCard = "modelSdCard_example"; // String | SD Card
    String modelUpnp = "modelUpnp_example"; // String | UPnP
    String modelAudioIn = "modelAudioIn_example"; // String | Audio In
    String modelAudioOut = "modelAudioOut_example"; // String | Audio Out
    String modelDefaultUsername = "modelDefaultUsername_example"; // String | Default Username
    String modelDefaultPassword = "modelDefaultPassword_example"; // String | Default Password
    String modelJpegUrl = "modelJpegUrl_example"; // String | JPEG URL
    String modelH264Url = "modelH264Url_example"; // String | H264 URL
    String modelMjpegUrl = "modelMjpegUrl_example"; // String | MJPEG URL
    try {
      apiInstance.apiV1ModelsIdJsonPut(id, vendorId, modelModel, modelShape, modelResolution, modelOnvif, modelPsia, modelPtz, modelInfrared, modelVarifocal, modelSdCard, modelUpnp, modelAudioIn, modelAudioOut, modelDefaultUsername, modelDefaultPassword, modelJpegUrl, modelH264Url, modelMjpegUrl);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelsApi#apiV1ModelsIdJsonPut");
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
| **id** | **String**| Model ID | |
| **vendorId** | **String**| Vendor ID | |
| **modelModel** | **String**| Model | [optional] |
| **modelShape** | **String**| Shape | [optional] |
| **modelResolution** | **String**| Resolution | [optional] |
| **modelOnvif** | **String**| ONVIF | [optional] |
| **modelPsia** | **String**| PSIA | [optional] |
| **modelPtz** | **String**| PTZ | [optional] |
| **modelInfrared** | **String**| Infrared | [optional] |
| **modelVarifocal** | **String**| Varifocal | [optional] |
| **modelSdCard** | **String**| SD Card | [optional] |
| **modelUpnp** | **String**| UPnP | [optional] |
| **modelAudioIn** | **String**| Audio In | [optional] |
| **modelAudioOut** | **String**| Audio Out | [optional] |
| **modelDefaultUsername** | **String**| Default Username | [optional] |
| **modelDefaultPassword** | **String**| Default Password | [optional] |
| **modelJpegUrl** | **String**| JPEG URL | [optional] |
| **modelH264Url** | **String**| H264 URL | [optional] |
| **modelMjpegUrl** | **String**| MJPEG URL | [optional] |

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

<a id="apiV1ModelsIndex"></a>
# **apiV1ModelsIndex**
> apiV1ModelsIndex(page, order)

Fetches all Models

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    ModelsApi apiInstance = new ModelsApi(defaultClient);
    Integer page = 56; // Integer | Page number
    String order = "order_example"; // String | Sort order
    try {
      apiInstance.apiV1ModelsIndex(page, order);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelsApi#apiV1ModelsIndex");
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

<a id="apiV1ModelsSearch"></a>
# **apiV1ModelsSearch**
> apiV1ModelsSearch(page, qModelCont, qManufacturerNameCont, qShapeEq, qResolutionEq, qOnvifTrue, qPsiaTrue, qPtzTrue, qInfraredTrue, qVarifocalTrue, qSdCardTrue, qUpnpTrue, qAudioInTrue, qAudioOutTrue)

Searches all Models

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    ModelsApi apiInstance = new ModelsApi(defaultClient);
    Integer page = 56; // Integer | Page number
    String qModelCont = "qModelCont_example"; // String | Model
    String qManufacturerNameCont = "qManufacturerNameCont_example"; // String | Vendor
    String qShapeEq = "qShapeEq_example"; // String | Shape
    String qResolutionEq = "qResolutionEq_example"; // String | Resolution
    String qOnvifTrue = "qOnvifTrue_example"; // String | ONVIF
    String qPsiaTrue = "qPsiaTrue_example"; // String | PSIA
    String qPtzTrue = "qPtzTrue_example"; // String | PTZ
    String qInfraredTrue = "qInfraredTrue_example"; // String | Infrared
    String qVarifocalTrue = "qVarifocalTrue_example"; // String | Varifocal
    String qSdCardTrue = "qSdCardTrue_example"; // String | SD Card
    String qUpnpTrue = "qUpnpTrue_example"; // String | UPnP
    String qAudioInTrue = "qAudioInTrue_example"; // String | Audio In
    String qAudioOutTrue = "qAudioOutTrue_example"; // String | Audio Out
    try {
      apiInstance.apiV1ModelsSearch(page, qModelCont, qManufacturerNameCont, qShapeEq, qResolutionEq, qOnvifTrue, qPsiaTrue, qPtzTrue, qInfraredTrue, qVarifocalTrue, qSdCardTrue, qUpnpTrue, qAudioInTrue, qAudioOutTrue);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelsApi#apiV1ModelsSearch");
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
| **qManufacturerNameCont** | **String**| Vendor | [optional] |
| **qShapeEq** | **String**| Shape | [optional] |
| **qResolutionEq** | **String**| Resolution | [optional] |
| **qOnvifTrue** | **String**| ONVIF | [optional] |
| **qPsiaTrue** | **String**| PSIA | [optional] |
| **qPtzTrue** | **String**| PTZ | [optional] |
| **qInfraredTrue** | **String**| Infrared | [optional] |
| **qVarifocalTrue** | **String**| Varifocal | [optional] |
| **qSdCardTrue** | **String**| SD Card | [optional] |
| **qUpnpTrue** | **String**| UPnP | [optional] |
| **qAudioInTrue** | **String**| Audio In | [optional] |
| **qAudioOutTrue** | **String**| Audio Out | [optional] |

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

<a id="apiV1ModelsShow"></a>
# **apiV1ModelsShow**
> apiV1ModelsShow(id)

Fetches a single Model

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ModelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.cambase.io");

    ModelsApi apiInstance = new ModelsApi(defaultClient);
    Integer id = 56; // Integer | Model ID
    try {
      apiInstance.apiV1ModelsShow(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ModelsApi#apiV1ModelsShow");
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
| **id** | **Integer**| Model ID | |

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

