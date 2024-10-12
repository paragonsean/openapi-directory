# RollbacksApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createNetworkFirmwareUpgradesRollback_2**](RollbacksApi.md#createNetworkFirmwareUpgradesRollback_2) | **POST** /networks/{networkId}/firmwareUpgrades/rollbacks | Rollback a Firmware Upgrade For A Network |


<a id="createNetworkFirmwareUpgradesRollback_2"></a>
# **createNetworkFirmwareUpgradesRollback_2**
> CreateNetworkFirmwareUpgradesRollback200Response createNetworkFirmwareUpgradesRollback_2(networkId, createNetworkFirmwareUpgradesRollbackRequest)

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
import org.openapitools.client.api.RollbacksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    RollbacksApi apiInstance = new RollbacksApi(defaultClient);
    String networkId = "networkId_example"; // String | 
    CreateNetworkFirmwareUpgradesRollbackRequest createNetworkFirmwareUpgradesRollbackRequest = new CreateNetworkFirmwareUpgradesRollbackRequest(); // CreateNetworkFirmwareUpgradesRollbackRequest | 
    try {
      CreateNetworkFirmwareUpgradesRollback200Response result = apiInstance.createNetworkFirmwareUpgradesRollback_2(networkId, createNetworkFirmwareUpgradesRollbackRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RollbacksApi#createNetworkFirmwareUpgradesRollback_2");
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

