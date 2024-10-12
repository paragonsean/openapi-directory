# ImuApi

All URIs are relative to *http://demo.waterlinked.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**imuCalibrate**](ImuApi.md#imuCalibrate) | **POST** /api/v1/imu/calibrate | Calibrate imu |
| [**imuGet**](ImuApi.md#imuGet) | **GET** /api/v1/imu/calibrate | Get imu |
| [**imuResetGyro**](ImuApi.md#imuResetGyro) | **POST** /api/v1/imu/resetgyros | ResetGyro imu |
| [**imuSetNorth**](ImuApi.md#imuSetNorth) | **POST** /api/v1/imu/setnorth | SetNorth imu |


<a id="imuCalibrate"></a>
# **imuCalibrate**
> imuCalibrate(payload)

Calibrate imu

[DEPRECATED]Start calibration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ImuApi apiInstance = new ImuApi(defaultClient);
    CalibrateImuPayload payload = new CalibrateImuPayload(); // CalibrateImuPayload | IMU calibration action
    try {
      apiInstance.imuCalibrate(payload);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImuApi#imuCalibrate");
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
| **payload** | [**CalibrateImuPayload**](CalibrateImuPayload.md)| IMU calibration action | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **408** | Request Timeout |  -  |
| **409** | Conflict |  -  |

<a id="imuGet"></a>
# **imuGet**
> WaterlinkedImu imuGet()

Get imu

Get IMU status and orientation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ImuApi apiInstance = new ImuApi(defaultClient);
    try {
      WaterlinkedImu result = apiInstance.imuGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImuApi#imuGet");
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

[**WaterlinkedImu**](WaterlinkedImu.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.waterlinked.imu+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="imuResetGyro"></a>
# **imuResetGyro**
> imuResetGyro()

ResetGyro imu

Reset Gyro

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ImuApi apiInstance = new ImuApi(defaultClient);
    try {
      apiInstance.imuResetGyro();
    } catch (ApiException e) {
      System.err.println("Exception when calling ImuApi#imuResetGyro");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **408** | Request Timeout |  -  |
| **409** | Conflict |  -  |

<a id="imuSetNorth"></a>
# **imuSetNorth**
> imuSetNorth(payload)

SetNorth imu

Set north point

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImuApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.waterlinked.com");

    ImuApi apiInstance = new ImuApi(defaultClient);
    SetNorthImuPayload payload = new SetNorthImuPayload(); // SetNorthImuPayload | IMU set north
    try {
      apiInstance.imuSetNorth(payload);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImuApi#imuSetNorth");
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
| **payload** | [**SetNorthImuPayload**](SetNorthImuPayload.md)| IMU set north | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **408** | Request Timeout |  -  |
| **409** | Conflict |  -  |

