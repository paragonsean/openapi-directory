# ExportEventsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationInventoryOnboardingCloudMonitoringExportEvent_4**](ExportEventsApi.md#createOrganizationInventoryOnboardingCloudMonitoringExportEvent_4) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/exportEvents | Imports event logs related to the onboarding app into elastisearch |


<a id="createOrganizationInventoryOnboardingCloudMonitoringExportEvent_4"></a>
# **createOrganizationInventoryOnboardingCloudMonitoringExportEvent_4**
> Object createOrganizationInventoryOnboardingCloudMonitoringExportEvent_4(organizationId, createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest)

Imports event logs related to the onboarding app into elastisearch

Imports event logs related to the onboarding app into elastisearch

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportEventsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ExportEventsApi apiInstance = new ExportEventsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest = new CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest | 
    try {
      Object result = apiInstance.createOrganizationInventoryOnboardingCloudMonitoringExportEvent_4(organizationId, createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportEventsApi#createOrganizationInventoryOnboardingCloudMonitoringExportEvent_4");
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
| **createOrganizationInventoryOnboardingCloudMonitoringExportEventRequest** | [**CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest**](CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.md)|  | |

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
| **202** | Successful operation |  -  |

