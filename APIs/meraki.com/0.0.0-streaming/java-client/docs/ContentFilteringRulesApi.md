# ContentFilteringRulesApi

All URIs are relative to *https://api.meraki.com/api/v0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkContentFiltering**](ContentFilteringRulesApi.md#getNetworkContentFiltering) | **GET** /networks/{networkId}/contentFiltering | Return the content filtering settings for an MX network |
| [**updateNetworkContentFiltering**](ContentFilteringRulesApi.md#updateNetworkContentFiltering) | **PUT** /networks/{networkId}/contentFiltering | Update the content filtering settings for an MX network |


<a id="getNetworkContentFiltering"></a>
# **getNetworkContentFiltering**
> Object getNetworkContentFiltering(networkId)

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
import org.openapitools.client.api.ContentFilteringRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ContentFilteringRulesApi apiInstance = new ContentFilteringRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      Object result = apiInstance.getNetworkContentFiltering(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentFilteringRulesApi#getNetworkContentFiltering");
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

<a id="updateNetworkContentFiltering"></a>
# **updateNetworkContentFiltering**
> Object updateNetworkContentFiltering(networkId, updateNetworkContentFilteringRequest)

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
import org.openapitools.client.api.ContentFilteringRulesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v0");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ContentFilteringRulesApi apiInstance = new ContentFilteringRulesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkContentFilteringRequest updateNetworkContentFilteringRequest = new UpdateNetworkContentFilteringRequest(); // UpdateNetworkContentFilteringRequest | 
    try {
      Object result = apiInstance.updateNetworkContentFiltering(networkId, updateNetworkContentFilteringRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContentFilteringRulesApi#updateNetworkContentFiltering");
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
| **updateNetworkContentFilteringRequest** | [**UpdateNetworkContentFilteringRequest**](UpdateNetworkContentFilteringRequest.md)|  | [optional] |

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

