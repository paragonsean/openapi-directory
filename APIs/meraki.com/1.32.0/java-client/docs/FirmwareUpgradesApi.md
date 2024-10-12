# FirmwareUpgradesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkFirmwareUpgradesRollback_1**](FirmwareUpgradesApi.md#createNetworkFirmwareUpgradesRollback_1) | **POST** /networks/{networkId}/firmwareUpgrades/rollbacks | Rollback a Firmware Upgrade For A Network |
| [**createNetworkFirmwareUpgradesStagedEvent_1**](FirmwareUpgradesApi.md#createNetworkFirmwareUpgradesStagedEvent_1) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events | Create a Staged Upgrade Event for a network |
| [**createNetworkFirmwareUpgradesStagedGroup_1**](FirmwareUpgradesApi.md#createNetworkFirmwareUpgradesStagedGroup_1) | **POST** /networks/{networkId}/firmwareUpgrades/staged/groups | Create a Staged Upgrade Group for a network |
| [**deferNetworkFirmwareUpgradesStagedEvents_1**](FirmwareUpgradesApi.md#deferNetworkFirmwareUpgradesStagedEvents_1) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events/defer | Postpone by 1 week all pending staged upgrade stages for a network |
| [**deleteNetworkFirmwareUpgradesStagedGroup_1**](FirmwareUpgradesApi.md#deleteNetworkFirmwareUpgradesStagedGroup_1) | **DELETE** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Delete a Staged Upgrade Group |
| [**getNetworkFirmwareUpgradesStagedEvents_1**](FirmwareUpgradesApi.md#getNetworkFirmwareUpgradesStagedEvents_1) | **GET** /networks/{networkId}/firmwareUpgrades/staged/events | Get the Staged Upgrade Event from a network |
| [**getNetworkFirmwareUpgradesStagedGroup_1**](FirmwareUpgradesApi.md#getNetworkFirmwareUpgradesStagedGroup_1) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Get a Staged Upgrade Group from a network |
| [**getNetworkFirmwareUpgradesStagedGroups_1**](FirmwareUpgradesApi.md#getNetworkFirmwareUpgradesStagedGroups_1) | **GET** /networks/{networkId}/firmwareUpgrades/staged/groups | List of Staged Upgrade Groups in a network |
| [**getNetworkFirmwareUpgradesStagedStages_1**](FirmwareUpgradesApi.md#getNetworkFirmwareUpgradesStagedStages_1) | **GET** /networks/{networkId}/firmwareUpgrades/staged/stages | Order of Staged Upgrade Groups in a network |
| [**getNetworkFirmwareUpgrades_1**](FirmwareUpgradesApi.md#getNetworkFirmwareUpgrades_1) | **GET** /networks/{networkId}/firmwareUpgrades | Get firmware upgrade information for a network |
| [**rollbacksNetworkFirmwareUpgradesStagedEvents_1**](FirmwareUpgradesApi.md#rollbacksNetworkFirmwareUpgradesStagedEvents_1) | **POST** /networks/{networkId}/firmwareUpgrades/staged/events/rollbacks | Rollback a Staged Upgrade Event for a network |
| [**updateNetworkFirmwareUpgradesStagedEvents_1**](FirmwareUpgradesApi.md#updateNetworkFirmwareUpgradesStagedEvents_1) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/events | Update the Staged Upgrade Event for a network |
| [**updateNetworkFirmwareUpgradesStagedGroup_1**](FirmwareUpgradesApi.md#updateNetworkFirmwareUpgradesStagedGroup_1) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId} | Update a Staged Upgrade Group for a network |
| [**updateNetworkFirmwareUpgradesStagedStages_1**](FirmwareUpgradesApi.md#updateNetworkFirmwareUpgradesStagedStages_1) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/stages | Assign Staged Upgrade Group order in the sequence. |
| [**updateNetworkFirmwareUpgrades_1**](FirmwareUpgradesApi.md#updateNetworkFirmwareUpgrades_1) | **PUT** /networks/{networkId}/firmwareUpgrades | Update firmware upgrade information for a network |


<a id="createNetworkFirmwareUpgradesRollback_1"></a>
# **createNetworkFirmwareUpgradesRollback_1**
> CreateNetworkFirmwareUpgradesRollback200Response createNetworkFirmwareUpgradesRollback_1(networkId, createNetworkFirmwareUpgradesRollbackRequest)

Rollback a Firmware Upgrade For A Network

Rollback a Firmware Upgrade For A Network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkFirmwareUpgradesRollbackRequest createNetworkFirmwareUpgradesRollbackRequest = new CreateNetworkFirmwareUpgradesRollbackRequest(); // CreateNetworkFirmwareUpgradesRollbackRequest | 
    try {
      CreateNetworkFirmwareUpgradesRollback200Response result = apiInstance.createNetworkFirmwareUpgradesRollback_1(networkId, createNetworkFirmwareUpgradesRollbackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#createNetworkFirmwareUpgradesRollback_1");
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
| **createNetworkFirmwareUpgradesRollbackRequest** | [**CreateNetworkFirmwareUpgradesRollbackRequest**](CreateNetworkFirmwareUpgradesRollbackRequest.md)|  | |

### Return type

[**CreateNetworkFirmwareUpgradesRollback200Response**](CreateNetworkFirmwareUpgradesRollback200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="createNetworkFirmwareUpgradesStagedEvent_1"></a>
# **createNetworkFirmwareUpgradesStagedEvent_1**
> GetNetworkFirmwareUpgradesStagedEvents200Response createNetworkFirmwareUpgradesStagedEvent_1(networkId, createNetworkFirmwareUpgradesStagedEventRequest)

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
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkFirmwareUpgradesStagedEventRequest createNetworkFirmwareUpgradesStagedEventRequest = new CreateNetworkFirmwareUpgradesStagedEventRequest(); // CreateNetworkFirmwareUpgradesStagedEventRequest | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.createNetworkFirmwareUpgradesStagedEvent_1(networkId, createNetworkFirmwareUpgradesStagedEventRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#createNetworkFirmwareUpgradesStagedEvent_1");
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

<a id="createNetworkFirmwareUpgradesStagedGroup_1"></a>
# **createNetworkFirmwareUpgradesStagedGroup_1**
> Object createNetworkFirmwareUpgradesStagedGroup_1(networkId, createNetworkFirmwareUpgradesStagedGroupRequest)

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
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkFirmwareUpgradesStagedGroupRequest createNetworkFirmwareUpgradesStagedGroupRequest = new CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
    try {
      Object result = apiInstance.createNetworkFirmwareUpgradesStagedGroup_1(networkId, createNetworkFirmwareUpgradesStagedGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#createNetworkFirmwareUpgradesStagedGroup_1");
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

<a id="deferNetworkFirmwareUpgradesStagedEvents_1"></a>
# **deferNetworkFirmwareUpgradesStagedEvents_1**
> GetNetworkFirmwareUpgradesStagedEvents200Response deferNetworkFirmwareUpgradesStagedEvents_1(networkId)

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
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.deferNetworkFirmwareUpgradesStagedEvents_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#deferNetworkFirmwareUpgradesStagedEvents_1");
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

<a id="deleteNetworkFirmwareUpgradesStagedGroup_1"></a>
# **deleteNetworkFirmwareUpgradesStagedGroup_1**
> deleteNetworkFirmwareUpgradesStagedGroup_1(networkId, groupId)

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
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupId = "groupId_example"; // String | 
    try {
      apiInstance.deleteNetworkFirmwareUpgradesStagedGroup_1(networkId, groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#deleteNetworkFirmwareUpgradesStagedGroup_1");
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

<a id="getNetworkFirmwareUpgradesStagedEvents_1"></a>
# **getNetworkFirmwareUpgradesStagedEvents_1**
> GetNetworkFirmwareUpgradesStagedEvents200Response getNetworkFirmwareUpgradesStagedEvents_1(networkId)

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
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.getNetworkFirmwareUpgradesStagedEvents_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#getNetworkFirmwareUpgradesStagedEvents_1");
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

<a id="getNetworkFirmwareUpgradesStagedGroup_1"></a>
# **getNetworkFirmwareUpgradesStagedGroup_1**
> GetNetworkFirmwareUpgradesStagedGroups200ResponseInner getNetworkFirmwareUpgradesStagedGroup_1(networkId, groupId)

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
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupId = "groupId_example"; // String | 
    try {
      GetNetworkFirmwareUpgradesStagedGroups200ResponseInner result = apiInstance.getNetworkFirmwareUpgradesStagedGroup_1(networkId, groupId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#getNetworkFirmwareUpgradesStagedGroup_1");
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

<a id="getNetworkFirmwareUpgradesStagedGroups_1"></a>
# **getNetworkFirmwareUpgradesStagedGroups_1**
> List&lt;GetNetworkFirmwareUpgradesStagedGroups200ResponseInner&gt; getNetworkFirmwareUpgradesStagedGroups_1(networkId)

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
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkFirmwareUpgradesStagedGroups200ResponseInner> result = apiInstance.getNetworkFirmwareUpgradesStagedGroups_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#getNetworkFirmwareUpgradesStagedGroups_1");
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

<a id="getNetworkFirmwareUpgradesStagedStages_1"></a>
# **getNetworkFirmwareUpgradesStagedStages_1**
> List&lt;GetNetworkFirmwareUpgradesStagedStages200ResponseInner&gt; getNetworkFirmwareUpgradesStagedStages_1(networkId)

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
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkFirmwareUpgradesStagedStages200ResponseInner> result = apiInstance.getNetworkFirmwareUpgradesStagedStages_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#getNetworkFirmwareUpgradesStagedStages_1");
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

<a id="getNetworkFirmwareUpgrades_1"></a>
# **getNetworkFirmwareUpgrades_1**
> GetNetworkFirmwareUpgrades200Response getNetworkFirmwareUpgrades_1(networkId)

Get firmware upgrade information for a network

Get firmware upgrade information for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      GetNetworkFirmwareUpgrades200Response result = apiInstance.getNetworkFirmwareUpgrades_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#getNetworkFirmwareUpgrades_1");
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

[**GetNetworkFirmwareUpgrades200Response**](GetNetworkFirmwareUpgrades200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

<a id="rollbacksNetworkFirmwareUpgradesStagedEvents_1"></a>
# **rollbacksNetworkFirmwareUpgradesStagedEvents_1**
> GetNetworkFirmwareUpgradesStagedEvents200Response rollbacksNetworkFirmwareUpgradesStagedEvents_1(networkId, rollbacksNetworkFirmwareUpgradesStagedEventsRequest)

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
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    RollbacksNetworkFirmwareUpgradesStagedEventsRequest rollbacksNetworkFirmwareUpgradesStagedEventsRequest = new RollbacksNetworkFirmwareUpgradesStagedEventsRequest(); // RollbacksNetworkFirmwareUpgradesStagedEventsRequest | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.rollbacksNetworkFirmwareUpgradesStagedEvents_1(networkId, rollbacksNetworkFirmwareUpgradesStagedEventsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#rollbacksNetworkFirmwareUpgradesStagedEvents_1");
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

<a id="updateNetworkFirmwareUpgradesStagedEvents_1"></a>
# **updateNetworkFirmwareUpgradesStagedEvents_1**
> GetNetworkFirmwareUpgradesStagedEvents200Response updateNetworkFirmwareUpgradesStagedEvents_1(networkId, updateNetworkFirmwareUpgradesStagedEventsRequest)

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
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkFirmwareUpgradesStagedEventsRequest updateNetworkFirmwareUpgradesStagedEventsRequest = new UpdateNetworkFirmwareUpgradesStagedEventsRequest(); // UpdateNetworkFirmwareUpgradesStagedEventsRequest | 
    try {
      GetNetworkFirmwareUpgradesStagedEvents200Response result = apiInstance.updateNetworkFirmwareUpgradesStagedEvents_1(networkId, updateNetworkFirmwareUpgradesStagedEventsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#updateNetworkFirmwareUpgradesStagedEvents_1");
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

<a id="updateNetworkFirmwareUpgradesStagedGroup_1"></a>
# **updateNetworkFirmwareUpgradesStagedGroup_1**
> Object updateNetworkFirmwareUpgradesStagedGroup_1(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest)

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
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String groupId = "groupId_example"; // String | 
    CreateNetworkFirmwareUpgradesStagedGroupRequest createNetworkFirmwareUpgradesStagedGroupRequest = new CreateNetworkFirmwareUpgradesStagedGroupRequest(); // CreateNetworkFirmwareUpgradesStagedGroupRequest | 
    try {
      Object result = apiInstance.updateNetworkFirmwareUpgradesStagedGroup_1(networkId, groupId, createNetworkFirmwareUpgradesStagedGroupRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#updateNetworkFirmwareUpgradesStagedGroup_1");
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

<a id="updateNetworkFirmwareUpgradesStagedStages_1"></a>
# **updateNetworkFirmwareUpgradesStagedStages_1**
> List&lt;GetNetworkFirmwareUpgradesStagedStages200ResponseInner&gt; updateNetworkFirmwareUpgradesStagedStages_1(networkId, updateNetworkFirmwareUpgradesStagedStagesRequest)

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
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkFirmwareUpgradesStagedStagesRequest updateNetworkFirmwareUpgradesStagedStagesRequest = new UpdateNetworkFirmwareUpgradesStagedStagesRequest(); // UpdateNetworkFirmwareUpgradesStagedStagesRequest | 
    try {
      List<GetNetworkFirmwareUpgradesStagedStages200ResponseInner> result = apiInstance.updateNetworkFirmwareUpgradesStagedStages_1(networkId, updateNetworkFirmwareUpgradesStagedStagesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#updateNetworkFirmwareUpgradesStagedStages_1");
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

<a id="updateNetworkFirmwareUpgrades_1"></a>
# **updateNetworkFirmwareUpgrades_1**
> GetNetworkFirmwareUpgrades200Response updateNetworkFirmwareUpgrades_1(networkId, updateNetworkFirmwareUpgradesRequest)

Update firmware upgrade information for a network

Update firmware upgrade information for a network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FirmwareUpgradesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FirmwareUpgradesApi apiInstance = new FirmwareUpgradesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkFirmwareUpgradesRequest updateNetworkFirmwareUpgradesRequest = new UpdateNetworkFirmwareUpgradesRequest(); // UpdateNetworkFirmwareUpgradesRequest | 
    try {
      GetNetworkFirmwareUpgrades200Response result = apiInstance.updateNetworkFirmwareUpgrades_1(networkId, updateNetworkFirmwareUpgradesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FirmwareUpgradesApi#updateNetworkFirmwareUpgrades_1");
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
| **updateNetworkFirmwareUpgradesRequest** | [**UpdateNetworkFirmwareUpgradesRequest**](UpdateNetworkFirmwareUpgradesRequest.md)|  | [optional] |

### Return type

[**GetNetworkFirmwareUpgrades200Response**](GetNetworkFirmwareUpgrades200Response.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

