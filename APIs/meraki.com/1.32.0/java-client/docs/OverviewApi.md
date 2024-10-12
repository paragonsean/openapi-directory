# OverviewApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDeviceCameraAnalyticsOverview_2**](OverviewApi.md#getDeviceCameraAnalyticsOverview_2) | **GET** /devices/{serial}/camera/analytics/overview | Returns an overview of aggregate analytics data for a timespan |
| [**getNetworkClientsOverview_2**](OverviewApi.md#getNetworkClientsOverview_2) | **GET** /networks/{networkId}/clients/overview | Return overview statistics for network clients |
| [**getNetworkSensorAlertsCurrentOverviewByMetric_3**](OverviewApi.md#getNetworkSensorAlertsCurrentOverviewByMetric_3) | **GET** /networks/{networkId}/sensor/alerts/current/overview/byMetric | Return an overview of currently alerting sensors by metric |
| [**getNetworkSensorAlertsOverviewByMetric_2**](OverviewApi.md#getNetworkSensorAlertsOverviewByMetric_2) | **GET** /networks/{networkId}/sensor/alerts/overview/byMetric | Return an overview of alert occurrences over a timespan, by metric |
| [**getOrganizationAdaptivePolicyOverview_2**](OverviewApi.md#getOrganizationAdaptivePolicyOverview_2) | **GET** /organizations/{organizationId}/adaptivePolicy/overview | Returns adaptive policy aggregate statistics for an organization |
| [**getOrganizationApiRequestsOverviewResponseCodesByInterval_2**](OverviewApi.md#getOrganizationApiRequestsOverviewResponseCodesByInterval_2) | **GET** /organizations/{organizationId}/apiRequests/overview/responseCodes/byInterval | Tracks organizations&#39; API requests by response code across a given time period |
| [**getOrganizationApiRequestsOverview_2**](OverviewApi.md#getOrganizationApiRequestsOverview_2) | **GET** /organizations/{organizationId}/apiRequests/overview | Return an aggregated overview of API requests data |
| [**getOrganizationClientsOverview_2**](OverviewApi.md#getOrganizationClientsOverview_2) | **GET** /organizations/{organizationId}/clients/overview | Return summary information around client data usage (in mb) across the given organization. |
| [**getOrganizationDevicesStatusesOverview_3**](OverviewApi.md#getOrganizationDevicesStatusesOverview_3) | **GET** /organizations/{organizationId}/devices/statuses/overview | Return an overview of current device statuses |
| [**getOrganizationLicensesOverview_2**](OverviewApi.md#getOrganizationLicensesOverview_2) | **GET** /organizations/{organizationId}/licenses/overview | Return an overview of the license state for an organization |


<a id="getDeviceCameraAnalyticsOverview_2"></a>
# **getDeviceCameraAnalyticsOverview_2**
> List&lt;Object&gt; getDeviceCameraAnalyticsOverview_2(serial, t0, t1, timespan, objectType)

Returns an overview of aggregate analytics data for a timespan

Returns an overview of aggregate analytics data for a timespan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OverviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OverviewApi apiInstance = new OverviewApi(defaultClient);
    String serial = "serial_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 7 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour.
    String objectType = "person"; // String | [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle].
    try {
      List<Object> result = apiInstance.getDeviceCameraAnalyticsOverview_2(serial, t0, t1, timespan, objectType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OverviewApi#getDeviceCameraAnalyticsOverview_2");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 365 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 7 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 7 days. The default is 1 hour. | [optional] |
| **objectType** | **String**| [optional] The object type for which analytics will be retrieved. The default object type is person. The available types are [person, vehicle]. | [optional] [enum: person, vehicle] |

### Return type

**List&lt;Object&gt;**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkClientsOverview_2"></a>
# **getNetworkClientsOverview_2**
> Object getNetworkClientsOverview_2(networkId, t0, t1, timespan, resolution)

Return overview statistics for network clients

Return overview statistics for network clients

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OverviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OverviewApi apiInstance = new OverviewApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    Integer resolution = 56; // Integer | The time resolution in seconds for returned data. The valid resolutions are: 7200, 86400, 604800, 2592000. The default is 604800.
    try {
      Object result = apiInstance.getNetworkClientsOverview_2(networkId, t0, t1, timespan, resolution);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OverviewApi#getNetworkClientsOverview_2");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |
| **resolution** | **Integer**| The time resolution in seconds for returned data. The valid resolutions are: 7200, 86400, 604800, 2592000. The default is 604800. | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkSensorAlertsCurrentOverviewByMetric_3"></a>
# **getNetworkSensorAlertsCurrentOverviewByMetric_3**
> GetNetworkSensorAlertsCurrentOverviewByMetric200Response getNetworkSensorAlertsCurrentOverviewByMetric_3(networkId)

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
import org.openapitools.client.api.OverviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OverviewApi apiInstance = new OverviewApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkSensorAlertsCurrentOverviewByMetric200Response result = apiInstance.getNetworkSensorAlertsCurrentOverviewByMetric_3(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OverviewApi#getNetworkSensorAlertsCurrentOverviewByMetric_3");
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

<a id="getNetworkSensorAlertsOverviewByMetric_2"></a>
# **getNetworkSensorAlertsOverviewByMetric_2**
> List&lt;GetNetworkSensorAlertsOverviewByMetric200ResponseInner&gt; getNetworkSensorAlertsOverviewByMetric_2(networkId, t0, t1, timespan, interval)

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
import org.openapitools.client.api.OverviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OverviewApi apiInstance = new OverviewApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 365 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 7 days.
    Integer interval = 56; // Integer | The time interval in seconds for returned data. The valid intervals are: 86400, 604800. The default is 604800.
    try {
      List<GetNetworkSensorAlertsOverviewByMetric200ResponseInner> result = apiInstance.getNetworkSensorAlertsOverviewByMetric_2(networkId, t0, t1, timespan, interval);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OverviewApi#getNetworkSensorAlertsOverviewByMetric_2");
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

<a id="getOrganizationAdaptivePolicyOverview_2"></a>
# **getOrganizationAdaptivePolicyOverview_2**
> GetOrganizationAdaptivePolicyOverview200Response getOrganizationAdaptivePolicyOverview_2(organizationId)

Returns adaptive policy aggregate statistics for an organization

Returns adaptive policy aggregate statistics for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OverviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OverviewApi apiInstance = new OverviewApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      GetOrganizationAdaptivePolicyOverview200Response result = apiInstance.getOrganizationAdaptivePolicyOverview_2(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OverviewApi#getOrganizationAdaptivePolicyOverview_2");
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

### Return type

[**GetOrganizationAdaptivePolicyOverview200Response**](GetOrganizationAdaptivePolicyOverview200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationApiRequestsOverviewResponseCodesByInterval_2"></a>
# **getOrganizationApiRequestsOverviewResponseCodesByInterval_2**
> List&lt;GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner&gt; getOrganizationApiRequestsOverviewResponseCodesByInterval_2(organizationId, t0, t1, timespan, interval, version, operationIds, sourceIps, adminIds, userAgent)

Tracks organizations&#39; API requests by response code across a given time period

Tracks organizations&#39; API requests by response code across a given time period

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OverviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OverviewApi apiInstance = new OverviewApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated.
    Integer interval = 56; // Integer | The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided.
    Integer version = 0; // Integer | Filter by API version of the endpoint. Allowable values are: [0, 1]
    List<String> operationIds = Arrays.asList(); // List<String> | Filter by operation ID of the endpoint
    List<String> sourceIps = Arrays.asList(); // List<String> | Filter by source IP that made the API request
    List<String> adminIds = Arrays.asList(); // List<String> | Filter by admin ID of user that made the API request
    String userAgent = "userAgent_example"; // String | Filter by user agent string for API request. This will filter by a complete or partial match.
    try {
      List<GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner> result = apiInstance.getOrganizationApiRequestsOverviewResponseCodesByInterval_2(organizationId, t0, t1, timespan, interval, version, operationIds, sourceIps, adminIds, userAgent);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OverviewApi#getOrganizationApiRequestsOverviewResponseCodesByInterval_2");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. If interval is provided, the timespan will be autocalculated. | [optional] |
| **interval** | **Integer**| The time interval in seconds for returned data. The valid intervals are: 120, 3600, 14400, 21600. The default is 21600. Interval is calculated if time params are provided. | [optional] |
| **version** | **Integer**| Filter by API version of the endpoint. Allowable values are: [0, 1] | [optional] [enum: 0, 1] |
| **operationIds** | [**List&lt;String&gt;**](String.md)| Filter by operation ID of the endpoint | [optional] |
| **sourceIps** | [**List&lt;String&gt;**](String.md)| Filter by source IP that made the API request | [optional] |
| **adminIds** | [**List&lt;String&gt;**](String.md)| Filter by admin ID of user that made the API request | [optional] |
| **userAgent** | **String**| Filter by user agent string for API request. This will filter by a complete or partial match. | [optional] |

### Return type

[**List&lt;GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner&gt;**](GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationApiRequestsOverview_2"></a>
# **getOrganizationApiRequestsOverview_2**
> Object getOrganizationApiRequestsOverview_2(organizationId, t0, t1, timespan)

Return an aggregated overview of API requests data

Return an aggregated overview of API requests data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OverviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OverviewApi apiInstance = new OverviewApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data. The maximum lookback period is 31 days from today.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days.
    try {
      Object result = apiInstance.getOrganizationApiRequestsOverview_2(organizationId, t0, t1, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OverviewApi#getOrganizationApiRequestsOverview_2");
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
| **t0** | **String**| The beginning of the timespan for the data. The maximum lookback period is 31 days from today. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 31 days. | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationClientsOverview_2"></a>
# **getOrganizationClientsOverview_2**
> GetOrganizationClientsOverview200Response getOrganizationClientsOverview_2(organizationId, t0, t1, timespan)

Return summary information around client data usage (in mb) across the given organization.

Return summary information around client data usage (in mb) across the given organization.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OverviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OverviewApi apiInstance = new OverviewApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    String t0 = "t0_example"; // String | The beginning of the timespan for the data.
    String t1 = "t1_example"; // String | The end of the timespan for the data. t1 can be a maximum of 31 days after t0.
    Float timespan = 3.4F; // Float | The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day.
    try {
      GetOrganizationClientsOverview200Response result = apiInstance.getOrganizationClientsOverview_2(organizationId, t0, t1, timespan);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OverviewApi#getOrganizationClientsOverview_2");
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
| **t0** | **String**| The beginning of the timespan for the data. | [optional] |
| **t1** | **String**| The end of the timespan for the data. t1 can be a maximum of 31 days after t0. | [optional] |
| **timespan** | **Float**| The timespan for which the information will be fetched. If specifying timespan, do not specify parameters t0 and t1. The value must be in seconds and be less than or equal to 31 days. The default is 1 day. | [optional] |

### Return type

[**GetOrganizationClientsOverview200Response**](GetOrganizationClientsOverview200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationDevicesStatusesOverview_3"></a>
# **getOrganizationDevicesStatusesOverview_3**
> GetOrganizationDevicesStatusesOverview200Response getOrganizationDevicesStatusesOverview_3(organizationId, productTypes, networkIds)

Return an overview of current device statuses

Return an overview of current device statuses

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OverviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OverviewApi apiInstance = new OverviewApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    List<String> productTypes = Arrays.asList(); // List<String> | An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor.
    List<String> networkIds = Arrays.asList(); // List<String> | An optional parameter to filter device statuses by network.
    try {
      GetOrganizationDevicesStatusesOverview200Response result = apiInstance.getOrganizationDevicesStatusesOverview_3(organizationId, productTypes, networkIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OverviewApi#getOrganizationDevicesStatusesOverview_3");
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
| **productTypes** | [**List&lt;String&gt;**](String.md)| An optional parameter to filter device statuses by product type. Valid types are wireless, appliance, switch, systemsManager, camera, cellularGateway, and sensor. | [optional] [enum: appliance, camera, cellularGateway, sensor, switch, systemsManager, wireless] |
| **networkIds** | [**List&lt;String&gt;**](String.md)| An optional parameter to filter device statuses by network. | [optional] |

### Return type

[**GetOrganizationDevicesStatusesOverview200Response**](GetOrganizationDevicesStatusesOverview200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getOrganizationLicensesOverview_2"></a>
# **getOrganizationLicensesOverview_2**
> Object getOrganizationLicensesOverview_2(organizationId)

Return an overview of the license state for an organization

Return an overview of the license state for an organization

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OverviewApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    OverviewApi apiInstance = new OverviewApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    try {
      Object result = apiInstance.getOrganizationLicensesOverview_2(organizationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OverviewApi#getOrganizationLicensesOverview_2");
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

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

