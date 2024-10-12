# ContentFilteringApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkApplianceContentFilteringCategories_1**](ContentFilteringApi.md#getNetworkApplianceContentFilteringCategories_1) | **GET** /networks/{networkId}/appliance/contentFiltering/categories | List all available content filtering categories for an MX network |
| [**getNetworkApplianceContentFiltering_1**](ContentFilteringApi.md#getNetworkApplianceContentFiltering_1) | **GET** /networks/{networkId}/appliance/contentFiltering | Return the content filtering settings for an MX network |
| [**updateNetworkApplianceContentFiltering_1**](ContentFilteringApi.md#updateNetworkApplianceContentFiltering_1) | **PUT** /networks/{networkId}/appliance/contentFiltering | Update the content filtering settings for an MX network |


<a id="getNetworkApplianceContentFilteringCategories_1"></a>
# **getNetworkApplianceContentFilteringCategories_1**
> Object getNetworkApplianceContentFilteringCategories_1(networkId)

List all available content filtering categories for an MX network

List all available content filtering categories for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentFilteringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ContentFilteringApi apiInstance = new ContentFilteringApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceContentFilteringCategories_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentFilteringApi#getNetworkApplianceContentFilteringCategories_1");
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

<a id="getNetworkApplianceContentFiltering_1"></a>
# **getNetworkApplianceContentFiltering_1**
> Object getNetworkApplianceContentFiltering_1(networkId)

Return the content filtering settings for an MX network

Return the content filtering settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentFilteringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ContentFilteringApi apiInstance = new ContentFilteringApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkApplianceContentFiltering_1(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentFilteringApi#getNetworkApplianceContentFiltering_1");
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

<a id="updateNetworkApplianceContentFiltering_1"></a>
# **updateNetworkApplianceContentFiltering_1**
> Object updateNetworkApplianceContentFiltering_1(networkId, updateNetworkApplianceContentFilteringRequest)

Update the content filtering settings for an MX network

Update the content filtering settings for an MX network

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContentFilteringApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ContentFilteringApi apiInstance = new ContentFilteringApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkApplianceContentFilteringRequest updateNetworkApplianceContentFilteringRequest = new UpdateNetworkApplianceContentFilteringRequest(); // UpdateNetworkApplianceContentFilteringRequest | 
    try {
      Object result = apiInstance.updateNetworkApplianceContentFiltering_1(networkId, updateNetworkApplianceContentFilteringRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentFilteringApi#updateNetworkApplianceContentFiltering_1");
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
| **updateNetworkApplianceContentFilteringRequest** | [**UpdateNetworkApplianceContentFilteringRequest**](UpdateNetworkApplianceContentFilteringRequest.md)|  | [optional] |

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

