# ExternalApi

All URIs are relative to *http://demo.waterlinked.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**externalGetOrientation**](ExternalApi.md#externalGetOrientation) | **GET** /api/v1/external/orientation | GetOrientation external |
| [**externalGetVehicleIMU**](ExternalApi.md#externalGetVehicleIMU) | **GET** /api/v1/external/imu | GetVehicleIMU external |
| [**externalSetDepth**](ExternalApi.md#externalSetDepth) | **PUT** /api/v1/external/depth | SetDepth external |
| [**externalSetMaster**](ExternalApi.md#externalSetMaster) | **PUT** /api/v1/external/master | SetMaster external |
| [**externalSetOrientation**](ExternalApi.md#externalSetOrientation) | **PUT** /api/v1/external/orientation | SetOrientation external |
| [**externalSetVehicleIMU**](ExternalApi.md#externalSetVehicleIMU) | **PUT** /api/v1/external/imu | SetVehicleIMU external |


<a id="externalGetOrientation"></a>
# **externalGetOrientation**
> WlExternalLocatorOrientation externalGetOrientation()

GetOrientation external

Get orientation of Vehicle/ROV/Locator set by SetOrientation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ExternalApi apiInstance = new ExternalApi(defaultClient);
    try {
      WlExternalLocatorOrientation result = apiInstance.externalGetOrientation();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalApi#externalGetOrientation");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WlExternalLocatorOrientation**](WlExternalLocatorOrientation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.operation_response+json, application/vnd.wl.external.locator.orientation+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Internal Server Error |  -  |

<a id="externalGetVehicleIMU"></a>
# **externalGetVehicleIMU**
> WlExternalVehicleImu externalGetVehicleIMU()

GetVehicleIMU external

[DEPRECATED]Get rotation and acceleration of vehicle Locator is mounted on which was previously set

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ExternalApi apiInstance = new ExternalApi(defaultClient);
    try {
      WlExternalVehicleImu result = apiInstance.externalGetVehicleIMU();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalApi#externalGetVehicleIMU");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**WlExternalVehicleImu**](WlExternalVehicleImu.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.wl.external.vehicle.imu+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **204** | No Content |  -  |

<a id="externalSetDepth"></a>
# **externalSetDepth**
> WaterlinkedOperationResponse externalSetDepth(payload)

SetDepth external

Set depth from external source. If Locator A1 is used, this is required to get a position

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ExternalApi apiInstance = new ExternalApi(defaultClient);
    SetDepthExternalPayload payload = new SetDepthExternalPayload(); // SetDepthExternalPayload | Current locator depth and temperature
    try {
      WaterlinkedOperationResponse result = apiInstance.externalSetDepth(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalApi#externalSetDepth");
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
| **payload** | [**SetDepthExternalPayload**](SetDepthExternalPayload.md)| Current locator depth and temperature | |

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.waterlinked.operation_response+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Internal Server Error |  -  |

<a id="externalSetMaster"></a>
# **externalSetMaster**
> WaterlinkedOperationResponse externalSetMaster(payload)

SetMaster external

Set current global position of master electronics from external source. Values are only used if GPS mode is set to use external GPS

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ExternalApi apiInstance = new ExternalApi(defaultClient);
    SetMasterExternalPayload payload = new SetMasterExternalPayload(); // SetMasterExternalPayload | Global master position from external source
    try {
      WaterlinkedOperationResponse result = apiInstance.externalSetMaster(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalApi#externalSetMaster");
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
| **payload** | [**SetMasterExternalPayload**](SetMasterExternalPayload.md)| Global master position from external source | |

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.waterlinked.operation_response+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Internal Server Error |  -  |

<a id="externalSetOrientation"></a>
# **externalSetOrientation**
> WaterlinkedOperationResponse externalSetOrientation(payload)

SetOrientation external

Set orientation/compass heading of Vehicle/ROV/Locator. This is used only for visualization in GUI

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ExternalApi apiInstance = new ExternalApi(defaultClient);
    SetOrientationExternalPayload payload = new SetOrientationExternalPayload(); // SetOrientationExternalPayload | Set current compass heading of ROV/locator
    try {
      WaterlinkedOperationResponse result = apiInstance.externalSetOrientation(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalApi#externalSetOrientation");
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
| **payload** | [**SetOrientationExternalPayload**](SetOrientationExternalPayload.md)| Set current compass heading of ROV/locator | |

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.waterlinked.operation_response+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Internal Server Error |  -  |

<a id="externalSetVehicleIMU"></a>
# **externalSetVehicleIMU**
> WaterlinkedOperationResponse externalSetVehicleIMU(payload)

SetVehicleIMU external

[DEPRECATED]Set rotation and acceleration of vehicle Locator is mounted on. This is used to improve positioning of vehicle

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExternalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ExternalApi apiInstance = new ExternalApi(defaultClient);
    SetVehicleIMUExternalPayload payload = new SetVehicleIMUExternalPayload(); // SetVehicleIMUExternalPayload | Set current rotation and acceleration of vehicle
    try {
      WaterlinkedOperationResponse result = apiInstance.externalSetVehicleIMU(payload);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExternalApi#externalSetVehicleIMU");
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
| **payload** | [**SetVehicleIMUExternalPayload**](SetVehicleIMUExternalPayload.md)| Set current rotation and acceleration of vehicle | |

### Return type

[**WaterlinkedOperationResponse**](WaterlinkedOperationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.waterlinked.operation_response+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | Internal Server Error |  -  |

