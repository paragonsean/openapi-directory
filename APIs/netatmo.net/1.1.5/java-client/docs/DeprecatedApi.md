# DeprecatedApi

All URIs are relative to *https://api.netatmo.net/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**devicelist**](DeprecatedApi.md#devicelist) | **GET** /devicelist |  |
| [**getthermstate**](DeprecatedApi.md#getthermstate) | **GET** /getthermstate |  |
| [**getuser**](DeprecatedApi.md#getuser) | **GET** /getuser |  |


<a id="devicelist"></a>
# **devicelist**
> NADeviceListResponse devicelist(appType, deviceId, getFavorites)



The method devicelist returns the list of devices owned by the user, and their modules. A device is identified by its _id (which is its mac address) and each device may have one, several or no modules, also identified by an _id. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    DeprecatedApi apiInstance = new DeprecatedApi(defaultClient);
    String appType = "app_thermostat"; // String | Defines which device type will be returned by devicelist. It could be app_thermostat or app_station (by default if not provided)
    String deviceId = "deviceId_example"; // String | Specify a device_id if you want to retrieve only this device informations.
    Boolean getFavorites = false; // Boolean | When set to \"true\", the favorite devices of the user are returned. This flag is available only if the devices requested are Weather Stations.
    try {
      NADeviceListResponse result = apiInstance.devicelist(appType, deviceId, getFavorites);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeprecatedApi#devicelist");
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
| **appType** | **String**| Defines which device type will be returned by devicelist. It could be app_thermostat or app_station (by default if not provided) | [optional] [enum: app_thermostat, app_station] |
| **deviceId** | **String**| Specify a device_id if you want to retrieve only this device informations. | [optional] |
| **getFavorites** | **Boolean**| When set to \&quot;true\&quot;, the favorite devices of the user are returned. This flag is available only if the devices requested are Weather Stations. | [optional] [default to false] |

### Return type

[**NADeviceListResponse**](NADeviceListResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="getthermstate"></a>
# **getthermstate**
> NAThermStateResponse getthermstate(deviceId, moduleId)



The method getthermstate returns the last Thermostat measurements, its current weekly schedule, and, if present, its current manual temperature setpoint.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    DeprecatedApi apiInstance = new DeprecatedApi(defaultClient);
    String deviceId = "deviceId_example"; // String | The relay id
    String moduleId = "moduleId_example"; // String | The thermostat id
    try {
      NAThermStateResponse result = apiInstance.getthermstate(deviceId, moduleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeprecatedApi#getthermstate");
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
| **deviceId** | **String**| The relay id | |
| **moduleId** | **String**| The thermostat id | |

### Return type

[**NAThermStateResponse**](NAThermStateResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

<a id="getuser"></a>
# **getuser**
> NAUserResponse getuser()



The method getuser returns information about a user such as prefered language, prefered units, and list of devices. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeprecatedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netatmo.net/api");
    
    // Configure OAuth2 access token for authorization: code_oauth
    OAuth code_oauth = (OAuth) defaultClient.getAuthentication("code_oauth");
    code_oauth.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: password_oauth
    OAuth password_oauth = (OAuth) defaultClient.getAuthentication("password_oauth");
    password_oauth.setAccessToken("YOUR ACCESS TOKEN");

    DeprecatedApi apiInstance = new DeprecatedApi(defaultClient);
    try {
      NAUserResponse result = apiInstance.getuser();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeprecatedApi#getuser");
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

[**NAUserResponse**](NAUserResponse.md)

### Authorization

[code_oauth](../README.md#code_oauth), [password_oauth](../README.md#password_oauth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful response |  -  |

