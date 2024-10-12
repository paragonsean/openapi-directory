# FloorPlansApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkFloorPlan_1**](FloorPlansApi.md#createNetworkFloorPlan_1) | **POST** /networks/{networkId}/floorPlans | Upload a floor plan |
| [**deleteNetworkFloorPlan_1**](FloorPlansApi.md#deleteNetworkFloorPlan_1) | **DELETE** /networks/{networkId}/floorPlans/{floorPlanId} | Destroy a floor plan |
| [**getNetworkFloorPlan_1**](FloorPlansApi.md#getNetworkFloorPlan_1) | **GET** /networks/{networkId}/floorPlans/{floorPlanId} | Find a floor plan by ID |
| [**getNetworkFloorPlans_1**](FloorPlansApi.md#getNetworkFloorPlans_1) | **GET** /networks/{networkId}/floorPlans | List the floor plans that belong to your network |
| [**updateNetworkFloorPlan_1**](FloorPlansApi.md#updateNetworkFloorPlan_1) | **PUT** /networks/{networkId}/floorPlans/{floorPlanId} | Update a floor plan&#39;s geolocation and other meta data |


<a id="createNetworkFloorPlan_1"></a>
# **createNetworkFloorPlan_1**
> Object createNetworkFloorPlan_1(networkId, createNetworkFloorPlanRequest)

Upload a floor plan

Upload a floor plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloorPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FloorPlansApi apiInstance = new FloorPlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkFloorPlanRequest createNetworkFloorPlanRequest = new CreateNetworkFloorPlanRequest(); // CreateNetworkFloorPlanRequest | 
    try {
      Object result = apiInstance.createNetworkFloorPlan_1(networkId, createNetworkFloorPlanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloorPlansApi#createNetworkFloorPlan_1");
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
| **createNetworkFloorPlanRequest** | [**CreateNetworkFloorPlanRequest**](CreateNetworkFloorPlanRequest.md)|  | |

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

<a id="deleteNetworkFloorPlan_1"></a>
# **deleteNetworkFloorPlan_1**
> deleteNetworkFloorPlan_1(networkId, floorPlanId)

Destroy a floor plan

Destroy a floor plan

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloorPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FloorPlansApi apiInstance = new FloorPlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String floorPlanId = "floorPlanId_example"; // String | 
    try {
      apiInstance.deleteNetworkFloorPlan_1(networkId, floorPlanId);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloorPlansApi#deleteNetworkFloorPlan_1");
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
| **floorPlanId** | **String**|  | |

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

<a id="getNetworkFloorPlan_1"></a>
# **getNetworkFloorPlan_1**
> Object getNetworkFloorPlan_1(networkId, floorPlanId)

Find a floor plan by ID

Find a floor plan by ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloorPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FloorPlansApi apiInstance = new FloorPlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String floorPlanId = "floorPlanId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkFloorPlan_1(networkId, floorPlanId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloorPlansApi#getNetworkFloorPlan_1");
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
| **floorPlanId** | **String**|  | |

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

<a id="getNetworkFloorPlans_1"></a>
# **getNetworkFloorPlans_1**
> List&lt;Object&gt; getNetworkFloorPlans_1(networkId)

List the floor plans that belong to your network

List the floor plans that belong to your network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloorPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FloorPlansApi apiInstance = new FloorPlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkFloorPlans_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloorPlansApi#getNetworkFloorPlans_1");
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

<a id="updateNetworkFloorPlan_1"></a>
# **updateNetworkFloorPlan_1**
> Object updateNetworkFloorPlan_1(networkId, floorPlanId, updateNetworkFloorPlanRequest)

Update a floor plan&#39;s geolocation and other meta data

Update a floor plan&#39;s geolocation and other meta data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FloorPlansApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    FloorPlansApi apiInstance = new FloorPlansApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String floorPlanId = "floorPlanId_example"; // String | 
    UpdateNetworkFloorPlanRequest updateNetworkFloorPlanRequest = new UpdateNetworkFloorPlanRequest(); // UpdateNetworkFloorPlanRequest | 
    try {
      Object result = apiInstance.updateNetworkFloorPlan_1(networkId, floorPlanId, updateNetworkFloorPlanRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FloorPlansApi#updateNetworkFloorPlan_1");
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
| **floorPlanId** | **String**|  | |
| **updateNetworkFloorPlanRequest** | [**UpdateNetworkFloorPlanRequest**](UpdateNetworkFloorPlanRequest.md)|  | [optional] |

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

