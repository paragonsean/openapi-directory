# SensorApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSensorAlertsProfile**](SensorApi.md#createNetworkSensorAlertsProfile) | **POST** /networks/{networkId}/sensor/alerts/profiles | Creates a sensor alert profile for a network. |
| [**deleteNetworkSensorAlertsProfile**](SensorApi.md#deleteNetworkSensorAlertsProfile) | **DELETE** /networks/{networkId}/sensor/alerts/profiles/{id} | Deletes a sensor alert profile from a network. |
| [**getDeviceSensorRelationships**](SensorApi.md#getDeviceSensorRelationships) | **GET** /devices/{serial}/sensor/relationships | List the sensor roles for a given sensor or camera device. |
| [**getNetworkSensorAlertsCurrentOverviewByMetric**](SensorApi.md#getNetworkSensorAlertsCurrentOverviewByMetric) | **GET** /networks/{networkId}/sensor/alerts/current/overview/byMetric | Return an overview of currently alerting sensors by metric |
| [**getNetworkSensorAlertsOverviewByMetric**](SensorApi.md#getNetworkSensorAlertsOverviewByMetric) | **GET** /networks/{networkId}/sensor/alerts/overview/byMetric | Return an overview of alert occurrences over a timespan, by metric |
| [**getNetworkSensorAlertsProfile**](SensorApi.md#getNetworkSensorAlertsProfile) | **GET** /networks/{networkId}/sensor/alerts/profiles/{id} | Show details of a sensor alert profile for a network. |
| [**getNetworkSensorAlertsProfiles**](SensorApi.md#getNetworkSensorAlertsProfiles) | **GET** /networks/{networkId}/sensor/alerts/profiles | Lists all sensor alert profiles for a network. |
| [**getNetworkSensorRelationships**](SensorApi.md#getNetworkSensorRelationships) | **GET** /networks/{networkId}/sensor/relationships | List the sensor roles for devices in a given network |
| [**getOrganizationSensorReadingsHistory**](SensorApi.md#getOrganizationSensorReadingsHistory) | **GET** /organizations/{organizationId}/sensor/readings/history | Return all reported readings from sensors in a given timespan, sorted by timestamp |
| [**getOrganizationSensorReadingsLatest**](SensorApi.md#getOrganizationSensorReadingsLatest) | **GET** /organizations/{organizationId}/sensor/readings/latest | Return the latest available reading for each metric from each sensor, sorted by sensor serial |
| [**updateDeviceSensorRelationships**](SensorApi.md#updateDeviceSensorRelationships) | **PUT** /devices/{serial}/sensor/relationships | Assign one or more sensor roles to a given sensor or camera device. |
| [**updateNetworkSensorAlertsProfile**](SensorApi.md#updateNetworkSensorAlertsProfile) | **PUT** /networks/{networkId}/sensor/alerts/profiles/{id} | Updates a sensor alert profile for a network. |


<a id="createNetworkSensorAlertsProfile"></a>
# **createNetworkSensorAlertsProfile**
> GetNetworkSensorAlertsProfiles200ResponseInner createNetworkSensorAlertsProfile(networkId, createNetworkSensorAlertsProfileRequest)

Creates a sensor alert profile for a network.

Creates a sensor alert profile for a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SensorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SensorApi apiInstance = new SensorApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSensorAlertsProfileRequest createNetworkSensorAlertsProfileRequest = new CreateNetworkSensorAlertsProfileRequest(); // CreateNetworkSensorAlertsProfileRequest | 
    try {
      GetNetworkSensorAlertsProfiles200ResponseInner result = apiInstance.createNetworkSensorAlertsProfile(networkId, createNetworkSensorAlertsProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensorApi#createNetworkSensorAlertsProfile");
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
| **createNetworkSensorAlertsProfileRequest** | [**CreateNetworkSensorAlertsProfileRequest**](CreateNetworkSensorAlertsProfileRequest.md)|  | |

### Return type

[**GetNetworkSensorAlertsProfiles200ResponseInner**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="deleteNetworkSensorAlertsProfile"></a>
# **deleteNetworkSensorAlertsProfile**
> deleteNetworkSensorAlertsProfile(networkId, id)

Deletes a sensor alert profile from a network.

Deletes a sensor alert profile from a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SensorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SensorApi apiInstance = new SensorApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      apiInstance.deleteNetworkSensorAlertsProfile(networkId, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensorApi#deleteNetworkSensorAlertsProfile");
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
| **id** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Successful operation |  -  |

<a id="getDeviceSensorRelationships"></a>
# **getDeviceSensorRelationships**
> List&lt;GetDeviceSensorRelationships200ResponseInner&gt; getDeviceSensorRelationships(serial)

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
import org.openapitools.client.api.SensorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SensorApi apiInstance = new SensorApi(defaultClient);
    String serial = "serial_example"; // String | 
    try {
      List<GetDeviceSensorRelationships200ResponseInner> result = apiInstance.getDeviceSensorRelationships(serial);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensorApi#getDeviceSensorRelationships");
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

<a id="getNetworkSensorAlertsCurrentOverviewByMetric"></a>
# **getNetworkSensorAlertsCurrentOverviewByMetric**
> GetNetworkSensorAlertsCurrentOverviewByMetric200Response getNetworkSensorAlertsCurrentOverviewByMetric(networkId)

Return an overview of currently alerting sensors by metric

Return an overview of currently alerting sensors by metric

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SensorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SensorApi apiInstance = new SensorApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSensorAlertsCurrentOverviewByMetric200Response result = apiInstance.getNetworkSensorAlertsCurrentOverviewByMetric(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensorApi#getNetworkSensorAlertsCurrentOverviewByMetric");
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

[**GetNetworkSensorAlertsCurrentOverviewByMetric200Response**](GetNetworkSensorAlertsCurrentOverviewByMetric200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSensorAlertsOverviewByMetric"></a>
# **getNetworkSensorAlertsOverviewByMetric**
> List&lt;GetNetworkSensorAlertsOverviewByMetric200ResponseInner&gt; getNetworkSensorAlertsOverviewByMetric(networkId, t0, t1, timespan, interval)

Return an overview of alert occurrences over a timespan, by metric

Return an overview of alert occurrences over a timespan, by metric

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SensorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SensorApi apiInstance = new SensorApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    Integer interval = 56; // Integer | The time interval in seconds for returned data. The valid intervals are: 86400, 604800. The default is 604800.
    try {
      List<GetNetworkSensorAlertsOverviewByMetric200ResponseInner> result = apiInstance.getNetworkSensorAlertsOverviewByMetric(networkId, t0, t1, timespan, interval);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensorApi#getNetworkSensorAlertsOverviewByMetric");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 365 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days. | [optional] |
| **interval** | **Integer**| The time interval in seconds for returned data. The valid intervals are: 86400, 604800. The default is 604800. | [optional] |

### Return type

[**List&lt;GetNetworkSensorAlertsOverviewByMetric200ResponseInner&gt;**](GetNetworkSensorAlertsOverviewByMetric200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSensorAlertsProfile"></a>
# **getNetworkSensorAlertsProfile**
> GetNetworkSensorAlertsProfiles200ResponseInner getNetworkSensorAlertsProfile(networkId, id)

Show details of a sensor alert profile for a network.

Show details of a sensor alert profile for a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SensorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SensorApi apiInstance = new SensorApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String id = "id_example"; // String | 
    try {
      GetNetworkSensorAlertsProfiles200ResponseInner result = apiInstance.getNetworkSensorAlertsProfile(networkId, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensorApi#getNetworkSensorAlertsProfile");
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
| **id** | **String**|  | |

### Return type

[**GetNetworkSensorAlertsProfiles200ResponseInner**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSensorAlertsProfiles"></a>
# **getNetworkSensorAlertsProfiles**
> List&lt;GetNetworkSensorAlertsProfiles200ResponseInner&gt; getNetworkSensorAlertsProfiles(networkId)

Lists all sensor alert profiles for a network.

Lists all sensor alert profiles for a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SensorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SensorApi apiInstance = new SensorApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkSensorAlertsProfiles200ResponseInner> result = apiInstance.getNetworkSensorAlertsProfiles(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensorApi#getNetworkSensorAlertsProfiles");
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

[**List&lt;GetNetworkSensorAlertsProfiles200ResponseInner&gt;**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSensorRelationships"></a>
# **getNetworkSensorRelationships**
> List&lt;GetNetworkSensorRelationships200ResponseInner&gt; getNetworkSensorRelationships(networkId)

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
import org.openapitools.client.api.SensorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SensorApi apiInstance = new SensorApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkSensorRelationships200ResponseInner> result = apiInstance.getNetworkSensorRelationships(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensorApi#getNetworkSensorRelationships");
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

<a id="getOrganizationSensorReadingsHistory"></a>
# **getOrganizationSensorReadingsHistory**
> List&lt;GetOrganizationSensorReadingsHistory200ResponseInner&gt; getOrganizationSensorReadingsHistory(organizationId, perPage, startingAfter, endingBefore, t0, t1, timespan, networkIds, serials, metrics)

Return all reported readings from sensors in a given timespan, sorted by timestamp

Return all reported readings from sensors in a given timespan, sorted by timestamp

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SensorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SensorApi apiInstance = new SensorApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 365 days and 6 hours from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours.
    List<String> networkIds = Arrays.asList(); // List<String> | Optional parameter to filter readings by network.
    List<String> serials = Arrays.asList(); // List<String> | Optional parameter to filter readings by sensor.
    List<String> metrics = Arrays.asList(); // List<String> | Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water.
    try {
      List<GetOrganizationSensorReadingsHistory200ResponseInner> result = apiInstance.getOrganizationSensorReadingsHistory(organizationId, perPage, startingAfter, endingBefore, t0, t1, timespan, networkIds, serials, metrics);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensorApi#getOrganizationSensorReadingsHistory");
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
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 365 days and 6 hours from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 2 hours. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter readings by network. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter readings by sensor. | [optional] |
| **metrics** | [**List&lt;String&gt;**](String.md)| Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water. | [optional] |

### Return type

[**List&lt;GetOrganizationSensorReadingsHistory200ResponseInner&gt;**](GetOrganizationSensorReadingsHistory200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="getOrganizationSensorReadingsLatest"></a>
# **getOrganizationSensorReadingsLatest**
> List&lt;GetOrganizationSensorReadingsLatest200ResponseInner&gt; getOrganizationSensorReadingsLatest(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, metrics)

Return the latest available reading for each metric from each sensor, sorted by sensor serial

Return the latest available reading for each metric from each sensor, sorted by sensor serial

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SensorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SensorApi apiInstance = new SensorApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    Integer perPage = 56; // Integer | The number of entries per page returned. Acceptable range is 3 - 100. Default is 100.
    String startingAfter = "startingAfter_example"; // String | A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    String endingBefore = "endingBefore_example"; // String | A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
    List<String> networkIds = Arrays.asList(); // List<String> | Optional parameter to filter readings by network.
    List<String> serials = Arrays.asList(); // List<String> | Optional parameter to filter readings by sensor.
    List<String> metrics = Arrays.asList(); // List<String> | Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water.
    try {
      List<GetOrganizationSensorReadingsLatest200ResponseInner> result = apiInstance.getOrganizationSensorReadingsLatest(organizationId, perPage, startingAfter, endingBefore, networkIds, serials, metrics);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensorApi#getOrganizationSensorReadingsLatest");
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
| **organizationId** | **String**|  | |
| **perPage** | **Integer**| The number of entries per page returned. Acceptable range is 3 - 100. Default is 100. | [optional] |
| **startingAfter** | **String**| A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **endingBefore** | **String**| A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. | [optional] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter readings by network. | [optional] |
| **serials** | [**List&lt;String&gt;**](String.md)| Optional parameter to filter readings by sensor. | [optional] |
| **metrics** | [**List&lt;String&gt;**](String.md)| Types of sensor readings to retrieve. If no metrics are supplied, all available types of readings will be retrieved. Allowed values are battery, button, door, humidity, indoorAirQuality, noise, pm25, temperature, tvoc, and water. | [optional] |

### Return type

[**List&lt;GetOrganizationSensorReadingsLatest200ResponseInner&gt;**](GetOrganizationSensorReadingsLatest200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  * Link - A comma-separated list of first, last, prev, and next relative links used for subsequent paginated requests. <br>  |

<a id="updateDeviceSensorRelationships"></a>
# **updateDeviceSensorRelationships**
> GetDeviceSensorRelationships200ResponseInner updateDeviceSensorRelationships(serial, updateDeviceSensorRelationshipsRequest)

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
import org.openapitools.client.api.SensorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SensorApi apiInstance = new SensorApi(defaultClient);
    String serial = "serial_example"; // String | 
    UpdateDeviceSensorRelationshipsRequest updateDeviceSensorRelationshipsRequest = new UpdateDeviceSensorRelationshipsRequest(); // UpdateDeviceSensorRelationshipsRequest | 
    try {
      GetDeviceSensorRelationships200ResponseInner result = apiInstance.updateDeviceSensorRelationships(serial, updateDeviceSensorRelationshipsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensorApi#updateDeviceSensorRelationships");
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

<a id="updateNetworkSensorAlertsProfile"></a>
# **updateNetworkSensorAlertsProfile**
> GetNetworkSensorAlertsProfiles200ResponseInner updateNetworkSensorAlertsProfile(networkId, id, updateNetworkSensorAlertsProfileRequest)

Updates a sensor alert profile for a network.

Updates a sensor alert profile for a network.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SensorApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    SensorApi apiInstance = new SensorApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String id = "id_example"; // String | 
    UpdateNetworkSensorAlertsProfileRequest updateNetworkSensorAlertsProfileRequest = new UpdateNetworkSensorAlertsProfileRequest(); // UpdateNetworkSensorAlertsProfileRequest | 
    try {
      GetNetworkSensorAlertsProfiles200ResponseInner result = apiInstance.updateNetworkSensorAlertsProfile(networkId, id, updateNetworkSensorAlertsProfileRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SensorApi#updateNetworkSensorAlertsProfile");
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
| **id** | **String**|  | |
| **updateNetworkSensorAlertsProfileRequest** | [**UpdateNetworkSensorAlertsProfileRequest**](UpdateNetworkSensorAlertsProfileRequest.md)|  | [optional] |

### Return type

[**GetNetworkSensorAlertsProfiles200ResponseInner**](GetNetworkSensorAlertsProfiles200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

