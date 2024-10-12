# PortSchedulesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSwitchPortSchedule_1**](PortSchedulesApi.md#createNetworkSwitchPortSchedule_1) | **POST** /networks/{networkId}/switch/portSchedules | Add a switch port schedule |
| [**deleteNetworkSwitchPortSchedule_1**](PortSchedulesApi.md#deleteNetworkSwitchPortSchedule_1) | **DELETE** /networks/{networkId}/switch/portSchedules/{portScheduleId} | Delete a switch port schedule |
| [**getNetworkSwitchPortSchedules_1**](PortSchedulesApi.md#getNetworkSwitchPortSchedules_1) | **GET** /networks/{networkId}/switch/portSchedules | List switch port schedules |
| [**updateNetworkSwitchPortSchedule_1**](PortSchedulesApi.md#updateNetworkSwitchPortSchedule_1) | **PUT** /networks/{networkId}/switch/portSchedules/{portScheduleId} | Update a switch port schedule |


<a id="createNetworkSwitchPortSchedule_1"></a>
# **createNetworkSwitchPortSchedule_1**
> Object createNetworkSwitchPortSchedule_1(networkId, createNetworkSwitchPortScheduleRequest)

Add a switch port schedule

Add a switch port schedule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PortSchedulesApi apiInstance = new PortSchedulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchPortScheduleRequest createNetworkSwitchPortScheduleRequest = new CreateNetworkSwitchPortScheduleRequest(); // CreateNetworkSwitchPortScheduleRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchPortSchedule_1(networkId, createNetworkSwitchPortScheduleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortSchedulesApi#createNetworkSwitchPortSchedule_1");
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
| **createNetworkSwitchPortScheduleRequest** | [**CreateNetworkSwitchPortScheduleRequest**](CreateNetworkSwitchPortScheduleRequest.md)|  | |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="deleteNetworkSwitchPortSchedule_1"></a>
# **deleteNetworkSwitchPortSchedule_1**
> deleteNetworkSwitchPortSchedule_1(networkId, portScheduleId)

Delete a switch port schedule

Delete a switch port schedule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PortSchedulesApi apiInstance = new PortSchedulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String portScheduleId = "portScheduleId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchPortSchedule_1(networkId, portScheduleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortSchedulesApi#deleteNetworkSwitchPortSchedule_1");
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
| **portScheduleId** | **String**|  | |

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

<a id="getNetworkSwitchPortSchedules_1"></a>
# **getNetworkSwitchPortSchedules_1**
> List&lt;Object&gt; getNetworkSwitchPortSchedules_1(networkId)

List switch port schedules

List switch port schedules

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PortSchedulesApi apiInstance = new PortSchedulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchPortSchedules_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortSchedulesApi#getNetworkSwitchPortSchedules_1");
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

<a id="updateNetworkSwitchPortSchedule_1"></a>
# **updateNetworkSwitchPortSchedule_1**
> Object updateNetworkSwitchPortSchedule_1(networkId, portScheduleId, updateNetworkSwitchPortScheduleRequest)

Update a switch port schedule

Update a switch port schedule

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PortSchedulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PortSchedulesApi apiInstance = new PortSchedulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String portScheduleId = "portScheduleId_example"; // String | 
    UpdateNetworkSwitchPortScheduleRequest updateNetworkSwitchPortScheduleRequest = new UpdateNetworkSwitchPortScheduleRequest(); // UpdateNetworkSwitchPortScheduleRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchPortSchedule_1(networkId, portScheduleId, updateNetworkSwitchPortScheduleRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PortSchedulesApi#updateNetworkSwitchPortSchedule_1");
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
| **portScheduleId** | **String**|  | |
| **updateNetworkSwitchPortScheduleRequest** | [**UpdateNetworkSwitchPortScheduleRequest**](UpdateNetworkSwitchPortScheduleRequest.md)|  | [optional] |

### Return type

**Object**

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

