# ImportsApi

All URIs are relative to *https://api.meraki.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createOrganizationInventoryOnboardingCloudMonitoringImport_4**](ImportsApi.md#createOrganizationInventoryOnboardingCloudMonitoringImport_4) | **POST** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports | Commits the import operation to complete the onboarding of a device into Dashboard for monitoring. |
| [**getOrganizationInventoryOnboardingCloudMonitoringImports_4**](ImportsApi.md#getOrganizationInventoryOnboardingCloudMonitoringImports_4) | **GET** /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports | Check the status of a committed Import operation |


<a id="createOrganizationInventoryOnboardingCloudMonitoringImport_4"></a>
# **createOrganizationInventoryOnboardingCloudMonitoringImport_4**
> List&lt;CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner&gt; createOrganizationInventoryOnboardingCloudMonitoringImport_4(organizationId, createOrganizationInventoryOnboardingCloudMonitoringImportRequest)

Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest createOrganizationInventoryOnboardingCloudMonitoringImportRequest = new CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest(); // CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest | 
    try {
      List<CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner> result = apiInstance.createOrganizationInventoryOnboardingCloudMonitoringImport_4(organizationId, createOrganizationInventoryOnboardingCloudMonitoringImportRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#createOrganizationInventoryOnboardingCloudMonitoringImport_4");
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
| **createOrganizationInventoryOnboardingCloudMonitoringImportRequest** | [**CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest**](CreateOrganizationInventoryOnboardingCloudMonitoringImportRequest.md)|  | |

### Return type

[**List&lt;CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner&gt;**](CreateOrganizationInventoryOnboardingCloudMonitoringImport201ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |

<a id="getOrganizationInventoryOnboardingCloudMonitoringImports_4"></a>
# **getOrganizationInventoryOnboardingCloudMonitoringImports_4**
> List&lt;GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner&gt; getOrganizationInventoryOnboardingCloudMonitoringImports_4(organizationId, importIds)

Check the status of a committed Import operation

Check the status of a committed Import operation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ImportsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.meraki.com/api/v1");
    
    // Configure API key authorization: meraki_api_key
    ApiKeyAuth meraki_api_key = (ApiKeyAuth) defaultClient.getAuthentication("meraki_api_key");
    meraki_api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //meraki_api_key.setApiKeyPrefix("Token");

    ImportsApi apiInstance = new ImportsApi(defaultClient);
    String organizationId = "organizationId_example"; // String | 
    List<String> importIds = Arrays.asList(); // List<String> | import ids from an imports
    try {
      List<GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner> result = apiInstance.getOrganizationInventoryOnboardingCloudMonitoringImports_4(organizationId, importIds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ImportsApi#getOrganizationInventoryOnboardingCloudMonitoringImports_4");
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
| **importIds** | [**List&lt;String&gt;**](String.md)| import ids from an imports | |

### Return type

[**List&lt;GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner&gt;**](GetOrganizationInventoryOnboardingCloudMonitoringImports200ResponseInner.md)

### Authorization

[meraki_api_key](../README.md#meraki_api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |

