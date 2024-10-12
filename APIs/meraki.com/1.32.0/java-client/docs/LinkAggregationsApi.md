# LinkAggregationsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkSwitchLinkAggregation_1**](LinkAggregationsApi.md#createNetworkSwitchLinkAggregation_1) | **POST** /networks/{networkId}/switch/linkAggregations | Create a link aggregation group |
| [**deleteNetworkSwitchLinkAggregation_1**](LinkAggregationsApi.md#deleteNetworkSwitchLinkAggregation_1) | **DELETE** /networks/{networkId}/switch/linkAggregations/{linkAggregationId} | Split a link aggregation group into separate ports |
| [**getNetworkSwitchLinkAggregations_1**](LinkAggregationsApi.md#getNetworkSwitchLinkAggregations_1) | **GET** /networks/{networkId}/switch/linkAggregations | List link aggregation groups |
| [**updateNetworkSwitchLinkAggregation_1**](LinkAggregationsApi.md#updateNetworkSwitchLinkAggregation_1) | **PUT** /networks/{networkId}/switch/linkAggregations/{linkAggregationId} | Update a link aggregation group |


<a id="createNetworkSwitchLinkAggregation_1"></a>
# **createNetworkSwitchLinkAggregation_1**
> Object createNetworkSwitchLinkAggregation_1(networkId, createNetworkSwitchLinkAggregationRequest)

Create a link aggregation group

Create a link aggregation group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkAggregationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LinkAggregationsApi apiInstance = new LinkAggregationsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkSwitchLinkAggregationRequest createNetworkSwitchLinkAggregationRequest = new CreateNetworkSwitchLinkAggregationRequest(); // CreateNetworkSwitchLinkAggregationRequest | 
    try {
      Object result = apiInstance.createNetworkSwitchLinkAggregation_1(networkId, createNetworkSwitchLinkAggregationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkAggregationsApi#createNetworkSwitchLinkAggregation_1");
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
| **createNetworkSwitchLinkAggregationRequest** | [**CreateNetworkSwitchLinkAggregationRequest**](CreateNetworkSwitchLinkAggregationRequest.md)|  | [optional] |

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

<a id="deleteNetworkSwitchLinkAggregation_1"></a>
# **deleteNetworkSwitchLinkAggregation_1**
> deleteNetworkSwitchLinkAggregation_1(networkId, linkAggregationId)

Split a link aggregation group into separate ports

Split a link aggregation group into separate ports

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkAggregationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LinkAggregationsApi apiInstance = new LinkAggregationsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String linkAggregationId = "linkAggregationId_example"; // String | 
    try {
      apiInstance.deleteNetworkSwitchLinkAggregation_1(networkId, linkAggregationId);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkAggregationsApi#deleteNetworkSwitchLinkAggregation_1");
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
| **linkAggregationId** | **String**|  | |

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

<a id="getNetworkSwitchLinkAggregations_1"></a>
# **getNetworkSwitchLinkAggregations_1**
> List&lt;Object&gt; getNetworkSwitchLinkAggregations_1(networkId)

List link aggregation groups

List link aggregation groups

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkAggregationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LinkAggregationsApi apiInstance = new LinkAggregationsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<Object> result = apiInstance.getNetworkSwitchLinkAggregations_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkAggregationsApi#getNetworkSwitchLinkAggregations_1");
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

<a id="updateNetworkSwitchLinkAggregation_1"></a>
# **updateNetworkSwitchLinkAggregation_1**
> Object updateNetworkSwitchLinkAggregation_1(networkId, linkAggregationId, updateNetworkSwitchLinkAggregationRequest)

Update a link aggregation group

Update a link aggregation group

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkAggregationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    LinkAggregationsApi apiInstance = new LinkAggregationsApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    String linkAggregationId = "linkAggregationId_example"; // String | 
    UpdateNetworkSwitchLinkAggregationRequest updateNetworkSwitchLinkAggregationRequest = new UpdateNetworkSwitchLinkAggregationRequest(); // UpdateNetworkSwitchLinkAggregationRequest | 
    try {
      Object result = apiInstance.updateNetworkSwitchLinkAggregation_1(networkId, linkAggregationId, updateNetworkSwitchLinkAggregationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkAggregationsApi#updateNetworkSwitchLinkAggregation_1");
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
| **linkAggregationId** | **String**|  | |
| **updateNetworkSwitchLinkAggregationRequest** | [**UpdateNetworkSwitchLinkAggregationRequest**](UpdateNetworkSwitchLinkAggregationRequest.md)|  | [optional] |

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

