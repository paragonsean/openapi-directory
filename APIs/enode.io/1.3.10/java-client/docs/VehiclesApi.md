# VehiclesApi

All URIs are relative to *https://api.test.enode.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getVehicleChargestate**](VehiclesApi.md#getVehicleChargestate) | **GET** /vehicles/{vehicleId}/charge-state | Get Vehicle Charge State |
| [**getVehicles**](VehiclesApi.md#getVehicles) | **GET** /vehicles | List Vehicles |
| [**getVehiclesVehicleid**](VehiclesApi.md#getVehiclesVehicleid) | **GET** /vehicles/{vehicleId} | Get Vehicle |
| [**getVehiclesVehicleidInformation**](VehiclesApi.md#getVehiclesVehicleidInformation) | **GET** /vehicles/{vehicleId}/information | Get Vehicle Information |
| [**getVehiclesVehicleidLocation**](VehiclesApi.md#getVehiclesVehicleidLocation) | **GET** /vehicles/{vehicleId}/location | Get Vehicle Location |
| [**getVehiclesVehicleidOdometer**](VehiclesApi.md#getVehiclesVehicleidOdometer) | **GET** /vehicles/{vehicleId}/odometer | Get Vehicle Odometer |
| [**getVehiclesVehicleidSmartchargingpolicy**](VehiclesApi.md#getVehiclesVehicleidSmartchargingpolicy) | **GET** /vehicles/{vehicleId}/smart-charging-policy | Get Vehicle Smart Charging Policy |
| [**postVehiclesVehicleidCharging**](VehiclesApi.md#postVehiclesVehicleidCharging) | **POST** /vehicles/{vehicleId}/charging | Start / Stop Charging |
| [**postVehiclesVehicleidWatch**](VehiclesApi.md#postVehiclesVehicleidWatch) | **POST** /vehicles/{vehicleId}/watch | Start Watching Vehicle |
| [**putVehiclesVehicleidSmartchargingpolicy**](VehiclesApi.md#putVehiclesVehicleidSmartchargingpolicy) | **PUT** /vehicles/{vehicleId}/smart-charging-policy | Update Vehicle Smart Charging Policy |


<a id="getVehicleChargestate"></a>
# **getVehicleChargestate**
> GetVehicleChargestate200Response getVehicleChargestate()

Get Vehicle Charge State

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    try {
      GetVehicleChargestate200Response result = apiInstance.getVehicleChargestate();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehicleChargestate");
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

[**GetVehicleChargestate200Response**](GetVehicleChargestate200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

<a id="getVehicles"></a>
# **getVehicles**
> List&lt;Object&gt; getVehicles(field)

List Vehicles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    List<Object> field = null; // List<Object> | An optional array of Vehicle fields that should be included in the response, for example: `?field[]=information&field[]=location`   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request.
    try {
      List<Object> result = apiInstance.getVehicles(field);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehicles");
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
| **field** | [**List&lt;Object&gt;**](Object.md)| An optional array of Vehicle fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;location&#x60;   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request. | [optional] |

### Return type

**List&lt;Object&gt;**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

<a id="getVehiclesVehicleid"></a>
# **getVehiclesVehicleid**
> GetVehiclesVehicleid200Response getVehiclesVehicleid(vehicleId, field)

Get Vehicle

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    String vehicleId = "vehicleId_example"; // String | ID of the Vehicle
    List<String> field = Arrays.asList(); // List<String> | An optional array of Vehicle fields that should be included in the response, for example: `?field[]=information&field[]=location`   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request.
    try {
      GetVehiclesVehicleid200Response result = apiInstance.getVehiclesVehicleid(vehicleId, field);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehiclesVehicleid");
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
| **vehicleId** | **String**| ID of the Vehicle | |
| **field** | [**List&lt;String&gt;**](String.md)| An optional array of Vehicle fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;location&#x60;   By default, no fields are included and only the Vehicle ID will be returned. Response time may be impacted by which fields you request. | [optional] [enum: smartChargingPolicy, chargeState, location, information, odometer] |

### Return type

[**GetVehiclesVehicleid200Response**](GetVehiclesVehicleid200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

<a id="getVehiclesVehicleidInformation"></a>
# **getVehiclesVehicleidInformation**
> GetVehiclesVehicleidInformation200Response getVehiclesVehicleidInformation()

Get Vehicle Information

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    try {
      GetVehiclesVehicleidInformation200Response result = apiInstance.getVehiclesVehicleidInformation();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehiclesVehicleidInformation");
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

[**GetVehiclesVehicleidInformation200Response**](GetVehiclesVehicleidInformation200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Descriptive information about the Vehicle |  -  |

<a id="getVehiclesVehicleidLocation"></a>
# **getVehiclesVehicleidLocation**
> GetVehiclesVehicleidLocation200Response getVehiclesVehicleidLocation()

Get Vehicle Location

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    try {
      GetVehiclesVehicleidLocation200Response result = apiInstance.getVehiclesVehicleidLocation();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehiclesVehicleidLocation");
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

[**GetVehiclesVehicleidLocation200Response**](GetVehiclesVehicleidLocation200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Vehicle&#39;s GPS coordinates with timestamp |  -  |

<a id="getVehiclesVehicleidOdometer"></a>
# **getVehiclesVehicleidOdometer**
> GetVehiclesVehicleidOdometer200Response getVehiclesVehicleidOdometer()

Get Vehicle Odometer

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    try {
      GetVehiclesVehicleidOdometer200Response result = apiInstance.getVehiclesVehicleidOdometer();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehiclesVehicleidOdometer");
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

[**GetVehiclesVehicleidOdometer200Response**](GetVehiclesVehicleidOdometer200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Vehicle&#39;s odometer with timestamp |  -  |

<a id="getVehiclesVehicleidSmartchargingpolicy"></a>
# **getVehiclesVehicleidSmartchargingpolicy**
> Object getVehiclesVehicleidSmartchargingpolicy()

Get Vehicle Smart Charging Policy

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    try {
      Object result = apiInstance.getVehiclesVehicleidSmartchargingpolicy();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#getVehiclesVehicleidSmartchargingpolicy");
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

**Object**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

<a id="postVehiclesVehicleidCharging"></a>
# **postVehiclesVehicleidCharging**
> postVehiclesVehicleidCharging()

Start / Stop Charging

Instruct the vehicle to start or stop charging.   #### Precedence over smart charging If the vehicle is at a charging location where smart charging is activated: - a request to &#x60;start&#x60; charging will override smart charging and charging will stay on until fully charged.  - a request to &#x60;stop&#x60; charging will override smart charging and charging will be kept off for the duration of the current smart charging cycle.  The smart charging settings are not altered by these actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    try {
      apiInstance.postVehiclesVehicleidCharging();
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#postVehiclesVehicleidCharging");
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

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="postVehiclesVehicleidWatch"></a>
# **postVehiclesVehicleidWatch**
> Object postVehiclesVehicleidWatch(vehicleId, postVehiclesVehicleidWatchRequest)

Start Watching Vehicle

Temporarily triggers high-rate updates of the vehicle&#39;s properties, and this state expires automatically. This gives you a way to tell us that user may be interacting with your application and are expecting as-fast-as-possible updates on the status of their vehicle in your UI.  Any data changes resulting from this high-rate updating are reflected everywhere, whether you pull data from the &#x60;Vehicles&#x60; endpoint, or recieve it via the [Firehose Webhook](#tag/Webhooks)  The specifics of the expiration times, watch behaviors, and change thresholds are tuned by us to make sure that they work as expected, without causing undue interruption to the vehicle. For many vendors, it is not appropriate to let the high-rate monitoring last indefinitely, as it will keep systems within the car awake that should be allowed to fall into low-power/standby modes. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    String vehicleId = "vehicleId_example"; // String | ID of the Vehicle
    PostVehiclesVehicleidWatchRequest postVehiclesVehicleidWatchRequest = new PostVehiclesVehicleidWatchRequest(); // PostVehiclesVehicleidWatchRequest | 
    try {
      Object result = apiInstance.postVehiclesVehicleidWatch(vehicleId, postVehiclesVehicleidWatchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#postVehiclesVehicleidWatch");
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
| **vehicleId** | **String**| ID of the Vehicle | |
| **postVehiclesVehicleidWatchRequest** | [**PostVehiclesVehicleidWatchRequest**](PostVehiclesVehicleidWatchRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

<a id="putVehiclesVehicleidSmartchargingpolicy"></a>
# **putVehiclesVehicleidSmartchargingpolicy**
> Object putVehiclesVehicleidSmartchargingpolicy(vehicleId, putVehiclesVehicleidSmartchargingpolicyRequest)

Update Vehicle Smart Charging Policy

Updates the Smart Charging settings for a vehicle

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VehiclesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    VehiclesApi apiInstance = new VehiclesApi(defaultClient);
    String vehicleId = "vehicleId_example"; // String | ID of the Vehicle
    PutVehiclesVehicleidSmartchargingpolicyRequest putVehiclesVehicleidSmartchargingpolicyRequest = new PutVehiclesVehicleidSmartchargingpolicyRequest(); // PutVehiclesVehicleidSmartchargingpolicyRequest | 
    try {
      Object result = apiInstance.putVehiclesVehicleidSmartchargingpolicy(vehicleId, putVehiclesVehicleidSmartchargingpolicyRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VehiclesApi#putVehiclesVehicleidSmartchargingpolicy");
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
| **vehicleId** | **String**| ID of the Vehicle | |
| **putVehiclesVehicleidSmartchargingpolicyRequest** | [**PutVehiclesVehicleidSmartchargingpolicyRequest**](PutVehiclesVehicleidSmartchargingpolicyRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

