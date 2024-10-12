# ChargersApi

All URIs are relative to *https://api.test.enode.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**controlChargerCharging**](ChargersApi.md#controlChargerCharging) | **POST** /chargers/{chargerId}/charging | Control Charging |
| [**getCharger**](ChargersApi.md#getCharger) | **GET** /chargers/{chargerId} | Get Charger |
| [**getChargers**](ChargersApi.md#getChargers) | **GET** /chargers | List Chargers |


<a id="controlChargerCharging"></a>
# **controlChargerCharging**
> controlChargerCharging(chargerId, controlChargerChargingRequest)

Control Charging

Instruct the charger to start or stop charging

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    ChargersApi apiInstance = new ChargersApi(defaultClient);
    String chargerId = "chargerId_example"; // String | ID of the Charger
    ControlChargerChargingRequest controlChargerChargingRequest = new ControlChargerChargingRequest(); // ControlChargerChargingRequest | 
    try {
      apiInstance.controlChargerCharging(chargerId, controlChargerChargingRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargersApi#controlChargerCharging");
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
| **chargerId** | **String**| ID of the Charger | |
| **controlChargerChargingRequest** | [**ControlChargerChargingRequest**](ControlChargerChargingRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | No Content |  -  |

<a id="getCharger"></a>
# **getCharger**
> GetCharger200Response getCharger(chargerId)

Get Charger

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    ChargersApi apiInstance = new ChargersApi(defaultClient);
    String chargerId = "chargerId_example"; // String | ID of the Charger
    try {
      GetCharger200Response result = apiInstance.getCharger(chargerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargersApi#getCharger");
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
| **chargerId** | **String**| ID of the Charger | |

### Return type

[**GetCharger200Response**](GetCharger200Response.md)

### Authorization

[UserAccessToken](../README.md#UserAccessToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful |  -  |

<a id="getChargers"></a>
# **getChargers**
> List&lt;Object&gt; getChargers(field)

List Chargers

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ChargersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.enode.io");
    
    // Configure OAuth2 access token for authorization: UserAccessToken
    OAuth UserAccessToken = (OAuth) defaultClient.getAuthentication("UserAccessToken");
    UserAccessToken.setAccessToken("YOUR ACCESS TOKEN");

    ChargersApi apiInstance = new ChargersApi(defaultClient);
    List<String> field = Arrays.asList(); // List<String> | An optional array of Charger fields that should be included in the response, for example: `?field[]=information&field[]=chargeState`   By default, no optional fields are included and only the Charger ID will be returned. Response time will generally be slower the more fields you request.
    try {
      List<Object> result = apiInstance.getChargers(field);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ChargersApi#getChargers");
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
| **field** | [**List&lt;String&gt;**](String.md)| An optional array of Charger fields that should be included in the response, for example: &#x60;?field[]&#x3D;information&amp;field[]&#x3D;chargeState&#x60;   By default, no optional fields are included and only the Charger ID will be returned. Response time will generally be slower the more fields you request. | [optional] [enum: chargeState, location] |

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

