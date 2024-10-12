# StagedApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkFirmwareUpgradesStagedEvent_2**](StagedApi.md#createNetworkFirmwareUpgradesStagedEvent_2) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events | Create a Staged Upgrade Event for a network |
| [**createNetworkFirmwareUpgradesStagedGroup_2**](StagedApi.md#createNetworkFirmwareUpgradesStagedGroup_2) | **POST** /networks/{networkId}/firmwareUpgrades/staged/groups | Create a Staged Upgrade Group for a network |
| [**deferNetworkFirmwareUpgradesStagedEvents_2**](StagedApi.md#deferNetworkFirmwareUpgradesStagedEvents_2) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events/defer | Postpone by 1 week all pending staged upgrade stages for a network |
| [**deleteNetworkFirmwareUpgradesStagedGroup_2**](StagedApi.md#deleteNetworkFirmwareUpgradesStagedGroup_2) | **DELETE** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Delete a Staged Upgrade Group |
| [**getNetworkFirmwareUpgradesStagedEvents_2**](StagedApi.md#getNetworkFirmwareUpgradesStagedEvents_2) | **GET** /networks/{networkId}/firmwareUpgrades/staged/events | Get the Staged Upgrade Event from a network |
| [**getNetworkFirmwareUpgradesStagedGroup_2**](StagedApi.md#getNetworkFirmwareUpgradesStagedGroup_2) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Get a Staged Upgrade Group from a network |
| [**getNetworkFirmwareUpgradesStagedGroups_2**](StagedApi.md#getNetworkFirmwareUpgradesStagedGroups_2) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups | List of Staged Upgrade Groups in a network |
| [**getNetworkFirmwareUpgradesStagedStages_2**](StagedApi.md#getNetworkFirmwareUpgradesStagedStages_2) | **GET** /networks/{networkId}/firmwareUpgrades/staged/stages | Order of Staged Upgrade Groups in a network |
| [**rollbacksNetworkFirmwareUpgradesStagedEvents_2**](StagedApi.md#rollbacksNetworkFirmwareUpgradesStagedEvents_2) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events/rollbacks | Rollback a Staged Upgrade Event for a network |
| [**updateNetworkFirmwareUpgradesStagedEvents_2**](StagedApi.md#updateNetworkFirmwareUpgradesStagedEvents_2) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/events | Update the Staged Upgrade Event for a network |
| [**updateNetworkFirmwareUpgradesStagedGroup_2**](StagedApi.md#updateNetworkFirmwareUpgradesStagedGroup_2) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Update a Staged Upgrade Group for a network |
| [**updateNetworkFirmwareUpgradesStagedStages_2**](StagedApi.md#updateNetworkFirmwareUpgradesStagedStages_2) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/stages | Assign Staged Upgrade Group order in the sequence. |


<a id="createNetworkFirmwareUpgradesStagedEvent_2"></a>
# **createNetworkFirmwareUpgradesStagedEvent_2**
> GetNetworkFirmwareUpgradesStagedEvents200Response createNetworkFirmwareUpgradesStagedEvent_2(networkId, createNetworkFirmwareUpgradesStagedEventRequest)

Create a Staged Upgrade Event for a network

Create a Staged Upgrade Event for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagedApi apiInstance = new StagedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkFirmwareUpgradesStagedEventRequest createNetworkFirmwareUpgradesStagedEventRequest = new CreateNetworkFirmwareUpgradesStagedEventRequest(); // CreateNetworkFirmwareUpgradesStagedEventRequest | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.createNetworkFirmwareUpgradesStagedEvent_2(networkId, createNetworkFirmwareUpgradesStagedEventRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagedApi#createNetworkFirmwareUpgradesStagedEvent_2");
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
| **createNetworkFirmwareUpgradesStagedEventRequest** | [**CreateNetworkFirmwareUpgradesStagedEventRequest**](CreateNetworkFirmwareUpgradesStagedEventRequest.md)|  | |

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="createNetworkFirmwareUpgradesStagedGroup_2"></a>
# **createNetworkFirmwareUpgradesStagedGroup_2**
> Object createNetworkFirmwareUpgradesStagedGroup_2(networkId, createNetworkFirmwareUpgradesStagedGroupRequest)

Create a Staged Upgrade Group for a network

Create a Staged Upgrade Group for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagedApi apiInstance = new StagedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkFirmwareUpgradesStagedGroupRequest createNetworkFirmwareUpgradesStagedGroupRequest = new CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
    try {
      Object result = apiInstance.createNetworkFirmwareUpgradesStagedGroup_2(networkId, createNetworkFirmwareUpgradesStagedGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagedApi#createNetworkFirmwareUpgradesStagedGroup_2");
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
| **createNetworkFirmwareUpgradesStagedGroupRequest** | [**CreateNetworkFirmwareUpgradesStagedGroupRequest**](CreateNetworkFirmwareUpgradesStagedGroupRequest.md)|  | |

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

<a id="deferNetworkFirmwareUpgradesStagedEvents_2"></a>
# **deferNetworkFirmwareUpgradesStagedEvents_2**
> GetNetworkFirmwareUpgradesStagedEvents200Response deferNetworkFirmwareUpgradesStagedEvents_2(networkId)

Postpone by 1 week all pending staged upgrade stages for a network

Postpone by 1 week all pending staged upgrade stages for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagedApi apiInstance = new StagedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.deferNetworkFirmwareUpgradesStagedEvents_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagedApi#deferNetworkFirmwareUpgradesStagedEvents_2");
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

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="deleteNetworkFirmwareUpgradesStagedGroup_2"></a>
# **deleteNetworkFirmwareUpgradesStagedGroup_2**
> deleteNetworkFirmwareUpgradesStagedGroup_2(networkId, groupId)

Delete a Staged Upgrade Group

Delete a Staged Upgrade Group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagedApi apiInstance = new StagedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupId = "groupId_example"; // String | 
    try {
      apiInstance.deleteNetworkFirmwareUpgradesStagedGroup_2(networkId, groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagedApi#deleteNetworkFirmwareUpgradesStagedGroup_2");
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
| **groupId** | **String**|  | |

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

<a id="getNetworkFirmwareUpgradesStagedEvents_2"></a>
# **getNetworkFirmwareUpgradesStagedEvents_2**
> GetNetworkFirmwareUpgradesStagedEvents200Response getNetworkFirmwareUpgradesStagedEvents_2(networkId)

Get the Staged Upgrade Event from a network

Get the Staged Upgrade Event from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagedApi apiInstance = new StagedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.getNetworkFirmwareUpgradesStagedEvents_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagedApi#getNetworkFirmwareUpgradesStagedEvents_2");
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

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkFirmwareUpgradesStagedGroup_2"></a>
# **getNetworkFirmwareUpgradesStagedGroup_2**
> GetNetworkFirmwareUpgradesStagedGroups200ResponseInner getNetworkFirmwareUpgradesStagedGroup_2(networkId, groupId)

Get a Staged Upgrade Group from a network

Get a Staged Upgrade Group from a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagedApi apiInstance = new StagedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupId = "groupId_example"; // String | 
    try {
      GetNetworkFirmwareUpgradesStagedGroups200ResponseInner result = apiInstance.getNetworkFirmwareUpgradesStagedGroup_2(networkId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagedApi#getNetworkFirmwareUpgradesStagedGroup_2");
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
| **groupId** | **String**|  | |

### Return type

[**GetNetworkFirmwareUpgradesStagedGroups200ResponseInner**](GetNetworkFirmwareUpgradesStagedGroups200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkFirmwareUpgradesStagedGroups_2"></a>
# **getNetworkFirmwareUpgradesStagedGroups_2**
> List&lt;GetNetworkFirmwareUpgradesStagedGroups200ResponseInner&gt; getNetworkFirmwareUpgradesStagedGroups_2(networkId)

List of Staged Upgrade Groups in a network

List of Staged Upgrade Groups in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagedApi apiInstance = new StagedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkFirmwareUpgradesStagedGroups200ResponseInner> result = apiInstance.getNetworkFirmwareUpgradesStagedGroups_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagedApi#getNetworkFirmwareUpgradesStagedGroups_2");
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

[**List&lt;GetNetworkFirmwareUpgradesStagedGroups200ResponseInner&gt;**](GetNetworkFirmwareUpgradesStagedGroups200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="getNetworkFirmwareUpgradesStagedStages_2"></a>
# **getNetworkFirmwareUpgradesStagedStages_2**
> List&lt;GetNetworkFirmwareUpgradesStagedStages200ResponseInner&gt; getNetworkFirmwareUpgradesStagedStages_2(networkId)

Order of Staged Upgrade Groups in a network

Order of Staged Upgrade Groups in a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagedApi apiInstance = new StagedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkFirmwareUpgradesStagedStages200ResponseInner> result = apiInstance.getNetworkFirmwareUpgradesStagedStages_2(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagedApi#getNetworkFirmwareUpgradesStagedStages_2");
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

[**List&lt;GetNetworkFirmwareUpgradesStagedStages200ResponseInner&gt;**](GetNetworkFirmwareUpgradesStagedStages200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="rollbacksNetworkFirmwareUpgradesStagedEvents_2"></a>
# **rollbacksNetworkFirmwareUpgradesStagedEvents_2**
> GetNetworkFirmwareUpgradesStagedEvents200Response rollbacksNetworkFirmwareUpgradesStagedEvents_2(networkId, rollbacksNetworkFirmwareUpgradesStagedEventsRequest)

Rollback a Staged Upgrade Event for a network

Rollback a Staged Upgrade Event for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagedApi apiInstance = new StagedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    RollbacksNetworkFirmwareUpgradesStagedEventsRequest rollbacksNetworkFirmwareUpgradesStagedEventsRequest = new RollbacksNetworkFirmwareUpgradesStagedEventsRequest(); // RollbacksNetworkFirmwareUpgradesStagedEventsRequest | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.rollbacksNetworkFirmwareUpgradesStagedEvents_2(networkId, rollbacksNetworkFirmwareUpgradesStagedEventsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagedApi#rollbacksNetworkFirmwareUpgradesStagedEvents_2");
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
| **rollbacksNetworkFirmwareUpgradesStagedEventsRequest** | [**RollbacksNetworkFirmwareUpgradesStagedEventsRequest**](RollbacksNetworkFirmwareUpgradesStagedEventsRequest.md)|  | |

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkFirmwareUpgradesStagedEvents_2"></a>
# **updateNetworkFirmwareUpgradesStagedEvents_2**
> GetNetworkFirmwareUpgradesStagedEvents200Response updateNetworkFirmwareUpgradesStagedEvents_2(networkId, updateNetworkFirmwareUpgradesStagedEventsRequest)

Update the Staged Upgrade Event for a network

Update the Staged Upgrade Event for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagedApi apiInstance = new StagedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkFirmwareUpgradesStagedEventsRequest updateNetworkFirmwareUpgradesStagedEventsRequest = new UpdateNetworkFirmwareUpgradesStagedEventsRequest(); // UpdateNetworkFirmwareUpgradesStagedEventsRequest | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.updateNetworkFirmwareUpgradesStagedEvents_2(networkId, updateNetworkFirmwareUpgradesStagedEventsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagedApi#updateNetworkFirmwareUpgradesStagedEvents_2");
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
| **updateNetworkFirmwareUpgradesStagedEventsRequest** | [**UpdateNetworkFirmwareUpgradesStagedEventsRequest**](UpdateNetworkFirmwareUpgradesStagedEventsRequest.md)|  | |

### Return type

[**GetNetworkFirmwareUpgradesStagedEvents200Response**](GetNetworkFirmwareUpgradesStagedEvents200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="updateNetworkFirmwareUpgradesStagedGroup_2"></a>
# **updateNetworkFirmwareUpgradesStagedGroup_2**
> Object updateNetworkFirmwareUpgradesStagedGroup_2(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest)

Update a Staged Upgrade Group for a network

Update a Staged Upgrade Group for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagedApi apiInstance = new StagedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupId = "groupId_example"; // String | 
    CreateNetworkFirmwareUpgradesStagedGroupRequest createNetworkFirmwareUpgradesStagedGroupRequest = new CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
    try {
      Object result = apiInstance.updateNetworkFirmwareUpgradesStagedGroup_2(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagedApi#updateNetworkFirmwareUpgradesStagedGroup_2");
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
| **groupId** | **String**|  | |
| **createNetworkFirmwareUpgradesStagedGroupRequest** | [**CreateNetworkFirmwareUpgradesStagedGroupRequest**](CreateNetworkFirmwareUpgradesStagedGroupRequest.md)|  | |

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

<a id="updateNetworkFirmwareUpgradesStagedStages_2"></a>
# **updateNetworkFirmwareUpgradesStagedStages_2**
> List&lt;GetNetworkFirmwareUpgradesStagedStages200ResponseInner&gt; updateNetworkFirmwareUpgradesStagedStages_2(networkId, updateNetworkFirmwareUpgradesStagedStagesRequest)

Assign Staged Upgrade Group order in the sequence.

Assign Staged Upgrade Group order in the sequence.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StagedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagedApi apiInstance = new StagedApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkFirmwareUpgradesStagedStagesRequest updateNetworkFirmwareUpgradesStagedStagesRequest = new UpdateNetworkFirmwareUpgradesStagedStagesRequest(); // UpdateNetworkFirmwareUpgradesStagedStagesRequest | 
    try {
      List<GetNetworkFirmwareUpgradesStagedStages200ResponseInner> result = apiInstance.updateNetworkFirmwareUpgradesStagedStages_2(networkId, updateNetworkFirmwareUpgradesStagedStagesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagedApi#updateNetworkFirmwareUpgradesStagedStages_2");
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
| **updateNetworkFirmwareUpgradesStagedStagesRequest** | [**UpdateNetworkFirmwareUpgradesStagedStagesRequest**](UpdateNetworkFirmwareUpgradesStagedStagesRequest.md)|  | [optional] |

### Return type

[**List&lt;GetNetworkFirmwareUpgradesStagedStages200ResponseInner&gt;**](GetNetworkFirmwareUpgradesStagedStages200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

