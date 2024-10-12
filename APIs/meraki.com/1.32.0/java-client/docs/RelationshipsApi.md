# RelationshipsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceSensorRelationships_1**](RelationshipsApi.md#getDeviceSensorRelationships_1) | **GET** /devices/{serial}/sensor/relationships | List the sensor roles for a given sensor or camera device. |
| [**getNetworkSensorRelationships_1**](RelationshipsApi.md#getNetworkSensorRelationships_1) | **GET** /networks/{networkId}/sensor/relationships | List the sensor roles for devices in a given network |
| [**updateDeviceSensorRelationships_1**](RelationshipsApi.md#updateDeviceSensorRelationships_1) | **PUT** /devices/{serial}/sensor/relationships | Assign one or more sensor roles to a given sensor or camera device. |


<a id="getDeviceSensorRelationships_1"></a>
# **getDeviceSensorRelationships_1**
> List&lt;GetDeviceSensorRelationships200ResponseInner&gt; getDeviceSensorRelationships_1(serial)

List the sensor roles for a given sensor or camera device.

List the sensor roles for a given sensor or camera device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelationshipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RelationshipsApi apiInstance = new RelationshipsApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<GetDeviceSensorRelationships200ResponseInner> result = apiInstance.getDeviceSensorRelationships_1(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelationshipsApi#getDeviceSensorRelationships_1");
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
| **serial** | **String**|  | |

### Return type

[**List&lt;GetDeviceSensorRelationships200ResponseInner&gt;**](GetDeviceSensorRelationships200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSensorRelationships_1"></a>
# **getNetworkSensorRelationships_1**
> List&lt;GetNetworkSensorRelationships200ResponseInner&gt; getNetworkSensorRelationships_1(networkId)

List the sensor roles for devices in a given network

List the sensor roles for devices in a given network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelationshipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RelationshipsApi apiInstance = new RelationshipsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkSensorRelationships200ResponseInner> result = apiInstance.getNetworkSensorRelationships_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelationshipsApi#getNetworkSensorRelationships_1");
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
| **networkId** | **String**|  | |

### Return type

[**List&lt;GetNetworkSensorRelationships200ResponseInner&gt;**](GetNetworkSensorRelationships200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateDeviceSensorRelationships_1"></a>
# **updateDeviceSensorRelationships_1**
> GetDeviceSensorRelationships200ResponseInner updateDeviceSensorRelationships_1(serial, updateDeviceSensorRelationshipsRequest)

Assign one or more sensor roles to a given sensor or camera device.

Assign one or more sensor roles to a given sensor or camera device.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RelationshipsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RelationshipsApi apiInstance = new RelationshipsApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceSensorRelationshipsRequest updateDeviceSensorRelationshipsRequest = new UpdateDeviceSensorRelationshipsRequest(); // UpdateDeviceSensorRelationshipsRequest | 
    try {
      GetDeviceSensorRelationships200ResponseInner result = apiInstance.updateDeviceSensorRelationships_1(serial, updateDeviceSensorRelationshipsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RelationshipsApi#updateDeviceSensorRelationships_1");
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
| **serial** | **String**|  | |
| **updateDeviceSensorRelationshipsRequest** | [**UpdateDeviceSensorRelationshipsRequest**](UpdateDeviceSensorRelationshipsRequest.md)|  | [optional] |

### Return type

[**GetDeviceSensorRelationships200ResponseInner**](GetDeviceSensorRelationships200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

