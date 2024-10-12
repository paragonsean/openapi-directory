# StagesApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNetworkFirmwareUpgradesStagedStages_3**](StagesApi.md#getNetworkFirmwareUpgradesStagedStages_3) | **GET** /networks/{networkId}/firmwareUpgrades/staged/stages | Order of Staged Upgrade Groups in a network |
| [**updateNetworkFirmwareUpgradesStagedStages_3**](StagesApi.md#updateNetworkFirmwareUpgradesStagedStages_3) | **PUT** /networks/{networkId}/firmwareUpgrades/staged/stages | Assign Staged Upgrade Group order in the sequence. |


<a id="getNetworkFirmwareUpgradesStagedStages_3"></a>
# **getNetworkFirmwareUpgradesStagedStages_3**
> List&lt;GetNetworkFirmwareUpgradesStagedStages200ResponseInner&gt; getNetworkFirmwareUpgradesStagedStages_3(networkId)

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
import org.openapitools.client.api.StagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagesApi apiInstance = new StagesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    try {
      List<GetNetworkFirmwareUpgradesStagedStages200ResponseInner> result = apiInstance.getNetworkFirmwareUpgradesStagedStages_3(networkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagesApi#getNetworkFirmwareUpgradesStagedStages_3");
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

<a id="updateNetworkFirmwareUpgradesStagedStages_3"></a>
# **updateNetworkFirmwareUpgradesStagedStages_3**
> List&lt;GetNetworkFirmwareUpgradesStagedStages200ResponseInner&gt; updateNetworkFirmwareUpgradesStagedStages_3(networkId, updateNetworkFirmwareUpgradesStagedStagesRequest)

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
import org.openapitools.client.api.StagesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    StagesApi apiInstance = new StagesApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    UpdateNetworkFirmwareUpgradesStagedStagesRequest updateNetworkFirmwareUpgradesStagedStagesRequest = new UpdateNetworkFirmwareUpgradesStagedStagesRequest(); // UpdateNetworkFirmwareUpgradesStagedStagesRequest | 
    try {
      List<GetNetworkFirmwareUpgradesStagedStages200ResponseInner> result = apiInstance.updateNetworkFirmwareUpgradesStagedStages_3(networkId, updateNetworkFirmwareUpgradesStagedStagesRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StagesApi#updateNetworkFirmwareUpgradesStagedStages_3");
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

