# PrepareApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationInventoryOnboardingCloudMonitoringPrepare_4**](PrepareApi.md#createOrganizationInventoryOnboardingCloudMonitoringPrepare_4) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/prepare | Initiates or updates an import session |


<a id="createOrganizationInventoryOnboardingCloudMonitoringPrepare_4"></a>
# **createOrganizationInventoryOnboardingCloudMonitoringPrepare_4**
> List&lt;CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner&gt; createOrganizationInventoryOnboardingCloudMonitoringPrepare_4(organizationId, createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest)

Initiates or updates an import session

Initiates or updates an import session. An import ID will be generated and used when you are ready to commit the import.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PrepareApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    PrepareApi apiInstance = new PrepareApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest = new CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest | 
    try {
      List<CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner> result = apiInstance.createOrganizationInventoryOnboardingCloudMonitoringPrepare_4(organizationId, createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PrepareApi#createOrganizationInventoryOnboardingCloudMonitoringPrepare_4");
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
| **createOrganizationInventoryOnboardingCloudMonitoringPrepareRequest** | [**CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest**](CreateOrganizationInventoryOnboardingCloudMonitoringPrepareRequest.md)|  | |

### Return type

[**List&lt;CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner&gt;**](CreateOrganizationInventoryOnboardingCloudMonitoringPrepare201ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

